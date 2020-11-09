from riotwatcher import LolWatcher, ApiError
try:
    x = LolWatcher("").lol_status.shard_data("na1")
    print(x)
except ApiError as err:
    if err.response.status_code == 403:
        print("Wrong API Code")


#0x0344E7C0

# from UnixTime import time_convert
#
# name = input("ID: ")
#
# lol_watcher = LolWatcher('')
#
# my_region = 'na1'
#
# me = lol_watcher.summoner.by_name(my_region, name)
#
# accountID = me["accountId"]
#
# # accountID = "t3HqOTTMP985E5vYgZ54w4R7k3uRXV2M-zzDWSuFHFVT4A"
#
# mlst = lol_watcher.match.matchlist_by_account(my_region, accountID)
# recent_match = mlst["matches"][0]["gameId"]
#
# my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
# game = lol_watcher.match.by_id(my_region, recent_match)
# print(my_ranked_stats)
#
# # from datetime import datetime
# #
# # # utc = datetime.utcnow()
# # timestamp = 1604042663
# # dt_object = datetime.fromtimestamp(timestamp)
# # utc_format = dt_object
# # utc = datetime.strptime(str(utc_format), '%Y-%m-%d %H:%M:%S')
# # print(utc)