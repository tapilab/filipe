# -*- coding: utf-8 -*-

from TwitterAPI import TwitterAPI
import json
import io

api = TwitterAPI("keys", "keys", "keys", "keys")

request = api.request('statuses/show', {'id': "606159589453766656"}) 


def main():
    
    tweet = None
    with io.open("spotify.json", mode='a+', encoding='utf-8') as outfile:
    
        for r in request:
            tweet = r
            dir(tweet)
            user = tweet['user']
            screen_name = user['screen_name'.encode("utf-8")]
            print screen_name
            print user['name'].encode("utf-8")
            print user['location'].encode("utf-8")
            print user['lang']
            '''print tweet['created_at']'''
            print tweet['text'].encode("utf-8")
            outfile.write(json.dumps(tweet, ensure_ascii=False, encoding='utf-8'))
            outfile.write(u"\n")
            
            """
            timeline = []
            for t in api.request('statuses/user_timeline', {'screen_name':screen_name}):
                timeline.append(t)
                
            print '\n'.join(t['text'].encode("utf-8") for t in timeline)  
               
            print 'got %d tweets for user %s' % (len(timeline), screen_name)
        
            outfile.write(" !--------!, user \n")
            json.dump(user, outfile)
            outfile.write("\n !--------!, tweet \n") 
            json.dump(tweet, outfile)
            outfile.write("\n !--------!, timeline \n")    
            json.dump(timeline, outfile)
            outfile.write("\n !--------!, end \n")
        
            Format of the file:
                screen name
                user name
                location
                lang
                text
                timeline
            ----------
            
            file.write(screen_name + "\n")
            file.write(user['name'].encode("utf-8") + "\n")
            file.write(user['location'].encode("utf-8") + "\n")
            file.write(user['lang'] + "\n")
            file.write('\n'.join(t['text'].encode("utf-8") for t in timeline));
            file.write('\n')
            file.write('----------')
            file.write('\n')
        
   

            file.close()
            """
if __name__ == '__main__':
    main()
