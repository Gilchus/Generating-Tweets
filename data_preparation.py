import pandas as pd
import json_lines
import os
import time

path = "C:/Users/taxi/JupyterLab/twitter-bundestag/data/"

tweets_all = {"acc_name":  {"mdb_name": "", "party": "", "tweets": []}}  # initialize dictionary with twitter acc. name as key

for root, dirs, files in os.walk(path):
    for filename in files:
        # print(filename)
        with open(path + filename) as f:
            for item in json_lines.reader(f):
                try:
                    mdb_name = item["account_data"]["Name"]
                    acc_name = item["account_data"]["screen_name"]
                    party = item["account_data"]["Partei"]
                    # print(f"------------------ {mdb_name} ({party}) -------------------------------------------------------")
                    # print()
                    # print(item["response"]["data"])
                    # print(len(item["response"]["data"]))

                    tweet_count = len(item["response"]["data"])
                    tweet_list = []
                    for i in range(tweet_count):

                        tweet_text = item["response"]["data"][i]["text"]
                        # creation_date = item["response"]["data"][i]["created_at"]
                        if tweet_text[:4] == "RT @":
                            tweet_text = tweet_text.split(":", 1)[1].strip()
                        tweet_list.append(tweet_text)


                        # print(tweet_text)
                        # print(creation_date)
                        # print("....................................")
                        #time.sleep(1)

                    tweets_all[acc_name] = {}
                    tweets_all[acc_name]["mdb_name"] = mdb_name
                    tweets_all[acc_name]["party"] = party
                    tweets_all[acc_name]["tweets"] = tweet_list
                    print(tweets_all[acc_name])


                except Exception as inst: # throw exception if there is no tweet-text-data in .jl-file
                    print(type(inst))
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx empty xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


                # print(tweet_list)
                print(
                    "--------------------------------------------------------------------------------------------------")
                # time.sleep(10)