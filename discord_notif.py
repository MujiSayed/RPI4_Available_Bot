import requests
import config as conf


def discord_push(product_url, rpi_name):
    if conf.discord_webhook != "":

        url = conf.discord_webhook 
        data = {
        "content" : f"RPI{rpi_name} found at {product_url}", 
        "username" : conf.discord_user
        }


        result = requests.post(url, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Message delievered to Discord Successfully, code {}.".format(result.status_code))

    else:
        print("Discord variables not configured, not pushing")
