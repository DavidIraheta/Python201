# make a virtual environment, install requests
#import the tools for making a web request
import requests
from pathlib import Path
import json

img_url = "https://randomfox.ca/images/13.jpg"
img = requests.get(img_url)

quote_url = "https://go-quote.azurewebsites.net/"
quote = requests.get(quote_url).json()['Text']
# breakpoint()
# print(quote)
#create a html structure
html = f"<p>{quote}<p/><img src='{img_url}'/>"
print(html)
f = Path.home().joinpath("Desktop").joinpath("quote.html")
f.write_text(html)
