from read_data import ReadData



class SitterController:

    def __init__(self):
        self.data = ReadData()
        # data.Owners()
        self.owners = self.data.readCSV()[0]
        # data.Sitters()
        self.sitters = self.data.readCSV()[1]

    def listAllSitters([ ]):
        # order it by score, email_id  
        # dog ='Barbarian'
        # location =''
        # 
    
    def listAllSitters([ ]):

    def GetSitter(string sitter_id):
        # Get 


    def AddSitting(): 
        # If no score Compute the score,  save to db and  return to user 
        # Not implemented 

    
    def 

    # Crud action
    # def update(sitter): 

    # def delete():
    # unimplemented 

# Class Score Caluclator 
# Make this just a function
    def overall_score_calculator(self):
        for sitter in self.sitters.keys():
            self.profile_score_calculator(sitter)
            self.ratings_score_calculator(sitter)

    def profile_score_calculator(self, email):
        # calculates & updates sitter object with profile score
        curr_sitter = self.sitters[email]
        sitter_name = curr_sitter.sitter
        distinct_chars = set()
        for letter in sitter_name[0]:
            if letter.isalpha():
                distinct_chars.add(letter)
        # The Profile Score is 5 times the fraction of the English alphabet comprised by the
        # distinct letters in what we've recovered of the sitter's name.
        profile_score_val = 5/26*len(distinct_chars)
        # O(n) time, space complexity where n is len(sitter_name)\
        self.data.sitters[email].profile_score = profile_score_val
        return profile_score_val

    def ratings_score_calculator(self, email):
        # calculates & updates sitter object with ratings score
        stays = self.data.stays
        total_ratings = 0
        count_ratings = 0
        for stay in stays.values():
            print(stay)
            if stay.sitter.sitter_email == email:
                count_ratings += 1
                total_ratings += stay.rating
        if total_ratings == 0 and count_ratings == 0:
            self.data.sitters[email].profile_score = 0
            return 0
        self.data.sitters[email].profile_score = total_ratings/count_ratings
        return total_ratings/count_ratings

    # def search_score_calculator(self,email):
        

s = ScoreCalculator()
s.overall_score_calculator()



