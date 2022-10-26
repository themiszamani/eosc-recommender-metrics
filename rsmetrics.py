#!/usr/bin/env python3
import sys, argparse
import json
import yaml
import pymongo
from datetime import datetime, timezone
import os
import pandas as pd
from inspect import getmembers, isfunction

# local lib
import metrics as m


__copyright__ = "© "+str(datetime.utcnow().year)+", National Infrastructures for Research and Technology (GRNET)"

__status__ = "Production"
__version__ = "0.2.2"


os.environ['COLUMNS'] = "90"

def print_help(func):
    def inner():
        print("""  _____   _____                _        _          
 |  __ \ / ____|              | |      (_)         
 | |__) | (___  _ __ ___   ___| |_ _ __ _  ___ ___ 
 |  _  / \___ \| '_ ` _ \ / _ \ __| '__| |/ __/ __|
 | | \ \ ____) | | | | | |  __/ |_| |  | | (__\__ \\
 |_|  \_\_____/|_| |_| |_|\___|\__|_|  |_|\___|___/
""")
        print('Version: ' + __version__)
        print( __copyright__+'\n')
        func()
    return inner


parser = argparse.ArgumentParser(prog='rsmetrics', description='Calculate metrics for the EOSC Marketplace RS', add_help=False)
parser.print_help=print_help(parser.print_help)
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

optional.add_argument('-c', '--config', metavar=('FILEPATH'), help='override default configuration file (./config.yaml)', nargs='?', default='./config.yaml', type=str)
optional.add_argument('-i', '--input', metavar=('FILEPATH'), help='override default output dir (./data)', nargs='?', default='./data', type=str)

optional.add_argument('-s', '--starttime', metavar=('DATETIME'), help='calculate metrics starting from given datetime in ISO format (UTC) e.g. YYYY-MM-DD', nargs='?', default=None)
optional.add_argument('-e', '--endtime', metavar=('DATETIME'), help='calculate metrics ending to given datetime in ISO format (UTC) e.g. YYYY-MM-DD', nargs='?', default=None)

optional.add_argument('-h', '--help', action='help', help='show this help message and exit')
optional.add_argument('-v', '--version', action='version', version='%(prog)s v'+__version__)

#args=parser.parse_args(args=None if sys.argv[1:] else ['--help'])

args=parser.parse_args()

run=m.Runtime()

if args.starttime:
    args.starttime=datetime.fromisoformat(args.starttime)

if args.endtime:
    args.endtime=datetime.fromisoformat(args.endtime)

if not args.endtime:
    args.endtime=datetime.utcnow()

if args.starttime and args.endtime:
    if args.endtime<args.starttime:
        print('End date must be older than start date')
        sys.exit(0)

# read configuration file
with open(args.config, 'r') as _f:
    config=yaml.load(_f, Loader=yaml.FullLoader)

# read data
# connect to db server
datastore = pymongo.MongoClient("mongodb://"+config["Datastore"]["MongoDB"]["host"]+":"+str(config["Datastore"]["MongoDB"]["port"])+"/", uuidRepresentation='pythonLegacy')

# use db
rsmetrics_db = datastore[config["Datastore"]["MongoDB"]["db"]]

# first column (_id) ignored, where iloc is used
run.user_actions_all=pd.DataFrame(list(rsmetrics_db["user_actions"].find())).iloc[:,1:]
run.user_actions_all.columns=["User", "Source_Service", "Target_Service", "Reward", "Action", "Timestamp", "Source_Page_ID", "Target_Page_ID", "Type", "Provider", "Ingestion"]

run.recommendations=pd.DataFrame(list(rsmetrics_db["recommendations"].aggregate([{"$unwind":"$resource_ids"}]))).iloc[:,1:]
run.recommendations.columns=["User", "Service", "Timestamp", "Type", "Provider", "Ingestion"]

run.users=pd.DataFrame(list(rsmetrics_db["users"].find())).iloc[:,1:]
run.users.columns=["User", "Services", "Created_on", "Deleted_on", "Provider", "Ingestion"]

run.services=pd.DataFrame(list(rsmetrics_db["resources"].find())).iloc[:,1:]
run.services.columns=["Service", "Name", "Page", "Created_on", "Deleted_on", "Type", "Provider", "Ingestion"]

# convert timestamp column to datetime object
run.user_actions_all['Timestamp']= pd.to_datetime(run.user_actions_all['Timestamp'])

run.recommendations['Timestamp']= pd.to_datetime(run.recommendations['Timestamp'])

# restrict user actions and recommendations data to datetime range
if args.starttime:
    run.user_actions_all=run.user_actions_all[(run.user_actions_all['Timestamp'] > args.starttime) & (run.user_actions_all['Timestamp'] < args.endtime)]
    run.recommendations=run.recommendations[(run.recommendations['Timestamp'] > args.starttime) & (run.recommendations['Timestamp'] < args.endtime)]

else:
    run.user_actions_all=run.user_actions_all[run.user_actions_all['Timestamp'] < args.endtime]
    run.recommendations=run.recommendations[run.recommendations['Timestamp'] < args.endtime]

# remove user actions when user or service does not exist in users' or services' catalogs
# adding -1 in all catalogs indicating the anonynoums users or not-known services
run.user_actions = run.user_actions_all[run.user_actions_all['User'].isin(run.users['User'].tolist()+[-1])]
run.user_actions = run.user_actions[run.user_actions['Source_Service'].isin(run.services['Service'].tolist()+[-1])]
run.user_actions = run.user_actions[run.user_actions['Target_Service'].isin(run.services['Service'].tolist()+[-1])]

# remove recommendations when user or service does not exist in users' or services' catalogs
# adding -1 in all catalogs indicating the anonynoums users or not-known services
run.recommendations = run.recommendations[run.recommendations['User'].isin(run.users['User'].tolist()+[-1])]
run.recommendations = run.recommendations[run.recommendations['Service'].isin(run.services['Service'].tolist()+[-1])]


output={'timestamp':str(datetime.utcnow())}
metrics = []
statistics = []

# get all function names in metrics module
func_names = list(map(lambda x: x[0], getmembers(m, isfunction)))
# keep all function names except decorators such as metric and statistic
func_names = list(filter(lambda x: not ( x=='metric' or x=='statistic') ,func_names))
for func_name in func_names:
    # get function based on function name
    func = getattr(m,func_name)
    # if function has attribute kind (which means that evaluates a metric or a static)
    if hasattr(func,"kind"):
        kind = getattr(func,"kind")
        # execute and get value
        value= func(run)
        documentation = ""
        # if has documentation ge it
        if hasattr(func,"doc"):
            documentation = func.doc
        # prepare json output object with function name, execution result and optional documentation
        item = {'name':func_name, 'value':value, 'doc':documentation}
        # if metric add it to the metrics list else to the statistics list
        if kind == "metric":
            metrics.append(item)
        elif kind == "statistic":
            statistics.append(item)

# Add the two lists to the final output onject
output['metrics'] = metrics
output['statistics'] = statistics

# this line is necessary in order to store the output to MongoDB
jsonstr = json.dumps(output,indent=4)

rsmetrics_db.drop_collection("metrics")
rsmetrics_db["metrics"].insert_one(output)

print(jsonstr)

# Using a JSON string
# export service catalog
if config['Datastore']['export_CSV']:
    with open(os.path.join(args.input,'metrics.json'), 'w') as outfile:
        outfile.write(jsonstr)
