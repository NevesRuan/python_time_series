# ----------------------------------------------------------------------------
# Script: cadeira_preto.py
# Created By: Ruan Neves
# Created Date: 2025-08-25
# Version: 1.0
# ---------------------------------------------------------------------------


# Cabeçalho do arquivo:
# é a parte inicial de um script Python, composta geralmente por comentários 
# e informações adicionais como autor, data, licença, propósito do código ou 
# até instruções especiais Ele não faz parte da execução do código em si, mas
# serve para organização, padronização e metadados que ajudam outros
# desenvolvedores ou  o sistema operacional a entender como rodar o arquivo.


""" 
Docstring:
é uma string de documentação colocada logo após a definição de módulos, funções, 
classes ou métodos, escrita entre aspas triplas (`""" """`). Diferente do 
cabeçalho, ela é interpretada pelo Python e pode ser acessada em tempo de 
execução (`.__doc__` ou `help()`). Sua função é explicar de forma estruturada 
o que o código faz, quais parâmetros recebe, o que retorna e outras instruções, 
sendo essencial para documentação oficial e geração automática de guias do programa.
"""


# parabéns... muito boa resposta


######################################################################

# implemente as funções abaixo e coloque as docstrings

def maximo(nums):

     # TODO: percorra a lista guardando o maior atual

    """ retorna o maior numero em uma lista (usando loop for)
    percorre a lista manualmente para encontrar o maior valor """

    maior = nums[0]
    for num in nums:
        if num > maior:
            maior = num
    return maior

# exemplo para verificacao da funcao
lista = [10,2,3,1,5,23] 
print({maximo(lista)})

    # """ retorna o maior numero em uma lista (usando funcao interna)
    # metodo mais eficiente """"

    #  if not nums:
    #      return None
        
    #  return max(nums)

## exemplo para verificacao da funcao
# lista = [10,2,3,1,5]
# print({maximo(lista)})


def e_par(n: int) -> bool:

    # TODO: retorne se n é par

    """ verifica se um numero e par (usando operador de modulo %)
    retorna True se for par e False se for impar. """

    return n % 2 == 0

## exemplo para verificacao da funcao
print(e_par(1)) #retorna false
print(e_par(2)) #retorna true


def fatorial(n: int) -> int:

    # TODO: implemente de forma iterativa (sem recursão)

        """   calcula o fatorial de um numero (usando loop for)
        metodo iteratico sem utilizacao de recursao """

        #erro caso usuario tente inserir numero negativo em fatorial, pois fatorial nao e definido para numeros negativos
        if n < 0:
             raise ValueError ("fatorial nao aceita numeros negativos.") #professor fiquei com uma duvida na hora de mostrar o erro, 
                                                                         #sempre que executo com o raise, ele retorna a linha de codigo com um Traceback mostrando o local do 
                                                                         #erro, tentei fazer sem o raise apenas com um print e um break ele fala que nao pode dar break fora de 
                                                                         #um loop, e o exit apenas é ignorado. tem alguma outra forma de fazer essa saida do codigo sem o raise?
                                                                         #(apenas para um melhor visual no retorno mesmo)

        #fatorial de 0 e 1
        if n == 0:
             return 1
        res = 1

        #multiplica o resultado ate o valor de n para retornar o fatorial
        for i in range(1, n + 1):
            res *= i
        
        return res

## exemplo para verificacao da funcao
num = -10
print({fatorial(num)}) #retornar erro, numero negativo
num = 10
print({fatorial(num)}) #retorna 3628800, fatorial de 10

import re
def limpa_texto(s: str) -> str:

    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_

        """ limpa string de texto (usando regex)
        converte texto para minusculo e remove pontuacoes"""

        #converte string para minusculo
        txt_minusculo = s.lower()

        #substitui a pontuacao com o re.sub (r no comeco para String Raw)
        txt_limpo = re.sub(r'[,\.;:!?\'"()-_]', '', txt_minusculo)

        return txt_limpo

## exemplo para verificacao da funcao
txt = "TeSSSSte!"
print (txt) #texto original
print (limpa_texto(txt)) #texto limpo

def conta_vogais(s: str) -> int:

     # TODO: conte as vogais simples

    """ recebe uma string e retorna quantidade de vogais (utilizando loop for)"""

    vogais = "AaEeIiOoUu"
    contador = 0

    #loop for, verifica cada char da strin, caso o char e uma vogal contador aumenta 1.
    for char in s:
        if char in vogais:
            contador += 1
    
    return contador

## exemplo para verificacao da funcao
txt = "frAse ExemplO"
print (txt) #txt original
print (conta_vogais(txt)) #contagem de vogais em txt

def palindromo(s: str) -> bool:

    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso

    """ verifica se a string e um palindromo (ignora maiusculas/minusculas, espacos e pontuacoes)
    retrna True se for palindromo e False caso nao"""

    txt_normalizado = ""

    #percore cada char na string original (convertida para minusculas), isalnum retorna true se o char for alfanumerico, e apenas os adiciona a nova string
    for char in s.lower():
         if char.isalnum():
              txt_normalizado += char
    
    #utiliza o [::1] para criar um copia invertida da string, e retorna True se as frases forem iguais, e false caso nao.
    return txt_normalizado == txt_normalizado [::-1]

## exemplo para verificacao da funcao
txt = "_A base do teto desaba?."
txt_1 = "nao e um palindromo"

print (palindromo(txt)) #retorna true, pois e um palindromo
print (palindromo(txt_1)) #retorna false, pois nao e um palindromo