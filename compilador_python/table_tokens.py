# coding=utf-8
import re 
def create_lst(): #Cria uma lista com todas as palavras do documento

	palavra=''
	lst 	= []
	lst2 	= []
	var 	= []
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

				if palavra == ' ':
					pass
				else:
					palavra = '%s%s' %(palavra,eachrow) 
					id_tokens(palavra)
					print "Teste: " + palavra
 
	
def id_tokens(palavra):
	if palavra == '//':
		return 'break'
	else:
		print '0'


create_lst()