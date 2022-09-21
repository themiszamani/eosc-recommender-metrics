#!/usr/bin/env python3
import sys, argparse
import json
import yaml
import pymongo
from datetime import datetime, timezone
import os
from natsort import natsorted
import natsort as ns
import pandas as pd
from inspect import getmembers, isfunction
import retrieval
import csv

# local lib
import pre_metrics as pm
import reward_mapping as rm
from get_service_catalog import get_eosc_marketplace_url, get_service_catalog_items, get_service_catalog_page_content, save_service_items_to_csv


__copyright__ = "© "+str(datetime.utcnow().year)+", National Infrastructures for Research and Technology (GRNET)"
__status__ = "Production"
__version__ = "0.2.2"


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

parser = argparse.ArgumentParser(prog='preprocessor', description='Prepare data for the EOSC Marketplace RS metrics calculation', add_help=False)
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
if config['Service']['download']:
    service_list_path = os.path.join(args.output,config['Service']['path'])
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
with open(os.path.join(args.output,config['Service']['path']), 'r') as f:
    lines=f.readlines()

keys=list(map(lambda x: remove_service_prefix(x.split(',')[-1]).strip(), lines))
ids=list(map(lambda x: x.split(',')[0].strip(), lines))
names=list(map(lambda x: x.split(',')[1].strip(), lines))

dmap=dict(zip(keys, zip(ids,names)))  #=> {'a': 1, 'b': 2}
rdmap=dict(zip(ids,zip(keys,names)))

# reward_mapping.py is modified so that the function
# reads the Transition rewards csv file once
# consequently, one argument has been added to the
# called function
ROOT_DIR='./'

TRANSITION_REWARDS_CSV_PATH = os.path.join(
    ROOT_DIR, "resources", "transition_rewards.csv"
)
transition_rewards_df = pd.read_csv(TRANSITION_REWARDS_CSV_PATH, index_col="source")

luas=[]

for ua in recdb["user_action"].find(query).sort("user"):

    # set -1 to anonymous users
    try:
        user=ua['user']
    except:
        user=-1

    # process data that map from page id to service id exist
    # for both source and target page ids
    # if not set service id to -1
    try:
        _pageid="/"+"/".join(ua['source']['page_id'].split('/')[1:3])
        source_service_id=dmap[_pageid][0]
    except:
        source_service_id=-1

    try:
        _pageid="/"+"/".join(ua['target']['page_id'].split('/')[1:3])
        target_service_id=dmap[_pageid][0]
    except:
        target_service_id=-1

    # function has been modified where one more argument is given
    # in order to avoid time-consuming processing of reading csv file
    # for every func call
    symbolic_reward=rm.ua_to_reward_id(transition_rewards_df,
                                       User_Action(ua['source']['page_id'],
                                                   ua['target']['page_id'],
                                                   ua['action']['order']))

    reward=reward_mapping[symbolic_reward]

    luas.append('{},{},{},{},{},{},{},{}\n'.format(user, 
                                          source_service_id, 
                                          target_service_id, 
                                          reward, 
                                          ua['source']['root']['type'], 
                                          ua['timestamp'], 
                                          ua['source']['page_id'], 
                                          ua['target']['page_id']))

#luas=natsorted(luas,alg=ns.ns.SIGNED)

with open(os.path.join(args.output,'user_actions.csv'), 'w') as o:
    o.writelines(luas)



recs=[]
for rec in recdb["recommendation"].find(query).sort("user"):

    try:
        user=rec['user']
    except:
        user=-1

    for service in rec['services']:
        recs.append('{},{},{},{}\n'.format(user, service, '1', rec['timestamp']))

#recs=natsorted(recs,alg=ns.ns.SIGNED)

with open(os.path.join(args.output,'recommendations.csv'), 'w') as o:
    o.writelines(recs)


# export user catalog
if config['User']['export']:

    # produce users csv with each user id along with the user's accessed services
    # query users from database for fields _id and accessed_services then create a list of rows
    # each rows contains two elements, first: user_id in string format and second: a space separated sorted list of accessed services 
    users = recdb['user'].find({},{'accessed_services':1})
    users = list(map(lambda x: [str(x['_id']), " ".join([str(service_id) for service_id in sorted(set(x['accessed_services']))])], users))

    # save the users list of rows to a csv file
    with open(os.path.join(args.output,'users.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerows(users)

# export service catalog
if config['Service']['export']:

    if config['Service']['from']=='page_map':

        _ss=natsorted(list(set(list(map(lambda x: x+'\n',ids)))),alg=ns.ns.SIGNED)
        ss=[]
        for s in _ss:
            try:
                ss.append(s.strip()+',"'+rdmap[s.strip()][1]+'",'+rdmap[s.strip()][0]+'\n')
            except:
                continue

    else: # 'source'
        _query=""
        if config['Service']['published']:
            _query={"status":"published"}
 
        _ss=natsorted(list(set(list(map(lambda x: str(x['_id'])+',"'+str(x['name'])+'"\n',recdb["service"].find(_query))))),alg=ns.ns.SIGNED)
        ss=[]
        for s in _ss:
            try:
                ss.append(s.strip()+','+rdmap[s.split(',')[0]]+'\n')
            except:
                continue

    with open(os.path.join(args.output,'services.csv'), 'w') as o:
        o.writelines(ss)


# calculate pre metrics
if config['Metrics']:

    run=pm.Runtime()
    run.recdb=recdb
    run.query=query
    run.config=config

    md={'timestamp':str(datetime.utcnow())}

    # get all functions found in pre_metrics module
    # apart from 'doc' func
    # run and save the result in dictionary
    # where key is the name of the function
    # and value what it returns
    # whereas, for each found functions
    # an extra key_doc element in dictionary is set
    # to save the text of the function
    funcs = list(map(lambda x: x[0], getmembers(pm, isfunction)))
    funcs = list(filter(lambda x: not x=='doc',funcs))
    for func in funcs:
        md[func+'_doc']=getattr(pm, func).text
        md[func]=getattr(pm, func)(run)


    jsonstr = json.dumps(md)

    print(jsonstr)

    # Using a JSON string
    with open(os.path.join(args.output,'pre_metrics.json'), 'w') as outfile:
        outfile.write(jsonstr)
