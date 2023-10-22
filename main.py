import json
import time
import asyncio


def alchemy_http_url(api_key):
    return f"https://eth-mainnet.g.alchemy.com/v2/{api_key}"


def alchemy_ws_url(api_key):
    return f"wss://eth-mainnet.g.alchemy.com/v2/{api_key}"


async def geth_style_tracing(tx_hash: str):
    async with aiohttp.ClientSession() as session:
        req = {
            "id": 1,
            "method": "debug_traceTransaction",
            "jsonrpc": "2.0",
            "params": [tx_hash, {"tracer": "prestateTracer"}],
        }
        request = await session.post(http_url, data=json.dumps(req))
        res = await request.json()

        result = res.get("result")

        if result:
            addresses_touched = list(result.keys())
            print("Geth style: ", addresses_touched)
            print(res)


async def parity_style_tracing(tx_hash: str):
    async with aiohttp.ClientSession() as session:
        req = {
            "id": 1,
            "method": "trace_replayTransaction",
            "jsonrpc": "2.0",
            "params": [tx_hash, ["stateDiff"]],
        }
        request = await session.post(http_url, data=json.dumps(req))
        res = await request.json()

        result = res.get("result")

        if result:
            state_diff = result["stateDiff"]
            addresses_touched = list(state_diff.keys())
            print("Parity style: ", addresses_touched)
            print(res)


async def main():
    while True:
        try:
            async with websockets.connect(ws_url) as ws:
                subscription = {
                    "json": "2.0",
                    "id": 1,
                    "method": "eth_subscribe",
                    "params": ["newPendingTransactions"],
                }

                await ws.send(json.dumps(subscription))
                _ = await ws.recv()

                while True:
                    msg = await asyncio.wait_for(ws.recv(), timeout=60 * 10)
                    response = json.loads(msg)
                    tx_hash = response["params"]["result"]

                    await geth_style_tracing(tx_hash)
                    await parity_style_tracing(tx_hash)

                    print("\n")
        except:
            time.sleep(2)
            print("reconnecting...")


if __name__ == "__main__":
    asyncio.run(main())
