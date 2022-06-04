import re
from rules import RULES

lastcolum = 0

class Token: 
    def __init__(self, type, value,line, colum):
      self.type = type
      self.value = value
      self.line = line
      self.colum = colum

    def __str__(self):
        return "<{}> : {} => {}:{}".format(self.type, self.value, self.line, self.colum)

class lexical:
    
    def __init__(self):
        self.REGEX = re.compile("|".join(self.appendGroups()))

    def compile(self, input):
        tokens = []
        lastcolum = 0
        line = 1
        colum = 0
        for match in self.REGEX.finditer(input):
            if(match.span()[0] != lastcolum):
              line +=1
              colum = 0
            colum += (match.span()[1] - match.span()[0])
            lastcolum = match.span()[1]
            if match.lastgroup == "SEPARADOR": # ao encontrar um separador continua
              continue
            tokens.append(Token(match.lastgroup, match.group(), line, colum,))
        return tokens

    @staticmethod
    def appendGroups():
        newRules = []
        for type, regex, before, after in RULES:
            tokenRegex = "(?P<{}>{})".format(type, regex)
            if before is not None:
                tokenRegex = before + tokenRegex # antes + token
            if after is not None:
                tokenRegex += after # token + depois
            newRules.append(tokenRegex)
        return newRules