# coding=utf-8
import re 
def create_lst(): #Cria uma lista com todas as palavras do documento

	lst 	= []
	lst2 	= []
	var 	= []
	delimi 	= []
	typeInt = []
	aux		= []
	#name = raw_input("Enter the document name: ")
	with open("codigo.txt", "r") as f: #Abre o documento
		rows = f.readlines()	#Armazena todas as linhas, em forma de lista, do documento em rows
	f.close()
	for i in xrange(len(rows)): 
		result 				= re.search("^[//].*$", rows[i]) #Expressão regular para retirada dos comentários		
		variable      		= re.search("[a-z]:[a-z]*",rows[i])
		valores				= re.search("^[:]$", rows[i])#x: e y:
		semicolon			= re.search("(?:;\s+)|(['""].+['""])(?:;\s+)", rows[i])
		two_points			= re.search("[:]",rows[i])  
		space				= re.search("[\s]",rows[i])
		teste				= re.search("^[a-z].+[:]$",rows[i])
 

		if result:
			pass
		elif variable:
			rows[i] = rows[i].split(':') 
			var.append(rows[i])
			#print var


#var.append(rows[i].split(':'))
		else:
			lst.append(rows[i].split()) #Coloca na lista dividindo entre os espaços
	for row in lst:
		for word in row:
			lst2.append(word)

	#print delimi
	
	table_token(lst2,var)

def table_token(lst_words,var): #Cria a tabela de tokens

	PR = ["var","program","integer","end;","begin","goto",'loop']
	NUM = ['0','1','2','3','4','5','6','7','8','9','1;']
	ID = ['x','L1','helloword','y']
	# criar identificadores com regex
	CE = [",","(",")"]
	Operador = ['<-','+']
	
	with open("table.txt", "w") as table: #Cria tabela um novo documento
		for words in lst_words:
			if words in PR:
				table.write("%s:Palavra Reservada \n" % words)
				print("%s:Palavra Reservada \n" % words) 
			#elif words in ID:
			#	table.write("%s:Identificador \n" % words)
			elif words in CE:
				table.write("%s:Caracter Especial\n" % words)
				print("%s:Palavra Reservada \n" % words)
			elif words in ID:
				table.write("%s:IDENTIFICADOR\n" % words)
				print("%s:IDENTIFICADOR\n" % words)
			elif words in Operador:
				table.write("%s:Operador\n" % words)
				print("%s:Operador\n" % words)
			elif words in NUM:
				table.write("%s: Numero\n" % words)
				print("%s: Numero\n" % words)
			else:
				table.write("%s:Literal \n" % words)
				print("%s:Literal \n" % words)

	table.close() # fecha

create_lst()