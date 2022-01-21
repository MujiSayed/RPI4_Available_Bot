import requests
from bs4 import BeautifulSoup


def rpi8gb():

    url = "https://www.adafruit.com/product/4564"
    response = requests.get(url).content

    soup_html5lib = BeautifulSoup(response, "html5lib")

    beautified = soup_html5lib.body.find_all(id="meta0_option_4564")

    if "Out of stock" not in beautified:
        return "RPI 8 GB is out of stock"
    else:
        return f"RPI 8 GB Available at {url}"
    
    


def discord_push():
    url = "https://discord.com/api/webhooks/933903313655709796/C3TSR1osoETvWeBERKakBraRyh0XBXZjsnwdVNGGVhfyvfCU_6ZehDO_hxlHUU5lpHlO" 
    rpi_availability = rpi8gb()
    data = {
    "content" : str(rpi_availability),
    "username" : "BasedMeezus"
    }


    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

rpi8gb()
discord_push()