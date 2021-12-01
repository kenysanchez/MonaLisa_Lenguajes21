#Kenia Sanchez
#A01244940
#Monalisa

from ntpath import join
import re
from numpy.core.fromnumeric import shape
from numpy.core.records import array
from numpy.lib import npyio
from numpy.typing import _256Bit, _32Bit
import ply.lex as lex
import ply.yacc as yacc
import numpy as np
import sys

reserved = {'if' :'IF', 
            'Let': 'LET', 
            'begin' : 'BEGIN', 
            'end': 'END', 
            'function': 'FUNCTION', 
            'read': 'READ', 
            'print': 'PRINT',
            'else' : 'ELSE', 
            'loop' : 'LOOP', 
            'break': 'BREAK' , 
            'for' : 'FOR', 
            'while' : 'WHILE', 
            'int': 'INT', 
            'flt': 'FLT',
            'and' : 'AND',
            'or' : 'OR'
            }

tokens = ['ID', 'asignacion', 'num', 'coma', 'puntoycoma', 'abrellave', 'cierrallave', 'abreparentesis', 'cierraparentesis',
          'suma', 'resta', 'multiplicacion', 'dividir','menorigual','mayorigual','mayor', 'menor', 'igualque', 
          'diferenteque'] + list(reserved.values())

operands = []
tempAvail = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6','T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20']
cuadruplos = np.zeros(shape=(1,4))
saltos = []
variables = []
valores = []
valoresArray = []
tipo = []

i = 0
k = 0
M = 0

t_ignore = r' '

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    print(str(t.value))
    return t

def t_asignacion(t):
    r'\=>'
    t.type = 'asignacion'
    print("=>")
    return t

def t_num(t):
    r'\d+'
    t.value = int(t.value)
    print(t.value)
    return t

def t_coma(t):
    r'\,'
    t.type = 'coma'
    print(",")
    return t

def t_puntoycoma(t):
    r'\;'
    t.type = 'puntoycoma'
    print(";")
    return t

def t_abrellave(t):
    r'\{'
    t.type = 'abrellave'
    print("{")
    return t

def t_cierrallave(t):
    r'\}'
    t.type = 'cierrallave'
    print("}")
    return t

def t_abreparentesis(t):
    r'\('
    t.type = 'abreparentesis'
    print("(")
    return t

def t_cierraparentesis(t):
    r'\)'
    t.type = 'cierraparentesis'
    print(")")
    return t

def t_suma(t):
    r'\+'
    t.type = 'suma'
    print("+")
    return t 

def t_resta(t):
    r'\-'
    t.type = 'resta'
    print("-")
    return t 

def t_multiplicacion(t):
    r'\*'
    t.type = 'multiplicacion'
    print("*")
    return t 

def t_dividir(t):
    r'\/'
    t.type = 'dividir'
    print("/")
    return t 

def t_menorigual(t):
    r'\<='
    t.type = 'menorigual'
    print("<=")
    return t    

def t_mayorigual(t):
    r'\>='
    t.type = 'mayorigual'
    print(">=")
    return t   

def t_mayor(t):
    r'\>'
    t.type = 'mayor'
    print(">")
    return t    

def t_menor(t):
    r'\<'
    t.type = 'menor'
    print("<")
    return t    

def t_igualque(t):
    r'\=='
    t.type = 'igualque'
    print("==")
    return t    

def t_diferenteque(t):
    r'\!='
    t.type = 'diferenteque'
    print("!=")
    return t   

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'\#.*'
    pass    

def t_error(t):
    print("Caracter ilegal")
    t.lexer.skip(1)

lexer = lex.lex()

#####################################
####          Gramatica         ##### 
#####################################
tipo_encontrado = ''
nombre_var = ''

#Programa-> V F Main 
def p_Programa(p):
    '''
    Programa : VDummy F Main
    '''
    print("\t***Correcto***")

def p_VDummy(p):
    '''
    VDummy : V
    '''
    i = 0
    generarGTI()

###VARIABLES
def p_V(p):
    '''
    V : auxVarSimple
    V : auxVarArray
      |
    '''
#VARIABLES SIMPLES
#V-> V Let id => K ; 
def p_auxVarSimple(p):
    '''
    auxVarSimple : V LET auxVar asignacion K puntoycoma
    ''' 
    valores.append(str(p[5]))

#VARIABLES ARREGLOS
#V-> V Let id => (A);
def p_auxVarArray(p):
    '''
    auxVarArray : V LET auxVar asignacion abreparentesis A cierraparentesis puntoycoma
    ''' 

#TYPE ID
def p_auxVar(p):
    '''
    auxVar : type ID
    ''' 
    tipo.append(str(p[1]))
    variables.append(str(p[2]))
    global M
    M=1


#TYPE
def p_type(p):
    '''
    type : INT
    type : FLT
    '''    
    p[0] = p[1]
    
#A -> num 
#A -> A , num
def p_A(p):
    '''
    A : num
    A : Aaux
    '''
    p[0] = p[1]
    valoresArray.append(p[0])
    global M
    M = M*p[0]
    print("M>", M)


def p_Aaux(p):
    '''
    Aaux : A coma num
    '''
    global k 
    p[0] = p[3]
    k = k + 1 
    print("AQUIII")

#Main -> begin ; Z end ;
def p_Main(p):
    '''
    Main : mainAux Z endAux
      |
    '''
#######PROGRAM
def p_mainAux(p):
    '''
    mainAux : BEGIN puntoycoma
    '''
    rellenarGTI(0,i)
    print("rellenar")
    print(i)

def p_endAux(p):
    '''
    endAux : END puntoycoma
    '''
    generarFIN()

#Z -> S ;
#Z -> Z S ;
def p_Z(p):
    '''
    Z : S puntoycoma
    Z : Z S puntoycoma
    '''

#k -> id
#k -> num
def p_K(p):
    '''
    K : ID
    K : num
    '''   
    p[0] = p[1]
    
#F-> F function id { S } 
def p_F(p):
    '''
    F : F FUNCTION ID abrellave S cierrallave
      |
    '''
#S - > 
def p_S(p):
    '''
    S : ID abreparentesis cierraparentesis
    S : IF EL ifAux Z cierrallave ELSE ifAux2 Z ifAux3
    S : READ abreparentesis readAux cierraparentesis
    S : PRINT abreparentesis printAux cierraparentesis
    S : LET ID asignacion IF abreparentesis EL cierraparentesis abrellave Z cierrallave ELSE abrellave Z cierrallave
    S : whileAux EL whileAux2 Z whileAux3
    S : loopAux abrellave Z abreparentesis EL cierraparentesis B cierrallave 
    S : FOR abreparentesis LET forAux asignacion forAux2  puntoycoma forAux3 puntoycoma forAux4 cierraparentesis abrellave Z forAux5
    S : Asignacion
    S : BREAK
      |
    '''
#######IF     
def p_ifAux(p):
    '''
    ifAux : abrellave
    ''' 
    R = operands.pop()
    generarGTF(R)
    saltos.append(i-1)

def p_ifAux2(p):
    '''
    ifAux2 : abrellave
    ''' 
    f = saltos.pop()
    generarGTI()
    saltos.append(i-1)
    rellenarGTF(f, i)

def p_ifAux3(p):
    '''
    ifAux3 : cierrallave
    ''' 
    fin = saltos.pop()
    rellenarGTI(fin, i)

#######READ
#Read(k);
#Read(id[a])
def p_readAux(p):
    '''
    readAux : readAux2
    readAux : ID abrellave A cierrallave
    '''

def p_readAux2(p):
    '''
    readAux2 : ID
    ''' 
    p[0] = p[1]
    cuadruploRead(operands, p[0])

#######PRINT
def p_printAux(p):
    '''
    printAux : M
    ''' 
    p[0] = p[1]
    cuadruploPrint(operands, p[0])

#######WHILE
def p_whileAux(p):
    '''
    whileAux : WHILE
    ''' 
    saltos.append(i)
    print("SALTOS")
    print(saltos)

def p_whileAux2(p):
    '''
    whileAux2 : abrellave
    '''    
    R = operands.pop()
    generarGTF(R);
    saltos.append(i-1)
    print("SALTOS")
    print(saltos)

def p_whileAux3(p):
    '''
    whileAux3 : cierrallave
    '''    
    f = saltos.pop()
    retorno = saltos.pop()
    generarGTWhile(retorno)
    rellenarGTF(f,i)

#######FOR
def p_forAux(p):
    '''
    forAux : type ID
    '''    
    tablaSimb[str(p[2])] = str(p[1])
    #Anadimos id a oper
    operands.append(p[2])
    print("****************ADD OPERAND")

def p_forAux2(p):
    '''
    forAux2 : num
    '''    
    p[0] = p[1]
    #Anadimos K a oper
    operands.append(p[1])
    cuadruploAsign(operands, tempAvail);

def p_forAux3(p):
    '''
    forAux3 : EL
    '''    
    Tx = operands.pop()
    generarGTF(Tx)
    saltos.append(i-2)
    
def p_forAux4(p):
    '''
    forAux4 :  ID suma num 
    '''    
    operands.append(p[1])
    operands.append(p[3])
    cuadruploMas(operands, tempAvail)
    
def p_forAux5(p):
    '''
    forAux5 : cierrallave
    '''    
    retorno = saltos.pop()
    generarGTWhile(retorno)
    
    rellenarGTF(retorno+1, i)

#######LOOP
def p_loopAux(p):
    '''
    loopAux : LOOP
    '''    
    saltos.append(i)


#B-> { break } 
def p_B(p):
    '''
    B : abrellave BREAK cierrallave
      |
    '''

#M-> "K"
#M-> K 
def p_M(p):
    '''
    M : K 
    M : A
    '''
    p[0] = p[1]

#####ASSIGN
def p_Asignacion(p):
    '''
    Asignacion : ID D asignacion E
    ''' 
    p[0] = p[1]
    #Anadimos K a oper
    operands.append(p[1])
    
    cuadruploAsignS(operands, tempAvail)

#D -> (A) 
def p_D(p):
    '''
    D : abreparentesis A cierraparentesis
      |
    ''' 
#E-> E + X
#E-> E - X
#E-> T
def p_E(p):
    '''
    E : expSuma
    E : expResta
    E : T
    '''
    p[0] = p[1]

def p_expSuma(p):
    '''
    expSuma : E suma T
    '''
    cuadruploMas(operands, tempAvail)

def p_expResta(p):
    '''
    expResta : E resta T
    '''
    cuadruploMenos(operands, tempAvail)

#T-> T * X
#T-> T / X
#T-> X
def p_T(p):
    '''
    T : expMult
    T : expDiv
    T : X
    '''
def p_expMult(p):
    '''
    expMult : T multiplicacion X
    '''
    cuadruploMult(operands, tempAvail)

def p_expDiv(p):
    '''
    expDiv : T dividir X
    '''
    cuadruploDiv(operands, tempAvail)

#X-> id
#X-> id (H)
#X-> num 
#X-> (E)
def p_X(p):
    '''
    X : IDaux
    X : ID abreparentesis A cierraparentesis
    X : NUMaux
    X : abreparentesis E cierraparentesis
    '''

def p_IDaux(p):
    '''
    IDaux : ID
    '''
    if checkVarDefined(p[1]) == True:
        operands.append(p[1])
        print("****************ADD OPERAND")
        #print(operands)
    else:
        print("VARIABLE NO DECLARADA")

def p_NUMaux(p):
    '''
    NUMaux : num
    '''
    operands.append(p[1])
    print("****************ADD VALUE")
   
#EL-> TL
#EL-> EL or TL
def p_EL(p):
    '''
    EL : AL
    EL : orAux
    '''
    
def p_AL(p):
    '''
    AL : TL
    AL : andAux
    '''

def p_orAux(p):
    '''
    orAux : EL OR AL
    '''
    print("OR*******")
    cuadruploOr(operands, tempAvail)

def p_andAux(p):
    '''
    andAux : AL AND TL
    '''
    print("AND*******")
    cuadruploAnd(operands, tempAvail)

#C-> (EL)
#C-> J signos(W) J
def p_TL(p):
    '''
    TL : abreparentesis EL cierraparentesis
    TL : Comp
    '''

def p_Comp(p):
    '''
    Comp : J W J
    '''
    print("AQUI CHECAMOS LOS OPERNADOS")
    print(operands)
    print(p[3])
    cuadruploComp(operands, tempAvail, p[2])

#J-> id (num,...)
#J-> id
#J-> num
def p_J(p):
    '''
    J : ID abreparentesis A cierraparentesis
    J : IDoux
    '''
def p_IDoux(p):
    '''
    IDoux : ID
    IDoux : num
    '''
    print("OPERANDO:")
    print(p[1])
    operands.append(p[1])

#W-> >=, <=, >, <, ==, !=
def p_W(p):
    '''
    W : mayorigual
    W : menorigual
    W : menor
    W : mayor
    W : igualque
    W : diferenteque
    '''
    p[0] = p[1]
    
#Por si hay un error
def p_error(p):
    print("\t****ERROR****")

parser = yacc.yacc()

#####################################
####      Tabla de simbolos     ##### 
#####################################
tablaSimb = {}

#####################################
####      Codigo intermedio     ##### 
#####################################
def cuadruploMas(operands, tempAvail):
    global i
    global cuadruplos
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)
      
    row = np.array(['+', oper1, oper2, result])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1

def cuadruploMenos(operands, tempAvail):
    global i
    global cuadruplos
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)

    row = np.array(['-', oper1, oper2, result])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1

def cuadruploDiv(operands, tempAvail):
    global i
    global cuadruplos
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)

    row = np.array(['/', oper1, oper2, result])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1

def cuadruploMult(operands, tempAvail):
    global i
    global cuadruplos
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)

    row = np.array(['*', oper1, oper2, result])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1

#Cuadruplos logicos
def cuadruploAnd(operands, tempAvail):
    global i
    global cuadruplos
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)

    row = np.array(['AND', oper1, oper2, result])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1
    
def cuadruploOr(operands, tempAvail):
    global i
    global cuadruplos

    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)

    row = np.array(['OR', oper1, oper2, result])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1

#Cuadruplos Comparativos
def cuadruploComp(operands, tempAvail, comp):
    global i
    global cuadruplos
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)

    row = np.array([str(comp), oper1, oper2, result])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1

#Cuadruplos S
def cuadruploAsign(operands, tempAvail):
    global i
    global cuadruplos
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)

    row = np.array(["=>", oper1, oper2, result])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1   

def cuadruploAsignS(operands, tempAvail):
    global i
    global cuadruplos
    oper1 = operands.pop()
    oper2 = operands.pop()

    row = np.array(["=>", oper2, oper1,  None])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1  



def cuadruploPrint(operands, valor):
    global i
    global cuadruplos
    row = np.array(["Print", str(valor), None, None])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1   

def cuadruploRead(operands, valor):
    global i
    global cuadruplos
    row = np.array(["Read", str(valor), None, None])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i=i+1  

def checkVarDefined(var):
    if var in variables:
        return True    
    else:
        return False

#####################################
####          Ciclos            ##### 
#####################################
#GOTOFALSO
def generarGTF(R):
    global cuadruplos , i
    row = np.array(["gotoF", R, None,None])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i = i + 1

#GOTOVERDADERO
def generarGTI():
    global cuadruplos , i
    row = np.array(["goto", None, None, None])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i = i + 1

#GOTOINCONDICIONAL
def generarGTWhile(retorno):
    global cuadruplos,i 
    row = np.array(["goto", retorno, None, None])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i = i + 1

#FINPROGRAMA
def generarFIN():
    global cuadruplos,i 
    row = np.array(["FinPrograma", None, None, None])  
    cuadruplos = np.concatenate((cuadruplos, [row]), axis = 0)
    i = i + 1

#GotoFalso
def rellenarGTF(f, i):
    print(f)
    cuadruplos[f+1][2] = i;
    print("cuadruplos " + str(f) + " cont: " + str(i))

#GotoCondicional
def rellenarGTI(fin, i):
    print(fin)
    cuadruplos[fin+1][1] = i;    


#####################################
####   Variables dimensionadas  ##### 
#####################################
##Estructura de datos LINKED LIST 
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
   def __init__(self):
      self.headval = None

###Anadir
   def AtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.headval is None:
         self.headval = NewNode
         return
      laste = self.headval
      while(laste.nextval):
         laste = laste.nextval
      laste.nextval=NewNode

###Imprimir
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

###Formulas 
def calcularM(index):
    arrayM =[]
    aux = 1
    k = 0
    
    while(k < len(index)-1):
        for i in range(len(index)):
            aux = aux*index[i]
            i = i + 1

            print(aux)
            arrayM.append(aux)
            i = k
            k = k + 1

    print("ARRAY DE MS")
    print(arrayM)
#corregir 

def calcularBase(index):
    print("Base")

def calcularD(index):
    print("D")

def createLL(name):
    name = LinkedList()

#####################################
####          Pruebas           ##### 
#####################################
f = open('test2.txt', 'r')
s = f.readlines()

# Function to convert  
def listToString(s): 
    
    str1 = "" 
    
    for ele in s: 
        str1 += ele  
    
    return str1 

##Correr el programa 
while True:
    try:
        s = listToString(s)
        
    except EOFError:
        break

    parser.parse(s)
    break

f.close()


#Imprimir tabla de simbolos
print("\n#######  TABLA DE SIMBOLOS  ######")
tablaDeSimb = np.column_stack((variables, tipo, valores))
print(tablaDeSimb)
#Importar cuadruplos a otro archivo para ejecuccion
np.savetxt("TablaDeSimbolos.txt", tablaDeSimb, fmt="%s")

#Imprimir Valores de array
print("\nARRAY")
print(valoresArray)
calcularM(valoresArray)

#Imprimir Pila de operandos
print("\nOPERANDS")
print(operands)

#Imprimir Cuadruplos
print("\nCUADRUPLOS")
cuadruplos = np.delete(cuadruplos, (0), axis=0)
print(cuadruplos)
#Importar cuadruplos a otro archivo para ejecuccion
np.savetxt("Cuadruplos.txt", cuadruplos, fmt="%s")

#Imprimir Saltos
print("\nSALTOS")
print(saltos)

#Imprimir CONTADOR
print("\nCONTADOR")
print(i)