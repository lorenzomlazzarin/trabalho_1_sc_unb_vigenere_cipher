import secrets

################################################### variaveis ##########################################################

s_box = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

############################################## funções crifrar #########################################################

#gera chave 16 bytes ou 128 bits
def gerador_chave():
    return secrets.token_bytes(16)

#dividi o texto em bytes em blocos de 128 bits e adiciona um incrimento no final caso o ultimo elemento não tenha esse
# tamanho.
def dividir_blocos_16_bytes(texto_bytes):
    lista_bytes = [texto_bytes[i:i + 16] for i in range(0, len(texto_bytes), 16)]
    tamanho = len(lista_bytes[len(lista_bytes)-1])
    if tamanho < 16:
        incremento = b"|" * (16 - tamanho)
        lista_bytes[len(lista_bytes) - 1] = lista_bytes[len(lista_bytes) - 1] + incremento
    return lista_bytes

def galois_counter(counter):
    r = (counter & 0x80)  # Verifica se o bit mais significativo é 1
    counter = (counter << 1) & 0xFF  # Desloca o contador para a esquerda e descarta o bit mais significativo
    if r != 0:
        counter ^= 0x1B  # Realiza a operação XOR com o polinômio irreducível (0x1B) em Galois
    return counter

def expancao_chave(chave, counter=0):
    round_constants = [1, 2, 4, 8, 16, 32, 64, 128, 27, 54]
    palavras = [chave[i:i + 4] for i in range(0, len(chave), 4)]

    for i in range(4, 44):
        if i % 4 == 0:
            # Atualiza o contador em Galois
            counter = galois_counter(counter)

            palavra = palavras[i-1]
            palavra = [palavra[1], palavra[2], palavra[3], palavra[0]]  # Rotacionar palavra
            palavra = [s_box[b] for b in palavra]  # Substituir usando S-Box
            palavra[0] ^= round_constants[i//4 - 1] ^ counter  # Realizar XOR com constante de rodada e contador
        else:
            palavra = [a ^ b for a, b in zip(palavras[i-4], palavras[i-1])]  # Realizar XOR com palavra anterior

        palavras.append(palavra)

    subchaves = []
    for i in range(0, 44, 4):
        try:
            juncaobytes = b''.join(palavras[i:i + 4])
        except:
            lista = palavras[i:i + 4]
            for t in range(4):
                lista[t] = bytes(lista[t])
            juncaobytes = b''.join(lista)

        subchaves.append(juncaobytes)

    return subchaves


def add_round_key(blocos_16, chave):
    msg_cifrada = []
    for t in range(len(blocos_16)):
        msg_cifrada.append(bytes([blocos_16[t][i] ^ chave[i] for i in range(16)]))
    return msg_cifrada

def sub_bytes (blocos_16):
    bloco_nova_mensagem = []
    for t in range(len(blocos_16)):
        nova_mensagem = []
        for i in range(len(blocos_16[t])):
            nova_mensagem.append(s_box[blocos_16[t][i]])
        bloco_nova_mensagem.append(bytes(nova_mensagem))
    return bloco_nova_mensagem

def shift_rows_alt(blocos_16):
    blocos_novos = []
    posicao = {1:5, 2:10, 3:15, 4:8, 6:14, 7:11, 9:13}
    for bloco in blocos_16:
        bloco = bytearray(bloco)
        for i in posicao:
            bloco[i], bloco[posicao[i]] = bloco[posicao[i]], bloco[i]
        blocos_novos.append(bytes(bloco))
    return blocos_novos

def mix_columns(blocks):
    mixed_blocks = []
    for block in blocks:
        mixed_block = bytearray(block)
        for i in range(0, 16, 4):
            a = mixed_block[i]
            b = mixed_block[i + 1]
            c = mixed_block[i + 2]
            d = mixed_block[i + 3]

            mixed_block[i] = ((2 * a) ^ (3 * b) ^ c ^ d) & 0xFF
            mixed_block[i + 1] = (a ^ (2 * b) ^ (3 * c) ^ d) & 0xFF
            mixed_block[i + 2] = (a ^ b ^ (2 * c) ^ (3 * d)) & 0xFF
            mixed_block[i + 3] = ((3 * a) ^ b ^ c ^ (2 * d)) & 0xFF

        mixed_blocks.append(bytes(mixed_block))
    return mixed_blocks

def cifrador(texto_bytes, lista_chaves):
    bloco_16 = dividir_blocos_16_bytes(texto_bytes)
    block = add_round_key(bloco_16, lista_chaves[0])

    for i in range(10):
        block = sub_bytes(block)
        block = shift_rows_alt(block)
        if (i == 9):
            block = mix_columns(block)
        block = add_round_key(block, lista_chaves[i + 1])

    return b''.join(block)

############################################# funções decifrar #########################################################


########################################################################################################################
################################################# Interface Usuario ####################################################
########################################################################################################################

if (int(input("1- texto já gravado\n2- digitar texto\n")) == 2):
    texto_input_bytes = bytes(input("Digite aqui o texto a ser criptografado:\n"), 'utf-8')
else:
    texto_input_bytes = b'0123456789abcdefghijklmno'

chave_gerada = gerador_chave()
subchaves = expancao_chave(chave_gerada)

texto_cifrado = cifrador(texto_input_bytes, subchaves)

print("Chave gerada:", chave_gerada)
print("Chaves da expanção:", subchaves)
print("Texto cifrado:", texto_cifrado)

texto_decifrado = "a"
