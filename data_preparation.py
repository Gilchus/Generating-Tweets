import pandas as pd
import json_lines
import os
import pickle

# import time

import main

PATH_RAW = "C:/Users/taxi/JupyterLab/twitter-bundestag/data_raw/"
PATH_PICKLE = "C:/Users/taxi/JupyterLab/twitter-bundestag/data_pickle/"
PARTIES = ['Bündnis 90/Die Grünen', 'Die Linke', 'SPD', 'AfD', 'FDP', 'CSU', 'CDU']


def dump_tweets_to_p_by_party():
    tweets_gruene = []
    tweets_linke = []
    tweets_spd = []
    tweets_afd = []
    tweets_fdp = []
    tweets_csu = []
    tweets_cdu = []

    for root, dirs, files in os.walk(PATH_RAW):
        for filename in files:
            with open(PATH_RAW + filename) as f:
                for item in json_lines.reader(f):
                    try:
                        party_of_tweets = item["account_data"]["Partei"]
                        tweet_count = len(item["response"]["data"])

                        for i in range(tweet_count):
                            tweet_text = item["response"]["data"][i]["text"]

                            if tweet_text[:4] == "RT @":
                                tweet_text = tweet_text.split(":", 1)[1]

                            tweet_text = tweet_text.strip()

                            if party_of_tweets == PARTIES[0]:
                                tweets_gruene.append(tweet_text)
                                # print("gruene tweet appended to tweets_gruene")

                            elif party_of_tweets == PARTIES[1]:
                                tweets_linke.append(tweet_text)
                                # print("linke tweet appended to tweets_linke")

                            elif party_of_tweets == PARTIES[2]:
                                tweets_spd.append(tweet_text)
                                # print("spd tweet appended to tweets_spd")

                            elif party_of_tweets == PARTIES[3]:
                                tweets_afd.append(tweet_text)
                                # print("afd tweet appended to tweets_afd")

                            elif party_of_tweets == PARTIES[4]:
                                tweets_fdp.append(tweet_text)
                                # print("fdp tweet appended to tweets_fdp")

                            elif party_of_tweets == PARTIES[5]:
                                tweets_csu.append(tweet_text)
                                # print("csu tweet appended to tweets_csu")

                            elif party_of_tweets == PARTIES[6]:
                                tweets_cdu.append(tweet_text)
                                # print("cdu tweet appended to tweets_cdu")





                    except Exception as inst:  # throw exception if there is no tweet-text-data in .jl-file:
                        print("empty dataset ignored: " + filename)
                        pass

            print(filename + " done")

    pickle.dump(tweets_gruene, open(PATH_PICKLE + "tweets_gruene.p", "wb"))
    print("tweets_gruene.p done")
    pickle.dump(tweets_linke, open(PATH_PICKLE + "tweets_linke.p", "wb"))
    print("tweets_linke.p done")
    pickle.dump(tweets_spd, open(PATH_PICKLE + "tweets_spd.p", "wb"))
    print("tweets_spd.p done")
    pickle.dump(tweets_afd, open(PATH_PICKLE + "tweets_afd.p", "wb"))
    print("tweets_afd.p done")
    pickle.dump(tweets_fdp, open(PATH_PICKLE + "tweets_fdp.p", "wb"))
    print("tweets_fdp.p done")
    pickle.dump(tweets_cdu, open(PATH_PICKLE + "tweets_cdu.p", "wb"))
    print("tweets_cdu.p done")
    pickle.dump(tweets_csu, open(PATH_PICKLE + "tweets_csu.p", "wb"))
    print("tweets_csu.p done")
    print("successfully finished dumping tweets to pickle files")

    return


def read_pickle_party(party):
    tweets_party = pickle.load(open(PATH_PICKLE + "tweets_" + party + ".p", "rb"))
    return tweets_party


# def data_to_dict():
#     tweets_all = {}
#     # "acc_name": {"mdb_name": "", "party": "", "tweets": []}}  # initialize dictionary with twitter acc. name as key
#
#     for root, dirs, files in os.walk(PATH_RAW):
#         for filename in files:
#             # print(filename)
#             with open(PATH_RAW + filename) as f:
#                 for item in json_lines.reader(f):
#                     try:
#                         mdb_name = item["account_data"]["Name"]
#                         acc_name = item["account_data"]["screen_name"]
#                         party = item["account_data"]["Partei"]
#                         # print(f"------------------ {mdb_name} ({party}) -------------------------------------------------------")
#                         # print()
#                         # print(item["response"]["data"])
#                         # print(len(item["response"]["data"]))
#
#                         tweet_count = len(item["response"]["data"])
#                         tweet_list = []
#                         for i in range(tweet_count):
#
#                             tweet_text = item["response"]["data"][i]["text"]
#                             # creation_date = item["response"]["data"][i]["created_at"]
#                             if tweet_text[:4] == "RT @":
#                                 tweet_text = tweet_text.split(":", 1)[1]
#                             tweet_list.append(tweet_text.strip())
#
#                             # print(tweet_text)
#                             # print(creation_date)
#                             # print("....................................")
#                             # time.sleep(1)
#
#                         tweets_all[acc_name] = {}
#                         tweets_all[acc_name]["mdb_name"] = mdb_name
#                         tweets_all[acc_name]["party"] = party
#                         tweets_all[acc_name]["tweets"] = tweet_list
#                         # print(tweets_all[acc_name])
#
#                     except Exception as inst:  # throw exception if there is no tweet-text-data in .jl-file
#                         # print(inst)
#                         pass
#
#     return tweets_all

# def dict_to_csv_by_party(dictionary):
#     gruene = open("gruene_tweets.csv", "a+")
#     linke = open("linke_tweets.csv", "a+")
#     spd = open("sod_tweets.csv", "a+")
#     afd = open("afd_tweets.csv", "a+")
#     fdp = open("fdp_tweets.csv", "a+")
#     csu = open("csu.csv", "a+")
#     cdu = open("cdu.csv", "a+")
#
#     for entry in dictionary:
#         if entry["party"] == "Bündnis 90/Die Grünen":
#
#         elif entry["party"] == "Die Linke":
#
#
#         else if entry["party"] == "SPD":
#
#         else if entry["party"] == "AfD":
#
#         else if entry["party"] == "FDP":
#
#         else if entry["party"] == "CSU":
#
#         else if entry["party"] == "CDU:


def dict_to_df(dictionary):
    # Set ipython's max row display
    pd.set_option('display.max_row', 1000)

    # Set iPython's max column width to 50
    pd.set_option('display.max_columns', 50)

    # Specify orient='index' to create the DataFrame using dictionary keys as rows
    return pd.DataFrame.from_dict(dictionary, orient='index')


def get_tweets_by_party(df, party):
    print("getting all tweets from: " + party)
    tweets_by_party_df = df[df["party"] == party]

    return tweets_by_party_df.tweets
