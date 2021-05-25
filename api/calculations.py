import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from '../data/data_cleaning' import df1

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
        
        return

    def search_score(self, email):
        return


x = Calculations()
x.profile_score("user4739@gmail.com")
