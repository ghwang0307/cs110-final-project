import csv
import pandas as pd
import matplotlib.pyplot as plot
#with open('2016_movie_data.csv', newline='') as csvfile:
    #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #for row in spamreader:
        #print(' '.join(row))
article_read = pd.read_csv('2016_movie_data.csv', delimiter = ',', encoding = "ISO-8859-1")
def convert_to_list(title):
    list_ = []
    for x in article_read[title]:
        list_.append(x)
    return list_

def convert_to_set(title):
    return set(convert_to_list(title))

def movie_stats(x):
    return len(x)

movie_list = convert_to_list('Movie')
release_date_list = convert_to_list('Release Date')
mpaa_list = convert_to_list('MPAA')
tickets_sold_list = convert_to_list('Tickets Sold')
genre_set = convert_to_set('Genre')
distributor_set = convert_to_set('Distributor')
release_date_set = convert_to_set('Release Date')
mpaa_set = convert_to_set('MPAA')
genres = ['Movies', 'different genres', 'different MPAA', 'different distributors']

tickets_int = [] #transferring tickets sold into integer values
for x in tickets_sold_list:
    x = x.replace(',' , '')
    tickets_int.append(int(x))
    
    
#1:
print('=========Dataset details=========')
print()
print(f'Number of Movies: {movie_stats(movie_list)}')
print(f'Number of different genres: {movie_stats(genre_set)}')
print(f'Number of different MPAA: {movie_stats(mpaa_set)}')
print(f'Number of distributors: {movie_stats(distributor_set)}')
print(f'Total number of tickets sold: {sum(tickets_int)}')
print()

#2:
print('================================')
print()
months_dictionary = {'January':0, 'February':0, 'March':0, 'April':0, 'May':0, 'June':0, 'July':0, 'August':0, 'September':0, 'October':0, 'November':0, 'December':0}
months_chart = plot.bar()



