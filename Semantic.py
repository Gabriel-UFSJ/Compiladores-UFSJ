class semantic:
  def __init__(self):
    self.arq_out = open("resp_semantic.txt", 'w')  
    self.identificador = ""

    self.idlist = []
    self.notreplaced = ""
    self.replaced_content = ""
    self.error = 0
    
  def tab_id (self, ID, type):
    comparar = ID.split('=')
    type = type[type.find('<')+1:type.find('>')]
    ID = ID[ID.find('<'):-1]
    if comparar[0] not in self.identificador:
      self.identificador += ID + " Unused:True " + type + "\n"
      data = ID + " Unused:True " + type + "\n"
      self.idlist.append(data)
      with open ("tabela_ID.txt", 'a') as txt:
        txt.write(data)
    else:
      id = ID[ID.find(':')+2:ID.find('=')-1]
      line = ID[ID.find('=>') + 2:ID.find('=>')+6]
      print("error: redefinition of '%s' - line: %s " %(id, line))
      self.arq_out.write("error: redefinition of '%s' - line: %s " %(id, line))
      self.error += 1
      
  def tab_consult(self,ID):
    comparar = ID.split('=')
    if comparar[0] not in self.identificador:
      id = ID[ID.find(':')+2:ID.find('=')-1]
      line = ID[ID.find('=>') + 2:-1]
      print("error: use of undeclared identifier '%s' - line: %s " %(id, line))
      self.arq_out.write("error: redefinition of '%s' - line: %s " %(id, line))
      self.error += 1
    else:
      id = ID[ID.find(':')+2:ID.find('=')-1]
      #print(id)
      with open ("tabela_ID.txt", 'r+') as txt:
        for line in txt:
          if id in line:
            line = line.strip()
            new_line = line.replace("True","False")
            if new_line not in self.replaced_content:
              self.replaced_content = self.replaced_content + new_line + "\n"

  def print_unused(self):
    with open ("tabela_ID.txt", 'r') as txt:
      data = txt.read()
      for ID in self.idlist:
        id = ID[ID.find(':')+2:ID.find('=')-1]
        if id not in data:
          print("warning: '%s' defined but not used" %(id))
    txt.close()
  
  def write_arq(self):
    if self.replaced_content:
      with open ("tabela_ID.txt", 'w') as txt:
        txt.write(self.replaced_content)
      
  def print_errors(self):
    if self.error != 0:
      print(f"{self.error} error generated")