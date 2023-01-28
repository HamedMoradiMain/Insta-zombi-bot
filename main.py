import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from modules.db import Database
import re
from instagrapi import Client
import time 
import threading
db = Database('instagram.db')
class Instabot(tk.Frame):
    ACCOUNTS = []
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Instagram Zombie Bot')
        # Width height
        master.geometry("335x600")
        self.create_widgets()
    def create_widgets(self):
        # Title Label 
        self.scraper_title = tk.Label(self.master, text="Photoshop Automation", font=("Bold",14), fg="black", height=2, width=30)
        self.scraper_title.grid(column=0,row=0,sticky=tk.NSEW)
        # Load accounts button 
        self.load_account_text = tk.StringVar()
        self.load_accounts_button = tk.Button(self.master, textvariable=self.load_account_text, command=self.load_accounts, font="Raleway", bg="white",fg="black", height=2, width=15)
        self.load_account_text.set("Load Accounts")
        self.load_accounts_button.grid(column=0,row=1,sticky=tk.NSEW)
        # Print all accounts button 
        self.print_account_text = tk.StringVar()
        self.print_accounts_button = tk.Button(self.master, textvariable=self.print_account_text, command=self.print_accounts, font="Raleway", bg="white",fg="black", height=2, width=15)
        self.print_account_text.set("Print Accounts")
        self.print_accounts_button.grid(column=0,row=2,sticky=tk.NSEW)
        # Post Entry Label
        self.post_link_label = tk.Label(self.master, text="Post Link", font=("Bold",14), fg="black", height=2, width=30)
        self.post_link_label.grid(column=0,row=3,sticky=tk.NSEW)
        # Post Entry
        self.post_text = tk.StringVar()
        self.post_entry = tk.Entry(self.master,textvariable=self.post_text,bg="white", fg="black", font=("Raleway",30),width=6)
        self.post_entry.grid(column=0,row=4,sticky=tk.NSEW)
        # Mass like Button 
        self.mass_like_text = tk.StringVar()
        self.mass_like_button = tk.Button(self.master, textvariable=self.mass_like_text, command=self.like, font="Raleway", bg="white",fg="black", height=2, width=15)
        self.mass_like_text.set("Like This Post")
        self.mass_like_button.grid(column=0,row=5,sticky=tk.NSEW)
        # Mass Comment 
        self.mass_comment_text = tk.StringVar()
        self.mass_comment_button = tk.Button(self.master, textvariable=self.mass_comment_text, command=self.comment, font="Raleway", bg="white",fg="black", height=2, width=15)
        self.mass_comment_text.set("Comment On This Post")
        self.mass_comment_button.grid(column=0,row=6,sticky=tk.NSEW)
        # Mass Unlike
        self.mass_unlike_text = tk.StringVar()
        self.mass_unlike_button = tk.Button(self.master, textvariable=self.mass_unlike_text, command=self.unlike, font="Raleway", bg="white",fg="black", height=2, width=15)
        self.mass_unlike_text.set("Unlike This Post")
        self.mass_unlike_button.grid(column=0,row=7,sticky=tk.NSEW)
        # Mass Follow 
        self.mass_follow_text = tk.StringVar()
        self.mass_follow_button = tk.Button(self.master, textvariable=self.mass_follow_text, command=self.follow, font="Raleway", bg="white",fg="black", height=2, width=15)
        self.mass_follow_text.set("Follow This Account")
        self.mass_follow_button.grid(column=0,row=8,sticky=tk.NSEW)
        # Mass Unfollow 
        self.mass_unfollow_text = tk.StringVar()
        self.mass_unfollow_button = tk.Button(self.master, textvariable=self.mass_unfollow_text, command=self.unfollow, font="Raleway", bg="white",fg="black", height=2, width=15)
        self.mass_unfollow_text.set("Unfollow This Account")
        self.mass_unfollow_button.grid(column=0,row=9,sticky=tk.NSEW)
        # Logs Label 
        self.logs_text = tk.StringVar()
        self.logs = tk.Label(root, textvariable=self.logs_text,  font=("Raleway",14),fg="black", height=2, width=30)
        self.logs_text.set("Ready to use!")
        self.logs.grid(columnspan=3, column=0, row=10)
    def load_accounts(self):
        file = askopenfile(parent=root, mode='r', title="Choose a file", filetypes=[("Text file", "*.txt")])
        if file is not None:
            for item in file.readlines():
                item = re.sub("\s{1,1000}","",item)
                item = item.split(",")
                #print()
                db.add(item[0],item[1])
    def print_accounts(self):
        items = db.fetch()
        for item in items:
            self.ACCOUNTS.append((item[1],item[2]))
        print(self.ACCOUNTS)
    def like(self):
        def call_back():
            for item in self.ACCOUNTS:
                # username password and post 
                user = item[0]
                password = item[1]
                post = self.post_text.get()
                print(user,password)
                print(post)
                try:
                    # login 
                    cl = Client()
                    cl.login(user,password)
                    # sleep
                    time.sleep(2)
                    # post id
                    post_id = cl.media_pk_from_url(post)
                    print(post_id)
                    # like the post 
                    cl.media_like(post_id)
                    #clean the post entry
                except Exception as e:
                    print(e)
                    pass 
            self.post_entry.delete(0,tk.END)
        # start a new thread 
        t1 = threading.Thread(target=call_back)
        t1.start()
    def comment(self):
        def call_back():
            for item in self.ACCOUNTS:
                # username password and post 
                user = item[0]
                password = item[1]
                post = self.post_text.get()
                print(user,password)
                print(post)
                try:
                    # login 
                    cl = Client()
                    cl.login(user,password)
                    # sleep
                    time.sleep(2)
                    # post id
                    post_id = cl.media_pk_from_url(post)
                    print(post_id)
                    # like the post 
                    cl.media_comment(post_id)
                    #clean the post entry
                except Exception as e:
                    print(e)
                    pass 
            self.post_entry.delete(0,tk.END)
        # start a new thread 
        t1 = threading.Thread(target=call_back)
        t1.start()
    def unlike(self):
        def call_back():
            for item in self.ACCOUNTS:
                # username password and post 
                user = item[0]
                password = item[1]
                post = self.post_text.get()
                print(user,password)
                print(post)
                try:
                    # login 
                    cl = Client()
                    cl.login(user,password)
                    # sleep
                    time.sleep(2)
                    # post id
                    post_id = cl.media_pk_from_url(post)
                    print(post_id)
                    # like the post 
                    cl.media_unlike(post_id)
                    #clean the post entry
                except Exception as e:
                    print(e)
                    pass 
            self.post_entry.delete(0,tk.END)
        # start a new thread 
        t1 = threading.Thread(target=call_back)
        t1.start()
    def follow(self):
        def call_back():
            for item in self.ACCOUNTS:
                # username password and post 
                user = item[0]
                password = item[1]
                username = self.post_text.get()
                print(user,password)
                print(username)
                try:
                    # login 
                    cl = Client()
                    cl.login(user,password)
                    # sleep
                    time.sleep(2)
                    # post id
                    user_id = cl.media_pk_from_url(username)
                    print(user_id)
                    # like the post 
                    cl.user_follow(user_id)
                    #clean the post entry
                except Exception as e:
                    print(e)
                    pass 
            self.post_entry.delete(0,tk.END)
        # start a new thread 
        t1 = threading.Thread(target=call_back)
        t1.start()
    def unfollow(self):
        def call_back():
            for item in self.ACCOUNTS:
                # username password and post 
                user = item[0]
                password = item[1]
                username = self.post_text.get()
                print(user,password)
                print(username)
                try:
                    # login 
                    cl = Client()
                    cl.login(user,password)
                    # sleep
                    time.sleep(2)
                    # post id
                    user_id = cl.media_pk_from_url(username)
                    print(user_id)
                    # like the post 
                    cl.user_unfollow(user_id)
                    #clean the post entry
                except Exception as e:
                    print(e)
                    pass 
            self.post_entry.delete(0,tk.END)
        # start a new thread 
        t1 = threading.Thread(target=call_back)
        t1.start()
if __name__ == "__main__":
    root = tk.Tk()
    app = Instabot(master=root)
    app.mainloop()