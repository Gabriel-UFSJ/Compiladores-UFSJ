# Rules :
# [
#     (TIPO , REGEX , ANTES , DEPOIS)
# ]

MATCH_UNTIL_SEQ = r"(?:(?=%s))"
UNTIL_SPACE = MATCH_UNTIL_SEQ % r"\s"
UNTIL_SPACE_OR_SEMICOLON = MATCH_UNTIL_SEQ % r"\s|\;"
UNTIL_SPACE_OR_COLON = MATCH_UNTIL_SEQ % r"\s|\:"

REGRAS = [
    ("BREAK", r"break", None, UNTIL_SPACE_OR_SEMICOLON),
    ("BOOL", r"bool", None, UNTIL_SPACE),
    ("CASE", r"case", None, UNTIL_SPACE),
    ("CHAR", r"char", None, UNTIL_SPACE),
    ("CONST", r"const", None, UNTIL_SPACE),
    ("ELSE", r"else", None, None),
    ("ENUM", r"enum", None, UNTIL_SPACE),
    ("FLOAT", r"float", None, UNTIL_SPACE),
    ("FOR", r"for", None, None),
    ("IF", r"if", None, None),
    ("INT", r"int\s", None, None),
    ("RETURN", r"return", None, None),
    ("PRINTF", r"printf", None, None),
    ("SCANF", r"scanf", None, None),
    ("PONTEIRO", r"\&", None, None),
    ("SWITCH", r"switch", None, None),
    ("VOID", r"void", None, None),
    ("WHILE", r"while", None, None),
    ("ID", r"[a-zA-Z]\w*", None, None),
    ("INT_LITERAL", r"\d+", None, MATCH_UNTIL_SEQ % r"\s|\+|\-|\*|\;|$|\)"),
    ("FLOAT_LITERAL", r"\d*\.?\d+", None, MATCH_UNTIL_SEQ % r"\s|\+|\-|\*|\;|$|\)"),
    ("STRING_LITERAL", r'\".*\"', None, None),
    ("CHAR_LITERAL", r"\'.?\'", None, None),
    ("ABRE_CHAVE", r"\{", None, None), # {
    ("FECHA_CHAVE", r"\}", None, None), # }
    ("ABRE_COLCHETE", r"\[", None, None), # [
    ("FECHA_COLCHETE", r"\]", None, None), # ]
    ("ABRE_PARENTESES", r"\(", None, None), # (
    ("FECHA_PARENTESES", r"\)", None, None), # )
    ("VIRGULA", r"\,", None, None), # ,
    ("PONTO_VIRGULA", r"\;", None, None), # ;
    ("PONTO", r"\.", None, None), # .
    ("NOT", r"\!", None, None), # !
    ("ATRIBUIÇÃO", r"\=", None, None), # =
    ("HASHTAG", r"\#", None, None), # #
    ("BARRA_INVERTIDA", r"\\", None, None), # \
    ("MAIS_MAIS", r"\+\+", None, None), # ++
    ("MENOS_MENOS", r"\-\-", None, None), # --
    ("MENOS", r"\-", None, None), # -
    ("MAIS", r"\+", None, None), # +
    ("MULTIPLICAÇÃO", r"\*", None, None), # *
    ("DIVISÃO", r"\/[^\/]", None, None),# /
    ("PORCENTAGEM", r"\%", None, None), # %
    ("MAIOR", r"\>", None, None), # >
    ("MENOR", r"\<", None, None), # <
    ("MAIOR_IGUAL", r"\>\=", None, None), # >=
    ("MENOR_IGUAL", r"\<\=", None, None), # =<
    ("IGUAL", r"\=\=", None, None), # ==
    ("DIFERENTE", r"\!\=", None, None), # != 
    ("AND", r"\&\&", None, None), # Operador logico &&
    ("OR", r"\|\|", None, None), # Operador logico ||
    ("COMENT_MULTI", r"\/\*.*\*\/", None, None), # Comentario de várias linhas
    ("COMENT_LINHA", r"\/\/.*", None, None), # Comentario de 1 linha
    ('SEPARADOR', r'[ \t]+', None, None),  # Separadores
    ("ERRO_LEXICO", r".+\s", None, None), # Erro léxico
]