from riotwatcher import LolWatcher
from datetime import datetime

name = input("ID: ")

lol_watcher = LolWatcher('RGAPI-ac524dea-9e7e-4a8d-a6a4-eee82569dce1', default_match_v5=True)

# accountID = "t3HqOTTMP985E5vYgZ54w4R7k3uRXV2M-zzDWSuFHFVT4A"

my_region = 'na1'

me = lol_watcher.summoner.by_name(my_region, name)

puuid = me["puuid"]

print(puuid)

matchlist = lol_watcher.match.matchlist_by_puuid('AMERICAS', puuid)

# mlst = lol_watcher.match_v5(region=my_region, encrypted_summoner_id=puuid)
print(matchlist)


