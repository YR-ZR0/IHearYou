# I Hear You
# YR-ZR0 (Jamex R)
# Hacknet Industries
# Last.Fm Recon Tool

import pylast
from pylast import PERIOD_OVERALL

# Insert your own API keys from Last.fm
API_KEY = "PublicMe"
API_SECRET = "SecretMe"

# Enter Own User name and password
username = "TestMe"
# This hashes your password using MD5 and sends it off for verification
password_hash = pylast.md5("P@$$w0RD")

#network item used for making a connection all calls go through this item
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=
    API_SECRET, username=username, password_hash=password_hash)

# Target Required
target = input(" Please enter Target ")
print("Your target is: " + target)

# Function to get loved tracks
def Love(target):

    # limit can be raised for more tracks but be respectful of your calls and follow Last.fm guidelines
    Loves = network.get_user(target).get_loved_tracks(limit=50)
    for s in Loves:
        print(s[0])
       

# Function: Fetch available Details from the network
def details(target):


        age = network.get_user(target).get_age()
        country = network.get_user(target).get_country()
        Gend = network.get_user(target).get_gender()

        print(age)
        print(Gend)
        print(country)

# Function: Get Top Tracks
def TT(target):


    Top = network.get_user(target).get_top_artists(period=PERIOD_OVERALL)
    for j in Top:
        print(j[0])

# Simple Menu system
print("1. Get Loved" + "\n" + "2. Get Details" + "\n" + "3. Get Top Tracks")
choice = input("Please enter a choice: ")
if (choice == "1"):
    Love(target)
elif(choice =="2"):
    details(target)
elif(choice=="3"):
    TT(target)