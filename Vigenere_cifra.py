from math import gcd

alfabeto = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "á", "ã", "à", "â", "ç", "è", "é", "ê", "í", "ì", "ı", "ô", "õ", "ò", "ó", "ù",
            "ú", " ", '”', '"', "'", "“", "‘", "!", "@", "#", "$", "%", "&", "*", "(", ")", "_", "-", "+", "=", "{",
            "[", "}", "]", "|", "<", ",", ">", ".", ":", ";", "?", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8",
            "9")

alfabeto_decifrando_sem_chave = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                                 "r", "s", "t", "u", "v", "w", "x", "y", "z")

msg_teste1 = """rvgllakieg tye tirtucatzoe.  whvnvvei i
winu mpsecf xronieg giid abfuk thv mfuty; wyenvvvr ik ij a drmg,
drzzqly eomemsei in dy jouc; wyenvvvr i wied mpsvlf znmollnkarzlp
palszng seworv cfffzn narvhfusvs, rnd srzngznx up khv rerr ff emeiy
flnvrac i deek; aed ejpvcirlcy wyeeevvr dy hppfs gvt jucy ae upgei
haed ff mv, tyat zt ieqliies r skroeg dorrl grieczplv tf prvvvnt de
wrod dvliseiatvlp stvpginx ieto khv stievt, aed detyouicrlcy keotkieg
geoglv's hrtj ofw--tyen, z atcolnk it yixh tzmv to xek to jer as jofn
aj i tan.  khzs ij mp susskitltv foi pzstfl rnd sacl.  wzty a
pyicosfpyicrl wlolrzsh tako tyrfws yidsecf lpoe hzs snoid; i huzetcy
kakv tf thv syip.  khvre zs eotyieg slrgrijieg ie tyis.  zf khep blt
keen it, rldosk acl mvn zn tyezr dvgiee, jode tzmv or ftyer, thvrijh
merp nvarcy khe jade fvecinxs kowrrus tye fcern nity mv."""

msg_teste2 = "tpsja kexis ttgztpb wq ssmil tfdxf vsetw ytafrttw btzf pcbroxdzo zn tqac wix, bwfd s, je ahvup sd " \
             "pcbqqxff lfzed d avu ytwoxavneh sg p aznst qaghv. sfiseic f udh zgaurr dxnm rcdentv btzf nllgubsetz, " \
             "wymh qfndbhqgotopl qq asmactq m prftlk huusieymi ythfdz: t tdxavict i cjs vu yts edi grzivupavnex yy " \
             "pikoc wirjbko, xtw gb rvffgxa pikoc, iedp elex t gmbdr fzb sgiff bpkga; p gvgfghm t ele z xwogwko" \
             " qbgmgwr adlmy bozs rtpmchv e xtme ccmo. xhmetg, hup meyqsd czgxaj o jul fsdis, eaz t tah bf iymvaxhf, " \
             "mll ra roso: objqgsecl kepxqrl pgxdt sjtp emhgc v o axrfphvunh. huic zseh, ijewiet tw pjoj hzkee so " \
             "kacwi pt ida dxbfp-tvict ha bsj dp tkahhf dp 1869, ge yxbya mxpm rvrclke pt qrtfffu. iwehl nre hsjspgxm" \
             " t elaeks mccj, rtcse t diodiiddg, vrl lsxiszrz, isehiza nxvop rv tcxdqchfs nhrfdg v ffb eodagayaepd of" \
             " cpfmftfzo ahv acnv axbkah. cezp tquvcj! vpkhmss v qfx rmd vfugx gmghrs yxq mciecthw. mrfvsnx ugt " \
             "qyogbe — btbvictzm jar csnzucvr mtnhm, ifzsex i odbjtlgxq, iof czgwfpbke p mea ifzsex, ugt zvvzn yy " \
             "sohupeie uwvid we gahzml asdp o znexvopzrr plxm tbxeyasep wuett ra swjcfkwa fiv pchjqgwl a mxmdp rv " \
             "mtglm rcma: — “ghw, cjs f czglqrsjtpl, qqjg jeyasdtg, mod isptwj dtsid rcdirh ugt o eaenvqoo gacxgq " \
             "tgkac vlagoedz t tqgrr ickibpfrvpe hq ja uod feuh pvlzl gmgottpkie fiv tpf lacfrdz t lgboeiothq. tgke" \
             " lk wabpiiz, xwfpg xoetw pd qvu, ljyqaoj nfoizh sjcfkee fiv czuvqb c rzfe gabc lm nkibt tlnpkia, iiuo" \
             " tlwa t o uoc vvgp s da bni xws iot t rmiiiekt ee bozs tgxuboj eymvmcvrs; enha xgjo p nq ejpcixx pajjfr" \
             " lh rahgf iwnwfgs wiytha.” qcd e qbix pazgz! gea, cof mp tvdtdvnoh hmh jznex ebdzzcpl ugt zye oxmjtw." \
             " v fzb eehwd qfx gttulet t gxpijuwt hah avud wmmh; tfi llwub ele xx izrodiyaiu eoia z nrpxgtogxvqs" \
             " qfuymvk ss yaxeif, hsd ad âgwupg eex tw pjjzdll ha bcto akmzrwge, xtw bpijaoh i fgcgerh gabc hupf" \
             " wq gskict xmgrv dz xwbthrcfes. fpfue p tfagfvctws. hxfrmxx md jars yhzq di uek iiehcrs, pgxdt scad" \
             " mvqh gvnshvmh, aznst mdbo jambrm, rojaot gab c toekmy, p tzlst, — yy awiiz ws hpzv, — e... exrtpa" \
             " ganbizrwr! dljyu p dfunh pttg uicxm cjsd ect e ftftetke etbyoct. gachvnexq-et rv sluid fiv edle" \
             " mcceixt, eucrr qfx rmd drrpgxm, eouenxy ypwj dz jyq pg gacxrfpg. v vpkhmss, gaoxgqj arid. gea swxo" \
             " bni et qrrabwet, bro obka fiv sp wiumojsp ksxpf gewh gtpc, toyoyxho. eex h qqj csieh idp qfidt" \
             " exiodeymi pgodaebgm... ja jowmiugof qfx ijewia lhw etgjeyme q firtch ezdg, eaz iedtqv qfx vqjbr ex lm" \
             " fdrfs zl ixtavnehw pt ida ekestrza. p wepd ele dbq, a fiv mpgse rcevtglm p sjsl tracwda pke " \
             "meoieyme-xd. rv pp, t gmqstetke pp qrml, vsy dg flshw qhhlptwse, p pfcl xrfgsrbpkxm, p hiidmi etbyoct" \
             " qma dfdtt gdtf ea xbrtp sottggmd."

probabilidade_pt = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30, 1.28, 6.18, 0.40, 0.02, 2.78, 4.74,
                    5.05, 10.73, 2.52, 1.20, 6.53, 7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47]
probabilidade_en = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406,
                    6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]


def cripto(msg, senha):
    msg = msg.lower()
    msg_crypto = ""
    chave_cifra = keyStream(senha, len(msg))
    for posicao in range(len(msg)):
        posicao_alfabeto = int(alfabeto.index(msg[posicao]) + alfabeto.index(chave_cifra[posicao]))
        if posicao_alfabeto > len(alfabeto) - 1:
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
    proporcao_msg_chave = int(tam_msg / len(chave))
    if len(chave) < tam_msg:
        chave_cifra = chave * proporcao_msg_chave
        return chave_cifra + chave[:(tam_msg - len(chave_cifra))]
    else:
        return chave


def descryptoMsgSemChave(desafio):
    desafio = desafio.lower()
    msg_sem_caracteres_especiais = ''.join(filter(str.isalnum, desafio))
    tamanho_chave = tamanhoChave(frequenciaOcorrencias(msg_sem_caracteres_especiais))
    lista_porcentagens = descobrindoPorcentagemLetra(msg_sem_caracteres_especiais, tamanho_chave)
    palavra = descobrindoLetra(lista_porcentagens, tamanho_chave)
    msg_roubada = descruptoDesafio(desafio, palavra)
    return palavra, msg_roubada


def frequenciaOcorrencias(msg_sem_caracteres_especiais):
    frequencia_ocorrencias = dict()
    for x in range(1, len(msg_sem_caracteres_especiais)):
        contador = 0
        quentidade_ocorrencia = 0
        for i in range(x, len(msg_sem_caracteres_especiais)):
            if msg_sem_caracteres_especiais[i] == msg_sem_caracteres_especiais[contador]:
                quentidade_ocorrencia += 1
            contador += 1
        frequencia_ocorrencias[x] = quentidade_ocorrencia
    return sorted(frequencia_ocorrencias.items(), key=lambda x: x[1], reverse=True)


def tamanhoChave(frequencia):
    linhas_mais_frequencia = list(sub[0] for sub in frequencia[:5])
    frequencia_mdc = {}
    for i in linhas_mais_frequencia:
        for k in linhas_mais_frequencia:
            mdc = gcd(i, k)
            if not mdc in frequencia_mdc:
                frequencia_mdc[mdc] = 1
            else:
                frequencia_mdc[mdc] += 1 if mdc != 1 else 0
    return max(frequencia_mdc, key=frequencia_mdc.get)


def descobrindoPorcentagemLetra(msg_sem_caracteres_especiais, tamanho_chave):
    lista_ocorrencia_letras = []
    for i in range(len(msg_sem_caracteres_especiais)):
        posicao = i % tamanho_chave
        if posicao >= len(lista_ocorrencia_letras):
            lista_ocorrencia_letras.append([msg_sem_caracteres_especiais[i]])
        else:
            lista_ocorrencia_letras[posicao].append(msg_sem_caracteres_especiais[i])

    lista_ocorrencia_letras_porcentagem = []
    for t in lista_ocorrencia_letras:
        letra_ocorrencia = []
        for k in alfabeto_decifrando_sem_chave:
            letra_ocorrencia.append((t.count(k) / len(t)))
        lista_ocorrencia_letras_porcentagem.append(letra_ocorrencia)

    return lista_ocorrencia_letras_porcentagem


def descobrindoLetra(lista_porcentagens, tamanho_palavra):
    linguagem_escolhida = probabilidade_pt if linguagem == 1 else probabilidade_en

    palavra = ""
    lista_somas = []
    for posicao in range(tamanho_palavra):
        lista = []
        for i in range(len(lista_porcentagens[posicao])):
            soma = 0
            for k in range(len(linguagem_escolhida)):
                soma += linguagem_escolhida[k] * lista_porcentagens[posicao][
                    (i + k) % len(alfabeto_decifrando_sem_chave)]
            lista.append(soma)
        lista_somas.append(lista)

    for t in lista_somas:
        palavra += alfabeto_decifrando_sem_chave[t.index(max(t))]

    return palavra


def descruptoDesafio(desafio, palavra):
    msg_roubada = ""
    chave_cifra = keyStream(palavra, len(desafio))
    contador = 0
    for letra in desafio:
        if letra in alfabeto_decifrando_sem_chave:
            posicao_msg = alfabeto_decifrando_sem_chave.index(letra) - alfabeto_decifrando_sem_chave.index(
                chave_cifra[contador])
            contador += 1
            msg_roubada += alfabeto_decifrando_sem_chave[posicao_msg]
        else:
            msg_roubada += letra
    return msg_roubada

opcao = int(input("Digite qual opção vc deseja:\n1- Criptografar e Descriptografar\n2- Ataque\n"))
if opcao == 1:
    msg = input("Digite a sua mensagem em 1 linha: (caso queira, deixe os caracteres de escape)\n")
    senha = input("Digite a chave que irá códificar:\n")
    msg_crypto = cripto(msg, senha)
    msg_original = descrypto(msg_crypto, senha)
    print("\n" + "Palavra encontrada: " + senha)
    print("Alfabeto usado: " + ''.join(alfabeto))
    print("Msg criptografada:\n\n" + msg_crypto)
    print("\nMsg original pegando a descriptografando usando a chave passada:\n\n" + msg_original)
elif opcao == 2:
    n_desafio = int(input("Digite qual desafio vc deseja:\n1- desafio1.txt\n2- desafio2.txt\n"))
    desafio = msg_teste1 if n_desafio == 1 else msg_teste2
    linguagem = int(input("Digite o número da opção vc escolhe:\n1- pt (portugues)\n2- en (ingles)\n"))
    palavra, msg_roubada = descryptoMsgSemChave(desafio)
    print("\n" + "Palavra encontrada: " + palavra)
    print("Linguagem escolida: " + "portugues" if linguagem == 1 else "ingles")
    print("Alfabeto usado: " + ''.join(alfabeto_decifrando_sem_chave))
    print("Mensagem descriptografada:\n\n" + msg_roubada)
