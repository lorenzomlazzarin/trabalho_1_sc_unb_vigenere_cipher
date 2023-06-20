import secrets

#gera chave 16 bytes ou 128 bits
def gerador_chave():
    return secrets.token_bytes(16)

#dividi o texto em bytes em blocos de 128 bits e adiciona um incrimento no final caso não tenha esse tamanho o ultimo
# elemento
def dividir_blocos_128_bits(texto_bytes):
    lista_bytes = [texto_bytes[i:i + 128] for i in range(0, len(texto_bytes), 128)]
    tamanho = len(lista_bytes[len(lista_bytes)-1])
    if tamanho < 128:
        incremento = "|" * (128 - tamanho)
        lista_bytes[len(lista_bytes) - 1] = lista_bytes[len(lista_bytes) - 1] + bytes(incremento, 'utf-8')
    return lista_bytes

########################################################################################################################
################################################# Interface Usuario ####################################################
########################################################################################################################

# parte 1
chave_gerada = gerador_chave()
texto_base = input("Digite aqui o texto a ser criptografado:\n")
texto_bytes = bytes(texto_base, 'utf-8')
blocos_128 = dividir_blocos_128_bits(texto_bytes)
print(chave_gerada)
print(texto_bytes)
print(blocos_128)