<div align="center">
  <img src="https://ichef.bbci.co.uk/news/976/cpsprodpb/D6E6/production/_109241055_mediaitem109241054.jpg" width = "651" height = "500">
</div>

-----------------

# Squirrel Tracker: Keeping Track of 2018 Central Park Squirrel


## Description
This web application **findsquirrels** allow users to add, update and view squirrel data. Users can view the location of the squirrel sightings on our map. Data source is from <a href='https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw'>NYC Open Data: 2018 Central Park Squirrel Census - Squirrel Data</a>

Users can import the 2018 Central Park Squirrel Census data by using the command:
```sh
python manage.py import_squirrel_data /path/to/file.csv
```

Besides, users can export the data in csv format with this command:
```sh
python manage.py export_squirrel_data /path/to/file.csv
```

## Functions

### Map
  - url: map/
  
    function: The map displays the location of squirrel sightings. You can see locations of 100 squirrels on the map. Click the location marker, the map can show this specific squirrel's unique id, age and primary fur colos.

### Sightings
  - url: sightings/
  
    function: List all squirrel sightings with links to edit each as well as a single link at the top to add a new sighting.
    
  - url: sightings/<unique_squirrel_id>
  
    function: View, edit and update a particular sighting.
    
  - url: sightings/add
  
    function: Create a new squirrel sighting.
    
  - url: sightings/stats
  
    function: Show general stats(e.g. Age, Color, Running, Chasing, Climbing, etc.) about the sightings. 
       


## Group Information
Project Group 54 (Group Name: 23:59)
  - Qianyu Hu
  - Xuan Chen
From Section 2
UNIs:[qh2218, xc2522]

## Link to Server Running Our App

Users can visit our website through https://virtual-dogfish-253823.appspot.com/sightings/

and https://virtual-dogfish-253823.appspot.com/map/

The relevant documents can all be found under folder squirrel.


