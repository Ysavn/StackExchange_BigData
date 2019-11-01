#Extract Id, UserId & Class from Badges XML filtering out rows not having UserId or Class
def extract_filter_badges(badge_root):
    '''

    Extract the necessary fields and filter any duplicate row or row having missing fields
    for Badges XML file in a domain

    :param badge_root:
    :return List of rows each having dictionary of required fields:
    '''
    filtered_badges_with_userId = []
    for child_badge in badge_root:
        if 'UserId' in child_badge.attrib and 'Class' in child_badge.attrib:
            child_badges_attribs = {}
            child_badges_attribs['Id'] = child_badge.attrib['Id']
            child_badges_attribs['UserId'] = child_badge.attrib['UserId']
            child_badges_attribs['Class'] = child_badge.attrib['Class']
            filtered_badges_with_userId.append(child_badges_attribs)
    return filtered_badges_with_userId
