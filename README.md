# Análisis de Bitcoin en tiempo real: deriva de lo inmutable

Descripción de la colección de scripts y Jupyter Notebooks, que acompañan a la memoria y forman parte del sumario de productos obtenidos en el presente TFM.

**Scripts**

* **btc_connect.py**: Conexión al nodo local de Bitcoin.

* **btc_mempool_dump.py**: Análisis de la mempool. Presenta por pantalla y escribe a un fichero CSV, a intervalos regulares, estadísticas del tamaño de transacciones alojadas en la mempool: media, varianza, mínimo, máximo. 

* **btc_transaction_dump.py**: Acceso al histórico de transacciones de la cadena de bloques.
Obtiene el número de bloque, el total de transacciones del bloque, su tamaño en bytes y la marca temporal de minado (con fecha, hora, minuto y segundo).
Permite seleccionar el intervalo de bloques a consultar y habilita la descarga a fichero CSV.

**Jupyter Notebooks**

* **btc_block_size_ADWIN**: Detección de derivas de concepto en el tamaño de bloque de la cadena de bloques, a partir del método matemático ADWIN, con salida gráfica.

* **btc_mempool_count_ADWIN.ipynb**: Detección de derivas de concepto en el total de transacciones de la mempool por intervalo de tiempo, a partir del método matemático ADWIN, con salida gráfica.

* **btc_mempool_mean_ADWIN.ipynb**: Detección de derivas de concepto en la media de transacciones de la mempool por intervalo de tiempo, a partir del método matemático ADWIN, con salida gráfica.

* **btc_transaction_ADWIN.ipynb**: Detección de derivas de concepto en el número de transacciones de la cadena de bloques, a partir del método matemático ADWIN, con salida gráfica.

* **btc_transaction_DummyDriftDetector**: Detección de derivas de concepto en el número de transacciones de la cadena de bloques, a partir del método DummyDriftDetector, con salida gráfica.

* **btc_transaction_KSWIN**: Detección de derivas de concepto en el número de transacciones de la cadena de bloques, a partir del método Kolmogorov-Smirnov Windowing (KSWIN), con salida gráfica.

* **btc_transaction_Page-Hinkley**: Detección de derivas de concepto en el número de transacciones de la cadena de bloques, a partir del método Page-Hinkley, con salida gráfica.
