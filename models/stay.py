import datetime

class Stay:

    # A Stay belongs to a unique sitter and owner in a one-to-one relationship

    def __init__(self, stay_id: int, rating: float, end_date: 'datetime', text: str, dogs: list('Dog'), start_date:'datetime', response_time_minutes: int=-1, owner: 'Owner' = None, sitter: 'Sitter' = None):
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

