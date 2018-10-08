#!/usr/bin/env python3

import requests
import json
import re
import bs4


def main():
    try:
        # Get the movie title and search it from OMDbApi to get the IMDB ID

        base_url = "https://yts-subtitles.com/"
        movie_title = str(input("What movie would you like subtitles for?\n"))

        count = len(re.findall(r'\w+', movie_title))

        if count > 1:
            title = ' '.join(movie_title.split())
            chars = title.replace(" ", "-")
            chars += "/"
        else:
            chars = movie_title
            chars += "/"

        def fetch_omdbapi(movie_title):
            omdbapi = "http://www.omdbapi.com/?apikey=e16de7a1&type=movie&t="
            req = requests.get(omdbapi + movie_title)
            resp = json.loads(req.text)
            return resp

        content = fetch_omdbapi(movie_title)
        imdbID = content['imdbID']
        print(content['imdbID'])

        # file_hash = re.findall('(?:\d{6,8})',)

        subtitle_url = base_url + chars + imdbID
        print(subtitle_url)

        resp = requests.get(re.findall(subtitle_url+"?:\d{6,8}",""))
        print(resp.content)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
