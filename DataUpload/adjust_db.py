from datetime import date
import requests
import json

'''
with open('./wildfire.json') as input_file:
    db_data = json.load(input_file)

for date,level_1 in db_data.items():
    for ID,level_2 in level_1.items():
        Incident_Name= level_2.get('IncidentName') or 'Unknown'
        city = level_2['City']
        county = level_2['County']
        Latitude = level_2['Latitude']
        Longitude = level_2['Longitude']
        State = level_2['State']
        Discovery_Acres = level_2.get('DiscoveryAcres') or -99 #level_2['DiscoveryAcres']
        Fire_Cause = level_2.get('FireCause') or 'Unknown' #level_2['FireCause']
        Daily_Acres = level_2.get('DailyAcres') or -99 #level_2['DailyAcres']
        Initial_Response_Acres = level_2.get('InitialResponseAcres') or -99 #level_2['InitialResponseAcres']
        Fire_Discovery_Date_Time = level_2.get('FireDiscoveryDateTime') or 'Unknown' #level_2['FireDiscoveryDateTime']
        Percent_Contained = level_2.get('PercentContained') or -99 #level_2['PercentContained']
        Containment_DateTime = level_2.get('ContainmentDateTime') or 'Unknown' #level_2['ContainmentDateTime']
        Control_DateTime = level_2.get('ControlDateTime') or 'Unknown' #level_2['ControlDateTime']
        with open('./insert.txt','a') as output:
            output.write("INSERT INTO instances VALUES('" + "','".join([ID,Incident_Name,city,county,State,date]) + "'," + ",".join([str(Latitude),str(Longitude),str(Discovery_Acres),str(Daily_Acres),str(Initial_Response_Acres)]) + ",'" + "','".join([Fire_Cause,Fire_Discovery_Date_Time])+"',"+str(Percent_Contained) + ",'" +"','".join([Containment_DateTime,Control_DateTime]) +"');\n")
'''
date = str(date.today())
url = 'https://wildfire-40a78.firebaseio.com/'
response = requests.get(url+date+".json").text
db_data = json.loads(response)

with open('./insert.txt','w') as output:
    output.close()

for ID,level_2 in db_data.items():
    Incident_Name= level_2.get('IncidentName') or 'Unknown'
    city = level_2['City']
    county = level_2['County']
    Latitude = level_2['Latitude']
    Longitude = level_2['Longitude']
    State = level_2['State']
    Discovery_Acres = level_2.get('DiscoveryAcres') or -99 #level_2['DiscoveryAcres']
    Fire_Cause = level_2.get('FireCause') or 'Unknown' #level_2['FireCause']
    Daily_Acres = level_2.get('DailyAcres') or -99 #level_2['DailyAcres']
    Initial_Response_Acres = level_2.get('InitialResponseAcres') or -99 #level_2['InitialResponseAcres']
    Fire_Discovery_Date_Time = level_2.get('FireDiscoveryDateTime') or 'Unknown' #level_2['FireDiscoveryDateTime']
    Percent_Contained = level_2.get('PercentContained') or -99 #level_2['PercentContained']
    Containment_DateTime = level_2.get('ContainmentDateTime') or 'Unknown' #level_2['ContainmentDateTime']
    Control_DateTime = level_2.get('ControlDateTime') or 'Unknown' #level_2['ControlDateTime']
    with open('./insert.txt','a') as output:
         output.write("INSERT INTO instances VALUES('" + "','".join([ID,Incident_Name,city,county,State,date]) + "'," + ",".join([str(Latitude),str(Longitude),str(Discovery_Acres),str(Daily_Acres),str(Initial_Response_Acres)]) + ",'" + "','".join([Fire_Cause,Fire_Discovery_Date_Time])+"',"+str(Percent_Contained) + ",'" +"','".join([Containment_DateTime,Control_DateTime]) +"');\n")
