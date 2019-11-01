#extract Id & UserId from Comments XML and filter out rows that don't have an UserId
def extract_filter_comments(comment_root):
    '''

    Extract the necessary fields and filter any duplicate row or row having missing fields
    for Comments XML file in a domain

    :param comment_root:
    :return List of rows each having dictionary of required fields:
    '''
    filtered_comments_with_userId = []
    for child_comment in comment_root:
        if 'UserId' in child_comment.attrib:
            child_comment_attribs = {}
            child_comment_attribs['Id'] = child_comment.attrib['Id']
            child_comment_attribs['UserId'] = child_comment.attrib['UserId']
            filtered_comments_with_userId.append(child_comment_attribs)
    return filtered_comments_with_userId
