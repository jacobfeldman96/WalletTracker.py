import argparse
from classes import wallet_class, wallet_history

parser = argparse.ArgumentParser(prog="WalletTracker.py", description="Proof of Concept Wallet Analysis and Tracking Application for EVM compatible blockchains")

parser.add_argument("--address", required=True, help="Please insert the wallet address you'd like to interrogate. (Required)")
parser.add_argument("--alchemy", required=True, help="Please insert your Alchemy Node API Key. (Required)")
parser.add_argument("--history", help="Optional flag to review wallet's history")
# parser.add_argument("--assets", nargs='*', help="Required flag for asset history. Examples: external, internal, erc20, erc721, erc1155, or special nft")

args = parser.parse_args()

def main():
    if args.history == None:
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
        print(history)


if __name__ == '__main__':
    main()