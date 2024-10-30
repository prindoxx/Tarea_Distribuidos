#-------------------------------------------------------
# Load Data from File: KDDTrain.txt
#--------------------------------------------------------

import numpy as np
#import utility_etl as ut

# Load parameters from config.csv
def config():
    ...

# Beginning ...
def main():
    config()
    
    # Definir la variable M
    M = 10

    # Leer el archivo de texto
    input_file = 'KDDTrain.txt'
    output_file = 'Data.csv'

    # Leer el archivo utilizando numpy
    data = np.genfromtxt(input_file, delimiter=',', dtype=str)

    # Eliminar la última columna
    data = data[:, :-1]

    # Modificar la penúltima columna según las condiciones dadas
    for i in range(len(data)):
        if data[i, -1] == 'normal':
            data[i, -1] = '1'
        elif data[i, -1] in ['neptune', 'teardrop', 'smurf', 'pod', 'back', 'land', 'apache2', 'processtable', 'mailbomb', 'udpstorm']:
            data[i, -1] = '2'
        elif data[i, -1] in ['ipsweep', 'portsweep', 'nmap', 'satan', 'saint', 'mscan']:
            data[i, -1] = '3'

    # Guardar los datos en un archivo CSV
    np.savetxt(output_file, data, delimiter=',', fmt='%s')

    print(f"Archivo CSV '{output_file}' creado con éxito.")

    # Leer el archivo Data.csv y dividir según la clase
    class1_data = data[data[:, -1] == '1']
    class2_data = data[data[:, -1] == '2']
    class3_data = data[data[:, -1] == '3']

    # Guardar cada clase en su respectivo archivo CSV
    np.savetxt('class1.csv', class1_data, delimiter=',', fmt='%s')
    np.savetxt('class2.csv', class2_data, delimiter=',', fmt='%s')
    np.savetxt('class3.csv', class3_data, delimiter=',', fmt='%s')

    print("Archivos 'class1.csv', 'class2.csv' y 'class3.csv' creados con éxito.")

    # Leer los índices de los archivos idx_class1.csv, idx_class2.csv, idx_class3.csv
    idx_class1 = np.genfromtxt('idx_class1.csv', delimiter=',', dtype=int)[:M]
    idx_class2 = np.genfromtxt('idx_class2.csv', delimiter=',', dtype=int)[:M]
    idx_class3 = np.genfromtxt('idx_class3.csv', delimiter=',', dtype=int)[:M]

    # Leer los datos del archivo Data.csv
    data = np.genfromtxt(output_file, delimiter=',', dtype=str)

    # Obtener las filas correspondientes a los índices
    selected_rows = np.vstack((data[idx_class1], data[idx_class2], data[idx_class3]))

    # Guardar las 30 filas en un archivo CSV llamado DataClass.csv
    np.savetxt('DataClass.csv', selected_rows, delimiter=',', fmt='%s')

    print("Archivo 'DataClass.csv' creado con éxito.")


   
if __name__ == '__main__':
    main()
