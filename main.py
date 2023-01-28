import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from modules.db import Database
import re
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
        self.scraper_title = tk.Label(self.master, text="Photoshop Automation", font=("Bold",14), fg="black", height=2, width=30)
        self.scraper_title.grid(column=0,row=0,sticky=tk.NSEW)
        # load accounts button 
        self.load_account_text = tk.StringVar()
        self.load_accounts_button = tk.Button(self.master, textvariable=self.load_account_text, command=self.load_accounts, font="Raleway", bg="white",fg="black", height=2, width=15)
        self.load_account_text.set("Load Accounts")
        self.load_accounts_button.grid(column=0,row=1,sticky=tk.NSEW)
        # print all accounts button 
        self.print_account_text = tk.StringVar()
        self.print_accounts_button = tk.Button(self.master, textvariable=self.print_account_text, command=self.print_accounts, font="Raleway", bg="white",fg="black", height=2, width=15)
        self.print_account_text.set("Print Accounts")
        self.print_accounts_button.grid(column=0,row=2,sticky=tk.NSEW)
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
    def comment(self):
        pass
    def like(self):
        pass
    def unlike(self):
        pass
    def follow(self):
        pass
    def unfollow(self):
        pass
if __name__ == "__main__":
    root = tk.Tk()
    app = Instabot(master=root)
    app.mainloop()