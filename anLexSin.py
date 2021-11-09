#Kenia Sanchez
#A01244940
#Monalisa

from ntpath import join
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
          'diferenteque', 'comillasdobles'] + list(reserved.values())

operands = []
operands2 = []
tempAvail = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6','T7', 'T8', 'T9', 'T10', 'T11']
tempAvail2 = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6','T7', 'T8', 'T9', 'T10', 'T11']
cuadruplos = []
cuadruplos2 = []
i = 0
j=0




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

def t_comillasdobles(t):
    r'\"'
    t.type = 'comillasdobles'
    print("comillasdobles ")
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
    Programa : V F Main
    '''
    print("\t***Correcto***")

#V-> V Let id => K ; 
#V-> V Let id => (A);
def p_V(p):
    '''
    V : LET aux asignacion K puntoycoma V
    V : LET aux asignacion abreparentesis  A cierraparentesis puntoycoma V
      |
    '''
def p_aux(p):
    '''
    aux : type ID
    ''' 
    tablaSimb[str(p[2])] = str(p[1])
    

#A -> num 
#A -> A , num
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
    A : A coma num
    '''    

#Main -> begin ; Z end ;
def p_Main(p):
    '''
    Main : BEGIN puntoycoma  Z END puntoycoma
      |
    '''
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
    S : IF EL abrellave Z cierrallave ELSE abrellave Z cierrallave
    S : READ abreparentesis ID abreparentesis A cierraparentesis cierraparentesis
    S : PRINT abreparentesis M cierraparentesis
    S : LET ID asignacion IF abreparentesis EL cierraparentesis abrellave Z cierrallave ELSE abrellave Z cierrallave
    S : WHILE EL abrellave Z cierrallave
    S : LOOP abrellave Z abreparentesis EL cierraparentesis B cierrallave 
    S : FOR abreparentesis LET type ID asignacion K  puntoycoma EL puntoycoma ID suma num cierraparentesis abrellave Z cierrallave
    S : ID D asignacion E
    S : BREAK
      |
    '''

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
    M : comillasdobles K comillasdobles
    M : A
    '''


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
    X : num
    X : abreparentesis E cierraparentesis
    '''
def p_IDaux(p):
    '''
    IDaux : ID
    '''
    if checkVarDefined(p[1]) == True:
        operands.append(p[1])
        print("****************ADD OPERAND")
        print(operands)
    else:
        print("VARIABLE NO DECLARADA")

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
    cuadruploOr(operands2, tempAvail2)

def p_andAux(p):
    '''
    andAux : AL AND TL
    '''
    print("AND*******")
    cuadruploAnd(operands2, tempAvail2)

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
    cuadruploComp(operands2, tempAvail2, p[2])


#J-> id (num,...)
#J-> id
#J-> num
def p_J(p):
    '''
    J : ID abreparentesis A cierraparentesis
    J : IDoux
    J : num
    '''
def p_IDoux(p):
    '''
    IDoux : ID
    '''
    if checkVarDefined(p[1]) ==  True:
        operands2.append(p[1])
        print("****************ADD OPERAND")
        print(operands2)
    else:
        print("VARIABLE NO DECLARADA")

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
    print("\t******")

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
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)
      
    cuadruplos.append("+")
    cuadruplos.append(oper1)
    cuadruplos.append(oper2)
    cuadruplos.append(result)
    i=i+1

def cuadruploMenos(operands, tempAvail):
    global i
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)

    cuadruplos.append("-")
    cuadruplos.append(oper1)
    cuadruplos.append(oper2)
    cuadruplos.append(result)
    i=i+1

def cuadruploDiv(operands, tempAvail):
    global i
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)

    cuadruplos.append("/")
    cuadruplos.append(oper1)
    cuadruplos.append(oper2)
    cuadruplos.append(result)
    i=i+1

def cuadruploMult(operands, tempAvail):
    global i
    oper2 = operands.pop()
    oper1 = operands.pop()
    result = tempAvail[i]
    operands.append(result)

    cuadruplos.append("*")
    cuadruplos.append(oper1)
    cuadruplos.append(oper2)
    cuadruplos.append(result)
    i=i+1
#Cuadruplos logicos
def cuadruploAnd(operands, tempAvail):
    global j
    oper2 = operands2.pop()
    oper1 = operands2.pop()
    result = tempAvail2[j]
    operands2.append(result)

    cuadruplos2.append("AND")
    cuadruplos2.append(oper1)
    cuadruplos2.append(oper2)
    cuadruplos2.append(result)
    j=j+1
    print("CuadruploAND")
    print(cuadruplos2)

def cuadruploOr(operands, tempAvail):
    global j
    oper2 = operands2.pop()
    oper1 = operands2.pop()
    result = tempAvail2[j]
    operands2.append(result)

    cuadruplos2.append("OR")
    cuadruplos2.append(oper1)
    cuadruplos2.append(oper2)
    cuadruplos2.append(result)
    j=j+1
    print("CuadruploOR")
    print(cuadruplos2)

#Cuadruplos Comparativos
def cuadruploComp(operands, tempAvail, comp):
    global j
    oper2 = operands2.pop()
    oper1 = operands2.pop()
    result = tempAvail2[j]
    operands2.append(result)

    cuadruplos2.append(str(comp))
    cuadruplos2.append(oper1)
    cuadruplos2.append(oper2)
    cuadruplos2.append(result)
    j=j+1
    print("CuadruploComparacion")
    print(cuadruplos2)

def checkVarDefined(key):
    if key in tablaSimb.keys():
        return True    
    else:
        return False



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
        print("\n")
        s = listToString(s)
        print(s+'\n')
        
    except EOFError:
        break

    parser.parse(s)
    break

f.close()

#Imprimir tabla de simbolos
print("\n#######  TABLA DE SIMBOLOS  ######")
tablaSimb_items = tablaSimb.items()
for item in tablaSimb_items:
    print(item)

#Imprimir Pila de operandos
print("\nOPERANDS")
print(operands)

#Imprimir Cuadruplos
print("\nCUADRUPLOS")
print(cuadruplos)

#Imprimir Pila de operandos
print("\nOPERANDS LOGICOS")
print(operands2)

#Imprimir Cuadruplos
print("\nCUADRUPLOS LOGICOS")
print(cuadruplos2)