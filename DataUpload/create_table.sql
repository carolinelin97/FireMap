
CREATE TABLE wildfire.instances 
	(Instance_ID varchar(200), 
    Incident_Name varchar(100),
    City varchar(100), 
    County varchar(100), 
    State varchar(100), 
    record_Date date, 
    Latitude double(10,6), 
    Longitude double(10,6), 
    Discovery_Acres double(10,2), 
    Fire_Cause varchar(100), 
    Fire_Discovery_Date_Time datetime) 
;
