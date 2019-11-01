import numpy as np

def top5UsersWithBadges(user_tree, validatedPath):
    '''

    Finds the top 5 users in a domain using badge count, i.e. sort in the following decreasing priority order:
    Gold -> Silver -> Bronze -> TotalBadges

    :param user_tree:
    :param validatedPath:
    :return List of DisplayNames of top 5 users in a domain:
    '''
    user_root = user_tree.getroot()
    user_map = {}
    for child_user in user_root:
        user_map[child_user.attrib['Id']] = child_user.attrib['DisplayName']
    user_badge_count_map = {}
    top5_Users = []
    badge_list = np.load(validatedPath + 'badges.npy', allow_pickle=True).tolist()
    for badge in badge_list:
        key = badge['UserId']
        if key in user_badge_count_map:
            val = user_badge_count_map[key]
            val[badge['Class']] += 1
            val['Total'] += 1
            user_badge_count_map[key] = val
        else:
            val = {'1': 0, '2': 0, '3': 0, 'Total': 0}
            val[badge['Class']] = 1
            val['Total'] = 1
            user_badge_count_map[key] = val
    topUserIds = sorted(user_badge_count_map.keys(), key=lambda x: (
    user_badge_count_map[x]['1'], user_badge_count_map[x]['2'], user_badge_count_map[x]['3'],
    user_badge_count_map[x]['Total']), reverse=True)
    for i in range(5):
        top5_Users.append(user_map[topUserIds[i]])
    return top5_Users
