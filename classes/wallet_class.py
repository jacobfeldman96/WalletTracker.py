from web3 import Web3
from hexbytes import HexBytes
import json

class Wallet_Movements:
    def __init__(self, address, alchemy_key):
        self.address = address
        self.alchemy_key = alchemy_key
        self.movement_list = []
        
    def auth(self):
        alchemy_ws = f"wss://eth-mainnet.g.alchemy.com/v2/{self.alchemy_key}"
        w3 = Web3(Web3.WebsocketProvider(alchemy_ws))
        return w3

    def fetch_latest_block_transactions(self):
        w3 = self.auth()
        latest_block = w3.eth.get_block('latest')
        latest_transactions = latest_block['transactions']
        return latest_transactions

    def watch_wallet(self):
        current_length = len(self.movement_list)
        transactions = self.fetch_latest_block_transactions()
        w3 = self.auth()
        for i in transactions:
            txns_in_block = w3.eth.get_transaction(i)
            if txns_in_block['from'] == self.address:
                txns_dict = {}
                txns_dict['txn hash'] = HexBytes.hex(i)
                txns_dict['event'] = 'out'
                txns_dict['from'] = txns_in_block['from']
                txns_dict['to'] = txns_in_block['to']
                txns_dict['amount'] = txns_in_block['value']
                self.movement_list.append(json.dumps(txns_dict))
            elif 'to' in txns_in_block:
                if txns_in_block['to'] == self.address: 
                    txns_dict = {}
                    txns_dict['txn hash'] = HexBytes.hex(i)
                    txns_dict['event'] = 'in'
                    txns_dict['from'] = txns_in_block['from']
                    txns_dict['to'] = txns_in_block['to']
                    txns_dict['amount'] = txns_in_block['value']
                    self.movement_list.append(json.dumps(txns_dict))
                else:
                    pass
            else:
                pass

        if len(self.movement_list) == 0:
            return "No movement in this block"

        elif len(self.movement_list) > current_length:
            latest_transactions = []
            for i in range(len(self.movement_list)):
                if i > current_length:
                    latest_transactions.append(i)
                else:
                    pass
            return latest_transactions

        else:
            return "No movement in this block"
        