#extract required attributes from Posts XML
def extract_filter_posts(post_root):
    '''

    Extract the necessary fields and filter any duplicate row or row having missing fields
    for Posts XML file in a domain

    :param post_root:
    :return List of rows each having dictionary of required fields:
    '''
    filtered_posts = []
    for child_post in post_root:
        child_post_attribs = {}
        child_post_attribs['Id'] = child_post.attrib['Id']
        child_post_attribs['PostTypeId'] = child_post.attrib['PostTypeId']
        child_post_attribs['AcceptedAnswerId'] = child_post.attrib['AcceptedAnswerId']
        child_post_attribs['CreationDate'] = child_post.attrib['CreationDate']
        child_post_attribs['AnswerCount'] = child_post.attrib['AnswerCount']
        child_post_attribs['ViewCount'] = child_post.attrib['ViewCount']
        child_post_attribs['Score'] = child_post.attrib['Score']
        child_post_attribs['Tags'] = child_post.attrib['Tags']
        filtered_posts.append(child_post_attribs)
    return filtered_posts
