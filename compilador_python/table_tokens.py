import re 
def create_lst(): #Cria uma lista com todas as palavras do documento

	lst = []
	lst2 = []
	#name = raw_input("Enter the document name: ")
	with open("codigo.txt", "r") as f: #Abre o documento
		rows = f.readlines()	#Armazena todas as linhas, em forma de lista, do documento em rows
	f.close()
	for i in xrange(len(rows)): 
		result = re.search("^[//].*$", rows[i]) #Expressão regular para retirada dos comentários
		if result:
			pass
		else:
			lst.append(rows[i].split()) #Coloca na lista dividindo entre os espaços
	for row in lst:
		for word in row:
			lst2.append(word)
	
	return lst2

def table_token(lst_words): #Cria a tabela de tokens

	PR = ["var","program","integer","end","begin","goto"]
	NUM = [0,1,2,3,4,5,6,7,8,9]
	# criar identificadores com regex
	CE= [",","(",")", "<-", "*"]
	
	with open("table.txt", "w") as table: #Cria tabela um novo documento
		for words in lst_words:
			if words in PR:
				table.write("%s:Palavra Reservada \n" % words)
			#elif words in ID:
			#	table.write("%s:Identificador \n" % words)
			elif words in CE:
				table.write("%s:Caracter Especial\n" % words)
			elif words in NUM:
				table.write("%s: Numero\n" % words)
			else:
				table.write("%s:Literal \n" % words)
	table.close() # fecha

lst_words = create_lst()
table_token(lst_words)