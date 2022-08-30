from email.mime import image
from bs4 import *
import requests
import os

url = "https://itms.online/"
page = requests.get("https://itms.online/partner")

souped = BeautifulSoup(page.content, "html.parser")

imgs = souped.find_all("img")

for img in imgs :
    imglink = url + img.attrs.get("src")
    image = requests.get(imglink).content
    filename = r"ITmS_Partner" + imglink[imglink.rfind("/"):]
    with open(filename, "wb") as file:
        file.write(image)