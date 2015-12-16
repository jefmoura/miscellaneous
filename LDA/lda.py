import MySQLdb
import socket
import numpy as np
import sys
import re
from nltk.tokenize import RegexpTokenizer
from gensim import corpora, models

if __name__ == '__main__':

	db = MySQLdb.connect(host="localhost", 
								user="root", 
								passwd="root", 
								db="datamining",
								charset="utf8",
								init_command="SET AUTOCOMMIT=0",
								unix_socket='/var/run/mysqld/mysqld.sock')

	tokenizer = RegexpTokenizer(r'\w\w\w\w+')

	cursor = db.cursor()
	# Query
	query = "SELECT prova, GROUP_CONCAT(disciplina) as disciplinas, GROUP_CONCAT(enunciado) as enunciados, GROUP_CONCAT(questao1, questao2, questao3, questao4, questao5, questao6, questao7, questao8, questao9) as questoes FROM questao_collection GROUP BY ano, prova"
	cursor.execute(query)
	rows = cursor.fetchall()

	query2 = "SELECT DISTINCT prova FROM questao_collection"
	cursor.execute(query2)
	rows2 = cursor.fetchall()

	exams = list()
	for i in rows2:
		string = i[0]
		exams.append(string.encode('utf8'))

	cursor.close()

	#docs = [tuple(prova, disciplinas, enunciados, questoes) for (prova, disciplinas, enunciados, questoes) in rows.iteritems()]
   
	for exam in exams:
		doc_set = []
		for prova, disciplinas, enunciados, questoes in rows:
			if prova.encode('utf8') == exam:
				doc_set.append(disciplinas + enunciados + questoes)

		# list for tokenized documents in loop
		texts = []

		# loop through document list
		for i in doc_set:
    
    		# clean and tokenize document string
			raw = i.lower()
			tokens = tokenizer.tokenize(raw)
    
    		# add tokens to list
			texts.append(tokens)

		# turn our tokenized documents into a id <-> term dictionary
		dictionary = corpora.Dictionary(texts)
    
		# convert tokenized documents into a document-term matrix
		corpus = [dictionary.doc2bow(text) for text in texts]

		# generate LDA model
		ldamodel = models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary, passes=20)

		print(ldamodel.print_topics(num_topics=5, num_words=5))
