#! /usr/bin/env python3
import webbrowser
from time import sleep

url = "https://visitor-badge.laobi.icu/badge?page_id=VerisimilitudeX.VerisimilitudeX" # your url
count = 0 # counter for refreshes

while count < 4000: # loop until 4000 refreshes
    webbrowser.open(url) # open the url
    sleep(0) # wait for 1 seconds
    count += 1 # increment the counter
