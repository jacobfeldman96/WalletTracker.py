import requests
import json

class Wallet_History:
    def __init__(self, address, alchemy_key):
        self.address = address
        self.alchemy_key = alchemy_key
        self.eth_endpoint = f"https://eth-mainnet.g.alchemy.com/v2/{alchemy_key}"
    
    def fetch_wallet_history(self, category: list):
        payload = {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "alchemy_getAssetTransfers",
                "params": [
                    {
                        "fromBlock": "0x0",
                        "toBlock": "latest",
                        "category": category,
                        "withMetadata": False,
                        "excludeZeroValue": True,
                        "maxCount": "0x3e8",
                        "fromAddress": self.address,
                        "order": "desc"
                    }
                ]
            }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(self.eth_endpoint,json=payload,headers=headers)
        res_dict = json.loads(response.text)
        return res_dict['result']['transfers']
