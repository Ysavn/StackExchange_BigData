import numpy as np

validatedAndCleaned = []
unique_comments = set([])

def validate_comment(cleanedPath):
    '''

    Validate necessary fields and clean duplicate rows for Comments XML file

    :param cleanedPath:
    :return List of rows each having dictionary of required fields:
    '''
    comment_list = np.load(cleanedPath + 'Comments.npy', allow_pickle=True).tolist()
    for comment in comment_list:
        if comment['Id'] not in unique_comments:
            unique_comments.add(comment['Id'])
            val = {}
            val['UserId']=comment['UserId']
            validatedAndCleaned.append(val)
    return validatedAndCleaned