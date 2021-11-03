#Kenia Sanchez
#A01244940
#Monalisa

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
    S : IF C abrellave Z cierrallave ELSE abrellave Z cierrallave
    S : READ abreparentesis ID abreparentesis A cierraparentesis cierraparentesis
    S : PRINT abreparentesis M cierraparentesis
    S : LET ID asignacion IF abreparentesis C cierraparentesis abrellave Z cierrallave ELSE abrellave Z cierrallave
    S : WHILE C abrellave Z cierrallave
    S : LOOP abrellave Z abreparentesis C cierraparentesis B cierrallave 
    S : FOR abreparentesis LET type ID asignacion K  puntoycoma C puntoycoma ID suma num cierraparentesis abrellave Z cierrallave
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
    E : E suma T
    E : E resta T
    E : T
    '''
#T-> T * X
#T-> T / X
#T-> X
def p_T(p):
    '''
    T : T multiplicacion X
    T : T dividir X
    T : X
    '''
#X-> id
#X-> id (H)
#X-> num 
#X-> (E)
def p_X(p):
    '''
    X : ID
    X : ID abreparentesis A cierraparentesis
    X : num
    X : abreparentesis E cierraparentesis
    '''
   
#EL-> TL
#EL-> EL or TL
def p_EL(p):
    '''
    EL : TL
    EL : EL OR TL
    '''

#TL-> C
#TL-> TL and C
def p_TL(p):
    '''
    TL : C
    TL : TL AND C
    '''    
#C-> (EL)
#C-> J signos(W) J
def p_C(p):
    '''
    C : abreparentesis EL cierraparentesis
    C : J W J
    '''

#J-> id (num,...)
#J-> id
#J-> num
def p_J(p):
    '''
    J : ID abreparentesis A cierraparentesis
    J : ID
    J : num
    '''

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

#Por si hay un error
def p_error(p):
    print("\t******")

parser = yacc.yacc()

#####################################
####      Tabla de simbolos     ##### 
#####################################
tablaSimb = {}

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