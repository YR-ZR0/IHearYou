# I Hear You
# YR-ZR0 (Jamex R)
# Hacknet Industries
# Last.Fm Recon Tool

import datetime
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile , askdirectory
import tkinter.messagebox

from pylast import PERIOD_OVERALL
import pylast


# Insert your own API keys from Last.fm
API_KEY = "Key"
API_SECRET = "Secret"

# File options
Today = str(datetime.date.today())
root =Tk()
Tk.withdraw(root)
dir = askdirectory()
output = open(dir + "/" +"IHY" + Today + ".log", mode='a',)

# Enter Own User name and password
username = "OwnUser"
# This hashes your password using MD5 and sends it off for verification
password_hash = pylast.md5("P@$$W0RD")

# network item used for making a connection all calls go through this item
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=
    API_SECRET, username=username, password_hash=password_hash)

# Target Required
target = input(" Please enter Target ")
print("Your target is: " + target)
output.write("Target is: " + target + "\n")
# Function to get loved tracks
def Love(target):

    # limit can be raised for more tracks but be respectful of your calls and follow Last.fm guidelines
    Loves = network.get_user(target).get_loved_tracks(limit=50)
    output.write("LOVED TRACKS" + "\n")
    for s in Loves:
        output.write(str((s[0])) + "\n")
    Menu()
       

# Function: Fetch available Details from the network
def details(target):

        age = network.get_user(target).get_age() 
        country = network.get_user(target).get_country() 
        Gend = network.get_user(target).get_gender() 
        output.write("They are " + str(age) + " Years Old" + " and they are a " + str(Gend) + " Living in " + str(country) + "\n") 
        Menu()
# Function: Get Top Tracks
def TT(target):


    Top = network.get_user(target).get_top_artists(period=PERIOD_OVERALL)
    output.write("TOP TRACKS " + "\n")
    
    for j in Top:
        output.write(str((j[0]))+ "\n")
    Menu()
        
def Menu():
    # Simple Menu system
    print("1. Get Loved" + "\n" + "2. Get Details" + "\n" + "3. Get Top Tracks" + "\n" + "4. Close File")
    choice = input("Please enter a choice: ")
    if (choice == "1"):
        Love(target)
    elif(choice == "2"):
        details(target)
    elif(choice == "3"):
        TT(target)
    elif(choice == "4"):
        output.close()
        
Menu()
