#----------------------------------------------------------------------------
# Created By  : Gabriel Resende Meireles
# Created Date: 07/04/2022
# version ='1.0'
# ---------------------------------------------------------------------------

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

with open ("saída.txt", 'r') as file:
  palavra = "ERRO_LEXICO"
  contador_linhas = 0
  erros = ""
  for linha in file:
    contador_linhas = contador_linhas + 1
    if palavra in linha:
      linha = linha.replace("<ERRO_LEXICO> : ", "")
      erros += linha


with open ("Erros_léxicos.txt", 'w') as file:
  data = file.write(erros)


with open ("saída.txt", 'r') as file:
  palavra = "ID"
  identificador = ""
  for linha in file:
    if palavra in linha and identificador != linha:
      identificador += linha

with open ("identificadores.txt", 'w') as file:
  data = file.write(identificador)

with open ("test.c", 'r') as file:
  with open ("Erros_léxicos.txt", 'r') as txt:
    while palavra:
      file.seek(0)
      contador_linhas = 0
      palavra = txt.readline()
      for linha in file:
        contador_linhas = contador_linhas + 1
        if palavra and palavra in linha:
          print("Erro léxico linha: %d, %s" % (contador_linhas, linha))
        

        

  
