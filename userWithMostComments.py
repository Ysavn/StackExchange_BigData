import xml.etree.ElementTree as ET
import filterCommentsWithoutUserId as FC
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

count_comments_per_userId = {}
for child_user in user_root:
    for child_comment in FC.filter_comments():
        if child_user.attrib['Id'] == child_comment['UserId']:
            if child_user.attrib['Id'] not in count_comments_per_userId:
                val = {'DisplayName': child_user.attrib['DisplayName'], 'commentCount': 1}
                count_comments_per_userId[child_user.attrib['Id']] = val
            else:
                val = count_comments_per_userId[child_user.attrib['Id']]
                val['commentCount'] += 1
                count_comments_per_userId[child_user.attrib['Id']] = val
mxComment = 0
userIdWithMaxComment = None
for child_user in user_root:
    key = child_user.attrib['Id']
    if key in count_comments_per_userId and count_comments_per_userId[key]['commentCount'] > mxComment:
        mxComment = count_comments_per_userId[key]['commentCount']
        userIdWithMaxComment = key

statement = session.prepare("insert into userInfo (id, usrMstComment) values (?, ?);")
session.execute(statement,
                ("astronomy.meta.stackexchange.com", count_comments_per_userId[userIdWithMaxComment]['DisplayName']))
