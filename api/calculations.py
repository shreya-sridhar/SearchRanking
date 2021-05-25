import pandas as pd
import numpy as np

df1 = pd.read_csv('data/reviews.csv')


class Calculations:

    def profile_score(self, email):
        sitter_name = df1[(df1['sitter_email'] == email)][0:1].sitter
        # getting the name of the sitter from the email
        distinct_chars = set()
        for letter in sitter_name[0]:
            if letter.isalpha():
                distinct_chars.add(letter)
        # The Profile Score is 5 times the fraction of the English alphabet comprised by the
        # distinct letters in what we've recovered of the sitter's name.
        profile_score_val = 5/26*len(distinct_chars)
        # O(n) time, space complexity where n is len(sitter_name)
        return profile_score_val

    def ratings_score(self, email):
        sitter_stays = df1[(df1['sitter_email'] == email)]
        ratings_mean = sitter_stays['rating'].mean()
        return ratings_mean

    def search_score(self, email):
        return 0


class ReadCSV:
    # Ouput csv rows
    # * Sitter email (`email`)
    # * Sitter name (`name`)
    # * Profile Score (`profile_score`)
    # * Ratings Score (`ratings_score`)
    # * Search Score (`search_score`)

    def gettingData(self):
        emails = []
        names = []
        profile_scores = []
        ratings_scores = []
        search_scores = []
        calcs = Calculations()
        for row in df1.itertuples():
            emails.append(row.sitter_email)
            names.append(row.sitter)
            curr_profile_score = calcs.profile_score(row.sitter_email)
            profile_scores.append(curr_profile_score)
            # ratings_scores.append(calcs.ratings_score(row.sitter_email))
            # search_scores.append(calcs.search_score(row.sitter_email))
        print(emails, names, profile_scores, rating_scores, search_scores)

        return

    def createDataFrame(self):
        df = pd.DataFrame({data}, columns=[
                          'email', 'name', 'profile_score', 'ratings_score', 'search_score'])
        return


x = Calculations()
# x.ratings_score("user4739@gmail.com")
y = ReadCSV()
y.gettingData()
