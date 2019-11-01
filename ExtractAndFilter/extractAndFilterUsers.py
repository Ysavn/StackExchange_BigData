#Extract out Id and Location from User XML and filter out rows not having a location attribute
def extract_filter_users(user_root):
    '''

    Extract the necessary fields and filter any duplicate row or row having missing fields
    for Users XML file in a domain

    :param user_root:
    :return List of rows each having dictionary of required fields:
    '''
    filter_users_with_loc = []
    for child_user in user_root:
        if 'Location' in child_user.attrib:
            child_user_attribs = {}
            child_user_attribs['Id'] = child_user.attrib['Id']
            child_user_attribs['Location'] = child_user.attrib['Location']
            filter_users_with_loc.append(child_user_attribs)
    return filter_users_with_loc