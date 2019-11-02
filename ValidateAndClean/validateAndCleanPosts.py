import numpy as np

validatedAndCleaned = []
unique_posts = set([])
def validate_posts(cleanedPath):
    '''

    Validate necessary fields and clean duplicate rows for Posts XML file

    :param cleanedPath:
    :return List of rows each having dictionary of required fields:
    '''
    posts_list = np.load(cleanedPath + 'posts.npy', allow_pickle=True).tolist()
    for post in posts_list:
        if post['Id'] not in unique_posts:
            unique_posts.add(post['Id'])
            val = {}
            validatedAndCleaned.append(post)
    return validatedAndCleaned