import json
import requests
from api_keys import ETHERSCAN_API_KEY


def get_abi_from_etherscan(contract_address):
    url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        raise requests.HTTPError(response=response)

    result = response.json()

    if result["status"] != "1":
        raise requests.HTTPError(response=response)

    abi = json.loads(result["result"])
    return abi
