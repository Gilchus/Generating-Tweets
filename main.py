import data_preparation
import pandas_stuff


PARTIES = {"gruene": "Bündnis 90/Die Grünen", "linke": "Die Linke", "spd": "SPD", "afd": "AfD", "fdp": "FDP",
           "csu": "CSU", "cdu": "CDU"}


def main():

    #data_preparation.dump_tweets_to_p_by_party()
    tweets_gruene = data_preparation.read_pickle_party("gruene")
    df_gruene = pandas_stuff.list_to_df(tweets_gruene)
    print(df_gruene.head())
    print(df_gruene.count())
    tweets_linke = data_preparation.read_pickle_party("linke")
    df_linke = pandas_stuff.list_to_df(tweets_linke)
    print(df_linke.head())
    print(df_linke.count())
    tweets_spd = data_preparation.read_pickle_party("spd")
    df_spd = pandas_stuff.list_to_df(tweets_spd)
    print(df_spd.head())
    print(df_spd.count())
    tweets_afd = data_preparation.read_pickle_party("afd")
    df_afd = pandas_stuff.list_to_df(tweets_afd)
    print(df_afd.head())
    print(df_afd.count())
    tweets_fdp = data_preparation.read_pickle_party("fdp")
    df_fdp = pandas_stuff.list_to_df(tweets_fdp)
    print(df_fdp.head())
    print(df_fdp.count())
    tweets_csu = data_preparation.read_pickle_party("csu")
    df_csu = pandas_stuff.list_to_df(tweets_csu)
    print(df_csu.head())
    print(df_csu.count())
    tweets_cdu = data_preparation.read_pickle_party("cdu")
    df_cdu = pandas_stuff.list_to_df(tweets_cdu)
    print(df_cdu.head())
    print(df_cdu.count())




if __name__ == "__main__":
    main()