#!/usr/bin/env python3
import sys, argparse
import json
import yaml
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

#optional.add_argument('-c', '--config', metavar=('FILEPATH'), help='override default configuration file (./config.yaml)', nargs='?', default='./config.yaml', type=str)
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

# read data
run.user_actions_all=pd.read_csv(os.path.join(args.input,'user_actions.csv'),names=["User", "Source_Service", "Target_Service", "Reward", "Action", "Timestamp", "Source_Page_ID", "Target_Page_ID"])
run.recommendations=pd.read_csv(os.path.join(args.input,'recommendations.csv'),names=["User", "Service", "Rating", "Timestamp"])

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


# users are populated with two columns: one includes user id and the other includes a list of accessed services
run.users=pd.read_csv(os.path.join(args.input,'users.csv'),names=["User","Services"],converters={'Services': lambda x: map(int,x.split())})
    
# populate services
run.services=pd.read_csv(os.path.join(args.input,'services.csv'),names=["Service", "Rating", "Name", "Page"])

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


jsonstr = json.dumps(output,indent=4)
#jsonstr = json.dumps(m.__dict__)
print(jsonstr)

# Using a JSON string
with open(os.path.join(args.input,'metrics.json'), 'w') as outfile:
    outfile.write(jsonstr)
