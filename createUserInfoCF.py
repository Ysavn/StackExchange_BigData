from cassandra.cluster import Cluster

hostname = '127.0.0.1'
keyspace = 'db1'
column_family = 'userInfo'
nodes = []
nodes.append(hostname)
cluster = Cluster(nodes)
session = cluster.connect(keyspace)

statement = session.prepare("""
create columnfamily if not exists userInfo(
id varchar primary key,
usrMstComment varchar,
top3ActiveLoc list<text>,
best5Users list<text>);
""")
session.execute(statement)
