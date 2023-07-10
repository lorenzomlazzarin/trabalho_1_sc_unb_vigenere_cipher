# -*- coding : utf-8 -*-

import base64
from millerRabin import MillerRabin
import hashlib
import random

class RSA(MillerRabin):
  kU: tuple
  kR: tuple
  DEFAULT_SIZE_PADDING = 512
  oaep_send = {'hashPart1': str(), 'hashNonce': str()}
  oaep_receive = {'hashPart1': str(), 'hashNonce': str()}

  def __init__(self, **kwargs) -> None:
    super().__init__(**kwargs)

  def __coprime(self, n1, n2) -> bool:
    while True:
      n1, n2 = n2, n1 % n2
      if n2 == 0:
        break
    return n1 == 1

  def generateKeys(self) -> None:
    '''
      Geração de duas chaves criptográficas, uma chave pública e uma privada.
    '''
    # Selecionar dois números primos p e q grandes
    p = self.primeGenerate()
    while True:
      q = self.primeGenerate()
      if q != p:
        break

    # Calculo do valor de n, tal qual  n = p * q
    n = p * q

    # Calculo do phi = (p-1) * (q-1)
    phi = (p-1) * (q-1)

    # Calcular “e” tal que: 1 < e < phi(n); “e” é coprimo com N e phi(n)
    e = random.randrange(1, phi)
    g = self.__coprime(e, phi)
    while g != 1:
      e = random.randrange(1, phi)
      g = self.__coprime(e, phi)

    # Selecionar um inteiro “d” relativamente primo à phi, sendo  d*e(mod phi(n)) = 1
    d = pow(e, -1, phi)

    # A chave pública definida pela dupla “e” e “n”, sendo KU = {e, n}
    # A chave privada é definida pela dupla “d” e “n”, sendo KR = {d, n}
    self.kU = (e, n)
    self.kR = (d, n)

  def __XOR(self, str1, str2) -> str:
    '''
      Realiza OR exclusivo (XOR) por cada caracter das strings
    '''
    def normalize(str1: str, str2: str) -> tuple:
      return (str1, ((len(str1) - len(str2))*'0')+str2) if len(str1) > len(str2) else (((len(str2) - len(str1))*'0')+str1, str2)

    str1Num, str2Num = normalize(str1, str2)
    return ''.join([str(ord(str1Num[i]) ^ ord(str2Num[i])) for i in range(len(str1Num))])

  def __strToByte(self, string) -> bytes:
    '''
      Transforma binário string em bytes.
    '''
    return int(string, 2).to_bytes((len(string)+7)//8, byteorder='big')

  def __bitStrToBytes(self, s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

  def toBase64(self, message: str) -> str:
    return str(base64.b64encode(message.encode('utf-8')))[2:-1]

  def oaep(self, message) -> int:
    '''
      Optimal asymmetric encryption padding
      * Usa o padrão OAER, e concatena a mensagem M com um nonce aleatório N e o usando em função hash para combiná-los.
      * Calcúlo do hash em da mensagem em claro
    '''
    # Gerar aleatoriamente uma string de bits de tamanho adequado para ser usada como "seed".
    nonce_bits = bin(random.getrandbits(self.DEFAULT_SIZE_PADDING))[2:]  # seed

    # Padding inicial da mensagem para 256 bits
    message_binary = ''.join([format(ord(i), '08b') for i in message])
    padded_message = message_binary + ((int(self.DEFAULT_SIZE_PADDING/2)-len(message_binary))*'0')

    # Parte 1
    # Calculo do hash do Nonce a partir dos bits nonce_bits, e já retorna em hexadecimal
    nonce_hash = int(hashlib.sha3_256(self.__strToByte(nonce_bits)).hexdigest(), 16)
    self.oaep_send['hashNonce'] = self.toBase64(str(nonce_hash))
    # Converte a string para bits usando a função format
    nonce_hash = format(nonce_hash, '0>256b')
    # Executa o XOR (OR exclusivo) da mensagem com o nonce_hash
    part1 = self.__XOR(padded_message, nonce_hash)

    # Parte 2
    # Calculo do hash part1_hash a partir da part1, e já retorna em hexadecimal
    part1_hash = int(hashlib.sha3_512(self.__strToByte(part1)).hexdigest(), 16)
    self.oaep_send['hashPart1'] = self.toBase64(str(part1_hash))
    # Converte de string para bits usando a função format
    part1_hash = format(part1_hash, '0>512b')
    # Executa o XOR do nonce com o hash da parte 1
    part2 = self.__XOR(nonce_bits, part1_hash)

    # Retorno da concatenacao de parte 1 e parte 2 já na base 2
    return int(part1 + part2, 2)

  def reverseOaep(self, message) -> str:
    '''
      Optimal asymmetric encryption padding reverse
      * Realiza o processo inverso do oaep. Quebra a mensagem com padding em dois, e faz o calculo dos hashes.
    '''

    # Mensagem em binário mais o padding
    message_bin = bin(message)[2:]
    message_bin_padding = ((int(self.DEFAULT_SIZE_PADDING/2) + self.DEFAULT_SIZE_PADDING - len(message_bin))*'0') + message_bin

    # Separa a mensagem em duas partes, assim como no processo de aplicação do oaep
    part1 = message_bin_padding[:int(self.DEFAULT_SIZE_PADDING/2)]
    part2 = message_bin_padding[int(self.DEFAULT_SIZE_PADDING/2):]

    # Calculo do hash hash_part1 usando part1, e já retona em hexadecimal
    hash_part1 = int(hashlib.sha3_512(self.__bitStrToBytes(part1)).hexdigest(), 16)
    self.oaep_receive['hashPart1'] = self.toBase64(str(hash_part1))
    # Conversao do hash_part1 para string de bits usando a função format
    hash_part1 = format(hash_part1, '0>512b')
    # Nonce obtido pelo XOR (OR exclusivo) da parte2 com o hash hash_part1
    nonce = self.__XOR(part2, hash_part1)

    # Calculo do hash hash_nonce usando o nonce, e já retorno em hexadecimal
    hash_nonce = int(hashlib.sha3_256(self.__bitStrToBytes(nonce)).hexdigest(), 16)
    self.oaep_receive['hashNonce'] = self.toBase64(str(hash_nonce))
    # Conversão do hash_nonce para string de bits
    hash_nonce = format(hash_nonce, '0>256b')
    # A mensagem é obtida pelo XOR da parte1 com o hash hash_nonce
    message_bits = self.__XOR(part1, hash_nonce)

    # Retorna os bits da mensagem após o processo de inversão
    return message_bits[:self.DEFAULT_SIZE_PADDING]

  def __encoderFunction(self, m):
    return (m**self.kU[0]) % self.kU[1]

  def __decoderFunction(self, c):
    return (c**self.kR[0]) % self.kR[1]

  def encoder(self, message: str, oaep=True) -> str:
    '''
      * A encriptação da mensagem consiste em elevar o valor inteiro da mensagem pelo padrão oaep à chave pública kU.
      * Assinatura da mensagem quando é utilizado o oaep, ou seja, cifração do hash da mensagem.
    '''
    return_ = []

    if oaep:
      # Preenchimento da mensagem clara com OAEP. O preenchimento adiciona aleatoriedade e garante que a mensagem cifrada tenha um tamanho fixo
      pedding_message = self.oaep(message)

      # Retorna a mensagem cifrada.
      try:
        return_ = [chr(self.__encoderFunction(int(m))) for m in str(pedding_message)]
      except ValueError:
        return '\n\n\n\t\t\tERRO NO PROCESSAMENTO!\n\n\n'
    else:
      # Encriptação sem usar o padding OAEP
      return_ = [chr(self.__encoderFunction(ord(m))) for m in message]

    return ''.join(return_)

  def decoder(self, coderMessage) -> str:
    '''
      A desencriptação da mensagem consiste em elevar o valor inteiro da mensagem pelo padrão oaep à chave priváda kR.
    '''
    # Decodificar a mensagem cifrada usando a chave privada
    decoder_message = [int(self.__decoderFunction(ord(c))) for c in coderMessage]
    decoder_message = int(''.join([str(i) for i in decoder_message]))

    # Processo de inverso do preenchimento da mensagem clara com OAEP.
    bits = self.reverseOaep(decoder_message)

    # Retorna a conversão dos bits para string
    return ''.join([chr(int(bits[i: i+8], 2)) for i in range(0, len(bits), 8)])




if __name__ == '__main__':
  ras = RSA(keyLen=8)
  message = "Teste 123"

  print('Message: ', message, '\n')

  print('Chaves:')
  ras.generateKeys()
  print('\tkU: ', ras.kU)
  print('\tkR: ', ras.kR)

  print('\nEncoder message: ', end='')
  encode_message = ras.encoder(message)
  # print(encode_message)
  print(ras.toBase64(encode_message))


  print('\nDencoder message: ', end='')
  decode_message = ras.decoder(encode_message)
  print(decode_message)

  print('oaep_send ->', ras.oaep_send)
  print('oaep_receive ->', ras.oaep_receive)

  if ras.oaep_send['hashPart1'] == ras.oaep_receive['hashPart1'] and ras.oaep_send['hashNonce'] == ras.oaep_receive['hashNonce']:
    print('\t\t>>> Assinatura pode ser confirmada!')
  else:
    print('\t\t>>> ERROR: Assinatura NÃO pode ser confirmada!')
