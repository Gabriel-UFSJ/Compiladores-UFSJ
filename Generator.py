import os
class generator:
  def __init__(self):
    self.arq_out = open("codgen.txt",'w')

    self.operation = ""
    self.operands = ""
    self.description = ""
    self.notes = ""
    self.ID = 0

    self.col_names = "ID - Operation - Operands - Description - Notes"

    self.data = ""

    self.arq_out.write(self.col_names + "\n")
    self.arq_out.write("------------------------------------------------" + "\n")
    
  def geration_table(self):
    data = str(self.ID) + " - " + self.operation + " - " + self.operands + " - " + self.description + " - " + self.notes +"\n"
    self.arq_out.write(data)
    self.ID += 1

  def print_table(self):
    with open('resp_semantic.txt') as file:
      file.seek(0, os.SEEK_END) # go to end of file
      if file.tell():
        print("Compile Error")
      else:
        with open("codgen.txt", 'r') as file:
          data = file.read()
        print(data)

  def opcode(self,op):
    #"<MAIS_MAIS>","<MENOSMENOS>"
    if "<MAIS>" in op:
      self.operation = "add"
    if "<MENOS>" in op:
      self.operation = "sub"
    if "<MULTIPLICAÇÃO>" in op:
      self.operation = "mul"
    if "<DIVISÃO>" in op:
      self.operation = "div"
    if "<MAIS_MAIS>" in op:
      self.operands += "," + self.operands
      self.operation = "add"
    if "<MENOS_MENOS>" in op:
      self.operands += "," + self.operands
      self.operation = "sub"
    if "<MAIOR>" in op:
      self.operation = "bne"
      self.gencode.operands = "temp,$zero,label"
    if "<MENOR>" in op:
      self.operation = "beq"
      self.gencode.operands = "temp,$zero,label"
    if "<ATRIBUIÇÃO>" in op:
      self.operation = "beq"