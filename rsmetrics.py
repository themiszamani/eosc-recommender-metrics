#!/usr/bin/env python3
import sys, argparse
import json
import yaml
from datetime import datetime, timezone
import os
import pandas as pd


__copyright__ = "© "+str(datetime.utcnow().year)+", National Infrastructures for Research and Technology (GRNET)"

__author__= 'Nikolaos Triantafyllis (triantafyl@noa.gr)'
__license__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Nikolaos Triantafyllis"
__email__ = "triantafyl@noa.gr"
__status__ = "Production"
__version__ = "1.0"


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
        print('License: ' + __license__)
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

optional.add_argument('--users', metavar=('INT'), help='provide the total number of users otherwise it will be calculated according to the user actions', type=int, default=None)
optional.add_argument('--services', metavar=('INT'), help='provide the total number of services otherwise it will be calculated according to the user actions', type=int, default=None)

optional.add_argument('-h', '--help', action='help', help='show this help message and exit')
optional.add_argument('-v', '--version', action='version', version='%(prog)s v'+__version__)

#args=parser.parse_args(args=None if sys.argv[1:] else ['--help'])

args=parser.parse_args()

class Metrics:
    pass

m=Metrics()

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
uas=pd.read_csv(os.path.join(args.input,'dataset.csv'),names=["User", "Service", "Reward", "Action", "Timestamp"])
recs=pd.read_csv(os.path.join(args.input,'recommendations.csv'),names=["User", "Service", "Rating", "Timestamp"])

# convert timestamp column to datetime object
uas['Timestamp']= pd.to_datetime(uas['Timestamp'])
recs['Timestamp']= pd.to_datetime(recs['Timestamp'])

# restrict data to datetime range
if args.starttime:
    uas=uas[(uas['Timestamp'] > args.starttime) & (uas['Timestamp'] < args.endtime)]
    recs=recs[(recs['Timestamp'] > args.starttime) & (recs['Timestamp'] < args.endtime)]

else:
    uas=uas[uas['Timestamp'] < args.endtime]
    recs=recs[recs['Timestamp'] < args.endtime]

# get uniq values per column of user actions
uniq_uas=uas.nunique()
uniq_recs=recs.nunique()

m.users=int(uniq_uas['User']) if not args.users else args.users
m.services=int(uniq_uas['Service']) if not args.services else args.services

m.recommendations=len(recs.index)
m.user_actions=len(uas.index)

m.user_actions_registered=len(uas[uas['User'] != -1].index)
m.user_actions_anonymous=m.user_actions-m.user_actions_registered

m.user_actions_registered_perc=round(m.user_actions_registered*100.0/m.user_actions,2)
m.user_actions_anonymous_perc=100-m.user_actions_registered_perc

m.user_actions_order=len(uas[uas['Reward'] == 1.0].index)

m.user_actions_order_registered=len(uas[(uas['Reward'] == 1.0) & (uas['User'] != -1)].index)
m.user_actions_order_anonymous=m.user_actions_order-m.user_actions_order_registered
m.user_actions_order_registered_perc=round(m.user_actions_order_registered*100.0/m.user_actions_order,2)
m.user_actions_order_anonymous_perc=100-m.user_actions_order_registered_perc

m.user_actions_panel=len(uas[uas['Action'] == 'recommendation_panel'].index)
m.user_actions_panel_perc=round(m.user_actions_panel*100.0/m.user_actions,2)

m.services_suggested=int(uniq_recs['Service'])

# catalog coverage
m.services_suggested_perc=round(m.services_suggested*100.0/m.services,2)

# user coverage
m.users_suggested=int(uniq_recs['User'])
m.users_suggested_perc=round(m.users_suggested*100.0/m.users,2)


jsonstr = json.dumps(m.__dict__)
print(jsonstr)

# Using a JSON string
with open(os.path.join(args.input,'metrics.json'), 'w') as outfile:
    outfile.write(jsonstr)
