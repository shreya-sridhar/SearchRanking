SETUP/RUNNING INSTRUCTIONS:
 
1. Compress & download file.
2. Install Python v3.2
3. Navigate to views/cli.py and run. 
4. The user is asked if they want to download csv. On selecting "Yes", output.csv is generated. 
 
Q. Describe how you would approach API design for a backend service to provide sitter and rank data to a client/web frontend
 
The API to provide sitter and rank data can be summarized as. 
 
GET Requests:
 
1. getallsitters (corresponding to index action) - Request for list of sitters filtered by input criteria 
 
a. Request - /sitters/
b. Parameters
takes as request parameters options like type of service, location, availability, pet type, dog size, rate, etc. along with pagination parameters of page number and results per page and sorting basis ratings and experience
 
{
    type_of_service: string,
    location: string,
    dropoff_date: datetime, //ISO 8601 format
    pickup_date: datetime,  //ISO 8601 format
    pet_type: string,
    dog_size: string,
    max_rate: float,
    page_num: int,
    results_per_page: int,
    sort_by: string        //option to sort by sitter name and search score ascending & descending
}
 
Example : /sitters?type_of_service=boarding&location=seattle&dropoff_date=2000-W03-7T01:23:45.678+09:00&pickup_date=2000-W03-7T01:23:45.678+012:00&pet_type=dog&dog_size=small&max_rate=gt:75&page_num=1&results_per_page=10&sort_by=search_score:desc,sitter_name:asc
 
output : JSON of Sitter objects with various sitter attributes including ranking, page_num, results_per_page
 
Output for each page:
 
[
    {   
        sitter_id: double,
        sitter_name: string,
        sitter_email: string,
        sitter_phone: double,
        sitter_location: string,
        sitter_rate: rate,
        sitter_housing_conditions: string,
        sitter_children: string,
        sitter_services: string,
        sitter_profile_score: float,
        sitter_ratings_score: float,
        sitter_search_score: float
    },
    {
 
    },
    {
 
    },
    .
    .
    .,
 
]
 
2. getsitter (corresponding to show action)
 
a. request - /sitter/
b. Schema - takes a input parameter of id, corresponding to the sitter
 
{
    id : double
}
 
Example - /sitter?id=606
 
output : JSON of a single Sitter object with various sitter attributes including ranking
 
[
    {   
        sitter_id: double,
        sitter_name: string,
        sitter_email: string,
        sitter_phone: double,
        sitter_location: string,
        sitter_rate: rate,
        sitter_housing_conditions: string,
        sitter_children: string,
        sitter_services: string,
        sitter_profile_score: float,
        sitter_ratings_score: float,
        sitter_search_score: float
    }
]
 
POST Requests:
 
When a stay is completed, the rating & reviews will be sent as a POST api request with corresponding sitter_id as parameter, thereby updating their ratings for the stay.
 
Post Sitter (corresponding to post action)
 
a. request - /sitter/
b. Schema - takes a input parameter of id, corresponding to the sitter and rating
 
{
    id : double,
    rating: int
}
 
Example - /sitter?id=606&rating=4
 
In real world scenarios, the ratings scores will be re-calculated in background jobs and factored into sitter rating only when the rating is deemed legit (using machine learning modelling which eliminates skewed ratings & bad players).
 
 
 

