from math import gcd

alfabeto = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "á", "ã", "à", "â", "ç", "è", "é", "ê", "í", "ì", "ı", "ô", "õ", "ò", "ó", "ù", "ú", " ",
            '"', "'", "“", "‘", "!", "@", "#", "$", "%", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|",
            "<", ",", ">", ".", ":", ";", "?", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

probabilidade_pt = {"a":14.63, "b":1.04, "c":3.88, "d":4.99, "e":12.57, "f":1.02, "g":1.30, "h":1.28, "i":6.18, "j":0.40, "k":0.02, "l":2.78, "m":4.74, "n":5.05, "o":10.73, "p":2.52, "q":1.20, "r":6.53, "s":7.81, "t":4.34, "u":4.63, "v":1.67, "w":0.01, "x":0.21, "y":0.01, "z":0.47}
probabilidade_en = {"a":8.167, "b":1.492, "c":2.782, "d":4.253, "e":12.702, "f":2.228, "g":2.015, "h":6.094, "i":6.966, "j":0.153, "k":0.772, "l":4.025, "m":2.406, "n":6.749, "o":7.507, "p":1.929, "q":0.095, "r":5.987, "s":6.327, "t":9.056, "u":2.758, "v":0.978, "w":2.360, "x":0.150, "y":1.974, "z":0.074}

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
    palavra = ""
    msg_crypto = msg_crypto.lower()
    tamanho_chave = tamanhoChave(frequenciaOcorrencias(msg_crypto))
    lista_porcentagens = descobrindoPorcentagemLetra(msg_crypto, tamanho_chave)


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

def descobrindoPorcentagemLetra(msg_crypto, tamanho_chave):
    lista_ocorrencia_letras = []
    for i in range (len(msg_crypto)):
        posicao = i % tamanho_chave
        if posicao >= len(lista_ocorrencia_letras):
            lista_ocorrencia_letras.append([msg_crypto[i]])
        else:
            lista_ocorrencia_letras[posicao].append(msg_crypto[i])

    lista_ocorrencia_letras_porcentagem = []
    for t in lista_ocorrencia_letras:
        letra_ocorrencia = {}
        lista_sem_duplicados = list(set(t))
        for k in lista_sem_duplicados:
            # apagar esse if
            if alfabeto.index(k) <=25:
                letra_ocorrencia[k] = (t.count(k)/len(t))*100
        lista_ocorrencia_letras_porcentagem.append(dict(sorted(letra_ocorrencia.items(), key=lambda x: x[0])))
        print(lista_ocorrencia_letras_porcentagem)

msg = input()
senha = input()
print("Digite o número da opção vc escolhe?\n1- pt (portugues)\n2- en (ingles)")
linguagem = int(input())
msg_crypto = cripto(msg, senha)
msg_original = descrypto(msg_crypto, senha)
descryptoMsgSemChave(msg_crypto)