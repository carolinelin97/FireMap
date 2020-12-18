# Wildfire Monitoring System
**DSCI 551 Final Project**

Github Page: [Wildfire Monitoring System](https://carolinelin97.github.io/FireMap)

Github Repo: See demo branch.

Report: [link](https://github.com/carolinelin97/FireMap/blob/demo/report_demo.pdf)

Presentation Vid: [link](https://drive.google.com/drive/folders/1Ltm4BS_efcbERJc9WPJe7gnp_VOAa133?usp=sharing)

### Project Description:
2020's fire season has already seen above-normal activity. It has been a brutal summer for firefighters and thousands of residents in California. While weather conditions and air quality have continued to get worse, firefighters are monitoring the shape, size, rate of perimeter increase, and rate of area growth of a wind-driven wildland fire closely. This project is to better share maps and data related to wildland fire activities across California, helping utility companies predict wildfire risk and taking proactive measures to save lives and property.

### Data Sets:
1) [Wildland Fire Open Data](https://data-nifc.opendata.arcgis.com/datasets/incident-3)
The data set describes the location, spreading, cause, etc. of current wildfire all over the United States. It is updated every 5 minutes.
2) [Latitude and Longitude of All US Cities](https://simplemaps.com/data/us-cities)
The data set includes location information of all the cities in the US (e.g. city, country, state, latitude, longitude, population, timezone, zip code, etc.)

### Implementation:
**1. Data Resource**: 
Our raw data are from 2 data resources. One is in json file format, the other in csv file format. We used Spark RDD to build a pipeline to preprocess and integrate two files.

**2. Database**: 
We used two databases to store our data. One is a relational database AWS RDS and the other is Firebase Realtime Database. We maintained these two databases everyday to keep updated to the latest wildfire status.

**3. Data visualization**:
We used ArcGIS (Geographic Information System) web API to draw our map. It shows the most current active wildfires in California. It has a popup table that shows up with the related attributes of chosen fire, a search box that allows users to search for individual fire and locate it with its name.

**4. Searching and Exploring**:
We created a table that presents all the raw data retrieved from the firebase. A date input and a search box allows users to explore raw data. These ‘on change’ functions will update the map and the table on a chosen day or with a certain value in real time. Users could search a location to find nearby wildfires or search an incident name to find its location.

**5. Aggregation**:
We set up a local server to query the data from RDS, and filter the fires whose Percent Contained are smaller than 100 percent, which means fires are not completely controlled. At the same time we query ‘group by city’ data from SQL by date. In this way we can show how many fires are in one city. We use Network Address Translator to allow users to access our back-end. Due to GitHub page security technical restrictions, we are not able to connect our back end, resulting the failure of updating the summary table in real-time.

### Project Member:
#### Jiaying Wang (Applied Data Science):

*LinkedIn: [https://www.linkedin.com/in/jiaying-wang-161694176](https://www.linkedin.com/in/jiaying-wang-161694176)*

*Skills: Data Visualization, Data Analysis, Machine Learning, NLP, Spark*

*Work Accomplished:*

*1.  Built up a pipeline with Spark to preprocess and integrate two different data structures and uploaded to the firebase database.*

*2.  Maintained the firebase database, synchronized it to AWS RDS and updated them everyday.*

*3.  Implemented the search function on our HTML web page to navigate raw data.*



#### Yanan Lin (Computer Science (Multimedia and Creative Technology)):

*LinkedIn: [https://linkedin.com/in/yanan-lin](https://linkedin.com/in/yanan-lin)*

*Skills: Full Stack, Computer Graphics*

*Work Accomplished:*

*1. Engineered HTML web page and basic functionality, designed front end UI, and published to GitHub.*

*2. Created GIS map module to receive and visualize wildfire geographic data.*

*3. Generated table to present raw data.*
