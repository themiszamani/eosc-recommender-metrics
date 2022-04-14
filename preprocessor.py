#!/usr/bin/env python3
import sys, argparse
import json
import yaml
import pymongo
from datetime import datetime, timezone
import os

import retrieval

import reward_mapping as rm
from get_service_catalog import get_eosc_marketplace_url, get_service_catalog_items, get_service_catalog_page_content, save_service_items_to_csv


__copyright__ = "© "+str(datetime.utcnow().year)+", National Infrastructures for Research and Technology (GRNET)"
__status__ = "Production"
__version__ = "1.0"


os.environ['COLUMNS'] = "90"

def print_help(func):
    def inner():
        print("""
  _____                                                       
 |  __ \                                                      
 | |__) | __ ___ _ __  _ __ ___   ___ ___  ___ ___  ___  _ __ 
 |  ___/ '__/ _ \ '_ \| '__/ _ \ / __/ _ \/ __/ __|/ _ \| '__|
 | |   | | |  __/ |_) | | | (_) | (_|  __/\__ \__ \ (_) | |   
 |_|   |_|  \___| .__/|_|  \___/ \___\___||___/___/\___/|_|   
                | |                                           
                |_|                                           
""")
        print('Version: ' + __version__)
        print( __copyright__+'\n')
        func()
    return inner

def remove_service_prefix(text):
    """Removes '/service/' prefix from eosc service paths

    Args:
        text (string): string containing a service path

    Returns:
        string: service path without the /service/ prefix
    """
    if text.startswith('/service/'):
        return text[len('/service/'):]
    return text

parser = argparse.ArgumentParser(prog='rsmetrics', description='Prepare data for the EOSC Marketplace RS metrics calculation', add_help=False)
parser.print_help=print_help(parser.print_help)
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

optional.add_argument('-c', '--config', metavar=('FILEPATH'), help='override default configuration file (./config.yaml)', nargs='?', default='./config.yaml', type=str)
optional.add_argument('-o', '--output', metavar=('DIRPATH'), help='override default output dir path (./data)', nargs='?', default='./data', type=str)

optional.add_argument('-s', '--starttime', metavar=('DATETIME'), help='process data starting from given datetime in ISO format (UTC) e.g. YYYY-MM-DD', nargs='?', default=None)
optional.add_argument('-e', '--endtime', metavar=('DATETIME'), help='process data ending to given datetime in ISO format (UTC) e.g. YYYY-MM-DD', nargs='?', default=None)


optional.add_argument('-h', '--help', action='help', help='show this help message and exit')
optional.add_argument('-v', '--version', action='version', version='%(prog)s v'+__version__)

#args=parser.parse_args(args=None if sys.argv[1:] else ['--help'])

args=parser.parse_args()

class Metrics:
    pass

class Mock:
    pass

class User_Action:
    def __init__(self, source_page_id, target_page_id, order):
        self.source=Mock()
        self.target=Mock()
        self.action=Mock()
        self.source.page_id=source_page_id
        self.target.page_id=target_page_id
        self.action.order=order



m=Metrics()

reward_mapping = {
        "order": 1.0,
        "interest": 0.7,
        "mild_interest": 0.3,
        "simple_transition": 0.0,
        "unknown_transition": 0.0,
        "exit": 0.0,
    }

query={'timestamp':{'$lt':datetime.utcnow()}}

if args.starttime:
    args.starttime=datetime.fromisoformat(args.starttime)
    query['timestamp']['$gte']=args.starttime

if args.endtime:
    args.endtime=datetime.fromisoformat(args.endtime)
    query['timestamp']['$lt']=args.endtime

if args.starttime and args.endtime:
    if args.endtime<args.starttime:
        print('End date must be older than start date')
        sys.exit(0)


with open(args.config, 'r') as _f:
    config=yaml.load(_f, Loader=yaml.FullLoader)


os.makedirs(args.output, exist_ok=True)

# connect to db server
myclient = pymongo.MongoClient("mongodb://"+config["Source"]["MongoDB"]["host"]+":"+str(config["Source"]["MongoDB"]["port"])+"/", uuidRepresentation='pythonLegacy')

# use db
recdb = myclient[config["Source"]["MongoDB"]["db"]]





# automatically associate page ids to service ids
if config['Marketplace']['download']:
    service_list_path = os.path.join(args.output,config['Marketplace']['path'])
    eosc_url = get_eosc_marketplace_url()
    print(
        "Retrieving page: marketplace list of services... \nGrabbing url: {0}".format(eosc_url))
    eosc_page_content = get_service_catalog_page_content(eosc_url)
    print("Page retrieved!\nGenerating results...")
    eosc_service_results = get_service_catalog_items(eosc_page_content)
    # output to csv
    save_service_items_to_csv(eosc_service_results, service_list_path)
    print("File written to {}".format(service_list_path))


# read map file and save in dict
with open(os.path.join(args.output,config['Marketplace']['path']), 'r') as f:
    lines=f.readlines()

keys=list(map(lambda x: remove_service_prefix(x.split(',')[2]).strip(), lines))
values=list(map(lambda x: x.split(',')[0].strip(), lines))

dmap=dict(zip(keys, values))  #=> {'a': 1, 'b': 2}


uas={}

for ua in recdb["user_action"].find(query):

   # print(ua)
    # set -1 to anonymous users
    try:
        user=ua['user']
    except:
        user=-1

    # process data that map from page id to service id exist
    try:
        service_id=dmap["/".join(ua['target']['page_id'].split('/')[2:3])]
    except:
        continue

    symbolic_reward=rm.ua_to_reward_id(User_Action(ua['source']['page_id'],
                                                   ua['target']['page_id'],
                                                   ua['action']['order']))

    reward=reward_mapping[symbolic_reward]

    uas.setdefault(user,{})

    # then we need to merge rewards
    # keep the max value for each record
    try:
        if uas[user][service_id][0] < reward:
            uas[user][service_id]=[reward, ua['source']['root']['type'], ua['timestamp']]
    except:
        uas[user].setdefault(service_id,[reward, ua['source']['root']['type'], ua['timestamp']])

luas=[]

for user,_ in sorted(uas.items()):
    for service,act in sorted(uas[user].items()):

        if service:
            luas.append('{},{},{},{},{}\n'.format(user, service, *act))


with open(os.path.join(args.output,'dataset.csv'), 'w') as o:
    o.writelines(luas)


recs=[]
for rec in recdb["recommendation"].find(query):

    try:
        user=rec['user']
    except:
        user=-1

    for service in rec['services']:
        recs.append('{},{},{},{}\n'.format(user, service, '1', rec['timestamp']))

recs=sorted(recs)

with open(os.path.join(args.output,'recommendations.csv'), 'w') as o:
    o.writelines(recs)


# calculate pre metrics
if config['Metrics']:
    time_range=recdb["user_action"].distinct("timestamp", query)

    m.users=recdb["user"].count_documents({})
    m.recommendations=recdb["recommendation"].count_documents(query)
    m.services=recdb["service"].count_documents({})
    m.user_actions=recdb["user_action"].count_documents(query)

    m.user_actions_registered=recdb["user_action"].count_documents({**query,**{"user":{"$exists":True}}})
    m.user_actions_anonymous=m.user_actions-m.user_actions_registered
    m.user_actions_registered_perc=round(m.user_actions_registered*100.0/m.user_actions,2)
    m.user_actions_anonymous_perc=100-m.user_actions_registered_perc

    m.user_actions_order=recdb["user_action"].count_documents({**query, **{"action.order":True}})
    m.user_actions_order_registered=recdb["user_action"].count_documents({**query, **{"action.order":True,"user":{"$exists":True}}})
    m.user_actions_order_anonymous=m.user_actions_order-m.user_actions_order_registered
    m.user_actions_order_registered_perc=round(m.user_actions_order_registered*100.0/m.user_actions_order,2)
    m.user_actions_order_anonymous_perc=100-m.user_actions_order_registered_perc

    m.user_actions_panel=recdb["user_action"].count_documents({**query, **{"source.root.type":"recommendation_panel"}})
    m.user_actions_panel_perc=round(m.user_actions_panel*100.0/m.user_actions,2)

    m.services_suggested=len(recdb["recommendation"].distinct("services", query))

    # catalog coverage
    m.services_suggested_perc=round(m.services_suggested*100.0/m.services,2)

    # user coverage
    m.users_suggested=len(recdb["user_action"].distinct("user", query))
    m.users_suggested_perc=round(m.users_suggested*100.0/m.users,2)

    jsonstr = json.dumps(m.__dict__)
    print(jsonstr)

    # Using a JSON string
    with open(os.path.join(args.output,'pre_metrics.json'), 'w') as outfile:
        outfile.write(jsonstr)
