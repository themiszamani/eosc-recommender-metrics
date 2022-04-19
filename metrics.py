#!/usr/bin/env python3
import pandas as pd
import numpy as np


class Runtime:
    def __init__(self):
        self.users=None
        self.services=None
        self.user_actions=None
        self.recommendations=None

# decorator to add the text attribute to function
def doc(r):
    def wrapper(f):
        f.text = r
        return f
    return wrapper


# Metrics

@doc('The total number of unique users found in users.csv (if provided), otherwise in user_actions.csv')
def users(object):
    """
    Calculate the total number of unique users 
    found in Pandas DataFrame object users (if provided)
    or user_actions otherwise
    """
    if isinstance(object.users, pd.DataFrame):
        return int(object.users.nunique()['User'])
    else:
        return int(object.user_actions.nunique()['User'])


@doc('The total number of unique services found in services.csv (if provided), otherwise in user_actions.csv')
def services(object):
    """
    Calculate the total number of unique services
    found in Pandas DataFrame object services (if provided)
    or user_actions otherwise
    """
    if isinstance(object.services, pd.DataFrame):
        return int(object.services.nunique()['Service'])
    else:
        return int(object.user_actions.nunique()['Service'])


@doc('The total number of recommendations found in recommendations.csv')
def recommendations(object):
    """
    Calculate the total number of recommendations
    found in Pandas DataFrame object recommendations
    """
    return len(object.recommendations.index)


@doc('The total number of user actions found in user_actions.csv')
def user_actions(object):
    """
    Calculate the total number of user_actions
    found in Pandas DataFrame object user_actions
    """
    return len(object.user_actions.index)


@doc('The total number of user actions occurred by registered users found in user_actions.csv')
def user_actions_registered(object):
    """
    Calculate the total number of user_actions occurred by registered users
    found in Pandas DataFrame object user_actions
    """
    return len(object.user_actions[object.user_actions['User'] != -1].index)


@doc('The total number of user actions occurred by anonymous users found in user_actions.csv')
def user_actions_anonymous(object):
    """
    Calculate the total number of user_actions occurred by anonymous users
    found in Pandas DataFrame object user_actions
    """
    return user_actions(object)-user_actions_registered(object)


@doc('The percentage (%) of user actions occurred by registered users to the total user actions')
def user_actions_registered_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by registered users to the total user actions
    found in Pandas DataFrame object user_actions (in two decimals)
    """
    return round(user_actions_registered(object)*100.0/user_actions(object),2)


@doc('The percentage (%) of user actions occurred by anonymous users to the total user actions')
def user_actions_anonymous_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by anonymous users to the total user actions
    found in Pandas DataFrame object user_actions (in two decimals)
    """
    return round(100.0-user_actions_registered_perc(object),2)


@doc('The total number of user actions led to order found in user_actions.csv')
def user_actions_order(object):
    """
    Calculate the total number of user_actions led to order
    found in Pandas DataFrame object user_actions
    """
    return len(object.user_actions[object.user_actions['Reward'] == 1.0].index)


@doc('The total number of user actions led to order by registered users found in user_actions.csv')
def user_actions_order_registered(object):
    """
    Calculate the total number of user_actions led to order by registered users
    found in Pandas DataFrame object user_actions
    """
    return len(object.user_actions[(object.user_actions['Reward'] == 1.0) & (object.user_actions['User'] != -1)].index)


@doc('The total number of user actions led to order by anonymous users found in user_actions.csv')
def user_actions_order_anonymous(object):
    """
    Calculate the total number of user_actions led to order by anonymous users
    found in Pandas DataFrame object user_actions
    """
    return user_actions_order(object)-user_actions_order_registered(object)


@doc('The percentage (%) of user actions occurred by registered users and led to order to the total user actions that led to order')
def user_actions_order_registered_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by registered users and led to order to the total user actions that led to order
    found in Pandas DataFrame object user_actions (in two decimals)
    """
    return round(user_actions_order_registered(object)*100.0/user_actions_order(object),2)


@doc('The percentage (%) of user actions occurred by anonymous users and led to order to the total user actions that led to order')
def user_actions_order_anonymous_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by anonymous users and led to order to the total user actions that led to order
    found in Pandas DataFrame object user_actions (in two decimals)
    """
    return round(100.0-user_actions_order_registered_perc(object),2)


@doc('The total number of user actions assosicated with the recommendation panel found in user_actions.csv')
def user_actions_panel(object):
    """
    Calculate the total number of user_actions assosicated with the recommendation panel
    found in Pandas DataFrame object user_actions
    """
    return len(object.user_actions[object.user_actions['Action'] == 'recommendation_panel'].index)


@doc('The percentage (%) of user actions assosicated with the recommendation panel to the total user actions')
def user_actions_panel_perc(object):
    """
    Calculate the percentage (%) of user actions assosicated with 
    the recommendation panel to the total user actions
    found in Pandas DataFrame object user_actions (in two decimals)
    """
    return round(user_actions_panel(object)*100.0/user_actions(object),2)


@doc('The total number of unique services found in recommendations.csv')
def catalog_coverage(object):
    """
    Calculate the total number of unique services 
    found in recommendations.csv
    """
    return int(object.recommendations.nunique()['Service'])


@doc('The percentage (%) of unique services found in recommedations.csv to the total number of services (provided or found otherwise in user_actions.csv)')
def catalog_coverage_perc(object):
    """
    Calculate the percentage (%) of unique services 
    found in recommedations.csv to the total number 
    of services (provided or found otherwise in user_actions.csv)
    """
    return round(catalog_coverage(object)*100.0/services(object),2)


@doc('The total number of unique users found in recommendations.csv')
def user_coverage(object):
    """
    Calculate the total number of unique users 
    found in recommendations.csv
    """
    return int(object.recommendations.nunique()['User'])


@doc('The percentage (%) of unique users found in recommedations.csv to the total number of users (provided or found otherwise in user_actions.csv)')
def user_coverage_perc(object):
    """
    Calculate the percentage (%) of unique users 
    found in recommedations.csv to the total number 
    of users (provided or found otherwise in user_actions.csv)
    """
    return round(user_coverage(object)*100.0/users(object),2)


