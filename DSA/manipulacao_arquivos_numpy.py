import numpy as np
import os
arquivo = os.path.join('/home/juliana/Documentos/testecsv.csv')
# o delimiter necessita do separador do texto, nesse caso vírgula. o usecols determina quantas colunas haverão e o
# skiprows pula determinado n de linhas do csv.
array = np.loadtxt(arquivo, delimiter=',', usecols=(0, 1, 2, 3), skiprows=1)
print(array)

