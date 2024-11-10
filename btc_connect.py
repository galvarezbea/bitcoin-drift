# -*- coding: utf-8 -*-
"""
----------------------------------------------------------
Análisis de Bitcoin en tiempo real: deriva de lo inmutable
----------------------------------------------------------

Conexión al nodo local de Bitcoin.
"""

from bitcoinrpc.authproxy import AuthServiceProxy

def btc_connect():
    # rpc_user y rpc_pass están configurados en el fichero bitcoin.conf
    rpc_user = "[usuario]" # MODIFICAR
    rpc_pass = "[clave]" # MODIFICAR
    rpc_host = "127.0.0.1"
    rpc_port = "8332"
    
    rpc_url = f"http://{rpc_user}:{rpc_pass}@{rpc_host}:{rpc_port}"
    rpc_connection = AuthServiceProxy(rpc_url)
    return rpc_connection
    
