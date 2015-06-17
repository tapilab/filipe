# -*- coding: utf-8 -*-

from TwitterAPI import TwitterAPI
import json
import io
import discogs_client
"""d = discogs_client.Client('SoundTaste/0.1')
d.set_consumer_key('AIzctyodZcXAnrhiJgDn', 'KyXNoMULGJVIuBptBryUYghajsYaFWSb')
"""
d = discogs_client.Client('SoundTaste/0.1', user_token="keys")


def main():
    results = d.search('Stockholm By Night', type='release')
    print results.pages

    artist = results[0].artists[0]
    print artist.name
if __name__ == '__main__':
    main()
