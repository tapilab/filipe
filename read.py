# -*- coding: utf-8 -*-

from TwitterAPI import TwitterAPI
import json
import io
import discogs_client
import glob
import math
from collections import defaultdict


"""d = discogs_client.Client('SoundTaste/0.1')
d.set_consumer_key('AIzctyodZcXAnrhiJgDn', 'KyXNoMULGJVIuBptBryUYghajsYaFWSb')
"""
d = discogs_client.Client('SoundTaste/0.1', user_token="user_token")
class Document(object):
  

    def __init__(self, filename):
        self.filename = filename
        



def main(): 
    for files in glob.glob("test/*.json"):
        twit = defaultdict(lambda: [])
        i = 0
        with io.open(files, mode='rt', encoding = 'utf-8') as infile:

            for line in infile:
                twit[i] = json.loads(line)
                i+= 1
            print twit[1]['text'].encode('utf-8')
if __name__ == '__main__':
    main()
