from Lexical import lexical
from Syntactic import syntactic

with open("test.c", 'r') as file: # abrindo arquivo de entrada
    data = file.read()
lex = lexical()
tokens = lex.compile(data) #verificação dos tokens
strTokens = ""

for token in tokens:
  strTokens += token.__str__() + "\n" # salvando os tokens com quebra de linha
strTokens += "$"

with open("saída.txt", 'w') as file:  # escrevendo a saída no arquivo
    data = file.write(strTokens)

with open ("saída.txt", 'r') as file: # função para verificar erros léxicos
  palavra = "ERRO_LEXICO"
  erros = ""
  numErros = 0
  for linha in file:
    if palavra in linha:
      linha = linha.replace("<ERRO_LEXICO> : ", "")
      erros += linha
      numErros = numErros + 1


with open ("Erros_léxicos.txt", 'w') as file: # escrevendo os erros no arquivo
  data = file.write(erros)


with open ("saída.txt", 'r') as file: # verificando as variáveis iniciadas no arquivo
  iniInt = "<INT>"
  iniChar = "<CHAR>"
  iniFloat = "<FLOAT>"
  id = "<ID>"
  identificador = ""
  for linha in file:
    if iniInt in linha or iniChar in linha or iniFloat in linha:
      prox = file.readline() # VÊ SE DÁ CERTO
      if id in prox:
        identificador += prox

with open ("identificadores.txt", 'w') as file: # escrevendo as variáveis iniciadas
  data = file.write(identificador)

with open ("test.c", 'r') as file: # achando as linhas do erro léxico
  with open ("Erros_léxicos.txt", 'r') as txt:
    while palavra:
      file.seek(0) # voltando ao inicio do arquivo
      contador_linhas = 0
      palavra = txt.readline()
      for linha in file:
        contador_linhas = contador_linhas + 1
        if palavra and palavra in linha:
          print("Erro léxico linha: %d, %s" % (contador_linhas, linha))
    print("exit status %d"% (numErros))
        
parser = syntactic()
parser.transition()

  