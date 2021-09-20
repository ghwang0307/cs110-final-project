import csv
import pandas as pd
import matplotlib.pyplot as plot
#with open('2016_movie_data.csv',newline='') as csvfile:
    #spamreader=csv.reader(csvfile, delimiter=' ',quotechar='|')
    #for row in spamreader:
        #print(row)
article_read=pd.read_csv('2016_movie_data.csv', delimiter = ',')
article_read['Tickets Sold']=article_read['Tickets Sold'].str.replace(',', '')
article_read['Tickets Sold']=article_read['Tickets Sold'].astype(int)
article_read['Distributor'] = article_read['Distributor'].fillna('Unknown')

def convert_to_list(title):
    list_=[]
    for x in article_read[title]:
        list_.append(x)
    return list_

def convert_to_set(title):
    return set(convert_to_list(title))

def movie_stats(x):
    return len(x)

movie_list=convert_to_list('Movie')
release_date_list=convert_to_list('Release Date')
mpaa_list=convert_to_list('MPAA')
tickets_sold_list=convert_to_list('Tickets Sold')
genre_set=convert_to_set('Genre')
distributor_set=convert_to_set('Distributor')
release_date_set=convert_to_set('Release Date')
mpaa_set=convert_to_set('MPAA')
genres=['Movies','different genres','different MPAA','different distributors']

tickets_int=[]
for x in tickets_sold_list:
    tickets_int.append(int(x))

tix_per_release=article_read.groupby('Release Date')['Tickets Sold'].apply(list).to_dict()

for (release_date,tix_sold) in tix_per_release.items():
    tix_per_release[release_date]=sum(tix_per_release[release_date])

tix_per_month={'January':[],'February':[],'March':[],'April':[],'May':[],'June':[],'July':[],'August':[],'September':[],'October':[],'November':[],'December':[]}

for (x,y) in tix_per_release.items():
    if x[0:2]=='1/':
        tix_per_month['January'].append(tix_per_release[x])
    if x[0]=='2':
        tix_per_month['February'].append(tix_per_release[x])
    if x[0]=='3':
        tix_per_month['March'].append(tix_per_release[x])   
    if x[0]=='4':
        tix_per_month['April'].append(tix_per_release[x])       
    if x[0]=='5':
        tix_per_month['May'].append(tix_per_release[x])          
    if x[0]=='6':
        tix_per_month['June'].append(tix_per_release[x])
    if x[0]=='7':
        tix_per_month['July'].append(tix_per_release[x])
    if x[0]=='8':
        tix_per_month['August'].append(tix_per_release[x])
    if x[0]=='9':
        tix_per_month['September'].append(tix_per_release[x]) 
    if x[1]=='0':
        tix_per_month['October'].append(tix_per_release[x])
    if x[0:2]=='11':
        tix_per_month['November'].append(tix_per_release[x])
    if x[0:2]=='12':
        tix_per_month['December'].append(tix_per_release[x])

for (month, tickets) in tix_per_month.items():
    tix_per_month[month]=sum(tix_per_month[month])

#1:
print('=========Dataset details=========')
print()
print('Number of movies: ',movie_stats(movie_list))
print('Number of different genres:', movie_stats(genre_set))   
print('Number of different MPAA:', movie_stats(mpaa_set))
print('Number of distributors:',movie_stats(distributor_set))
print('Total number of tickets sold:',sum(tickets_int))
print()

#2:
print('================================')
print()
months_dictionary={'January':0,'February':0,'March':0,'April':0,'May':0,'June':0,'July':0,'August':0,'September':0,'October':0,'November':0,'December':0}
for x in release_date_list:
    if x[0:2]=='1/':
        months_dictionary['January']+=1
    if x[0]=='2':
        months_dictionary['February']+=1
    if x[0]=='3':
        months_dictionary['March']+=1    
    if x[0]=='4':
        months_dictionary['April']+=1        
    if x[0]=='5':
        months_dictionary['May']+=1            
    if x[0]=='6':
        months_dictionary['June']+=1 
    if x[0]=='7':
        months_dictionary['July']+=1
    if x[0]=='8':
        months_dictionary['August']+=1
    if x[0]=='9':
        months_dictionary['September']+=1   
    if x[1]=='0':
        months_dictionary['October']+=1
    if x[0:2]=='11':
        months_dictionary['November']+=1
    if x[0:2]=='12':
        months_dictionary['December']+=1

print('Most number of movies released','('+str(max(months_dictionary.values()))+')','in', max(months_dictionary,key=months_dictionary.get)+'.')
print('Most amount of tickets sold','('+str(max(tix_per_month.values()))+')','in',max(tix_per_month,key=tix_per_month.get)+'.')
print()
print('================================')
print()
print('========Tickets sold by distributors========')
print()

tix_per_dist=article_read.groupby('Distributor')['Tickets Sold'].apply(list).to_dict()

for (dist,tix_sold) in tix_per_dist.items():
    tix_per_dist[dist]=sum(tix_per_dist[dist])

total=sum(tix_per_dist.values())

for (dist,tix_sold) in tix_per_dist.items():
    tix_per_dist[dist]=float((tix_per_dist[dist]/total)*100)

new_d={'Others':[]}
for (dist,tix_sold) in tix_per_dist.items():
    if tix_sold<1.00:
        new_d['Others'].append(tix_sold)
your_dic = {k:v for k,v in tix_per_dist.items() if v <1.0}

for k,v in new_d.items():
    new_d[k]=sum(new_d[k])

tix_per_dist.update(new_d)

final_d={k:v for k,v in tix_per_dist.items() if v>=1.0}
for k,v in final_d.items():
    final_d[k]=round(final_d[k],2)

result = sorted(final_d.items() , key=lambda t : t[1] , reverse=True)

for k,v in result:
    print(k,':',str(v)+'%')

print()
print('================================')
