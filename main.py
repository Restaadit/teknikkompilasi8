import lexer
import resta

def main ():
 #baca flow source di coba.langc
 content = ""
 with open('coba.lang', 'r') as file:
 	content = file.read()


 	#lexer

 	lex = lexer.Lexer(content)
 	#panggil tokenize
 	tokens = lex.tokenize()

 	#parser
 	parse = resta.Resta(tokens)
 	parse.parse()


main()



