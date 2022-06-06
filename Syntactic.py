from rules import RULES

class syntactic:
  
  def __init__ (self):  
    self.arq_in = open("saída.txt", 'r')        
    self.tokens = self.arq_in.readlines()
    self.arq_in.close

    self.arq_out = open("resp_syntactic.txt", 'w')
      
    self.line = 0 # line count
    self.colum = 1 # colum count
  
    self.current_line = 1
    self.last_line = 1
    self.current_type = ""
    self.symbol_table = ""
    self.temp = 1
  
  def next_token(self):
    self.last_line = self.tokens[self.line][self.tokens[self.line].find('=>') + 2:-1]
    self.line += 1
    self.current_line = self.tokens[self.line][self.tokens[self.line].find('=>') + 2:-1]

  def type_token(self):
    return self.tokens[self.line][self.tokens[self.line].find('<')+1:self.tokens[self.line].find('>')]

  def which_token(self):
    return self.tokens[self.line][:self.tokens[self.line].find('>')]
  
  def transition(self):
    if("$" not in self.tokens[self.line]):
      if any(x in self.tokens[self.line] for x in ["<INT>", "<CHAR>", "<FLOAT>"]):
        self.declaration()
      elif "<ID>" in self.tokens[self.line]:
        self.next_token()
        self.assignment()
      elif any(x in self.tokens[self.line] for x in["<FOR>", "<WHILE>"]):
        self.repeat()
      elif("<IF>") in self.tokens[self.line]:
        self.next_token()
        self.decision()
      elif("<ELSE>") in self.tokens[self.line]:
        print("error: expected expression - line:%s" %self.last_line + "\n")
      if("<FECHA_CHAVE>") in self.tokens[self.line]:    
        return
      if ("$") not in self.tokens[self.line]:
        self.next_token()
      self.transition()
    else:
      print("EOF")
      self.arq_out.close()
      
  def declaration(self):
    self.next_token()
    if "<ERRO_LEXICO>" in self.tokens[self.line]:
      self.next_token()
    elif any(x in self.tokens[self.line] for x in ["<ID>"]):
      self.next_token()
      if "<PONTO_VIRGULA>" in self.tokens[self.line]:
        self.next_token()
      elif("<ATRIBUIÇÃO>") in self.tokens[self.line]:
        self.assignment()
      else:
        print("error: expected ';' - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected ';' - line:%s" %self.last_line + "\n")
    else:
      print("Error missing identifier - line: %s " %self.last_line + "\n" )
      self.arq_out.write("Error" +self.type_token() + "Missing identifier - line: %s " %self.last_line + "\n" )
      
  def assignment(self):
    if "<ERRO_LEXICO>" in self.tokens[self.line]:
      self.next_token()
    if any(x in self.tokens[self.line] for x in["<MAIS>","<MENOS>","<MULTIPLICAÇÃO>","<DIVISÃO>"]):
      self.expression()
    if ("<ATRIBUIÇÃO>") in self.tokens[self.line]:
      self.next_token()
      if any(x in self.tokens[self.line] for x in["<INT_LITERAL>","<FLOAT_LITERAL>","<STRING_LITERAL>","<CHAR_LITERAL>"]):
        self.next_token()
        if "<PONTO_VIRGULA>" in self.tokens[self.line]:
          self.next_token()
        else:
          print("error: expected ';' - line:%s" %self.last_line + "\n")
          self.arq_out.write("error: expected ';' - line:%s" %self.last_line + "\n")
      else:
        self.next_token()
        print("error: expected expression - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected ';' - line:%s" %self.last_line + "\n")
        if "<PONTO_VIRGULA>" in self.tokens[self.line]:
          self.next_token()

  def relation(self):
    if "<ERRO_LEXICO>" in self.tokens[self.line]:
      self.next_token()
    self.next_token()
    if "<ATRIBUIÇÃO>" in self.tokens[self.line]: # =
      self.next_token()
    elif "<DIFERENTE>" in self.tokens[self.line]: # !=
      self.next_token()
    elif "<MAIOR_IGUAL>" in self.tokens[self.line]:# >=
      self.next_token()
    elif "<MENOR_IGUAL>" in self.tokens[self.line]: # <=
      self.next_token()
    elif "<MAIOR>" in self.tokens[self.line]: # >
      self.next_token()
    elif "<MENOR>" in self.tokens[self.line]:# <
      self.next_token()
    elif "<AND>" in self.tokens[self.line]:# <
      self.next_token()
    elif "<OR>" in self.tokens[self.line]:# <
      self.next_token()
    else:
      print("error: expected '= | <> | >= | <= | > | <' - line:%s" %self.last_line + "\n")
      self.arq_out.write("error: expected '= | <> | >= | <= | > | <' - line:%s" %self.last_line + "\n")
    self.expression()

  def repeat(self):
    if("<FOR>") in self.tokens[self.line]:
      self.next_token()
      if("<ABRE_PARENTESES>") in self.tokens[self.line]:
        self.condition()
        if("<FECHA_PARENTESES>") in self.tokens[self.line]:
          self.next_token()
          self.block()
        else:
          print("error: expected ')' - line:%s" %self.last_line + "\n")
          self.arq_out.write("error: expected ')' - line:%s" %self.last_line + "\n") 
      else:
        print("error: expected '(' - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected '(' - line:%s" %self.last_line + "\n") 
    elif("<WHILE>") in self.tokens[self.line]:
      self.next_token()
      if("<ABRE_PARENTESES>") in self.tokens[self.line]:
        self.next_token()
        if any(x in self.tokens[self.line] for x in["<INT_LITERAL>","<FLOAT_LITERAL>","<STRING_LITERAL>","<CHAR_LITERAL>"]):
          self.expression()
        else:
          self.relation()
        if("<FECHA_PARENTESES>") in self.tokens[self.line]:
          self.next_token()
          self.block()
        else:
          print("error: expected ')' - line:%s" %self.last_line + "\n")
          self.arq_out.write("error: expected ')' - line:%s" %self.last_line + "\n") 
      else:
        print("error: expected '(' - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected '(' - line:%s" %self.last_line + "\n") 
        
  def condition(self):
    self.next_token()
    if "<ERRO_LEXICO>" in self.tokens[self.line]:
      self.next_token()
    self.declaration()
    self.relation()
    self.expression()

  def decision(self):
    if("<ABRE_PARENTESES>") in self.tokens[self.line]:
      self.next_token()
      print(self.tokens[self.line])
      self.relation()
      if any(x in self.tokens[self.line] for x in["<AND>", "<OR>"]):
        self.next_token()
        self.relation()
      elif("<FECHA_PARENTESES>") in self.tokens[self.line]:
        self.next_token()
        self.block()
        if("<ELSE>") in self.tokens[self.line]:
          self.next_token()
          if("<IF>") in self.tokens[self.line]:
            self.next_token()
            self.decision()
          self.block()
      else:
        print("error: expected ')' - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected ')' - line:%s" %self.last_line + "\n") 
    else:
      print("error: expected '(' - line:%s" %self.last_line + "\n")
      self.arq_out.write("error: expected '(' - line:%s" %self.last_line + "\n")
  
  def expression(self):
    if "<ERRO_LEXICO>" in self.tokens[self.line]:
      self.next_token()
    if "<ID>" in self.tokens[self.line]:
      self.next_token()
    if any(x in self.tokens[self.line] for x in["<MAIS>","<MENOS>","<MULTIPLICAÇÃO>","<DIVISÃO>","<MAIS_MAIS>","<MENOS+MENOS>"]):
      self.next_token()
    if any(x in self.tokens[self.line] for x in["<INT_LITERAL>","<FLOAT_LITERAL>","<STRING_LITERAL>","<CHAR_LITERAL>"]):
      self.next_token()
    if "<PONTO_VIRGULA>" in self.tokens[self.line]:
          self.next_token()

  def block(self):
    if("<ABRE_CHAVE>") in self.tokens[self.line]:
      self.next_token()
      self.transition()
      if("<FECHA_CHAVE") in self.tokens[self.line]:
        self.next_token()
      else:
        print("error: expected '}' - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected '}' - line:%s" %self.last_line + "\n")
    else:
      print("error: expected '{' - line:%s" %self.last_line + "\n")
      self.arq_out.write("error: expected '{' - line:%s" %self.last_line + "\n")