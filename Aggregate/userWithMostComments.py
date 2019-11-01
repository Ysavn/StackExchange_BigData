import xml.etree.ElementTree as ET
import numpy as np

def userWithMostComments(user_tree, validatedPath):
    '''

    Aggregates number of comments for each userId, sorts them in decreasing order
    and finally returns the first userId having the maximum comment count

    :param user_tree:
    :param validatedPath:
    :return DisplayName of UserId having maximum comments:
    '''
    user_root = user_tree.getroot()
    user_map = {}
    for child_user in user_root:
        user_map[child_user.attrib['Id']] = child_user.attrib['DisplayName']

    user_comment_count_map = {}
    comment_list = np.load(validatedPath + 'Comments.npy', allow_pickle=True).tolist()
    for comment in comment_list:
        key = comment['UserId']
        if key in user_comment_count_map:
            user_comment_count_map[key]+=1
        else:
            user_comment_count_map[key]=1
    userIdsWithMostComments = sorted(user_comment_count_map.keys(), key = lambda x: user_comment_count_map[x], reverse=True)
    return user_map[userIdsWithMostComments[0]]


