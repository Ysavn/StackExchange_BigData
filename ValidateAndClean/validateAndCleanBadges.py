import numpy as np

validatedAndCleaned = []
unique_badges = set([])
def validate_badge(cleanedPath):
    '''

    Validate necessary fields and clean duplicate rows for Badges XML file

    :param cleanedPath:
    :return List of rows each having dictionary of required fields:
    '''
    badge_list = np.load(cleanedPath + 'badges.npy', allow_pickle=True).tolist()
    for badge in badge_list:
        if badge['Id'] not in unique_badges:
            unique_badges.add(badge['Id'])
            val = {}
            val['UserId'] = badge['UserId']
            val['Class'] = badge['Class']
            validatedAndCleaned.append(val)
    return validatedAndCleaned