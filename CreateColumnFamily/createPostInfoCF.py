from cassandra.cluster import Cluster
hostname = '127.0.0.1'
keyspace = 'db1'
column_family = 'postInfo'
nodes = []
nodes.append(hostname)
cluster = Cluster(nodes)
session = cluster.connect(keyspace)

def createPostInfoCF():
    '''

    Create the column family 'PostInfo' in the cassandra keyspace

    :return:
    '''
    createColumnFamily = session.prepare("""
    create columnfamily if not exists postInfo(
    Domain TEXT PRIMARY KEY
    ,TotalQuestions INT
    ,UnansweredQuestions INT
    ,TrendingTags LIST<TEXT>
    ,AverageAnswersCount INT
    ,MostViewedPosts LIST<INT>
    ,MostScoredPosts LIST<INT>
    ,AverageTimeToAnswer INT
    """)
    session.execute(createColumnFamily)
