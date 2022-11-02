# WalletTracker.py
Keep an eye on those sus wallets...

### What it does?
WalletTracker.py establishes a websocket with Alchemy's Ethereum Node as a Service and monitors each incoming block. If your wallet has a transaction, it'll print to the console. 

---------------------------------------------------

### How to get started 

1. `git clone https://github.com/jacobfeldman96/WalletTracker.py.git; cd WalletTracker.py; pip install -r requirements.txt`

2. Head over to alchemy's sign up page https://auth.alchemy.com/signup?redirectUrl=https%3A%2F%2Fdashboard.alchemyapi.io

3. Copy your key 

---------------------------------------------------

### Example command 

`python3 ./monitor.py --address <Ethereum address> --alchemy <Alchemy API Key>`

---------------------------------------------------

### TODO

1. Add in wallet history for given wallet
