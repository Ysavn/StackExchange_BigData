from cassandra.cluster import Cluster

hostname = '127.0.0.1'
keyspace = 'db1'
column_family = 'userInfo'
nodes = []
nodes.append(hostname)
cluster = Cluster(nodes)
session = cluster.connect(keyspace)

def insertInUserInfoCF(domainName, userinfo_map):
    '''

    Inserts a row into User_Info ColumnFamily with key as domainName

    :param domainName:
    :param userinfo_map:
    :return:
    '''
    executeBQ = session.prepare(
        "insert into userInfo (domain, usr_With_Most_Comment, best5_Users, top3Loc_With_Most_Users) values (?, ?, ?, ?);")
    session.execute(executeBQ,
                    (domainName, userinfo_map['usr_With_Most_Comment'], userinfo_map['best5_Users'],
                     userinfo_map['top3Loc_With_Most_Users']))
