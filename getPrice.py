#https://eth-mainnet.g.alchemy.com/v2/-Oo6Y1F3-1XO8vvIg6inpWboi0itglZF

from web3 import Web3 
from abi import ERC20ABI, LPABI
import decimal
#from getEthPrice import getEthPrice

node = 'get 100$ free credit using this link here https://bit.ly/3x67pnF alchemy node'
web3 = Web3(Web3.HTTPProvider(node))

#print(web3.is_connected())


lpAddress=web3.to_checksum_address('0xA43fe16908251ee70EF74718545e4FE6C5cCEc9f')
lpContract = web3.eth.contract(address=lpAddress, abi=LPABI)



def token_price():
    # Get the addresses of the two tokens in the pair
    token0, token1 = lpContract.functions.token0().call(), lpContract.functions.token1().call()
    print("Token0:", token0)
    print("Token1:", token1)

    # Get the decimals of the two tokens
    token0c = web3.eth.contract(address=token0, abi=ERC20ABI)
    token1c = web3.eth.contract(address=token1, abi=ERC20ABI)
    decimals0 = token0c.functions.decimals().call()
    decimals1 = token1c.functions.decimals().call()

    # Get the current reserves of the two tokens
    reserves = lpContract.functions.getReserves().call()
    reserve0 = float(reserves[0]) / 10 ** decimals0
    reserve1 = float(reserves[1]) / 10 ** decimals1
    print("Reserve0:", reserve0)
    print("Reserve1:", reserve1)

    # Calculate the token price
    price = reserve1 / reserve0

    # Format the token price as a string with 8 decimal places
    price_formatted = "{:.15f} {} per {}".format(price, token1c.functions.symbol().call(), token0c.functions.symbol().call())
    
    return price_formatted
    
def usd_price():
    usdPrice= float(token_price()) * float(getEthPrice())
    return usdPrice

print(token_price())
print(usd_price())
