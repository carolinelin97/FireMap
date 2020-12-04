from pyspark import SparkContext
from pyspark.sql import SQLContext
import requests
import csv
import json
import copy
import math
from datetime import date
from datetime import datetime

wild_fire_link = 'https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/Active_Fires/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)
wf_raw_data = sc.parallelize(json.loads(requests.get(wild_fire_link).text)['features'])


ca_cities = []
with open('/Users/chloe/USC/INF_551/project/wildfire/data_upload/ca_cities.csv','r') as csvfile:
    data = csv.reader(csvfile)
    header = next(data)
    if header != None:
        for row in data:
                ca_cities.append(row)

'''
import pandas as pd
cities = pd.read_csv('/Users/chloe/Downloads/simplemaps_uscities/uscities.csv')
CA = cities[cities.state_id == 'CA'][['city','county_name','state_id','lat','lng','population']]
CA.to_csv('Documents/Study/INF_551/project/ca_cities.csv',index=False,header=True)
'''
def getDistance(lon1, lat1, lon2, lat2):
    R = 6371000
    x = (float(lon2) - float(lon1)) * math.cos(0.5*(float(lat2)+float(lat1)))
    y = (float(lat2) - float(lat1))
    return R * math.sqrt( x*x + y*y )

def getCity(partition,ca_cities):
    records = copy.deepcopy(list(partition))
    for row in records:
        if row['City'] is None:
            closest_distance = math.inf
            for city in ca_cities:
                distance = getDistance(row['Latitude'],row['Longitude'],city[3],city[4])
                if distance < closest_distance:
                    closest_distance = distance
                    closet_city = city
            row['City'] = closet_city[0].title()
        if ',' in row['City']:
            row['City'] = row['City'].split(',')[0].title()
        else:
            row['City'] = row['City'].title()
    return records

## select feature##
wild_fire = wf_raw_data.map(lambda x: x['attributes']) \
                       .filter(lambda x:x['InitialLatitude'] is not None and x['InitialLongitude'] is not None)\
                       .filter(lambda x: x['InitialLatitude']<42.1 and x['InitialLatitude']>32 and x['InitialLongitude']> -125 and x['InitialLongitude']< -113)\
                       .map(lambda x: {'UniqueID':x['UniqueFireIdentifier'],'IncidentName':x['IncidentName'].title(),\
                                       'FireDiscoveryDateTime':datetime.fromtimestamp(x['FireDiscoveryDateTime']/1000).strftime('%Y-%m-%d %H:%M:%S'),\
                                       'Latitude':x['InitialLatitude'],'Longitude':x['InitialLongitude'],\
                                       'City': x['POOCity'], 'County': x['POOCounty'].title(), 'State': x['POOState'].split('-')[1], \
                                       'FireCause':x['FireCause'],'DiscoveryAcres':x['DiscoveryAcres'],\
                                       'DailyAcres': x['DailyAcres'],'InitialResponseAcres':x['InitialResponseAcres'],\
                                       'PercentContained':x['PercentContained'],'ContainmentDateTime':x['ContainmentDateTime'],\
                                       'ControlDateTime':x['ControlDateTime']}) \
                        .filter(lambda x: x['State']=='CA') \
                        .mapPartitions(lambda x: getCity(x,ca_cities))\
                        .collect()

today = date.today()
#print(wild_fire)
load_data = dict(map(lambda x: (x.pop('UniqueID'),x),wild_fire))
url = 'https://wildfire-40a78.firebaseio.com/'
#print('{"'+ str(today) +'":'+ json.dumps(load_data) + '}')
requests.put(url+str(today)+'.json',json.dumps(load_data))

