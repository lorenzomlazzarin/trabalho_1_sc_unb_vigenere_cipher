# -*- coding : utf-8 -*-
import random

class MillerRabin:
  keyLen: int

  def __init__(self, **kwargs) -> None:
    self.keyLen = kwargs.pop('keyLen', None)

  def __primality(self, n: int, t=2000) -> bool:  # Realiza o Teste de Fermat t vezes para o numero n
    t = n - 3 if t > n - 3 else t # o numero de tentativas nao pode exceder n -3
    s = 0
    m = n - 1
    div = divmod(m, 2)

    while div[1] == 0:  # encontra r e s de n -1= (2^s)m
      m = div[0]
      # if m == 0:
      #   break
      div = divmod(m, 2)
      s += 1

    r = []  # será a lista com os os restos da divisao sucessiva de m por 2
    while m > 0:  # encontra os r_1 de da conversao para base 2
      divisao = divmod(m, 2)
      m = divisao[0]  # faz m igual ao quaciente da divis ão de m por 2
      r.append(divisao[1])  # adiciona m mod 2 na lista r

    bases = []
    j = 0
    # cria uma lista com t numeros inteiros distintos petencentes intervalo [2 ,n -1[
    while j < t:
      # randrange (a,b) retorna um numero aleatorio dentro do intervalo [a,b[
      a_i = random.randrange(2, n - 1)
      if a_i not in bases:
        bases.append(a_i)
        j += 1

    for a in bases:
      e = a  # para nao alterar o valo de a, usei outra variavel com seu valor
      # como m é impar , r[0] sempre é 1 , sendo descencessario fazer e** r[0]
      y = a
      for expoente in r[1:]:  # calcula a^k mod n pelo algoritmo da reducao de custo de a^c mod n
        e = e ** 2 % n
        if expoente == 1:
          y = y * e % n
      if y != 1 and y != n - 1:
        i = 1
        while i <= s - 1 and y != n - 1:
          y = y ** 2 % n
          if y == 1:
            return False
          i += 1
        if y != n - 1:
          return False
    # se ao final de t testes , n não for como composto , dizemos que ele é primo
    return True

  def setBit(self, value, bit):
    '''
      Faz sets de bit para garantir que o número é impar. Move x bit.
    '''
    return (value | (1 << bit))

  def primeGenerate(self, **args) -> int:
    if args.get('keyLen'):
      self.keyLen = args.pop('keyLen')

    while True:
      # O método getrandbits retorna um inteiro com quantidade de bits especificada
      number = random.getrandbits(self.keyLen)
      prime = self.setBit(self.setBit(number, 0), self.keyLen-1)
      if self.__primality(prime):
        return prime



if __name__ == '__main__':
  miller_rabin = MillerRabin(keyLen=1024)

  print("p = %d" % miller_rabin.primeGenerate())
  print("q = %d" % miller_rabin.primeGenerate())

