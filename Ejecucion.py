from re import template
import numpy as np 

#Leer la informacion de cuadruplos
cuadruplos = np.loadtxt("Cuadruplos.txt", dtype = "str")
print("Cuadruplos")
print(cuadruplos)
print(" ")
TablaSimbolos = np.loadtxt("TablaDeSimbolos.txt", dtype = "str")
print("TablaSimbolos")
print(TablaSimbolos)
print(" ")

tempAvail = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6','T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20']

Temporales = [x for x in range(21)]
ValorTemp = np.zeros(21, dtype= "int")
Temp = np.column_stack((Temporales, ValorTemp))
print("TEMPORALES")
print(Temp)
print(" ")

###FUNCIONES
def getValue(var):
    k = 0
    #Variable a agarrar 
    for k in range(len(TablaSimbolos)):
        if TablaSimbolos[k][0] == var:
            print("LO ENCONTRE")
            print(TablaSimbolos)
            print(Temp)
            return TablaSimbolos[k][2]
        #print(k)
        k = k + 1

def setValue(var):
    #Valor a actualizar
    for i in range(len(Temp)):
        temp = "T" + str(i)
        if Temp[i][0] == temp:
            print("AQUI ESTA EL ERROR")
            if Temp[i][1]== None:
                return 0
            else:
                return Temp[i][1]
        else:
            i = i + 1

def getIndex(var):
    i = 0
    print(var)
    #Variable a agarrar 
    for i in range(len(TablaSimbolos)):
        if TablaSimbolos[i][0] == var:
            return i
        else:
            i = i + 1
            print(TablaSimbolos[i][0])


#####################################
####         EJECUCION          ##### 
#####################################
PC = 0

while(PC != -1):
    print("PC = " + str(PC))
    cuadruplo = cuadruplos[PC]
    oc = cuadruplo[0]
    print("Cuadruplo = " + str(cuadruplo))
    print("OC = " + str(oc))

    if oc == "+":
        #TEMPORAL 
        for i in range(len(tempAvail)):
            if tempAvail[i] == cuadruplo[3]:
                Temp[i+1][1] = int(getValue(cuadruplo[1])) + int(getValue(cuadruplo[2]))
                
        PC = PC + 1

    elif oc == "-":
        #TEMPORAL 
        for i in range(len(tempAvail)):
            if tempAvail[i] == cuadruplo[3]:
                Temp[i+1][1] = int(getValue(cuadruplo[1])) - int(getValue(cuadruplo[2]))
        
        PC = PC + 1

    elif oc == "/":
        #TEMPORAL 
        for i in range(len(tempAvail)):
            if tempAvail[i] == cuadruplo[3]:
                Temp[i+1][1] = int(getValue(cuadruplo[1])) / int(getValue(cuadruplo[2]))

        PC = PC + 1

    elif oc == "*":
        #TEMPORAL 
        for i in range(len(tempAvail)):
            if tempAvail[i] == cuadruplo[3]:
                Temp[i+1][1] = int(getValue(cuadruplo[1])) * int(getValue(cuadruplo[2]))
        PC = PC + 1

    elif oc == "=>":
        #TEMPORAL 
        for i in range(len(tempAvail)):
            if tempAvail[i] == cuadruplo[1]:
                print("ASIGNACION")
                if getValue(cuadruplo[1]) == None:
                    Temp[i+1][1] = 0
                else:
                    Temp[i+1][1] = getValue(cuadruplo[1])
                print("SETVALUE:")
                print(setValue(cuadruplo[1]))
                TablaSimbolos[getIndex(cuadruplo[2])][2] = setValue(cuadruplo[1])
                print(TablaSimbolos)
                print(setValue(cuadruplo[1]))

        PC = PC + 1

    elif oc == ">":
        #TEMPORAL 
        for i in range(len(tempAvail)):
            if tempAvail[i] == cuadruplo[3]:
                Temp[i+1][1] = int(getValue(cuadruplo[1])) > int(getValue(cuadruplo[2]))
    
        PC = PC + 1
    
    elif oc == "<":
        PC = PC + 1
        #TEMPORAL 
        for i in range(len(tempAvail)):
            if tempAvail[i] == cuadruplo[3]:
                Temp[i+1][1] = int(getValue(cuadruplo[1])) < int(getValue(cuadruplo[2]))

    elif oc == "==":
        PC = PC + 1
    
    elif oc == "Print":
        PC = PC + 1

    elif oc == "Read":
        PC = PC + 1

    elif oc == "goto":
        PC = int(cuadruplo[1])

    elif oc == "gotoF":
        PC = int(cuadruplo[2])

    elif oc == "FinPrograma":
        PC = -1
        print("END")
        print(Temp)
        print(TablaSimbolos)
        
    else:
        print("ELSE")
        PC = PC + 1##