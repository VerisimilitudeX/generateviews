#! /usr/bin/env python3
import webbrowser
from time import sleep

URL = "https://www.bing.com/search?DAF0=1&FORM=ANNTA1&PC=U531&adlt=strict&aqs=edge.0.0l9.2078j0j1&cvid=3be7defb486d479eb5a9ee0cbb1d1311&pglt=161&q=hello" # your url
COUNT = 0 # counter for refreshes

while COUNT < 20: # loop until 4000 refreshes
    webbrowser.open(URL) # open the url
    sleep(0) # wait for 1 seconds
    COUNT += 1 # increment the counter
    URL += "oihuldekugf"