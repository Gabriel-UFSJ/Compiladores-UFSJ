from analyzer import Analyzer


with open("test.c", 'r') as file:
    data = file.read()

analyzer = Analyzer()
tokens = analyzer.compile(data)
strTokens = ""

for token in tokens:
    strTokens += token.__str__() +"\n"

with open("saída.txt", 'w') as file:
    data = file.write(strTokens)
print(strTokens)

with open ("saída.txt", 'r') as file:
  palavra = "ERRO_LEXICO"
  contador_linhas = 0
  erros = ""
  for linha in file:
    contador_linhas = contador_linhas + 1
    if palavra in linha:
      print("Erro léxico linha: %d, %s" % (contador_linhas, linha))
      erros += linha


with open ("Erros_léxicos.txt", 'w') as file:
  data = file.write(erros)