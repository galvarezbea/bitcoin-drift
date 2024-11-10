# Análisis de Bitcoin en tiempo real: deriva de lo inmutable

Descripción de la colección de scripts, que acompañan a la memoria y forman parte del sumario de productos obtenidos en el presente TFM.

* **btc_connect.py**: Conexión al nodo local de Bitcoin.

* **btc_mempool.py**: Análisis de la mempool.<br>
Presenta por pantalla y escribe a un fichero CSV, a intervalos regulares, estadísticas del tamaño de transacciones alojadas en la mempool: media, varianza, mínimo, máximo. 

* **btc_transactions.py**: Acceso al histórico de transacciones de la cadena de bloques. 
Permite seleccionar el intervalo de bloques a consultar y habilita la descarga a fichero CSV.


