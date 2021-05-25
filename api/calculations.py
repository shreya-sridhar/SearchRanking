import pandas as pd
import numpy as np
import csv
import tkinter as tk
from tkinter import filedialog

df1 = pd.read_csv('data/reviews.csv')

class Calculations:

    def profile_score(self, email):
        profile_score = 0
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
        for row in df1.itertuples():
            emails.append(row.sitter_email)
            names.append(row.sitter)
            calcs = Calculations()
            curr_ratings_score = calcs.ratings_score(row.sitter_email)
            curr_profile_score = calcs.ratings_score(row.sitter_email)
            curr_search_score = calcs.search_score(row.sitter_email)
            ratings_scores.append(curr_ratings_score)
            profile_scores.append(curr_search_score)
            search_scores.append(curr_search_score)
        # print(emails, names, profile_scores, ratings_scores, search_scores)

        return [emails, names, profile_scores, ratings_scores, search_scores]

    def createDataFrame(self):
        getData = self.gettingData()
        # print(getData[0])
        data = {'email': getData[0], 'name': getData[1], 'profile_score': getData[2],
                'ratings_score': getData[3], 'search_score': getData[4]}
        df = pd.DataFrame(data, columns=[
                          'email', 'name', 'profile_score', 'ratings_score', 'search_score'])
        # The csv should be sorted by Search Score (descending), sorting alphabetically on the
        # sitter name as a tie-breaker.
        df = df.drop_duplicates().sort_values(["search_score", "name"], ascending = (False, True))
        df.to_csv('output.csv', header=True)
        return df

    def exportCSV(self):
        root = tk.Tk()
        canvas1 = tk.Canvas(root, width=300, height=300,
                            bg='lightsteelblue2', relief='raised')
        canvas1.pack()
        global df
        df = self.createDataFrame()

        export_file_path = filedialog.asksaveasfilename(
            defaultextension='.csv')
        df.to_csv(export_file_path, index=False, header=True)

        saveAsButton_CSV = tk.Button(text='Export CSV', bg='green', fg='white', font=('helvetica', 12, 'bold'))
        canvas1.create_window(150, 150, window=saveAsButton_CSV)
        root.mainloop()


y = ReadCSV()
y.exportCSV()


