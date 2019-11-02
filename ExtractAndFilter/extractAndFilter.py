import xml.etree.ElementTree as ET
from ExtractAndFilter import extractAndFilterBadges as EAC_Badges, extractAndFilterComments as EAC_Comments, \
    extractAndFilterUsers as EAC_Users, extractAndFilterPosts as EAC_Posts
import os
import numpy as np


def extractAndFilter(outputPath, inputPath):
    '''

    Extract the necessary fields and filter any duplicate row or row having missing fields
    for every required XML file in a domain, saving the result as numpy array

    :param outputPath:
    :param inputPath:
    :return:
    '''
    comment_tree = ET.parse(inputPath + 'Comments.xml')
    comment_root = comment_tree.getroot()

    user_tree = ET.parse(inputPath + 'Users.xml')
    user_root = user_tree.getroot()

    badge_tree = ET.parse(inputPath + 'Badges.xml')
    badge_root = badge_tree.getroot()

    post_tree = ET.parse(inputPath + 'Posts.xml')
    post_root = post_tree.getroot()

    if not os.path.isdir(outputPath):
        os.makedirs(outputPath)

    comments_with_userId = (np.array(EAC_Comments.extract_filter_comments(comment_root)))
    np.save(outputPath + 'Comments.npy', comments_with_userId)

    user_with_Loc = np.array(EAC_Users.extract_filter_users(user_root))
    np.save(outputPath + 'Users.npy', user_with_Loc)

    cleaned_badges_with_userId = (np.array(EAC_Badges.extract_filter_badges(badge_root)))
    np.save(outputPath + 'Badges.npy', cleaned_badges_with_userId)

    cleaned_posts_with_postId = (np.array(EAC_Posts.extract_filter_posts(post_root)))
    np.save(outputPath + 'posts.npy', cleaned_posts_with_postId)