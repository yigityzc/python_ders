# requests ve json kütüphanelerini içe aktar
import requests
import json

# CoinMarketCap API'ye bağlan
api_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical"
api_key = "330de88c-ab51-4056-8599-d1a74e7349e3"

params = {
  "id": "1",
  "time_start": "2022-01-01",
 # "time_end": "2022-01-31"
}

headers = {
  "Accepts": "application/json",
  "X-CMC_PRO_API_KEY": api_key,
}

veri = requests.get(api_url, params=params, headers=headers)

# Veriyi yazdır
print(json.dumps(veri.json(), indent=4))