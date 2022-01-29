import requests
import scraper
import email_notif
   

product_found():




def discord_push():
    url = "https://discord.com/api/webhooks/933903313655709796/C3TSR1osoETvWeBERKakBraRyh0XBXZjsnwdVNGGVhfyvfCU_6ZehDO_hxlHUU5lpHlO" 
    product_found = rpi8gb()
    data = {
    "content" : str(product_found),
    "username" : "BasedMeezus"
    }


    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))


if __name__ == '__main__':
scraper()
discord_push()