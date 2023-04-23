from math import gcd

alfabeto = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "á", "ã", "à", "â", "ç", "è", "é", "ê", "í", "ì", "ı", "ô", "õ", "ò", "ó", "ù", "ú", " ",
            '"', "'", "“", "‘", "!", "@", "#", "$", "%", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|",
            "<", ",", ">", ".", ":", ";", "?", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


def cripto(msg, senha):
    msg = msg.lower()
    msg_crypto = ""
    chave_cifra = keyStream(senha, len(msg))
    for posicao in range(len(msg)):
        posicao_alfabeto = int(alfabeto.index(msg[posicao]) + alfabeto.index(chave_cifra[posicao]))
        if (posicao_alfabeto > len(alfabeto)-1):
            posicao_alfabeto -= len(alfabeto)
        msg_crypto += alfabeto[posicao_alfabeto]
    return msg_crypto

def descrypto(msg_crypto, senha):
    msg = ""
    chave_cifra = keyStream(senha, len(msg_crypto))
    for posicao in range(len(msg_crypto)):
        posicao_msg = alfabeto.index(msg_crypto[posicao]) - alfabeto.index(chave_cifra[posicao])
        msg += alfabeto[posicao_msg]
    return msg

def keyStream(chave, tam_msg):
    chave = chave.lower()
    proporcao_msg_chave = int(tam_msg/len(chave))
    if (len(chave) < tam_msg):
        chave_cifra = chave * proporcao_msg_chave
        return chave_cifra + chave[:(tam_msg-len(chave_cifra))]
    else:
        return chave

def descryptoMsgSemChave(msg_crypto):
    msg_crypto = msg_crypto.lower()
    tamanho_chave = gcd(*frequenciaOcorrencias(msg_crypto))

def frequenciaOcorrencias(msg_crypto):
    frequencia_ocorrencias = dict()
    for x in range(1, len(msg_crypto)):
        contador = 0
        quentidade_ocorrencia = 0
        for i in range(x, len(msg_crypto)):
            if (msg_crypto[i] == msg_crypto[contador]):
                quentidade_ocorrencia += 1
            contador += 1
        frequencia_ocorrencias[x] = quentidade_ocorrencia
    return sorted(frequencia_ocorrencias.items(), key=lambda x: x[1], reverse=True)

def tamanhoChave(frequencia):
    linhas_mais_frequencia = list(sub[0] for sub in frequencia[:10])
    return gcd(*linhas_mais_frequencia)

msg = input()
senha = input()
msg_crypto = cripto(msg, senha)
msg_original = descrypto(msg_crypto, senha)
descryptoMsgSemChave(msg_crypto)