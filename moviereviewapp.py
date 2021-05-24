import requests_with_caching
import requests
import json
def get_movies_from_tastedive(string):
    baseurl= 'https://tastedive.com/api/similar'
    params_diction={}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    resp=requests_with_caching.get(baseurl,params=params_diction)  
    print(resp.json())
    return resp.json()
(get_movies_from_tastedive("Black Panther"))


import requests_with_caching
import requests
import json
def get_movies_from_tastedive(string):
    baseurl= 'https://tastedive.com/api/similar'
    params_diction={}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    resp=requests_with_caching.get(baseurl,params=params_diction)
    return resp.json()
def extract_movie_titles(g):
    s=g['Similar']['Results']
    mov=[]
    for d in s:
        mov.append(d['Name'])
    return mov
extract_movie_titles(get_movies_from_tastedive("Black Panther"))


import requests_with_caching
import requests
import json
def get_movies_from_tastedive(string):
    baseurl= 'https://tastedive.com/api/similar'
    params_diction={}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    resp=requests_with_caching.get(baseurl,params=params_diction)
    return resp.json()
def extract_movie_titles(g):
    s=g['Similar']['Results']
    mov=[]
    for d in s:
        mov.append(d['Name'])
    return mov

def get_related_titles(l):
    j=[]
    for x in l:
        j+=(extract_movie_titles(get_movies_from_tastedive(x)))
    return list(dict.fromkeys(j))
        
get_related_titles([])
get_related_titles(["Black Panther", "Captain Marvel"])    



import requests_with_caching
import requests
import json
def get_movie_data(str):
    baseurl= "http://www.omdbapi.com/"
    params_dict={}
    params_dict['t']=str
    params_dict['r']="json"
    resp1=requests_with_caching.get(baseurl,params_dict)  
    print(resp1.json())
    return resp1.json()

get_movie_data("Venom")
# get_movie_data("Baby Mama")


import requests_with_caching
import requests
import json
def get_movie_data(str):
    baseurl= "http://www.omdbapi.com/"
    params_dict={}
    params_dict['t']=str
    params_dict['r']="json"
    resp1=requests_with_caching.get(baseurl,params_dict)  
    return resp1.json()
def get_movie_rating(s):
    print(s)
    k = s['Ratings']
    i=0
    while i<len(k):
        if k[i]['Source']== 'Rotten Tomatoes':
            print(k[i]['Value'])
            return int((k[i]['Value'])[:len(k)-1])
        if i==len(k)-1 and k[i]['Source']!= 'Rotten Tomatoes':
            print(k[i])
            return 0
        i+=1
        
get_movie_rating(get_movie_data("Deadpool 2"))


import requests_with_caching
import requests
import json
def get_movies_from_tastedive(string):
    baseurl= 'https://tastedive.com/api/similar'
    params_diction={}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    resp=requests_with_caching.get(baseurl,params=params_diction)
    return resp.json()
def extract_movie_titles(g):
    s=g['Similar']['Results']
    mov=[]
    for d in s:
        mov.append(d['Name'])
    return mov
def get_related_titles(l):
    j=[]
    for x in l:
        j+=(extract_movie_titles(get_movies_from_tastedive(x)))
    return list(dict.fromkeys(j))
def get_movie_data(stri):
    baseurl= "http://www.omdbapi.com/"
    params_dict={}
    params_dict['t']=stri
    params_dict['r']="json"
    resp1=requests_with_caching.get(baseurl,params_dict)  
    return resp1.json()
def get_movie_rating(s):
    k = s['Ratings']
    i=0
    while i<len(k):
        if k[i]['Source']== 'Rotten Tomatoes':
            return int((k[i]['Value'])[:len(k)-1])
        if i==len(k)-1 and k[i]['Source']!= 'Rotten Tomatoes':
            return 0
        i+=1
def get_sorted_recommendations(u):
    o={}
    y=[]
    l=[]
    for i in u:
        o[i]=(get_movie_rating(get_movie_data(i)))
    for k,v in o.items():
        y.append((v,k))
    y=sorted(y,reverse=True)
    for p,q in y:
        l.append(q)
    return(l)
print(get_sorted_recommendations(get_related_titles(["Bridesmaids", "Sherlock Holmes"])))

import requests_with_caching
import requests
import json
def get_movies_from_tastedive(string):
    baseurl= 'https://tastedive.com/api/similar'
    params_diction={}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    resp=requests_with_caching.get(baseurl,params=params_diction)
    return resp.json()
def extract_movie_titles(g):
    s=g['Similar']['Results']
    mov=[d['Name'] for d in s]
    return mov
def get_related_titles(l):
    j=[]
    for x in l:
        j+=(extract_movie_titles(get_movies_from_tastedive(x)))
    return list(dict.fromkeys(j))
def get_movie_data(stri):
    baseurl= "http://www.omdbapi.com/"
    params_dict={}
    params_dict['t']=stri
    params_dict['r']="json"
    resp1=requests_with_caching.get(baseurl,params=params_dict)  
    return resp1.json()
def get_movie_rating(s):
    k = s['Ratings']
    for i in k:
        if i['Source']== 'Rotten Tomatoes':
            return int((i['Value'])[:len(k)-1])
        if k.index(i)==len(k)-1 and i['Source']!= 'Rotten Tomatoes':
            return 0

def get_sorted_recommendations(u):
    o={}
    y,l=[],[]
    for i in u:
        o[i]=(get_movie_rating(get_movie_data(i)))
    l= [q for p,q in sorted([(v,k) for k,v in o.items()],reverse=True)]
    return(l)
print(get_sorted_recommendations(get_related_titles(["Bridesmaids", "Sherlock Holmes"])))

w=get_sorted_recommendations(get_related_titles(["Bridesmaids", "Sherlock Holmes"]))

