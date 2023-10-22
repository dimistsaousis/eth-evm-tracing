import os

ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
ALCHEMY_HTTP_URL = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"
ALCHEMY_WS_URL = f"wss://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"
