import pandas as pd
d1 = {}
d2 = {}
cont = 0

def insertNewValue(cont):
    d1[cont] = nombre_var
    d2[cont] = tipo_ocurrido
    cont += 1
    return cont


nombre_var = 'adios'
tipo_ocurrido = 'int'
insertNewValue(cont)
tablaSimbolos = pd.DataFrame({'nombre':pd.Series(d1), 'tipo':pd.Series(d2)})
print(tablaSimbolos)
print(cont)

nombre_var = 'hola'
tipo_ocurrido = 'flt'
insertNewValue(cont)
tablaSimbolos = pd.DataFrame({'nombre':pd.Series(d1), 'tipo':pd.Series(d2)})
print(tablaSimbolos)
print(cont)

