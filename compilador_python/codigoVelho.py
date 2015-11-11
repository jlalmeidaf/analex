# coding=utf-8
import re 
def create_lst(): #Cria uma lista com todas as palavras do documento

	lst 	= []
	lst2 	= []
	var 	= []
	PALAVRAS_RESERVADAS = ["var","program","integer","end;","begin","goto",'loop']
	NUMEROS = ['0','1','2','3','4','5','6','7','8','9']
	#IDENTIFICADORES = ['x','L1','helloword','y', 'L1;']
	DELIMITADORES = [",",";",":"]
	OPERADORES = ['<-','+']
	
	#name = raw_input("Enter the document name: ")
	with open("codigo.txt", "r") as f: #Abre o documento
		rows = f.readlines()	#Armazena todas as linhas, em forma de lista, do documento em rows
	f.close()
	for row in rows: 
		#result 				= re.search("^[//].*$", rows[i]) #Expressão regular para retirada dos comentários		
		#variable      		= re.search("[a-z]:[a-z]*",rows[i])
		#valores				= re.search("^[:]$", rows[i])#x: e y:
		#semicolon			= re.search("(?:;\s+)|(['""].+['""])(?:;\s+)", rows[i])
		#two_points			= re.search("[:]",rows[i])  
		#space				= re.search("[\s]",rows[i])
		#teste				= re.search("^[a-z].+[:]$",rows[i])
 

		print "T:" + row # é cada linha
		for eachrow in row:#esse cada caracter
			print eachrow
			if(eachrow == '/'):
				aux += eachrow
				if(aux == '//')


		#if result:
		#	pass
		#elif variable:
		#	rows[i] = rows[i].split(':') 
		#	var.append(rows[i])
			#print var


#var.append(rows[i].split(':'))
		#else:
		#	lst.append(rows[i].split()) #Coloca na lista dividindo entre os espaços
	#for row in lst:
	#	for word in row:
	#		lst2.append(word)

	#print delimi
	
	#table_token(lst2,var)

#def table_token(lst_words,var): #Cria a tabela de tokens

	
	
#	with open("table.txt", "w") as table: #Cria tabela um novo documento
#		for words in lst_words:
#			if words in PR:
#				table.write("%s:Palavra Reservada \n" % words)
#				print("%s:Palavra Reservada \n" % words) 
#			elif words in CE:
#				table.write("%s:Caracter Especial\n" % words)
#				print("%s:Palavra Reservada \n" % words)
#			elif words in ID:
#				table.write("%s:Identificador\n" % words)
#				print("%s:Identificador\n" % words)
#			elif words in OP:
#				table.write("%s:Operador\n" % words)
#				print("%s:Operador\n" % words)
#			elif words in NUM:
#				table.write("%s: Numero\n" % words)
#				print("%s: Numero\n" % words)
#			else:
#				table.write("%s:Literal \n" % words)
#				print("%s:Literal \n" % words)

#	table.close() # fecha

def 

create_lst()