from web3 import Web3
import random


def calculate_next_block_base_fee(
    gas_used: int, gas_limit: int, base_fee_per_gas: int
) -> int:
    gas_used = Web3.toWei(gas_used, "gwei")
    gas_limit = Web3.toWei(gas_limit, "gwei")
    base_fee_per_gas = Web3.toWei(base_fee_per_gas, "gwei")

    target_gas_used = gas_limit // 2
    target_gas_used = (
        Web3.toWei(1, "gwei")
        if target_gas_used == Web3.toWei(0, "gwei")
        else target_gas_used
    )

    if gas_used > target_gas_used:
        new_base_fee = base_fee_per_gas + (
            (base_fee_per_gas * (gas_used - target_gas_used)) // target_gas_used
        ) // Web3.toWei(8, "gwei")
    else:
        new_base_fee = base_fee_per_gas - (
            (base_fee_per_gas * (target_gas_used - gas_used)) // target_gas_used
        ) // Web3.toWei(8, "gwei")

    seed = random.randint(0, 8)
    new_base_fee = new_base_fee + Web3.toWei(seed, "gwei")

    return Web3.fromWei(new_base_fee, "gwei")
