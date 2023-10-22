from pathlib import Path
from web3 import Web3
from dataclasses import dataclass


class DexVariant:
    UniswapV2 = "UniswapV2"
    UniswapV3 = "UniswapV3"


class Dex:
    address: str
    DexVariant: DexVariant
    deployment_block_number: int
    some_value: int


async def mempool_watching(target_address, wss_url):
    w3 = Web3(Web3.WebsocketProvider(wss_url))
    checkpoint_path = ".cfmms-checkpoint.json"
    pools = {}

    dexes_data = [
        ("0x1F98431c8aD98523631AE4a59f267346ea31F984", DexVariant.UniswapV3, 12369621),
    ]
    dexes = [
        Dex(address, variant, number, 300) for address, variant, number in dexes_data
    ]

    if Path(checkpoint_path).exists():
        _, pools_vec = await sync_pools_from_checkpoint(checkpoint_path, 100000, w3)
    else:
        pools_vec = await sync_pairs(dexes, w3, checkpoint_path)

    for pool in pools_vec:
        pools[pool.address] = pool

    print(f"Pools synced: {len(pools)}")
