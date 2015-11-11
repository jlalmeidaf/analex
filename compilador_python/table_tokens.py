# coding=utf-8
import re
import sys 
def create_lst(): #Cria uma lista com todas as palavras do documento

	palavra=''
	lst 	= []
	lst2 	= []
	ListaDelimitador 	= []
	PALAVRAS_RESERVADAS = ["var","program","integer","end;","begin","goto",'loop']
	NUMEROS = ['0','1','2','3','4','5','6','7','8','9']
	DELIMITADORES = [",",";",":"]
	OPERADORES = ['<-','+']
	
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
						print 'PALAVRAS: %s' % palavra
					palavra = ''
				elif eachrow in DELIMITADORES:
					if len(palavra) == 0:
						pass
					else:
						print 'Palavra: %s' % palavra
						print 'Delimitador: %s' % eachrow 
					palavra = ''
				elif eachrow in OPERADORES:
					if len(palavra) == 0:
						pass
					else:
						print 'Operador: %s' % eachrow
				else:
					palavra = '%s%s' %(palavra,eachrow)



					#print "Teste: " + palavra



					#if palavra == 'program':
					#	print "PALAVRAS_RESERVADAS - %s" % palavra
					#else:
					#	palavra = '%s%s' %(palavra,eachrow) 
					#	print "Teste: " + palavra
 
	

create_lst()


def palavra_vazia(palavra):
	if not palavra:
		return true
	else:
		return false