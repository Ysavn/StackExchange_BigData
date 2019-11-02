from cassandra.cluster import Cluster

hostname = '127.0.0.1'
keyspace = 'db1'
column_family = 'postInfo'
nodes = []
nodes.append(hostname)
cluster = Cluster(nodes)
session = cluster.connect(keyspace)


def insertInPostInfoCF(domainName, postinfo_map):
    '''

    Inserts a row into Post_Info ColumnFamily with key as domainName

    :param domainName:
    :param Postinfo_map:
    :return:
    '''
    executeBQ = session.prepare(
        "insert into postInfo (domain, totalQuestions, unansweredQuestions, trendingTags, averageAnswersCount, mostViewedPosts, mostScoredPosts, averageTimeToAnswer) values (?, ?, ?, ?, ?, ?, ?);")
    session.execute(executeBQ,
                    (domainName, postinfo_map['totalQuestions'], postinfo_map['unansweredQuestions'], postinfo_map['trendingTags'], postinfo_map['averageAnswersCount'],
                    postinfo_map['mostViewedPosts'], postinfo_map['mostScoredPosts'], postinfo_map['averageTimeToAnswer']))
