#!/usr/bin/env python3
import pandas as pd
import numpy as np
import math

class Runtime:
    def __init__(self):
        self.users=None
        self.services=None
        self.user_actions=None
        self.user_actions_all=None
        self.recommendations=None



# decorator to add the text attribute to function as major metric
def metric(txt):
    def wrapper(f):
        f.kind = "metric"
        f.doc = txt
        return f
    return wrapper

# decorator to add the text attribute to function
def statistic(txt):
    def wrapper(f):
        f.kind = "statistic"
        f.doc = txt
        return f
    return wrapper

# Metrics


@statistic('The initial date where metrics are calculated on')
def start(object):
    """
    Calculate the start date where metrics are calculated on
    found in min value between Pandas DataFrame object user_action
    and recommendation
    """
    return str(min(min(object.user_actions['Timestamp']),min(object.recommendations['Timestamp'])))


@statistic('The final date where metrics are calculated on')
def end(object):
    """
    Calculate the end date where metrics are calculated on
    found in max value between Pandas DataFrame object user_action
    and recommendation
    """
    return str(max(max(object.user_actions['Timestamp']),max(object.recommendations['Timestamp'])))


@statistic('The total number of unique users found in users.csv (if provided), otherwise in user_actions.csv')
def users(object):
    """
    Calculate the total number of unique users 
    found in Pandas DataFrame object users (if provided)
    or user_actions otherwise
    """
    return int(object.users['User'].nunique())


@statistic('The total number of unique services found in services.csv (if provided), otherwise in user_actions.csv')
def services(object):
    """
    Calculate the total number of unique services
    found in Pandas DataFrame object services (if provided)
    or user_actions otherwise (from both Source and Target Service)
    """
    return int(object.services['Service'].nunique())


@statistic('The total number of recommendations found in recommendations.csv')
def recommendations(object):
    """
    Calculate the total number of recommendations
    found in Pandas DataFrame object recommendations
    """
    return len(object.recommendations.index)


@statistic('The total number of recommendations for registered users found in recommendations.csv')
def recommendations_registered(object):
    """
    Calculate the total number of recommendations for registered users
    found in Pandas DataFrame object recommendations
    """
    return len(object.recommendations[object.recommendations['User'] != -1].index)


@statistic('The total number of recommendations for anonymous users found in recommendations.csv')
def recommendations_anonymous(object):
    """
    Calculate the total number of recommendations for anonymous users
    found in Pandas DataFrame object recommendations
    """
    return recommendations(object)-recommendations_registered(object)



@statistic('The percentage (%) of recommendations for registered users to the total recommendations')
def recommendations_registered_perc(object):
    """
    Calculate the percentage (%) of recommendations occurred 
    by registered users to the total recommendations
    found in Pandas DataFrame object recommendations (in two decimals)
    """
    return round(recommendations_registered(object)*100.0/recommendations(object),2)


@statistic('The percentage (%) of recommendations for anonymous users to the total recommendations')
def recommendations_anonymous_perc(object):
    """
    Calculate the percentage (%) of recommendations occurred 
    by anonymous users to the total recommendations
    found in Pandas DataFrame object recommendations (in two decimals)
    """
    return round(100.0-recommendations_registered_perc(object),2)


@statistic('The total number of user actions found in user_actions.csv')
def user_actions(object):
    """
    Calculate the total number of user_actions
    found in Pandas DataFrame object user_actions
    """
    return len(object.user_actions.index)


@statistic('The total number of user actions occurred by registered users found in user_actions.csv')
def user_actions_registered(object):
    """
    Calculate the total number of user_actions occurred by registered users
    found in Pandas DataFrame object user_actions
    """
    return len(object.user_actions[object.user_actions['User'] != -1].index)


@statistic('The total number of user actions occurred by anonymous users found in user_actions.csv')
def user_actions_anonymous(object):
    """
    Calculate the total number of user_actions occurred by anonymous users
    found in Pandas DataFrame object user_actions
    """
    return user_actions(object)-user_actions_registered(object)


@statistic('The percentage (%) of user actions occurred by registered users to the total user actions')
def user_actions_registered_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by registered users to the total user actions
    found in Pandas DataFrame object user_actions (in two decimals)
    """
    return round(user_actions_registered(object)*100.0/user_actions(object),2)


@statistic('The percentage (%) of user actions occurred by anonymous users to the total user actions')
def user_actions_anonymous_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by anonymous users to the total user actions
    found in Pandas DataFrame object user_actions (in two decimals)
    """
    return round(100.0-user_actions_registered_perc(object),2)


@statistic('The total number of user actions led to order found in user_actions.csv')
def user_actions_order(object):
    """
    Calculate the total number of user_actions led to order
    found in Pandas DataFrame object user_actions
    """
    return len(object.user_actions[object.user_actions['Reward'] == 1.0].index)


@statistic('The total number of user actions led to order by registered users found in user_actions.csv')
def user_actions_order_registered(object):
    """
    Calculate the total number of user_actions led to order by registered users
    found in Pandas DataFrame object user_actions
    """
    return len(object.user_actions[(object.user_actions['Reward'] == 1.0) & (object.user_actions['User'] != -1)].index)


@statistic('The total number of user actions led to order by anonymous users found in user_actions.csv')
def user_actions_order_anonymous(object):
    """
    Calculate the total number of user_actions led to order by anonymous users
    found in Pandas DataFrame object user_actions
    """
    return user_actions_order(object)-user_actions_order_registered(object)


@statistic('The percentage (%) of user actions occurred by registered users and led to order to the total user actions that led to order')
def user_actions_order_registered_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by registered users and led to order to the total user actions that led to order
    found in Pandas DataFrame object user_actions (in two decimals)
    """
    return round(user_actions_order_registered(object)*100.0/user_actions_order(object),2)


@statistic('The percentage (%) of user actions occurred by anonymous users and led to order to the total user actions that led to order')
def user_actions_order_anonymous_perc(object):
    """
    Calculate the percentage (%) of user actions occurred 
    by anonymous users and led to order to the total user actions that led to order
    found in Pandas DataFrame object user_actions (in two decimals)
    """
    return round(100.0-user_actions_order_registered_perc(object),2)


@statistic('The total number of user actions assosicated with the recommendation panel found in user_actions.csv')
def user_actions_panel(object):
    """
    Calculate the total number of user_actions assosicated with the recommendation panel
    found in Pandas DataFrame object user_actions
    """
    return len(object.user_actions[object.user_actions['Action'] == 'recommendation_panel'].index)


@statistic('The percentage (%) of user actions assosicated with the recommendation panel to the total user actions')
def user_actions_panel_perc(object):
    """
    Calculate the percentage (%) of user actions assosicated with 
    the recommendation panel to the total user actions
    found in Pandas DataFrame object user_actions (in two decimals)
    """
    return round(user_actions_panel(object)*100.0/user_actions(object),2)


@statistic('The total number of unique services found in recommendations.csv')
def total_unique_services_recommended(object):
    """
    Calculate the total number of unique services 
    found in recommendations.csv
    """
    return int(object.recommendations.nunique()['Service'])


@metric('The percentage (%) of unique services found in recommedations.csv to the total number of services (provided or found otherwise in user_actions.csv)')
def catalog_coverage(object):
    """
    Calculate the percentage (%) of unique services 
    found in recommedations.csv to the total number 
    of services (provided or found otherwise in user_actions.csv)
    """
    return round(total_unique_services_recommended(object)*100.0/services(object),2)


@statistic('The total number of unique users found in recommendations.csv')
def total_unique_users_recommended(object):
    """
    Calculate the total number of unique users 
    found in recommendations.csv
    """
    return int(object.recommendations.nunique()['User'])


@metric('The percentage (%) of unique users found in recommedations.csv to the total number of users (provided or found otherwise in user_actions.csv)')
def user_coverage(object):
    """
    Calculate the percentage (%) of unique users 
    found in recommedations.csv to the total number 
    of users (provided or found otherwise in user_actions.csv)
    """
    return round(total_unique_users_recommended(object)*100.0/users(object),2)


@metric('The ratio of user hits divided by the total number of users (user hit: a user that has accessed at least one service that is also a personal recommendation)')
def hit_rate(object):
    """
    For each user get the recommended services and the services the user accessed
    Check if the user has at least one accessed service in recommendations. If yes increase number of hits by one
    Divide by the total number of users
    """
    users = object.users.values.tolist()
    recs = object.recommendations.values.tolist()
    # Fill lookup dictionary with all services recommender per user id
    user_recs = dict()
    for item in recs:
        # skip anonymous users
        if item == -1:
            continue
        user_id = item[0]
        service_id = item[1]
        if user_id in user_recs.keys():
            user_recs[user_id].append(service_id)
        else:
            user_recs[user_id] = [service_id]
    
    hits = 0
    # For each user in users check if his accessed services are in his recommendations
    
    for user in users:
        user_id = user[0]
        # create a set of unique accessed services by user
        services = set(user[1])
        if user_id in user_recs.keys():
            # create a set of unique recommended services to the user
            recommendations = set(user_recs.get(user_id))
            # intersection should include services that have been both accessed by and recommended to the user 
            intersection = services.intersection(recommendations)
            # If the user has at least one service (both recommended and accessed), this user is considered a hit
            if len(intersection) > 0: 
                hits = hits + 1

    

    return round(hits/len(users),5)


@metric('The number of user clicks through recommendations panels divided by the total times recommendation panels were presented to users. Takes into account all historical data of user actions')
def click_through_rate(object):
    """
    Get only the user actions that present a recommendation panel to the user in the source page
    Those are actions with the following source paths:
     - /services
     - /services/
     - /services/c/{any category name}
    Count the items in above list as they represent the times recommendations panels were presented to the users of the portal
    Narrow the above list into a new subset by selecting only user actions that originate from a recommendation panel
    Those are actions that have the 'recommendation' string in the Action column
    Count the items in the subset as they represent the times users clicked through recommendations
    Divide the items of the subset with the items of the first list to get the click-through rate
    """
    
    # get user actions
    user_actions_all = object.user_actions_all.values.tolist()
    
    # filter only user actions with the needed source paths (/services, /services/, /services/c/...). 
    # source paths are on the [6] index of each list item
    user_actions_recpanel_views = list(filter(lambda x: x[6] in ['/services', '/services/'] or x[6].startswith('/services/c/'),user_actions_all))
    
    # further filter with those actions that they have 'recommender' 
    user_actions_recpanel_clicks = list(filter(lambda x: x[4]=='recommendation_panel',user_actions_recpanel_views))

    return round(len(user_actions_recpanel_clicks)/len(user_actions_recpanel_views),2)


@metric('The diversity of the recommendations according to Shannon Entropy. The entropy is 0 when a single item is always chosen or recommended, and log n when n items are chosen or recommended equally often.')
def diversity(object, anonymous=False):
    """
    Calculate Shannon Entropy. The entropy is 0 when a single item is always chosen or recommended, and log n when n items are chosen or recommended equally often.
    """
    # keep recommendations with or without anonymous suggestions
    # based on anonymous flag (default=False, i.e. ignore anonymous)
    if anonymous:
        recs=object.recommendations
    else:
        recs=object.recommendations[(object.recommendations['User'] != -1)]

    # this variable keeps the sum of user_norm (where user_norm is 
    # the count of how many times a User has been suggested)
    # however since no cutoff at per user recommendations is applied and 
    # also since each recommendation entry is one-to-one <user id> <service id> 
    # then the total number of recommendations is equal to this sum
    free_norm=len(recs.index) 

    # (remember that recommendations have been previously
    # filtered based on the existance of users in user.csv and 
    # services in services.csv)

    # user_norm
    # group recommendations entries by user id and 
    # then count how many times each user has been suggested
    gr_user=recs.groupby(['User']).count()

    # create a dictionary of user_norm in order to
    # map the user id to the respective user_norm
    # key=<user id> and value=<user_norm>
    d_user=gr_user['Service'].to_dict()

    # item_count
    # group recommendations entries by service id and 
    # then count how many times each service has been suggested
    gr_service=recs.groupby(['Service']).count()

    # create a dictionary of item_count in order to
    # map the service id to the respective item_count
    # key=<service id> and value=<item_count>
    d_service=gr_service['User'].to_dict()

    # each element represent the service's recommendations occurance
    # e.g. [1,6,7]
    # a service was recommended 1 time, another 6 times and another 7 times
    services_recommendation_count = np.array(list(d_service.values()))

    # the total number of recommendations
    n_recommendations = services_recommendation_count.sum()

    # element-wise computations (division for each service's recommendations occurance)
    recommended_probability = services_recommendation_count/n_recommendations

    # H=-Sum(p*logp) [element-wise]
    shannon_entropy = -np.sum(recommended_probability * np.log2(recommended_probability))

    return round(shannon_entropy,4)


@metric('Calculate novelty (Expected Free Discovery -EFD-) as the expected Inverse Collection Frequency -ICF- of (relevant and seen) recommended items')
def novelty(object, anonymous=False):
    """
    Calculate novelty (Expected Free Discovery -EFD-) as 
    the expected Inverse Collection Frequency -ICF- of 
    (relevant and seen) recommended items
    """
    # inner function to run on each pandas df row
    def nanmap(row):
        if np.isnan(row.values[0]):
            try:
                return gr_service_target['User'][row.name]
            except:
                return gr_service_source['User'][row.name]
        else:
            return row
    # no ranking (rank=1) - recommendation items are equally weighted
    # no relevance (p(rel)=1) - an item is liked, picked, enjoyed (not such info)
    # no discount - (disc(k)=1) - user views all recommendation items (not paging)

    # keep recommendations with or without anonymous suggestions
    # based on anonymous flag (default=False, i.e. ignore anonymous)
    if anonymous:
        recs=object.recommendations
        uas=object.user_actions
    else:
        recs=object.recommendations[(object.recommendations['User'] != -1)]
        uas=object.user_actions[(object.user_actions['User'] != -1)]

    # item_count
    # group user actions entries by service id and 
    # then count how many times each service has been suggested
    gr_service_source=uas.groupby(['Source_Service']).count()
    gr_service_target=uas.groupby(['Target_Service']).count()
    # merge above results
    gr_service=gr_service_source+gr_service_target
    # when nan value find a keep the other value (search on both dfs)
    gr_service=gr_service.apply(nanmap, axis=1)

    # create a dictionary of item_count in order to
    # map the service id to the respective item_count
    # key=<service id> and value=<item_count>
    d_service=gr_service['User'].to_dict()

    # this variable keeps the sum of user_norm (where user_norm is 
    # the count of how many times a User has been suggested)
    # however since no cutoff at per user recommendations is applied and 
    # also since each recommendation entry is one-to-one <user id> <service id> 
    # then the total number of recommendations is equal to this sum
    norm=sum(d_service.values())    

    # get the max novelty by getting the service with the lowest item_count
    max_nov=-math.log2(min(d_service.values())/norm)

    # calculate novelty for all services
    d_service = {service: -math.log2(item_count/norm) for service, item_count in d_service.items()} # fix user_actions not recommendations to gather services
 
    # get all unique users found in recommendations
    users = recs['User'].unique()

    # use max_nov -> min count if x service not found (removed functionality)
    d_user={}
    for u in users:
        u_norm=len(recs[(recs['User']==u)].index)
        d_user[u]=sum(list(map(lambda x: d_service.get(x, max_nov),recs[(recs['User']==u)]['Service'].tolist())))/u_norm # fix norm=number of recommended items per user

    # average value (not in elliot)
    return round(sum(d_user.values())/len(users),4)

@metric('The diversity of the recommendations according to GiniIndex. The index is 0 when all items are chosen equally often, and 1 when a single item is always chosen.')
def diversity_gini(object, anonymous=False):
    """
    Calculate GiniIndex based on https://elliot.readthedocs.io/en/latest/_modules/elliot/evaluation/metrics/diversity/gini_index/gini_index.html#GiniIndex. (see book https://link.springer.com/10.1007/978-1-4939-7131-2_110158)
    """
    # keep recommendations with or without anonymous suggestions
    # based on anonymous flag (default=False, i.e. ignore anonymous)
    if anonymous:
        recs=object.recommendations
    else:
        recs=object.recommendations[(object.recommendations['User'] != -1)]

    # this variable keeps the sum of user_norm (where user_norm is 
    # the count of how many times a User has been suggested)
    # however since no cutoff at per user recommendations is applied and 
    # also since each recommendation entry is one-to-one <user id> <service id> 
    # then the total number of recommendations is equal to this sum
    free_norm=len(recs.index) 

    # item_count
    # group recommendations entries by service id and 
    # then count how many times each service has been suggested
    gr_service=recs.groupby(['Service']).count()

    # create a dictionary of item_count in order to
    # map the service id to the respective item_count
    # key=<service id> and value=<item_count>
    d_service=gr_service['User'].to_dict()


    n_recommended_items = len(d_service)
    num_items = services(object)

    gini = sum([(2 * (j + 1 + num_items-n_recommended_items) -num_items -1) * (cs / free_norm) for j, cs in enumerate(sorted(d_service.values()))])

    gini /= (num_items - 1)
    gini = 1 - gini

    return round(gini,4)

@metric('The Top 5 recommended services according to recommendations entries')
def top5_services_recommended(object, k=5, base='https://marketplace.eosc-portal.eu', anonymous=False):
    """
    Calculate the Top 5 recommended service according to the recommendations entries.
    Return a list of list with the elements:
        #   (i) service id
        #  (ii) service name
        # (iii) service page appended with base (to create the URL)
        #  (iv) total number of recommendations of the service
        #   (v) percentage of the (iv) to the total number of recommendations 
        #       expressed in %, with or without anonymous, based on the function's flag
    Service's info is being retrieved from the servives.csv file 
    (i.e. each line forms: service_id, rating, service_name, page_id)
    """
    # keep recommendations with or without anonymous suggestions
    # based on anonymous flag (default=False, i.e. ignore anonymous)
    if anonymous:
        recs=object.recommendations
    else:
        recs=object.recommendations[(object.recommendations['User'] != -1)]

    # item_count
    # group recommendations entries by service id and 
    # then count how many times each service has been suggested
    gr_service=recs.groupby(['Service']).count()

    # create a dictionary of item_count in order to
    # map the service id to the respective item_count
    # key=<service id> and value=<item_count>
    d_service=gr_service['User'].to_dict()

    # convert dictionary to double list (list of lists)
    # where the sublist is <service_id> <item_count>
    # and sort them from max to min <item_count>
    l_service=list(map(lambda x: [x,d_service[x]],d_service))
    l_service.sort(key = lambda x: x[1], reverse=True)

    # get only the first k elements
    l_service=l_service[:k]

    topk_services=[]

    for service in l_service:
        # get service's info from dataframe
        _df_service=object.services[object.services['Service'].isin([service[0]])]
        # append a list with the elements:
        #   (i) service id
        #  (ii) service name
        # (iii) service page appended with base (to create the URL)
        #  (iv) total number of recommendations of the service
        #   (v) percentage of the (iv) to the total number of recommendations 
        #       expressed in %, with or without anonymous, based on the function's flag
        topk_services.append({"service_id": service[0], 
                              "service_name": str(_df_service['Name'].item()), 
                              "service_url": base+str(_df_service['Page'].item()), 
                              "recommendations": {
                                "value":service[1], 
                                "percentage": round(100*service[1]/len(recs.index),2),
                                "of_total": len(recs.index)
                                }
                            })

    return topk_services

@metric('The Top 5 ordered services according to user actions entries')
def top5_services_ordered(object, k=5, base='https://marketplace.eosc-portal.eu', anonymous=False):
    """
    Calculate the Top 5 ordered services according to user actions entries.
    User actions with Target Pages that lead to unknown services (=-1) are being ignored.
    Return a list of list with the elements:
        #   (i) service id
        #  (ii) service name
        # (iii) service page appended with base (to create the URL)
        #  (iv) total number of orders of the service
        #   (v) percentage of the (iv) to the total number of orders 
        #       expressed in %, with or without anonymous, based on the function's flag
    Service's info is being retrieved from the services.csv file 
    (i.e. each line forms: service_id, rating, service_name, page_id)
    """
    # keep user actions with or without anonymous suggestions
    # based on anonymous flag (default=False, i.e. ignore anonymous)
    # user_actions with Target Pages that lead to unknown services (=-1) are being ignored
    if anonymous:
        uas=object.user_actions[(object.user_actions['Reward'] == 1.0) & (object.user_actions['Target_Service'] != -1)  & (object.user_actions['User'] != -1)]
    else:
        uas=object.user_actions[(object.user_actions['Reward'] == 1.0) & (object.user_actions['Target_Service'] != -1)]

    # item_count
    # group user_actions entries by service id and 
    # then count how many times each service has been suggested
    gr_service=uas.groupby(['Target_Service']).count()

    # create a dictionary of item_count in order to
    # map the service id to the respective item_count
    # key=<service id> and value=<item_count>
    d_service=gr_service['User'].to_dict()

    # convert dictionary to double list (list of lists)
    # where the sublist is <service_id> <item_count>
    # and sort them from max to min <item_count>
    l_service=list(map(lambda x: [x,d_service[x]],d_service))
    l_service.sort(key = lambda x: x[1], reverse=True)

    # get only the first k elements
    l_service=l_service[:k]

    topk_services=[]

    for service in l_service:
        # get service's info from dataframe
        _df_service=object.services[object.services['Service'].isin([service[0]])]
        # append a list with the elements:
        #   (i) service id
        #  (ii) service name
        # (iii) service page appended with base (to create the URL)
        #  (iv) total number of orders of the service
        #   (v) percentage of the (iv) to the total number of orders 
        #       expressed in %, with or without anonymous, based on the function's flag
        topk_services.append({"service_id":service[0], 
                             "service_name": str(_df_service['Name'].item()), 
                             "service_url": base+str(_df_service['Page'].item()), 
                             "orders": {
                                "value": service[1], 
                                "percentage": round(100*service[1]/len(uas.index),2),
                                "of_total": len(uas.index)
                            }})

    return topk_services
