from cassandra.cluster import Cluster
hostname = '127.0.0.1'
keyspace = 'db1'
column_family = 'userInfo'
nodes = []
nodes.append(hostname)
cluster = Cluster(nodes)
session = cluster.connect(keyspace)

def createUserInfoCF():
    '''

    Create the column family 'UserInfo' in the cassandra keyspace

    :return:
    '''
    createColumnFamily = session.prepare("""
    create columnfamily if not exists userInfo(
    domain varchar primary key,
    usr_With_Most_Comment varchar,
    top3Loc_With_Most_Users list<text>,
    best5_Users list<text>);
    """)
    session.execute(createColumnFamily)
