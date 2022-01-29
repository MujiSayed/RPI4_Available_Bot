import requests
import scraper
import email_notif
import config as conf

product_found():




def discord_push():
    url = discord_webhook.conf 
    #product_found = rpi8gb()
    data = {
    "content" : str(product_found),
    "username" : discord_user.conf
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