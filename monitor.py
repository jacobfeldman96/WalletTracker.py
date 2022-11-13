import argparse
import pprint
from classes import wallet_class, wallet_history

parser = argparse.ArgumentParser(prog="WalletTracker.py", description="Proof of Concept Wallet Analysis and Tracking Application for EVM compatible blockchains")

parser.add_argument("--address", required=True, help="Please insert the wallet address you'd like to interrogate. (Required)")
parser.add_argument("--alchemy", required=True, help="Please insert your Alchemy Node API Key. (Required)")
parser.add_argument("--history", default=False, help="Optional flag to review wallet's history")
parser.add_argument("--assets", default=None, nargs='*', help="Required flag for asset history. Examples: external, internal, erc20, erc721, erc1155, or special nft")
parser.add_argument("--asset_name", help="Required flag for looking at single asset in wallet's history. Examples: USDT, WBTC, BNB, etc.")
args = parser.parse_args()

def main():
    if args.history == False:
        while True:
            active_monitor = wallet_class.Wallet_Movements(args.address, args.alchemy)
            watch_wallet = active_monitor.watch_wallet()
            if watch_wallet == "No movement in this block":
                print(watch_wallet)
                pass
            else:
                print(active_monitor.movement_list)
                pass

    else:
        history = wallet_history.Wallet_History(args.address, args.alchemy)
                
        if args.assets != None:
            if args.asset_name:
                specific_asset_history_from_wallet = history.filter_to_asset(args.assets,args.asset_name, 'fromAddress')
                specific_asset_history_to_wallet = history.filter_to_asset(args.assets, args.asset_name, 'toAddress')
                print(f"All {args.asset_name} transactions leaving this wallet are....")
                pprint.pprint(specific_asset_history_from_wallet)
                print(f"All {args.asset_name} transcations entering this wallet are....")
                pprint.pprint(specific_asset_history_to_wallet)
            else:
                from_transaction_history = history.fetch_wallet_history(args.assets, 'fromAddress')
                to_transaction_history = history.fetch_wallet_history(args.assets, 'toAddress')
                print('All Transactions leaving this wallet are the following....')
                pprint.pprint(from_transaction_history)
                print('All Transactions entering this wallet are the following....')
                pprint.pprint(to_transaction_history)
            
if __name__ == '__main__':
    main()