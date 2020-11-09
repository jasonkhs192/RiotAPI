from tkinter import *
from riotwatcher import LolWatcher, ApiError
from tkinter import messagebox as msgbox
from datetime import datetime

def test(api_key, name, match_num):
    try:
        lol_watcher = LolWatcher(api_key)
        my_region = 'na1'
        me = lol_watcher.summoner.by_name(my_region, name)
        accountID = me["accountId"]
        mlst = lol_watcher.match.matchlist_by_account(my_region, accountID)
        recent_match = mlst["matches"][int(match_num)]["gameId"]

        my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])

        root2 = Tk()
        root2.title("Jason.GG")
        root2.resizable(False, False)
        lbl_frame = LabelFrame(root2)
        lbl_frame.pack(fill="x")
        lbl_frame2 = LabelFrame(root2)
        lbl_frame2.pack(fill="x")
        lbl_frame3 = LabelFrame(root2)
        lbl_frame3.pack(fill="x")
        lbl_frame4 = LabelFrame(root2)
        lbl_frame4.pack(fill="x")
        lbl_frame5 = LabelFrame(root2)
        lbl_frame5.pack(fill="x")
        lbl_frame6 = LabelFrame(root2)
        lbl_frame6.pack(fill="x")
        lbl_frame7 = LabelFrame(root2)
        lbl_frame7.pack(fill="x")
        lbl_frame8 = LabelFrame(root2)
        lbl_frame8.pack(fill="x")
        lbl_frame9 = LabelFrame(root2)
        lbl_frame9.pack(fill="x")
        lbl_frame10 = LabelFrame(root2)
        lbl_frame10.pack(fill="x")
        lbl_frame11 = LabelFrame(root2)
        lbl_frame11.pack(fill="x")
        lbl_frame12 = LabelFrame(root2)
        lbl_frame12.pack(fill="x")
        lbl_frame13 = LabelFrame(root2)
        lbl_frame13.pack(fill="x")
        lbl_frame14 = LabelFrame(root2)
        lbl_frame14.pack(fill="x")
        lbl_frame15 = LabelFrame(root2)
        lbl_frame15.pack(fill="x")
        lbl_frame16 = LabelFrame(root2)
        lbl_frame16.pack(fill="x")
        lbl_frame17 = LabelFrame(root2)
        lbl_frame17.pack(fill="x")
        lbl_frame18 = LabelFrame(root2)
        lbl_frame18.pack(fill="x")
        lbl_frame19 = LabelFrame(root2)
        lbl_frame19.pack(fill="x")
        lbl_frame20 = LabelFrame(root2)
        lbl_frame20.pack(fill="x")


        lbl = Label(lbl_frame, text="Hello, {}. Welcome to Summoner's Rift!".format(me["name"]))
        lbl.pack(side="left")

        stat_count = 0
        for count in my_ranked_stats:
            stat_count = stat_count + 1
        if stat_count == 1:
            stat1 = my_ranked_stats[0]
            lbl2 = Label(lbl_frame2, text="Rank: {} {} {} LP".format(stat1["tier"], stat1["rank"], stat1["leaguePoints"]))
            lbl2.pack(side="left")
            # print("Rank: {} {} {} LP".format(stat1["tier"], stat1["rank"], stat1["leaguePoints"]))

        if stat_count == 2:
            stat1 = my_ranked_stats[0]
            stat2 = my_ranked_stats[1]
            if stat1["queueType"] == "RANKED_SOLO_5x5":
                lbl3 = Label(lbl_frame2, text="Rank: {} {} {} LP".format(stat1["tier"], stat1["rank"], stat1["leaguePoints"]))
                lbl3.pack(side="left")
                # print("Rank: {} {} {} LP".format(stat1["tier"], stat1["rank"], stat1["leaguePoints"]))
            else:
                lbl3 = Label(lbl_frame2, text="Rank: {} {} {} LP".format(stat2["tier"], stat2["rank"], stat2["leaguePoints"]))
                lbl3.pack(side="left")
                # print("Rank: {} {} {} LP".format(stat2["tier"], stat2["rank"], stat2["leaguePoints"]))

        game = lol_watcher.match.by_id(my_region, recent_match)

        lbl4 = Label(lbl_frame4, text=">---- Last Match Status ----<")
        lbl4.pack()
        # print("---------------------------------------------")
        # print("             Last Match Status")
        # print("---------------------------------------------")

        if game["queueId"] == 420:
            lbl5 = Label(lbl_frame5, text="Game Type: Ranked")
            lbl5.pack(side="left")
            # print("Game Type: Ranked")
        else:
            lbl5 = Label(lbl_frame5, text="Game Type: Casual")
            lbl5.pack(side="left")
            # print("Game Type: Casual")

        if game["gameType"] == "CUSTOM_GAME":
            lbl5 = Label(lbl_frame5, text="**Custom Game**")
            lbl5.pack(side="left")
            # print("**Custom Game**")

        classic = 0
        if game["gameMode"] == "CLASSIC":
            classic = classic + 1
            lbl6 = Label(lbl_frame6, text="Map: Summoner's Rift")
            lbl6.pack(side="left")
            # print("Map: Summoner's Rift")
        elif game["gameMode"] == "ARAM":
            lbl6 = Label(lbl_frame6, text="Map: Howling Abyss [ARAM]")
            lbl6.pack(side="left")
            # print("Map: Howling Abyss [ARAM]")
        elif game["gameMode"] == "URF":
            lbl6 = Label(lbl_frame6, text="Map: Summoner's Rift [URF]")
            lbl6.pack(side="left")
            # print("Map: Summoner's Rift [URF]")
        elif game["gameMode"] == "ONEFORALL":
            lbl6 = Label(lbl_frame6, text="Map: Summoner's Rift [OneForAll]")
            lbl6.pack(side="left")
            # print("Map: Summoner's Rift [OneForAll]")
        else:
            lbl6 = Label(lbl_frame6, text="Map: Unknown")
            lbl6.pack(side="left")
            # print("Map: Unknown")

        # find participant id with account id
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        position = 0
        for x in lst:
            if game["participantIdentities"][x]["player"]["accountId"] == accountID:
                position = position + x
                if game["participants"][x]["stats"]["win"] and game["gameDuration"] > 300:
                    lbl7 = Label(lbl_frame7, text="-Match Status: Victory")
                    lbl7.pack(side="left")
                    # print("-Match Status: Victory")
                elif game["participants"][x]["stats"]["win"] == False and game["gameDuration"] > 300:
                    lbl7 = Label(lbl_frame7, text="-Match Status: Defeat")
                    lbl7.pack(side="left")
                else:
                    lbl7 = Label(lbl_frame7, text="-Match Status: Remake")
                    lbl7.pack(side="left")

                    # print("-Match Status: Defeat")

        duration_seconds = game["gameDuration"]
        duration_minutes = duration_seconds // 60
        duration_seconds_remainder = duration_seconds % 60
        if duration_seconds_remainder < 10:
            duration_seconds_remainder = "0" + str(duration_seconds_remainder)

        lbl8 = Label(lbl_frame8, text="-Game Length: {}:{}".format(duration_minutes, duration_seconds_remainder))
        lbl8.pack(side="left")
        # print("-Game Length: {}:{}".format(duration_minutes, duration_seconds_remainder))

        timestamp = game["gameCreation"] / 1000
        matchdate_start = round(timestamp)
        dt_object = datetime.fromtimestamp(matchdate_start)
        utc_format = dt_object
        utc = datetime.strptime(str(utc_format), '%Y-%m-%d %H:%M:%S')
        time = utc.strftime("%Y-%m-%d %I:%M:%S %p")
        lbl9 = Label(lbl_frame9, text="-Match Start Date & Time: {}".format(time))
        lbl9.pack(side="left")
        # print("-Match Start Date & Time: {}".format(time))

        matchdate_end = matchdate_start + duration_seconds
        dt_object = datetime.fromtimestamp(matchdate_end)
        utc_format = dt_object
        utc = datetime.strptime(str(utc_format), '%Y-%m-%d %H:%M:%S')
        time = utc.strftime("%Y-%m-%d %I:%M:%S %p")
        lbl10 = Label(lbl_frame10, text="-Match End Date & Time: {}".format(time))
        lbl10.pack(side="left")
        # print("-Match End Date & Time: {}".format(time))

        time_diff = (datetime.now().timestamp() - matchdate_end)
        if time_diff // 60 < 60:
            time_diff_min = time_diff // 60
            time_diff_sec = round(time_diff % 60)
            if time_diff_sec == 0:
                time_diff_sec = "00"
            elif time_diff_sec < 10:
                time_diff_sec = "0" + str(time_diff_sec)

            lbl11 = Label(lbl_frame11, text="-Match Ended {}min {}sec ago".format(int(time_diff_min), time_diff_sec))
            lbl11.pack(side="left")
            # print("-Match Ended {}min {}sec ago".format(int(time_diff_min), time_diff_sec))
        else:
            time_diff_min = time_diff / 60
            time_diff_hour = time_diff_min / 60
            lbl12 = Label(lbl_frame12, text="-Match Ended {} hour(s) ago.".format(round(time_diff_hour)))
            lbl12.pack(side="left")
            # print("-Match Ended {} hour(s) ago.".format(round(time_diff_hour)))

        champion_list = lol_watcher.data_dragon.champions("10.22.1")
        # print(test["data"]["Aatrox"]["key"])

        my_champion_id = (game["participants"][position]["championId"])

        for champion in champion_list["data"]:
            if (champion_list["data"][champion]["key"]) == str(my_champion_id):
                lbl13 = Label(lbl_frame13, text="-Champion: {}".format(champion))
                lbl13.pack(side="left")
                # print("-Champion: {}".format(champion))

        kills = game["participants"][position]["stats"]["kills"]
        deaths = game["participants"][position]["stats"]["deaths"]
        assists = game["participants"][position]["stats"]["assists"]
        survive_time = game["participants"][position]["stats"]["longestTimeSpentLiving"]

        try:
            kda = (kills + assists) / deaths
            kda = round(kda, 2)

            lbl14 = Label(lbl_frame14, text="-KDA: {}/{}/{} | Ratio: {}:1".format(kills, deaths, assists, kda))
            lbl14.pack(side="left")
        except ZeroDivisionError:
            lbl14 = Label(lbl_frame14, text="-KDA: {}/{}/{} | Ratio: Perfect".format(kills, deaths, assists))
            lbl14.pack(side="left")
        # print("-KDA: {}/{}/{} | Ratio: {}:1".format(kills, deaths, assists, kda))
        survive_time_minutes = survive_time // 60
        survive_remainder = survive_time % 60
        if survive_remainder < 10:
            survive_remainder = "0" + str(survive_remainder)
        lbl15 = Label(lbl_frame15, text="-Longest time spent living: {} seconds. [{}:{}]".format(survive_time, survive_time_minutes, survive_remainder))
        lbl15.pack(side="left")
        # print(
        #     "-Longest time spent living: {} seconds. [{}:{}]".format(survive_time, survive_time_minutes,
        #                                                              survive_remainder))

        if classic == 1:
            wardsPlaced = game["participants"][position]["stats"]["wardsPlaced"]
            wardsKilled = game["participants"][position]["stats"]["wardsKilled"]
            visionWardsBoughtInGame = game["participants"][position]["stats"]["visionWardsBoughtInGame"]
            visionScore = game["participants"][position]["stats"]["visionScore"]

            lbl16 = Label(lbl_frame16, text="-Wards Placed Count: {}".format(wardsPlaced))
            lbl16.pack(side="left")
            # print("-Wards Placed Count: {}".format(wardsPlaced))
            lbl17 = Label(lbl_frame17, text="-Wards Killed Count: {}".format(wardsKilled))
            lbl17.pack(side="left")
            # print("-Wards Killed Count: {}".format(wardsKilled))
            lbl18 = Label(lbl_frame18, text="-Pink Wards Bought Count: {}".format(visionWardsBoughtInGame))
            lbl18.pack(side="left")
            # print("-Pink Wards Bought Count: {}".format(visionWardsBoughtInGame))
            time = duration_seconds / 60
            above_average = time * 1.5
            average = time
            if visionScore > above_average:
                lbl19 = Label(lbl_frame19, text="-Vision Score: {} | Above Average".format(visionScore))
                lbl19.pack(side="left")
                # print("-Vision Score: {} | Above Average".format(visionScore))
            elif visionScore <= above_average and visionScore >= average:
                lbl19 = Label(lbl_frame19, text="-Vision Score: {} | Average".format(visionScore))
                lbl19.pack(side="left")
                # print("-Vision Score: {} | Average".format(visionScore))
            elif visionScore < average:
                lbl19 = Label(lbl_frame19, text="-Vision Score: {} | Below Average".format(visionScore))
                lbl19.pack(side="left")
                # print("-Vision Score: {} | Below Average".format(visionScore))

        def close():
            root2.destroy()


        Button(lbl_frame20, text="Close", command=close).pack(side="right")
    except ApiError as err:
        if err.response.status_code == 403:
            msgbox.showerror("Error", "Wrong API Key or Empty Summoner's Name")
            # print("Wrong API Key")
        elif err.response.status_code == 404:
            msgbox.showerror("Error", "Invalid Summoner's Name")
        else:
            msgbox.showerror("Error", "Error 404")
    except IndexError:
        msgbox.showerror("Error", "Invalid Match #.\nPick [0 ~ 99]\nExample:\n0 = Last match\n99 = Last 100th match.")
    except ValueError:
        msgbox.showerror("Error", "Invalid Match #.\nPick [0 ~ 99]\nExample:\n0 = Last match\n99 = Last 100th match.")


def submit():
    api_key = api_entry.get()
    name = id_entry.get()
    match_num = match_count_entry.get()
    test(api_key, name, match_num)


def clear():
    api_entry.delete(0,END)
    id_entry.delete(0, END)
    match_count_entry.delete(0, END)


root = Tk()
root.title("Jason.GG")
root.resizable(False, False)

api_frame = LabelFrame(root)
api_frame.pack(fill="x")

api_label = Label(api_frame, text="API Key: ")
api_label.pack(side="left")

api_entry = Entry(api_frame)
api_entry.pack(side="right")

id_frame = LabelFrame(root)
id_frame.pack(fill="x")

id_label = Label(id_frame, text="Summoner's Name: ")
id_label.pack(side="left")

id_entry = Entry(id_frame)
id_entry.pack(side="right")

match_count_frame = LabelFrame(root)
match_count_frame.pack(fill="x")

match_count_label = Label(match_count_frame, text="Past Match #: ")
match_count_label.pack(side="left")

match_count_entry = Entry(match_count_frame)
match_count_entry.pack(side="right")

submit_button_frame = LabelFrame(root)
submit_button_frame.pack(fill="x")

clear_button_button = Button(submit_button_frame, text="Clear", command=clear)
clear_button_button.pack(side="right")

submit_button_button = Button(submit_button_frame, text="Submit", command=submit)
submit_button_button.pack(side="right")

root.mainloop()