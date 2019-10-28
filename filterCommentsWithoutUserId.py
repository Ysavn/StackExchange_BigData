import xml.etree.ElementTree as ET

def filter_comments():
    comment_tree = ET.parse(
        '/Users/avneet/Documents/Fall-19/SE_BD_ExtractedFolder/astronomy.meta.stackexchange.com/Comments.xml')
    comment_root = comment_tree.getroot()

    filtered_comments_with_userId = []
    for child_comment in comment_root:
        if 'UserId' in child_comment.attrib:
            filtered_comments_with_userId.append(child_comment.attrib)
    return filtered_comments_with_userId
