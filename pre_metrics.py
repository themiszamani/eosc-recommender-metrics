#!/usr/bin/env python3
import pandas as pd
import numpy as np


class Runtime:
    def __init__(self):
        self.query={}
        self.recdb=None
        self.config=None

# decorator to add the text attribute to function
def doc(r):
    def wrapper(f):
        f.text = r
        return f
    return wrapper


# Pre Metrics
@doc('The type of the resource')
def type(object):
    """
    The type of the resource, e.g. service
    """
    # currently
    return "service"

# Pre Metrics
@doc('The provider of the resource')
def provider(object):
    """
    The provider of the resource, e.g. cyfronet
    """
    # currently
    return "cyfronet"


@doc('The initial date where metrics are calculated on')
def start(object):
    """
    Calculate the start date where metrics are calculated on
    found in min value between source object user_action
    and recommendation
    """
    ua_start=object.recdb["user_action"].find_one(object.query,sort=[("timestamp", 1)])["timestamp"]
    rec_start=object.recdb["recommendation"].find_one(object.query,sort=[("timestamp", 1)])["timestamp"]

    return str(min(ua_start, rec_start))


@doc('The final date where metrics are calculated on')
def end(object):
    """
    Calculate the end date where metrics are calculated on
    found in max value between source object user_action
    and recommendation
    """
    ua_end=object.recdb["user_action"].find_one(object.query,sort=[("timestamp", -1)])["timestamp"]
    rec_end=object.recdb["recommendation"].find_one(object.query,sort=[("timestamp", -1)])["timestamp"]
    return str(max(ua_end, rec_end))


@doc('The total number of unique users found in users of the source')
def users(object):
    """
    Calculate the total number of unique users 
    found in source object
    """
    return object.recdb["user"].count_documents({})


@doc('The total number of unique services found in services of the source')
def services(object):
    """
    Calculate the total number of unique services
    found in source object (default to published only)
    """
    if object.config['Service']['published']:
        return object.recdb["service"].count_documents({"status":"published"})
    else:
        return object.recdb["service"].count_documents({})


@doc('The total number of recommendation_actions found in recommendation_actions of the source')
def recommendation_actions(object):
    """
    Calculate the total number of recommendation_actions
    found in source object
    """
    return object.recdb["recommendation"].count_documents(object.query)

@doc('The total number of recommendation_actions for registered users found in recommendation_actions.csv')
def recommendation_actions_registered(object):
    """
    Calculate the total number of recommendation_actions for registered users
    found in Pandas DataFrame object recommendation_actions
    """
    return object.recdb["recommendation"].count_documents({**object.query,**{"user":{"$exists":True}}})


@doc('The total number of recommendation_actions for anonymous users found in recommendation_actions.csv')
def recommendation_actions_anonymous(object):
    """
    Calculate the total number of recommendation_actions for anonymous users
    found in Pandas DataFrame object recommendation_actions
    """
    return recommendation_actions(object)-recommendation_actions_registered(object)


@doc('The percentage (%) of recommendation_actions for registered users to the total recommendation_actions')
def recommendation_actions_registered_perc(object):
    """
    Calculate the percentage (%) of recommendation_actions occurred 
    by registered users to the total recommendation_actions
    found in Pandas DataFrame object recommendation_actions (in two decimals)
    """
    return round(recommendation_actions_registered(object)*100.0/recommendation_actions(object),2)


@doc('The percentage (%) of recommendation_actions for anonymous users to the total recommendation_actions')
def recommendation_actions_anonymous_perc(object):
    """
    Calculate the percentage (%) of recommendation_actions occurred 
    by anonymous users to the total recommendation_actions
    found in Pandas DataFrame object recommendation_actions (in two decimals)
    """
    return round(100.0-recommendation_actions_registered_perc(object),2)


@doc('The total number of user actions found in user actions of the source')
def user_actions(object):
    """
    Calculate the total number of user_actions
    found in source object
    """
    return object.recdb["user_action"].count_documents(object.query)


@doc('The total number of user actions occurred by registered users found in user actions of the source')
def user_actions_registered(object):
    """
    Calculate the total number of user_actions occurred by registered users
    found in source object
    """
    return object.recdb["user_action"].count_documents({**object.query,**{"user":{"$exists":True}}})


@doc('The total number of user actions occurred by anonymous users found in user actions of the source')
def user_actions_anonymous(object):
    """
    Calculate the total number of user_actions occurred by anonymous users
    found in source object
    """
    return user_actions(object)-user_actions_registered(object)


@doc('The percentage (%) of user actions occurred by registered users to the total user actions')
def user_actions_registered_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by registered users to the total user actions
    found in source object user_actions (in two decimals)
    """
    return round(user_actions_registered(object)*100.0/user_actions(object),2)


@doc('The percentage (%) of user actions occurred by anonymous users to the total user actions')
def user_actions_anonymous_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by anonymous users to the total user actions
    found in source object user_actions (in two decimals)
    """
    return round(100.0-user_actions_registered_perc(object),2)


@doc('The total number of user actions led to order found in user actions of the source')
def user_actions_order(object):
    """
    Calculate the total number of user_actions led to order
    found in source object user_actions
    """
    return object.recdb["user_action"].count_documents({**object.query, **{"action.order":True}})


@doc('The total number of user actions led to order by registered users found in user actions of the source')
def user_actions_order_registered(object):
    """
    Calculate the total number of user_actions led to order by registered users
    found in source object user_actions
    """
    return object.recdb["user_action"].count_documents({**object.query, **{"action.order":True,"user":{"$exists":True}}})


@doc('The total number of user actions led to order by anonymous users found in user actions of the source')
def user_actions_order_anonymous(object):
    """
    Calculate the total number of user_actions led to order by anonymous users
    found in source object user_actions
    """
    return user_actions_order(object)-user_actions_order_registered(object)


@doc('The percentage (%) of user actions occurred by registered users and led to order to the total user actions that led to order')
def user_actions_order_registered_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by registered users and led to order to the total user actions that led to order
    found in source object user_actions (in two decimals)
    """
    return round(user_actions_order_registered(object)*100.0/user_actions_order(object),2)


@doc('The percentage (%) of user actions occurred by anonymous users and led to order to the total user actions that led to order')
def user_actions_order_anonymous_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by anonymous users and led to order to the total user actions that led to order
    found in source object user_actions (in two decimals)
    """
    return round(100.0-user_actions_order_registered_perc(object),2)


@doc('The total number of user actions assosicated with the recommendation panel found in user actions of the source')
def user_actions_panel(object):
    """
    Calculate the total number of user_actions assosicated with the recommendation panel
    found in source object user_actions
    """
    return object.recdb["user_action"].count_documents({**object.query, **{"source.root.type":"recommendation_panel"}})


@doc('The percentage (%) of user actions assosicated with the recommendation panel to the total user actions')
def user_actions_panel_perc(object):
    """
    Calculate the percentage (%) of user actions assosicated with 
    the recommendation panel to the total user actions
    found in source object user_actions (in two decimals)
    """
    return round(user_actions_panel(object)*100.0/user_actions(object),2)

