# -*- coding: utf-8 -*-
import io
import json
from collections import Counter
from collections import defaultdict
import codecs
import time
import requests
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterRequestError
from TwitterAPI import TwitterConnectionError

api = TwitterAPI("keys", "keys", "keys", "keys")

twit = defaultdict(lambda: [])
def read_twitters(filename):
    """ Read profiles into a list of Counter objects.
    DO NOT MODIFY"""
    twitters = []
    
    i = 0
    with io.open(filename, mode='rt', encoding = 'utf-8') as infile:

        for line in infile:
            line = line.encode('utf-8')
            twitters.append((line.split()))
            twit[i] = json.loads(line)
            i += 1
            
            
            

def define_users(screen_name, limit=5):
    
    max_id = None
    lim = 0
    user = "twitters/" + screen_name + ".json"
    file = io.open(user, mode='w+', encoding='utf-8')
    while (lim<limit):
            
            try:
                if max_id:
                    response = api.request('statuses/user_timeline', {'screen_name': screen_name, 'count': 200, 'max_id': max_id})
                    print "maxID"
                else:
                    response = api.request('statuses/user_timeline', {'screen_name': screen_name, 'count': 200})
                    print "not"
                print "code:" + str(response.status_code)
                if response.status_code == 200:
                    items = [t for t in response]
                  
                 
                    print "len:" + str(len(items))
                    if len(items) == 0:
                        return
                    else:
                        for item in items:
                            file.write(json.dumps(item, ensure_ascii=False, encoding='utf-8') + u"\n")
                                         
                    max_id = min(t['id'] for t in response) - 1
                    lim += 1
                elif response.status_code == 429:
                    print "something wrong, sleeping"
                    time.sleep(300)
                    print "sleep time is over"
                elif response.status_code == 401 or response.status_code == 404 or response.status_code == 34:
                    print "unauthorized"
                    return
               
                 
            except TwitterRequestError as e:
               print str(e) 
            except TwitterConnectionError as er:
                print str(er)
                    
    print "end" 
         
def define_500_users():
    listUsers = []
    filea = io.open("users.txt", mode="w+", encoding="utf-8")
    for x in range (len(twit)):
        if twit[x]["user"]["statuses_count"] > 500:
            listUsers.append(twit[x]["user"]["screen_name"])    
    listUsers = set(listUsers)
    print len(listUsers)
    for user in listUsers:
        filea.write(user + u"\n")
        
def main():
    
    
    read_twitters('twitter3.json')
    print 'read', len(twit), 'twitters.'
    'print twitters[0]'
    'print twit[1]["user"]["screen_name"]'
    with io.open("users.txt", mode='rt', encoding='utf8') as usersfile:
         for user in usersfile:
             user = user.rstrip('\n')
             define_users(user)
    """for x in range (len(twit)):
    
        if twit[x]["user"]["statuses_count"] > 500:
            screen_name = twit[x]["user"]["screen_name"]
            define_users(screen_name)

    """
if __name__ == '__main__':
    main()