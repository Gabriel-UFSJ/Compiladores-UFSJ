# Compiladores-UFSJ
Aluno: Gabriel Resende Meireles
Usando regex e python

# Sobre
Para compilar digite no terminal: python main.py
Requer instalado: Python

# Tokens Aceitos
```c
"BREAK","BOOL","CASE","CHAR","CONST","ELSE","ENUM","FLOAT","FOR","IF","INT","RETURN","PRINTF","SCANF","PONTEIRO","SWITCH","VOID","WHILE","ID","INT_LITERAL","FLOAT_LITERAL","STRING_LITERAL","CHAR_LITERAL","ABRE_CHAVE","FECHA_CHAVE","ABRE_COLCHETE","FECHA_COLCHETE","ABRE_PARENTESES","FECHA_PARENTESES","VIRGULA","PONTO_VIRGULA","PONTO","NOT","ATRIBUIÇÃO","HASHTAG","BARRA_INVERTIDA","MAIS_MAIS","MENOS_MENOS","MENOS","MAIS","MULTIPLICAÇÃO","DIVISÃO","PORCENTAGEM","MAIOR","MENOR","MAIOR_IGUAL","MENOR_IGUAL","IGUAL","DIFERENTE","AND","OR","COMENT_MULTI","COMENT_LINHA","SEPARADOR","ERRO_LEXICO"
````

```c
//teste.c
int main() {
  int t1 = 0 , t2 = 1 , nextTerm = 0 , n;
  printf("Enter a positive number: ");
  scanf("%d", &n);

  // displays the first two terms which is always 0 and 1
  printf("Fibonacci Series: %d, %d, ", t1, t2);
  nextTerm = t1 + t2;

  while (nextTerm <= n) {
    printf("%d, ", nextTerm);
    t1 = t2;
    t2 = nextTerm;
    nextTerm = t1 + t2;
  }

  return 0;
}
```
# Saída
```c
<INT> : int 
<ID> : main
<ABRE_PARENTESES> : (
<FECHA_PARENTESES> : )
<ABRE_CHAVE> : {
<INT> : int 
<ID> : t1
<ATRIBUIÇÃO> : =
<INT_LITERAL> : 0
<VIRGULA> : ,
<ID> : t2
<ATRIBUIÇÃO> : =
<INT_LITERAL> : 1
<VIRGULA> : ,
<ID> : nextTerm
<ATRIBUIÇÃO> : =
<INT_LITERAL> : 0
<VIRGULA> : ,
<ID> : n
<PONTO_VIRGULA> : ;
<PRINTF> : printf
<ABRE_PARENTESES> : (
<STRING_LITERAL> : "Enter a positive number: "
<FECHA_PARENTESES> : )
<PONTO_VIRGULA> : ;
<SCANF> : scanf
<ABRE_PARENTESES> : (
<STRING_LITERAL> : "%d"
<VIRGULA> : ,
<PONTEIRO> : &
<ID> : n
<FECHA_PARENTESES> : )
<PONTO_VIRGULA> : ;
<COMENT_LINHA> : // displays the first two terms which is always 0 and 1
<PRINTF> : printf
<ABRE_PARENTESES> : (
<STRING_LITERAL> : "Fibonacci Series: %d, %d, "
<VIRGULA> : ,
<ID> : t1
<VIRGULA> : ,
<ID> : t2
<FECHA_PARENTESES> : )
<PONTO_VIRGULA> : ;
<ID> : nextTerm
<ATRIBUIÇÃO> : =
<ID> : t1
<MAIS> : +
<ID> : t2
<PONTO_VIRGULA> : ;
<WHILE> : while
<ABRE_PARENTESES> : (
<ID> : nextTerm
<MENOR> : <
<ATRIBUIÇÃO> : =
<ID> : n
<FECHA_PARENTESES> : )
<ABRE_CHAVE> : {
<PRINTF> : printf
<ABRE_PARENTESES> : (
<STRING_LITERAL> : "%d, "
<VIRGULA> : ,
<ID> : nextTerm
<FECHA_PARENTESES> : )
<PONTO_VIRGULA> : ;
<ID> : t1
<ATRIBUIÇÃO> : =
<ID> : t2
<PONTO_VIRGULA> : ;
<ID> : t2
<ATRIBUIÇÃO> : =
<ID> : nextTerm
<PONTO_VIRGULA> : ;
<ID> : nextTerm
<ATRIBUIÇÃO> : =
<ID> : t1
<MAIS> : +
<ID> : t2
<PONTO_VIRGULA> : ;
<FECHA_CHAVE> : }
<RETURN> : return
<INT_LITERAL> : 0
<PONTO_VIRGULA> : ;
<FECHA_CHAVE> : }
```
# Fontes
https://regexr.com/

https://www.w3schools.com/python/python_regex.asp

https://www.programiz.com/python-programming/regex

http://www.mit.edu/people/amliu/vrut/python/ref/ref-4.html

