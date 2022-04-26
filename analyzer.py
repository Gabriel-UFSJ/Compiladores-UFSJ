import re
from rules import REGRAS



class Token: 
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "<{}> : {}".format(self.type, self.value)




class Analyzer:

    def __init__(self):
        self.REGEX = re.compile("|".join(self.appendGroups()))

    def compile(self, input):
        tokens = []
        for match in self.REGEX.finditer(input):
            if match.lastgroup == "SEPARADOR": # ao encontrar um separador continua
                continue
            tokens.append(Token(match.lastgroup, match.group(),))
        return tokens

    @staticmethod
    def appendGroups():
        newRules = []
        for type, regex, before, after in REGRAS:
            tokenRegex = "(?P<{}>{})".format(type, regex)
            if before is not None:
                tokenRegex = before + tokenRegex # antes + token
            if after is not None:
                tokenRegex += after # token + depois
            newRules.append(tokenRegex)
        return newRules