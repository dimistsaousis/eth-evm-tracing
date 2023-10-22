import os
from dotenv import load_dotenv

load_dotenv()

ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
