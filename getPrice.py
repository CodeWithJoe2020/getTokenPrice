from web3 import Web3 
from abis import TOKENLPABI, ABI
import decimal
from getEthPrice import ethPrice


node = config.node
web3 = Web3(Web3.HTTPProvider(node))



lp_address = web3.to_checksum_address(config.lpAddress)
lpContract = web3.eth.contract(address=lp_address, abi=TOKENLPABI)
tokenAddress = web3.to_checksum_address(config.tokenAddress)
waterfallContract = web3.eth.contract(address=tokenAddress, abi=ABI)

def token_price():
    reserves = lpContract.functions.getReserves().call()
    price = reserves[0] / reserves[1]
    priced = decimal.Decimal(price).quantize(decimal.Decimal('0.00000001'))
    return priced

def token_price_usd():
    tokenPriceEth = token_price()
    tokenPriceUsd = float(tokenPriceEth) * float(ethPrice())
    return tokenPriceUsd
