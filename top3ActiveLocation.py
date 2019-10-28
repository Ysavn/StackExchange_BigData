import filterUsersWithoutLocation as FU
from geopy.exc import GeocoderTimedOut

from geopy.geocoders import Nominatim
geo_locator = Nominatim()
from cassandra.cluster import Cluster

hostname = '127.0.0.1'
keyspace = 'db1'
column_family = 'userInfo'
nodes = []
nodes.append(hostname)
cluster = Cluster(nodes)
session = cluster.connect(keyspace)

country_map = {}
abbr = {'USA':'United States of America', 'UK':'United Kingdom'}
for child_user in FU.filter_users():
    address = child_user['Location']
    try:
        location = geo_locator.geocode(address)
    except GeocoderTimedOut:
        continue
    if location is not None:
        country = location.address.split(',')[-1].lstrip()
        if country in abbr.keys():
            country = abbr[country]
        if country in country_map.keys():
            country_map[country]+=1
        else:
            country_map[country]=1
top_locations = sorted(country_map.keys(), key = lambda x : (country_map[x]), reverse=True)
statement = session.prepare("update userInfo set top3ActiveLoc=? where id=?;")
session.execute(statement, (top_locations[0:3], "astronomy.meta.stackexchange.com"))
