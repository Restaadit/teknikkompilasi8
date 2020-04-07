import re

class Lexer(object):
	"""docstring for Lexer"""
	def __init__(self, source_code):
		self.source_code = source_code

	def  tokenize(self):
		
		#tdimna semua token dibuat lexer
		tokens = []
		
		# buat sebuah list kata

		source_code = self.source_code.split()

		#ini akan menyimpan jalur kata di sourcecode
		source_index = 0

		#untuk loo[]
		while  source_index < len(source_code):

			word = source_code[source_index]
			#untuk recognize sebuah variabel dan sebuah token
			if word == "var": 
				tokens.append(["VAR_DECLERATION", word])
			#untuk recognize sebuah kata dan melakukan indetifier token
			elif re.match('[a-z]',word) or re.match('[A-Z]', word):
				if word[len(word) - 1] == ";":
					tokens.append(['IDETINFIER', word[0:len(word) - 1]])
				else:
					tokens.append(['IDETINFIER', word])
			#untuk recognize sebuah kata dan membuah sebuah token integer
			elif re.match('[0-9]', word):
				if word[len(word) - 1] == ";":
					tokens.append(['INTEGER', word[0:len(word) - 1]])
				else:
					tokens.append(['INTEGER', word])
			#untuk recognize sebuah kata dan membuah sebuah token operasional
			elif word in "=/*=-+":
				tokens.append(['OPERASIONAL', word])

			if word[len(word) - 1] == ";":
				tokens.append(['STATEMENT_END', ';'])
		

			source_index += 1

		print(tokens)

		return tokens 
		