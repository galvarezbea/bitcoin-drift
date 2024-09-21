# -*- coding: utf-8 -*-
"""
Análisis de Bitcoin en tiempo real: deriva de lo inmutable

Descarga de transacciones
"""

from bitcoinrpc.authproxy import AuthServiceProxy
import csv, datetime

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_user = "tfmbitcoin"
rpc_pass = "bitcoin.TFM58"
rpc_host = "127.0.0.1"
rpc_client = AuthServiceProxy(f"http://{rpc_user}:{rpc_pass}@{rpc_host}:8332", timeout=120)

start = 0
end = rpc_client.getblockcount() + 1

with open("btc_transactions.csv", "w", newline="") as csvfile:
    fieldnames = ["Block", "Transactions", "Block size", "Datetime"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range (start, end):
        blockhash = rpc_client.getblockhash(i)
        block = rpc_client.getblock(blockhash)
        block_time = datetime.datetime.fromtimestamp(block["time"])
        writer.writerow({"Block": i, "Transactions": block["nTx"], "Block size": block["size"], "Datetime": block_time})
