import numpy as np

def getTop3LocWithMostUsers(validatedPath):
    '''

    Evaluate the top 3 countries, having the maximum number of users
    :param validatedPath:
    :return List of the names of top 3 countries:
    '''
    user_loc_list = np.load(validatedPath + 'Users.npy', allow_pickle=True).tolist()
    country_map = {}
    for user_loc in user_loc_list:
        location = user_loc['Location']
        if location in country_map:
            country_map[location]+=1
        else:
            country_map[location]=1
    return sorted(country_map.keys(), key = lambda x : country_map[x], reverse=True)[0:3]