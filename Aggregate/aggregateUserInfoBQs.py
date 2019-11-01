import xml.etree.ElementTree as ET
from Aggregate import userWithMostComments as UWithMostC, top3LocationWithMostUsers as MostUserLocs, \
    top5Users as top5Users

def aggregate(inputPath1, inputPath2):
    '''
    Aggregates for each BQ {Business Question} in answered by UserInfo Column Family
    :param inputPath1:
    :param inputPath2:
    :return A map with:
            Key = name of column for the BQ as in Cassandra Column Family
            Value = the answer for the BQ:
    '''
    user_tree = ET.parse(inputPath2 + 'Users.xml')
    map_solutions_BQs = {}
    map_solutions_BQs['best5_Users'] = top5Users.top5UsersWithBadges(user_tree, inputPath1)
    map_solutions_BQs['usr_With_Most_Comment'] = UWithMostC.userWithMostComments(user_tree, inputPath1)
    map_solutions_BQs['top3Loc_With_Most_Users'] = MostUserLocs.getTop3LocWithMostUsers(inputPath1)
    return map_solutions_BQs