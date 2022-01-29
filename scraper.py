import requests
from bs4 import BeautifulSoup


baseurl = "https://www.adafruit.com/product/"


def rpi1gb():
    
    url = f"{baseurl}4295"
    response = requests.get(url).content

    soup_html5lib = BeautifulSoup(response, "html5lib")

    beautified = soup_html5lib.body.find_all(id="meta0_option_4295")

    if "Out of stock" not in beautified:
        return "RPI 1 GB is out of stock"
    else:
        return f"RPI 1 GB Available at {url}"


def rpi2gb():
    
    url = f"{baseurl}4292"
    response = requests.get(url).content

    soup_html5lib = BeautifulSoup(response, "html5lib")

    beautified = soup_html5lib.body.find_all(id="meta0_option_4292")

    if "Out of stock" not in beautified:
        return "RPI 2 GB is out of stock"
    else:
        return f"RPI 2 GB Available at {url}"


def rpi4gb():
    
    url = f"{baseurl}4296"
    response = requests.get(url).content

    soup_html5lib = BeautifulSoup(response, "html5lib")

    beautified = soup_html5lib.body.find_all(id="meta0_option_4296")

    if "Out of stock" not in beautified:
        return "RPI 4 GB is out of stock"
    else:
        return f"RPI 4 GB Available at {url}"
    

def rpi8gb():

    url = f"{baseurl}4564"
    response = requests.get(url).content

    soup_html5lib = BeautifulSoup(response, "html5lib")

    beautified = soup_html5lib.body.find_all(id="meta0_option_4564")

    if "Out of stock" not in beautified:
        return "RPI 8 GB is out of stock"
    else:
        return f"RPI 8 GB Available at {url}"
    
    


if __name__ == '__main__':
rpi8gb()
discord_push()