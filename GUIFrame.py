from tkinter import *


def submit():
    global api_key
    api_key = api_entry.get()

    global name
    name = id_entry.get()

    global match_num
    match_num = match_count_entry.get()

    new()

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

clear_button_button = Button(submit_button_frame, text="Clear", command="")
clear_button_button.pack(side="right")

submit_button_button = Button(submit_button_frame, text="Submit", command=submit)
submit_button_button.pack(side="right")

root.mainloop()