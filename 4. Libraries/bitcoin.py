import requests
import sys
import json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
object = response.json()
bitcoin_price = object["bpi"]["USD"]["rate"].replace(",", "")

try:
    number = sys.argv[1]
    calculated_price = float(bitcoin_price) * float(number)
    print(f"${calculated_price:,.4f}")
except requests.RequestException:
    pass
except ValueError:
    sys.exit("Command-line argument is not a number")



