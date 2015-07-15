# -*- coding: utf-8 -*-

from TwitterAPI import TwitterAPI
import json
import io
import discogs_client
import glob
import math
import requests
import time
import sys
from collections import defaultdict
import re

genresdict = defaultdict(lambda: [])

d = discogs_client.Client('SoundTaste/0.1', user_token="SadTsSgFWUhyffGXzZFbNtRzQHOxTRIXdfzbonJB")
class Document(object):
  

    def __init__(self, filename):
        self.filename = filename
        



def search_genre(artist, relId = 0):
    genre = []
    cache = 0
    for bands in genresdict.keys():
        if artist == bands:
            cache = 1   
            if len(genresdict[artist]) > 0:                
                genre = genresdict[artist]
            print "got from cache!!!"
            
    if (cache == 0):
        try:
            results = d.search(artist, type='artist')
   
            if len(results) > 0 :
                print "got from API!!!"
                id = results[0].id
                artistData = d.artist(id)
                found = False
                while(not found and relId <21):
                    if hasattr(artistData.releases[relId], 'main_release'):
                        if hasattr(artistData.releases[relId].main_release, 'genres'):
                            found = True       
                            for genres in artistData.releases[relId].main_release.genres:
                                genre.append(genres)
                    relId += 1
            
                
                if len(genre) > 0:
                    
                    genresdict[artist] = genre
                else:
                    print "got here"
                    genresdict[artist] = []
                    print "error?"
        except requests.exceptions.ConnectionError as c:
            print "connectionError, sleeping"
            time.sleep(30)
            print "sleep time is over"
            genre = search_genre(artist, relId)
        except ValueError as value:
            print "valueError"
        except discogs_client.exceptions.HTTPError as code:
            cod = str.split(str(code), ":")
            if cod[0] == '404':
                print "not found"
            elif cod[0] == '401':
                print "unauthorized"
            elif cod[0] == '429':
                print "too many, time to sleep"
                time.sleep(60)
                print "sleep time is over"
                genre = search_genre(artist, relId)
        except :
            print "Unexpected error:", sys.exc_info()[0]
            if str(sys.exc_info()[0]) == "<type 'exceptions.AttributeError'>":
                print "got here!"
                genresdict[artist] = []
         
    return genre
def users_file():
    numberQuery = 0
    numberRE = 0
    for files in glob.glob("twitters/*.json"):
        user = str.split(files, ".")
        user = str.split(user[0], "\\")
        userFinal = "data/" + user[1] + ".json"
        fileN = io.open(userFinal, mode='w+', encoding='utf-8')
        fileInfo = io.open("error/info.txt", mode='a+', encoding='utf-8')
        fileQuery = io.open("error/query.txt", mode='a+', encoding='utf-8')
        twit = defaultdict(lambda: [])
        i = 0
        
        with io.open(files, mode='rt', encoding = 'utf-8') as infile:
            
            for line in infile:
                dataTwit = defaultdict(lambda: [])
                twit[i] = json.loads(line)                
                text = twit[i]['text'].encode('utf-8')
                if "I'm listening to" in text:
                    if "#pandora" in text:
                      print "before RE"
                      numberQuery += 1
                      search = re.search('to "?(.*?)"? by (.*?) on #?Pandora', text)
                      if search is not None:
                          numberRE += 1
                          try:
                              genre = []
                              artist = search.group(2)
                        
                              id = twit[i]['id']
                        
                              genre = search_genre(artist)
                              dataTwit['id'] = id 
                              dataTwit['artist'] = artist.encode('utf8')
                              print artist
                              if genre is not None:
                                  dataTwit['genre'] = genre
                                  print genre
                              fileN.write(json.dumps(dataTwit, ensure_ascii=False, encoding='utf-8') + u"\n")
                              print "success!"
                          except:
                            print "not success!:", sys.exc_info()[0]
                            try:
                                fileInfo.write(unicode(sys.exc_info()[0]) + u"\n" )
                            except:
                                print "did not success to write on the file"
                      else:
                          try:
                              fileQuery.write(unicode(user[1]) +u" "+ unicode(text) + u"\n")
                          except:
                              print "could not write on the file"
                i+= 1
    try:
        fileQuery.write(u"Number Query: " + unicode(numberQuery) + u"Number RE: " + unicode(numberRE) + u"\n")            
    except:
        print "error on writing"
def main(): 
    users_file()
if __name__ == '__main__':
    main()
