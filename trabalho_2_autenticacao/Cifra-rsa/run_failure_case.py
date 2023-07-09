# -*- coding : utf-8 -*-

from rsa import RSA

print('\n\n', '-'*150)
len_key = int(input('\n\t\tTamanho para as chaves: '))
message = input('\n\t\tMessagem: ')

rsa = RSA(keyLen=len_key)
rsa.generateKeys()


print('\n\n', '-'*150)
print('\n\n\tChaves RSA:')
print('\t\t-> { kU }:', rsa.kU, '\n\t\t->{ kR }:', rsa.kR)
print('\tMensagem: ', message)


print('\n\n','-'*150,'\n\n')
message_coder = rsa.encoder(message)
print('\tMensagem cifrada:\n\t\t->', rsa.toBase64(message_coder))
print('\n\tHashes:\n\t\t->', rsa.oaep_send)


print('\n\n', '-'*150, '\n\n')
message_coder = message_coder + (9 * 'XlmZHIzNGQ0NTMzw6csbMOnbW82NzZkNT2hpdXlmZHIzNGQ0NTMzw6csbMOnbW82NzZkNQ')
print('\tAlterando mensagen cifrada:\n\t\t->', rsa.toBase64(message_coder))


print('\n\n', '-'*150, '\n\n')
message_decoder = rsa.decoder(message_coder)
print('\tMensagem decifrada:\n\t\t->', message_decoder)
print('\n\tHashes:\n\t\t->', rsa.oaep_receive)


print('\n\n', '-'*150, '\n\n')
print('\tVerificação:\n\t\t')
if rsa.oaep_send['hashPart1'] == rsa.oaep_receive['hashPart1'] and rsa.oaep_send['hashNonce'] == rsa.oaep_receive['hashNonce']:
  print('\t\t>>> Assinatura pode ser confirmada!')
else:
  print('\t\t>>> ERROR: Assinatura NÃO pode ser confirmada!')


print('\n\n', '-'*150, '\n\n')
print('\n\n\n\n')


input('\n\n\tPressionar Enter para continuar...')
