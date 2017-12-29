#!/usr/bin/env python3
import json
import random
import sys

def generate_random_playlist(playlist_len=5):
    episodes_file = "episodes.json"
    with open(episodes_file, 'r', encoding='utf-8-sig') as episodes:
        episodes_json = json.load(episodes)

        for i in range(0,playlist_len):
            season = random.randint(0,8)
            episode = random.randint(0,len(episodes_json["seasons"][season]["episodes"])-1)
            selected_episode = episodes_json["seasons"][season]["episodes"][episode]

            print("(_{}_)".format(i+1))
            print("Season: {}".format(season+1))
            print("Episode: {}".format(selected_episode["episode"]))
            print("Title: {}".format(selected_episode["title"]))
            print("\n{}\n".format(selected_episode["description"]))



if __name__ == "__main__":

    if len(sys.argv) == 2:
        p_length = int(sys.argv[1])
        generate_random_playlist(p_length)
    else:
        generate_random_playlist()