import xml.etree.ElementTree as ET
from cassandra.cluster import Cluster

hostname = '127.0.0.1'
keyspace = 'db1'
column_family = 'userInfo'
nodes = []
nodes.append(hostname)
cluster = Cluster(nodes)
session = cluster.connect(keyspace)

user_tree = ET.parse('/Users/avneet/Documents/Fall-19/SE_BD_ExtractedFolder/astronomy.meta.stackexchange.com/Users.xml')
user_root = user_tree.getroot()

badge_tree = ET.parse(
    '/Users/avneet/Documents/Fall-19/SE_BD_ExtractedFolder/astronomy.meta.stackexchange.com/Badges.xml')
badge_root = badge_tree.getroot()

user_badge = {}
for child_user in user_root:
    for child_badge in badge_root:
        if child_user.attrib['Id'] == child_badge.attrib['UserId']:
            if child_user.attrib['Id'] in user_badge:
                key = child_user.attrib['Id']
                val = user_badge[key]
                val[child_badge.attrib['Class']] += 1
                val['Total'] += 1
                user_badge[key] = val
            else:
                key = child_user.attrib['Id']
                val = {'DisplayName': child_user.attrib['DisplayName'], '1': 0, '2': 0, '3': 0, 'Total': 0}
                val[child_badge.attrib['Class']] = 1
                val['Total'] = 1
                user_badge[key] = val
top_user_ids = sorted(user_badge.keys(),
       key=lambda x: (user_badge[x]['1'], user_badge[x]['2'], user_badge[x]['3'], user_badge[x]['Total']), reverse=True)
top5Users = []
for i in range(5):
    top5Users.append(user_badge[top_user_ids[i]]['DisplayName'])
statement = session.prepare("update userInfo set best5Users=? where id=?;")
session.execute(statement, (top5Users, "astronomy.meta.stackexchange.com"))

