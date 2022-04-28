#!/usr/bin/env python3
import requests
import wget

URL= "http://www.omdbapi.com/?apikey=875c4c78&s="

def main():
    choice= input("Enter a movie title:\n>")

    full_url= URL + choice

    movies= requests.get(full_url).json()
    
    #get only Search 
    movieslist= movies.get('Search')
    #looping over Search
    for x in movieslist:
        if (x['Type']) == 'movie':
            print (f"{x['Title']} was released in {x['Year']}")    
    
    wget.download(movieslist[0]['Poster'], '/home/student/static/')


if __name__ == "__main__":
    main()
