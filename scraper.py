import requests
from bs4 import BeautifulSoup
from discord_notif import discord_push
from email_notif import email_notif

baseurl = "https://www.adafruit.com/product/"
RPI1GB_URL = f"{baseurl}4295"
RPI2GB_URL = f"{baseurl}4292"
RPI4GB_URL = f"{baseurl}4296"
RPI8GB_URL = f"{baseurl}4564"

def rpi1gb_isavailable():
    
    url = f"{baseurl}4295"
    response = requests.get(url).content

    soup_html5lib = BeautifulSoup(response, "html5lib")

    beautified = soup_html5lib.body.find_all(id="meta0_option_4295")

    if "Out of stock" not in beautified:
        return False
    else:
        return True


def rpi2gb_isavailable():
    
    url = f"{baseurl}4292"
    response = requests.get(url).content

    soup_html5lib = BeautifulSoup(response, "html5lib")

    beautified = soup_html5lib.body.find_all(id="meta0_option_4292")

    if "Out of stock" not in beautified:
        return False
    else:
        return True


def rpi4gb_isavailable():
    
    url = f"{baseurl}4296"
    response = requests.get(url).content

    soup_html5lib = BeautifulSoup(response, "html5lib")

    beautified = soup_html5lib.body.find_all(id="meta0_option_4296")

    if "Out of stock" not in beautified:
        return False
    else:
        return True


def rpi8gb_isavailable():

    url = RPI8GB_URL
    response = requests.get(url).content

    soup_html5lib = BeautifulSoup(response, "html5lib")

    beautified = soup_html5lib.body.find_all(id="meta0_option_4564")

    if "Out of stock" not in beautified:
        return True
    else:
        return False

    


if __name__ == '__main__':
    if rpi1gb_isavailable() == True:
        #discord_push(RPI1GB_URL, "4-1GB")
        email_notif(RPI1GB_URL, "4-1GB")
    if rpi2gb_isavailable() == True:
        #discord_push(RPI2GB_URL, "4-2GB")
        email_notif(RPI2GB_URL, "4-2GB")
    if rpi4gb_isavailable() == True:
        #discord_push(RPI4GB_URL, "4-4GB")
        email_notif(RPI4GB_URL, "4-4GB")
    if rpi8gb_isavailable() == True:
        #discord_push(RPI8GB_URL, "4-8GB")
        email_notif(RPI8GB_URL, "4-8GB")                