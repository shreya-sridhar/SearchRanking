class Stay:
    def __init__(self,stay_id,rating,end_date,text,dogs,start_date,response_time_minutes,owner=None,sitter=None):
        self.stay_id = stay_id
        self.rating = rating
        self.start_date = start_date
        self.end_date = end_date
        self.text = text 
        self.dogs = dogs
        self.response_time_minutes = response_time_minutes
        # Sitter & Owner associated with that stay
        self.owner = owner 
        self.sitter = sitter

    

