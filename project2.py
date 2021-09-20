import csv
import pandas as pd
import matplotlib.pyplot as plot

'''This reads the opens and reads the CSV file'''
article_read=pd.read_csv('2016_movie_data.csv', delimiter = ',')
article_read['Tickets Sold']=article_read['Tickets Sold'].str.replace(',', '')
article_read['Tickets Sold']=article_read['Tickets Sold'].astype(int)
article_read['Distributor'] = article_read['Distributor'].fillna('Unknown')



def convert_to_list(title):
    '''This is a function that adds the data set to a list'''
    list_=[]
    for x in article_read[title]:
        list_.append(x)
    return list_

def convert_to_set(title):
    '''This is a function that adds the data set into a set (to ensure no repeated values)'''
    return set(convert_to_list(title))

def movie_stats(x):
    '''This allows us to see how many values there are in that data set'''
    return len(x)



'''Converting the CSV datasets to make it more accessible in the program'''
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

'''Question 1:''' 
print('=========Dataset details=========')
print()
print('Number of movies: ',movie_stats(movie_list))
print('Number of different genres:', movie_stats(genre_set))   
print('Number of different MPAA:', movie_stats(mpaa_set))
print('Number of distributors:',movie_stats(distributor_set))
print('Total number of tickets sold:',sum(tickets_int))
print()

'''Question 2:'''

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


    
    
    


"""Question 2 (graph)"""
months = []
values = []
for x in months_dictionary:
    months.append(x)
for x in months_dictionary.values():
    values.append(x)
def q2graph():
    q2_chart = plot.bar(months, values, align = 'center', alpha = 1.0)
    plot.title('Number of movies released in diffferent months of 2016')
    plot.xlabel('Month')
    plot.ylabel('Number of Movies')
    plot.show()


"""Question 3 (graph)"""
def q3graph():
    values = []
    for x in tix_per_month.values():
        values.append(x)
    plot.plot(months, values, color = 'b', linestyle = '-')
    plot.title('Tickets sold in different months of 2016')
    plot.xlabel('Month')
    plot.ylabel('Number of tickets sold')
    plot.show()

'''Question 4'''
name = []
percent = []
for x, y in result:
    name.append(x)
    percent.append(y)
    
def q4graph():
    plot.clf()
    pie = plot.pie(percent, labels = name, autopct='%1.1f%%')
    plot.title('Percentage of tickets sold by different distributors')
    plot.show()

    


#'''Question 5'''
#action_counter=[0,0,0,0,0,0,0,0,0,0,0,0] #These lists will contain a counter for the number of genre movies released in each months
#comedy_counter=[0,0,0,0,0,0,0,0,0,0,0,0]
#drama_counter=[0,0,0,0,0,0,0,0,0,0,0,0]
#horror_counter=[0,0,0,0,0,0,0,0,0,0,0,0]

#month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',' August', 'September', 'October', 'November', 'December']

#genre_counter =[action_counter,comedy_counter,drama_counter,horror_counter]
#genres_checked=['Action','Comedy', 'Drama','Horror'] 
#for x in range(len(release_date_list)): #This incrementally adds 1 for each movie released per genre per month
    #for y in range(4):
        #if release_date_list[x][0:2]=='1/' and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][0] +=1
        #if release_date_list[x][0]=='2'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][1]+=1
        #if release_date_list[x][0]=='3'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][2]+=1
        #if release_date_list[x][0]=='4'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][3]+=1
        #if release_date_list[x][0]=='5'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][4]+=1
        #if release_date_list[x][0]=='6'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][5]+=1
        #if release_date_list[x][0]=='7'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][6]+=1
        #if release_date_list[x][0]=='8'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][7]+=1
        #if release_date_list[x][0]=='9'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][8]+=1
        #if release_date_list[x][1]=='0'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][9]+=1
        #if release_date_list[x][0:2]=='11'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][10]+=1
        #if release_date_list[x][0:2]=='12'and bool(genre_list[x]== genres_checked[y]):
            #genre_counter[y][11]+=1

## This commented out section was to test to make sure that every movie of a given genre was accounted for
##genre_counter1=[0,0,0,0]
##for x in genre_list:
    ##if x == 'Action':
        ##genre_counter1[0]+=1
    ##if x == 'Comedy':
        ##genre_counter1[1]+=1
    ##if x == 'Drama':
        ##genre_counter1[2]+=1
    ##if x == 'Horror':
        ##genre_counter1[3]+=1
    ##else:
        ##pass
##All the plotting directions for Q5 are here
#plot.plot(month_list,genre_counter[0], label='Action',color='green')
#plot.plot(month_list,genre_counter[1], label='Comedy',color='red')
#plot.plot(month_list,genre_counter[2], label='Drama',color='blue')
#plot.plot(month_list,genre_counter[3], label='Horror',color='orange')
#plot.title('Number of movies released in different months of 2016')
#plot.legend()
#plot.ylabel('Number of Movies')
#plot.xlabel('Month')
#plot.show             
def main():
    input('Press Enter to show graph')
    q2graph()
    input('Press Enter to show the next graph')
    q3graph()
    input('Press Enter to show the next graph')
main()
q4graph()

    