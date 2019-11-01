import numpy as np
from geopy.geocoders import Nominatim
import time
geo_locator = Nominatim()

validatedAndCleaned = []
abbr = {'USA':'United States of America', 'UK':'United Kingdom', 'United States':'United States of America'}
def validate_user_loc(cleanedPath):
    '''

    Validate necessary fields and clean duplicate rows for Users XML file

    :param cleanedPath:
    :return List of rows each having dictionary of required fields:
    '''
    user_list = np.load(cleanedPath + 'Users.npy', allow_pickle=True).tolist()
    for user in user_list:
        try:
            location = geo_locator.geocode(user['Location'])
        except Exception as e:
            continue
        if location is not None:
            country = location.address.split(',')[-1].lstrip()
            if country in abbr.keys():
                country = abbr[country]
            user_value = user
            user_value['Location'] = country
            #print(user_value)
            validatedAndCleaned.append(user_value)
        time.sleep(1)
    return validatedAndCleaned