# coding=utf-8
import re
import sys 


PALAVRAS_RESERVADAS = ["var","program","end;","begin","goto",'loop']
LITERAL = ["integer"]
NUMEROS = ['0','1','2','3','4','5','6','7','8','9']
DELIMITADORES = [",",";",":"]
OPERADORES = ['<-','+']


def create_lst(): #Cria uma lista com todas as palavras do documento

	palavra=''
	lst 	= []
	lst2 	= []
	ListaDelimitador 	= []
	
	#name = raw_input("Enter the document name: ")
	with open("codigo.txt", "r") as f: #Abre o documento
		rows = f.readlines()	#Armazena todas as linhas, em forma de lista, do documento em rows
	f.close()

	for row in rows:
		#print "T:" + row # é cada linha

		if (row.find("//") != -1):#retira comentário
			pass
		elif row == "\n":#retira linha em branco
			pass
		else:
			for eachrow in row:#esse cada caracter

				if eachrow == ' ':
					if len(palavra) == 0:
						pass
					else: 
						tokens = token(palavra) 
						print '%s: %s' %(tokens,palavra)
					palavra = ''
				elif eachrow in DELIMITADORES:
					if len(palavra) == 0:
						pass
					else:
						tokens = token(palavra)  
						print '%s: %s' %(tokens,palavra)
						tokens = token(eachrow) 
						print '%s: %s' %(tokens,eachrow)  
					palavra = ''
				elif eachrow in OPERADORES:
					if len(palavra) == 0:
						pass
					else:
						tokens = token(palavra)  
						print '%s: %s' %(tokens,palavra)
						tokens = token(eachrow) 
						print '%s: %s' %(tokens,eachrow)
						
						print 'Verificando: %s' % eachrow  
					palavra = ''
				else:
					palavra = '%s%s' %(palavra,eachrow)



					#print "Teste: " + palavra



					#if palavra == 'program':
					#	print "PALAVRAS_RESERVADAS - %s" % palavra
					#else:
					#	palavra = '%s%s' %(palavra,eachrow) 
					#	print "Teste: " + palavra
 
def token(palavra):

	token = ''

	if palavra in PALAVRAS_RESERVADAS:
		token = 'Palavra Reservada'
		return token
	elif palavra in NUMEROS:
		token = 'NUMEROS'
		return token
	elif palavra in DELIMITADORES:
		token = 'DELIMITADORES'
		return token
	elif palavra in OPERADORES:
		token = 'OPERADORES'
		return token
	elif palavra in LITERAL:
		token = 'LITERAL'
		return token
	else:
		return 'IDENTIFICADOR'	



if __name__ == "__main__":
	create_lst()


