import xml.etree.ElementTree as ET
def filter_users():
    user_tree = ET.parse(
        '/Users/avneet/Documents/Fall-19/SE_BD_ExtractedFolder/astronomy.meta.stackexchange.com/Users.xml')
    user_root = user_tree.getroot()

    filter_users_with_loc = []
    for child_user in user_root:
        if 'Location' in child_user.attrib:
            filter_users_with_loc.append(child_user.attrib)
    return filter_users_with_loc
