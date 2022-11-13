import requests
import json

class Wallet_History:
    def __init__(self, address, alchemy_key):
        self.address = address
        self.alchemy_key = alchemy_key
        self.eth_endpoint = f"https://eth-mainnet.g.alchemy.com/v2/{self.alchemy_key}"
    
    def fetch_wallet_history(self, category: list, from_or_to: str) -> str:
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
                        from_or_to: self.address,
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
        transfers = res_dict['result']['transfers']
        useful_data = []
        for i in transfers:
            dict = {}
            dict['asset'] = i['asset']
            dict['contract_address'] = i['rawContract']['address']
            dict['category'] = i['category']
            dict['hash'] = i['hash']
            dict['from'] = i['from']
            dict['to'] = i['to']
            dict['value'] = i['value']
            useful_data.append(dict)
        return useful_data

    def results_to_json(self, asset_type: list, from_or_to: str) -> str:
        txn_history = self.fetch_wallet_history(asset_type, from_or_to)
        to_json = json.dumps(txn_history)
        return to_json

    def filter_to_asset(self, assets_type: list, asset: str, from_or_to: str) -> str:
        txn_history = self.fetch_wallet_history(assets_type, from_or_to)
        filtered_asset = []
        for i in txn_history:
            if i['asset'] == asset:
                filtered_asset.append(i)
        return filtered_asset