from Semantic import semantic
from Generator import generator

class syntactic:
  
  def __init__ (self):  
    self.arq_in = open("saída.txt", 'r')        
    self.tokens = self.arq_in.readlines()
    self.arq_in.close

    self.arq_out = open("resp_syntactic.txt", 'w')

    self.semantic = semantic()
    self.gencode = generator()
    
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
    return self.tokens[self.line][self.tokens[self.line].find(':')+2:self.tokens[self.line].find(' =>')]
    
  def which_neighbor(self,line):
    return self.tokens[line][self.tokens[line].find(':')+2:self.tokens[line].find(' =>')]
  
  def transition(self):
    #print(self.tokens[self.line])
    if("$" not in self.tokens[self.line]):
      if any(x in self.tokens[self.line] for x in ["<INT>", "<CHAR>", "<FLOAT>"]):
        self.gencode.notes = "declaration"
        self.gencode.operation = "word"
        self.gencode.description = ".word"
        self.declaration()
      elif "<ID>" in self.tokens[self.line]:
        self.gencode.operands = self.which_token()
        self.semantic.tab_consult(self.tokens[self.line])
        self.next_token()
        self.assignment()
      elif any(x in self.tokens[self.line] for x in["<FOR>", "<WHILE>"]):
        self.repeat()
      elif("<IF>") in self.tokens[self.line]:
        self.next_token()       
        if("<ABRE_PARENTESES>") in self.tokens[self.line]:
          self.next_token()
          self.decision()
        else:
          print("Error: expected '(' - line :%s" %self.last_line + "\n")
          self.arq_out.write("Error: expected '(' - line :%s" %self.last_line + "\n")
      elif("<ELSE>") in self.tokens[self.line]:
        print("error: expected expression - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected expression - line:%s" %self.last_line + "\n")
      if("<FECHA_CHAVE>") in self.tokens[self.line]:
        #print(self.tokens[self.line])
        self.next_token()
      #if ("$") not in self.tokens[self.line]:
        #print(self.tokens[self.line])
        #self.next_token()
      self.transition()
    else:
      #print("EOF")
      self.arq_out.close()
      self.semantic.write_arq()
      self.semantic.print_errors()
      self.semantic.print_unused()
      self.semantic.arq_out.close()
      self.gencode.arq_out.close()
      print("\n")
      self.gencode.print_table()
      
  def declaration(self):
    self.next_token()
    if "<ERRO_LEXICO>" in self.tokens[self.line]:
      self.next_token()
    elif any(x in self.tokens[self.line] for x in ["<ID>"]):
      self.gencode.operands = self.which_token()
      self.semantic.tab_id(self.tokens[self.line],self.tokens[self.line -1])      
      self.next_token()
      if "<PONTO_VIRGULA>" in self.tokens[self.line]:
        #print("chegou")
        #print(self.tokens[self.line])
        self.gencode.geration_table()
        self.next_token()
      elif("<ATRIBUIÇÃO>") in self.tokens[self.line]:
        self.gencode.description = ".word <- number"
        self.assignment()
      else:
        print("error: expected ';' - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected ';' - line:%s" %self.last_line + "\n")
    else:
      print("Error missing identifier - line: %s " %self.last_line + "\n" )
      self.arq_out.write("Error" +self.type_token() + "Missing identifier - line: %s " %self.last_line + "\n" )
      
  def assignment(self):
    #print(self.tokens[self.line])
    if "<ERRO_LEXICO>" in self.tokens[self.line]:
      self.next_token()
    if any(x in self.tokens[self.line] for x in["<MAIS>","<MENOS>","<MULTIPLICAÇÃO>","<DIVISÃO>"]):
      self.gencode.operands += "," + self.which_neighbor(self.line-1)
      self.gencode.opcode(self.tokens[self.line])
      self.gencode.description = "dest <- src1 " + self.which_token() + " src2"
      self.next_token()
    if ("<ATRIBUIÇÃO>") in self.tokens[self.line]:
      #print(self.tokens[self.line])
      self.gencode.notes = "assignment"
      self.gencode.operation = "lw"
      self.gencode.description = ".word <- number"
      self.next_token()
      if any(x in self.tokens[self.line] for x in["<INT_LITERAL>","<FLOAT_LITERAL>","<STRING_LITERAL>","<CHAR_LITERAL>","<ID>"]):
        #print(self.tokens[self.line])
        if ("<ID>") in self.tokens[self.line]:
          self.semantic.tab_consult(self.tokens[self.line])
        self.gencode.operands += "," + self.which_token()
        self.next_token()  
        if "<PONTO_VIRGULA>" in self.tokens[self.line]:
          self.gencode.geration_table()
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
    #print(self.tokens[self.line])
    if "<ERRO_LEXICO>" in self.tokens[self.line]:
      self.next_token()
    if "<TRUE>" in self.tokens[self.line]:# true
      self.next_token()
    elif "<FALSE>" in self.tokens[self.line]:# false
      self.next_token()
    else:
      op = self.tokens[self.line]
      self.gencode.operands = "temp" + "," 
      if "<ATRIBUIÇÃO>" in self.tokens[self.line]: # =
        self.next_token()
        self.gencode.operands += self.which_neighbor(self.line-2) 
        self.next_token()
      elif "<DIFERENTE>" in self.tokens[self.line]: # !=
        self.gencode.operands += self.which_neighbor(self.line-2) 
        self.next_token()
      elif "<MAIOR_IGUAL>" in self.tokens[self.line]:# >=
        self.gencode.operands += self.which_neighbor(self.line-2) 
        self.next_token()
      elif "<MENOR_IGUAL>" in self.tokens[self.line]: # <=
        self.gencode.operands += self.which_neighbor(self.line-2) 
        self.next_token()
      elif "<MAIOR>" in self.tokens[self.line]: # >
        self.gencode.operands += self.which_neighbor(self.line-1) 
        self.next_token()
      elif "<MENOR>" in self.tokens[self.line]:# <
        self.gencode.operands += self.which_neighbor(self.line-1) 
        self.next_token()
      elif "<AND>" in self.tokens[self.line]:# <
        self.gencode.operands += self.which_neighbor(self.line-1) 
        self.next_token()
      elif "<OR>" in self.tokens[self.line]:# <
        self.gencode.operands += self.which_neighbor(self.line-1) 
        self.next_token()
      else:
        print("error: expected '= | <> | >= | <= | > | <' - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected '= | <> | >= | <= | > | <' - line:%s" %self.last_line + "\n")
      self.gencode.operands += "," + self.which_token()
      self.gencode.notes = "compare contents"
      self.gencode.description = "$rs,$rt,branch value"
      self.gencode.geration_table()
      
      self.gencode.opcode(op)
      self.gencode.operands = self.which_neighbor(self.line - 3)
      self.gencode.operands += "," + self.which_token()
      self.gencode.geration_table()
      
      self.expression()

  def repeat(self):
    #print("chegou")
    #print(self.tokens[self.line])
    if("<FOR>") in self.tokens[self.line]:
      self.next_token()
      if("<ABRE_PARENTESES>") in self.tokens[self.line]:
        self.condition()
        if("<FECHA_PARENTESES>") in self.tokens[self.line]:
          self.next_token()
          if("<ABRE_CHAVE>") in self.tokens[self.line]:
            self.next_token()
            self.block()
          else:
            print("error: expected '{' - line:%s" %self.last_line + "\n")
            self.arq_out.write("error: expected '{' - line:%s" %self.last_line + "\n")
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
        #print("while - " + self.tokens[self.line])
        if ("<ID>") in self.tokens[self.line]:
          self.next_token()
          self.relation()
          self.expression()
          #print("voltou - " + self.tokens[self.line] )
        elif any(x in self.tokens[self.line] for x in["<INT_LITERAL>","<FLOAT_LITERAL>","<STRING_LITERAL>","<CHAR_LITERAL>"]):
            self.expression()
        else:
          self.relation()
          #print(self.tokens[self.line])
        if("<FECHA_PARENTESES>") in self.tokens[self.line]:
          self.next_token()
          if("<ABRE_CHAVE>") in self.tokens[self.line]:
            self.next_token()
            self.block()
          else:
            print("error: expected '{' - line:%s" %self.last_line + "\n")
            self.arq_out.write("error: expected '{' - line:%s" %self.last_line + "\n")
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
    self.gencode.operation = "lw"
    self.gencode.description = "literal assignment"
    self.declaration()
    
    self.gencode.operation = "slt"
    self.relation()

    self.gencode.notes = "arithmetic expressions"
    self.gencode.operands = self.which_token()
    self.gencode.description = "dest <- src1 " + self.which_token() + " src2"
    self.expression()
    self.gencode.geration_table()

  def decision(self):
    #print(self.tokens[self.line])
    if("<ID>") in self.tokens[self.line]:
      self.gencode.operation = "slt"
      self.gencode.description = "branch on equal"
      self.gencode.notes = "compare contents"
      self.next_token()
      self.relation()
      self.expression()
      #print(self.tokens[self.line])
    if any(x in self.tokens[self.line] for x in["<AND>", "<OR>"]):
      self.next_token()
      self.decision()
    if("<FECHA_PARENTESES>") in self.tokens[self.line]:
      self.next_token()
      if("<ABRE_CHAVE>") in self.tokens[self.line]:
        self.next_token()
        #print(self.tokens[self.line])
        self.block()
      else:
        print("error: expected '{' - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected '{' - line:%s" %self.last_line + "\n")
      if("<ELSE>") in self.tokens[self.line]:
        self.next_token()
        if("<IF>") in self.tokens[self.line]:
          self.next_token()
          self.decision()
        if("<ABRE_CHAVE>") in self.tokens[self.line]:
          self.next_token()
          #print(self.tokens[self.line])
          self.block()
        else:
          print("error: expected '{' - line:%s" %self.last_line + "\n")
          self.arq_out.write("error: expected '{' - line:%s" %self.last_line + "\n")     
    else:
      print("error: expected ')' - line:%s" %self.last_line + "\n")
      self.arq_out.write("error: expected ')' - line:%s" %self.last_line + "\n") 
  
  def expression(self):
    if "<ERRO_LEXICO>" in self.tokens[self.line]:
      self.next_token()
    if "<ID>" in self.tokens[self.line]:
      #print(self.tokens[self.line])
      self.semantic.tab_consult(self.tokens[self.line])
      self.next_token()
    if any(x in self.tokens[self.line] for x in["<MAIS>","<MENOS>","<MULTIPLICAÇÃO>","<DIVISÃO>","<MAIS_MAIS>","<MENOS_MENOS>"]):
      #print(self.tokens[self.line])
      self.gencode.opcode(self.tokens[self.line])
      self.next_token()
      #print(self.tokens[self.line])
    if any(x in self.tokens[self.line] for x in["<INT_LITERAL>","<FLOAT_LITERAL>","<STRING_LITERAL>","<CHAR_LITERAL>","<ID>"]):
      self.next_token()
      #print(self.tokens[self.line])
    if "<PONTO_VIRGULA>" in self.tokens[self.line]:
      self.next_token()

  def block(self):
    if("$" not in self.tokens[self.line]):
      #print(self.tokens[self.line])
      if any(x in self.tokens[self.line] for x in ["<INT>", "<CHAR>", "<FLOAT>"]):
        self.gencode.notes = "declaration"
        self.gencode.operation = "word"
        self.gencode.description = ".word"
        self.declaration()
      elif "<ID>" in self.tokens[self.line]:
        #print(self.tokens[self.line])
        self.gencode.operands = self.which_token()
        self.semantic.tab_consult(self.tokens[self.line])
        self.next_token()
        self.assignment()
      elif any(x in self.tokens[self.line] for x in["<FOR>", "<WHILE>"]):
        #print("passou")
        self.repeat()
      elif("<IF>") in self.tokens[self.line]:
        self.next_token()
        if("<ABRE_PARENTESES>") in self.tokens[self.line]:
          self.next_token()
          self.decision()
          #print("voltou")
        else:
          print("Error: expected '(' - line :%s" %self.last_line + "\n")
          self.arq_out.write("Error: expected '(' - line :%s" %self.last_line + "\n")
      elif("<ELSE>") in self.tokens[self.line]:
        print("error: expected expression - line:%s" %self.last_line + "\n")
        self.arq_out.write("error: expected expression - line:%s" %self.last_line + "\n")
      #print("antes - " + self.tokens[self.line])
      if("<PONTO_VIRGULA>") in self.tokens[self.line]:
        self.next_token()
      if("<FECHA_CHAVE>") not in self.tokens[self.line]:
        self.block()
    #print("chegou" + self.tokens[self.line])
    if("<FECHA_CHAVE") in self.tokens[self.line]:
      self.next_token()
      if("$") in self.tokens[self.line]:
        self.line -= 1
      return
    else:
      print("error: expected '}' - line:%s" %self.last_line + "\n")
      self.arq_out.write("error: expected '}' - line:%s" %self.last_line + "\n")