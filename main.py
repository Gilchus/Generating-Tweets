import data_preparation as dp


# parties: ['Bündnis 90/Die Grünen' 'Die Linke' 'SPD' 'AfD' 'FDP' 'CSU' 'CDU']
def main():
    data = dp.data_to_dict()
    df = dp.dict_to_df(data)
    # print(df.head())
    # print(df["mdb_name"])
    # print(df.party)
    # print(df.party.unique())
    # print(df.tweets)

    print(dp.get_tweets_by_party(df, "Die Linke").head())





if __name__ == "__main__":
    main()
