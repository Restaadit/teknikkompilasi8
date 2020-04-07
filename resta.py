class Resta(object):

	def __init__(self, tokens):
		#untuk menahan token yang sudah dibuat di lexer
		self.tokens = tokens
		#untuk menahan token index
		self.token_index = 0

	def parse(self):
		
		while  self.token_index < len(self.tokens):
			
			#utk menahan tipe token
			token_type = self.tokens[self.token_index][0]
			#untuk menahan nilai token
			token_value = self.tokens[self.token_index][1]
			#ini untuk trigger variable declaration ada
			if token_type == "VAR_DECLERATION" and token_value == "var":
				self.parse_variable_decleration(self.tokens[self.token_index:len(self.tokens)])


			#agar bisa loop untuk token selanjutnya
			self.token_index += 1


	def parse_variable_decleration(self, token_stream):
		
		tokens_checked = 0

		for token in range (0, len(token_stream)):

			token_type  = token_stream[tokens_checked][0]
			token_value = token_stream[tokens_checked][1]


			#jika statement end loop berhenti
			if token == 4 and token_type == "STATEMENT_END": break

			#untuk mendapatkan tipe variabel
			if token == 0:
				print('Variable type: ' + token_value)

			#untuk mendapatkan nama variabel dan untuk menngecek kecocokan
			elif token == 1 and token_type == "IDENTIFIER":
				print("Variable name: " + token_value)

			elif token == 1 and token_type != "IDENTIFIER":
				print("ERROR: tidak cocok variabel'" + token_value + "'")
				quit()

			#untuk mendapatkan variabel operator
			elif token == 2 and token_type == "OPERATOR":
				print("Assignment OPperator" + token_value)

			elif token == 2 and token_type != "OPERATOR":
				print("ERROR: OPperator tidak cocok invalid it should be '='")
				quit()

			#untuk mendapatkan nilai variabel assign
			elif token == 3 and token_type in ['STRING', 'INTEGER', 'IDENTIFIER']:
				print('Variable Value :' + token_value)

			elif token == 3 and token_type not in ['STRING', 'INTEGER', 'IDENTIFIER']:
				print ("Invalid variable assignment '" + token_value + "'" )
				quit()


			tokens_checked +=1

		self.token_index += tokens_checked


	