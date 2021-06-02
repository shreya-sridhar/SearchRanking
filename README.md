### SETUP/RUNNING INSTRUCTIONS:
 
1. Compress & download file.
2. Install Python v3.2
3. Navigate to views/cli.py and run. 
4. The user is asked if they want to download csv. On selecting "Yes", output.csv is generated. 
 
#### Q. Describe how you would approach API design for a backend service to provide sitter and rank data to a client/web frontend
 
The API to provide sitter and rank data can be summarized as. 
 
##### GET Requests:
 
1. getallsitters (corresponding to index action) - Request for list of sitters filtered by input criteria 
 
a. Request - /sitters/
b. Parameters
takes as request parameters options like type of service, location, availability, pet type, dog size, rate, etc. along with pagination parameters of page number and results per page and sorting basis ratings and experience
 
&nbsp;{\
    &nbsp; type_of_service: string,\
    &nbsp; location: string,\
    &nbsp; dropoff_date: datetime, //ISO 8601 format\
    &nbsp; pickup_date: datetime,  //ISO 8601 format\
    &nbsp; pet_type: string,\
    &nbsp; dog_size: string,\
    &nbsp; max_rate: float,\
    &nbsp; page_num: int,\
    &nbsp; results_per_page: int,\
    &nbsp; sort_by: string        //option to sort by sitter name and search score ascending & descending\
&nbsp;}\
 
Example : /sitters?type_of_service=boarding&location=seattle&dropoff_date=2000-W03-7T01:23:45.678+09:00&pickup_date=2000-W03-7T01:23:45.678+012:00&pet_type=dog&dog_size=small&max_rate=gt:75&page_num=1&results_per_page=10&sort_by=search_score:desc,sitter_name:asc
 
output : JSON of Sitter objects with various sitter attributes including ranking, page_num, results_per_page
 
Output for each page:
 
&nbsp;[\
    &nbsp;{   
        &nbsp;sitter_id: double,\
        &nbsp;sitter_name: string,\
        &nbsp;sitter_email: string,\
        &nbsp;sitter_phone: double,\
        &nbsp;sitter_location: string,\
        &nbsp;sitter_rate: rate,\
        &nbsp;sitter_housing_conditions: string,\
        &nbsp;sitter_children: string,\
        &nbsp;sitter_services: string,\
        &nbsp;sitter_profile_score: float,\
        &nbsp;sitter_ratings_score: float,\
        &nbsp;sitter_search_score: float\
    &nbsp;},\
    &nbsp;{\
 \
 &nbsp;   },\
    &nbsp;{\
 \
    &nbsp;},\
    &nbsp;.\
    &nbsp;.\
    &nbsp;.,\
 \
&nbsp;]\
 
2. getsitter (corresponding to show action)
 
a. request - /sitter/
b. Schema - takes a input parameter of id, corresponding to the sitter
 
&nbsp;{\
    &nbsp;id : double\
&nbsp;}\
 
Example - /sitter?id=606
 
output : JSON of a single Sitter object with various sitter attributes including ranking
 
&nbsp;[\
    &nbsp;{   \
        &nbsp;sitter_id: double,\
        &nbsp;sitter_name: string,\
        &nbsp;sitter_email: string,\
        &nbsp;sitter_phone: double,\
        &nbsp;sitter_location: string,\
        &nbsp;sitter_rate: rate,\
        &nbsp;sitter_housing_conditions: string,\
        &nbsp;sitter_children: string,\
        &nbsp;sitter_services: string,\
        &nbsp;sitter_profile_score: float,\
        &nbsp;sitter_ratings_score: float,\
        &nbsp;sitter_search_score: float\
    &nbsp;}\
&nbsp;]\
 
##### POST Requests:
 
When a stay is completed, the rating & reviews will be sent as a POST api request with corresponding sitter_id as parameter, thereby updating their ratings for the stay.
 
Post Sitter (corresponding to post action)
 
a. request - /sitter/
b. Schema - takes a input parameter of id, corresponding to the sitter and rating
 
&nbsp;{\
    &nbsp;id : double,\
    &nbsp;rating: int\
&nbsp;}\
 
Example - /sitter?id=606&rating=4
 
In real world scenarios, the ratings scores will be re-calculated in background jobs and factored into sitter rating only when the rating is deemed legit (using data modelling or machine learning to eliminate skewed ratings & bad players).
 
 
 

