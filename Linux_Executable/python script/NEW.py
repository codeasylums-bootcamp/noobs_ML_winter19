#!/home/ishuu/anaconda3/bin/python3

import webbrowser


n = input("Enter the Location you want to know the co-ordinates and other details\n")


string1 = "https://api.opencagedata.com/geocode/v1/json?q="
string2 = "&key=8316e6b32f084ff1b99e2eb0f34ebd62"

string3 = string1+n+string2

webbrowser.open(string3)


