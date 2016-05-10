import requests, json

def prRed(prt): return "\033[91m {}\033[00m" .format(prt)
def prGreen(prt): return "\033[92m {}\033[00m" .format(prt)

response = requests.get("https://www.betfair.com/www/sports/exchange/readonly/v1/bymarket?currencyCode=USD&locale=en_GB&marketIds=1.107373419&rollupLimit=25&rollupModel=STAKE&types=MARKET_STATE,RUNNER_STATE,RUNNER_EXCHANGE_PRICES_BEST,RUNNER_DESCRIPTION")
data = json.loads(response.text)
market_data = data["eventTypes"][0]["eventNodes"][0]["marketNodes"][0]["runners"]
for runner in market_data[:3]:
  name = runner["description"]["runnerName"]
  price = runner["exchange"]["availableToBack"][0]["price"]
  print "{0}: ${1} - implied chance = {2}".format(prRed(name), price, prGreen(str(int(100/price)) + "%"))