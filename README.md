# Script de Procesamiento de Datos CSV

## Descripción

Este script de Python toma un archivo de entrada en formato CSV, procesa y transforma los datos, y genera un archivo de texto de salida con los datos procesados. Durante el procesamiento, los registros con errores se separan y se escriben en un archivo de errores para su posterior revisión.

## Funcionamiento

El script realiza las siguientes operaciones:

1. Lee los datos de un archivo CSV de entrada. Este archivo se proporciona al script en el momento de su ejecución. El script es capaz de manejar archivos CSV que están delimitados tanto por comas como por punto y coma.

2. Procesa el campo NSS o RUT de cada registro, transformándolo en un formato numérico. Si este campo está vacío, se reemplaza por el texto "SINRUT" seguido del nombre que aparece en la columna correspondiente.

3. Transforma el campo de la hora desde el formato original "DD/MM/YYYY HH:MM" al nuevo formato "YYYYMMDD HHMM".

4. Procesa los campos de "Estado" y "NuevoEstado" para mapear los valores "Checarse/Entrada" y "Checarse/Salida" a "1" y "0" respectivamente. Si el campo no coincide con estos valores, se marca con "X", que luego se reemplaza por "VALOR_NO_RECONOCIDO" en el archivo de errores.

5. Escribe los datos procesados en un nuevo archivo de texto. El nombre de este archivo se genera automáticamente a partir del nombre del archivo de entrada, con un sello de tiempo y la extensión ".txt" agregados.

6. Durante el procesamiento, los registros con errores (aquellos con "SINRUT" en el NSS/RUT o "VALOR_NO_RECONOCIDO" en el campo de estado) se separan y se escriben en un archivo de errores.

## Cómo convertir un archivo Excel a CSV

Si tus datos están en un archivo de Excel y necesitas convertirlos a formato CSV, puedes seguir estos pasos en Microsoft Excel:

1. Abre tu archivo en Microsoft Excel.
2. Haz clic en "Archivo" en la barra de menú.
3. Haz clic en "Guardar como" y selecciona la ubicación donde deseas guardar el archivo.
4. En el menú desplegable "Guardar como tipo", selecciona "CSV (delimitado por comas) (*.csv)".
5. Haz clic en "Guardar".

Ahora tendrás una copia de tu archivo Excel en formato CSV que puedes usar con este script.

## Ejemplo de ejecución

Para ejecutar el script, utiliza el siguiente comando en la terminal:

```bash
python script.py "ruta/al/archivo.csv"
```

Donde "ruta/al/archivo.csv" es la ruta al archivo CSV que deseas procesar.

Por ejemplo, si tu archivo se llama "datos.csv" y está en la misma carpeta que el script, el comando sería:

```bash
python script.py "datos.csv"
```

Los archivos de salida se generarán en la carpeta "SALIDA" y tendrán el mismo nombre que el archivo de entrada, con un sello de tiempo agregado al inicio y la extensión ".txt". Los registros con errores se escribirán en un archivo separado que termina en "_ERRORES".
