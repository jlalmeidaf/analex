import re 
def create_lst(): #Cria uma lista com todas as palavras do documento

	lst = []
	lst2 = []
	#name = raw_input("Enter the document name: ")
	with open("codigo.txt", "r") as f: #Abre o documento
		rows = f.readlines()	#Armazena todas as linhas, em forma de lista, do documento em rows
	f.close()
