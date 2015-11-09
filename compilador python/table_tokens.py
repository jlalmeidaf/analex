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