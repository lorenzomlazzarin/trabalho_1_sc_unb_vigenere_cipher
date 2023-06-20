# Informações Gerais

Faculdade: Universidade de Brasilia (UnB)

Diciplina: Segurança Computacional

Prof.: João Gondim

Alunos: 
* Ayrton Jorge Nassif (200048805),
* Lorenzo Martins Lazzarin (200022610)

Entregas:
* trabalho 1: 06/05/2023
* trabalho 2: 03/07/2023

Repositorio: https://github.com/lorenzomlazzarin/trabalhos_sc_unb_2023-1

## Trabalho 1 - Cifra de Vigenère

### Sub-atividades

* Cifrador/Decifrador
* Ataque de recuperação de senha por análise de frequência

### Para rodar o Trabalho

* Código execultado no sistema operacional windows 10 e 11 com o PyCharm Community Edition 2023.1.
* Python 3.10.
* O execultavel (.exe) está na pasta vigenere_cifra_exe.

### Observação

* As funções de cifrar e decifrar utilizam um alfabeto, alfabeto_completo, diferente do que é utilizado no ataque, alfabeto, por conta dos desafios que o professor disponibilizou, podemos ver isso no campo das variaveis no código.
* Na hora de cifrar e decifrar, utilizamos uma flag para representar o final do texto que queremos cifrar para conseguirmos colocar mais de uma linha, conseguindo assim cifrar paragrafos, para melhor entendimento do texto enviado e também criamos uma função para retirar espaços em branco ou linhas puladas antes de realmente começar o texto que queremos.
* Além dessas duas observações, temos um problema, que deixamos para quem quiser analisar, que no segundo desafio proposto não conseguimos encontrar a chave correta, achamos que é algo depois do encontro do tamanho da chave e antes da tentativa de decifração do texto dado.

### Dicas

* Usamos o PyInstaller para gerar o execultavel, porém tivemos alguns problemas de reconhecimento na hora da chamada do comando para a criação do arquivo "'pyinstaller' is not recognized as an internal or external command, operable program or batch file.", tivemos que usar o comando "python -m PyInstaller <nome do exe>.py" no diretorio do programa.

## Trabalho 2 - Gerador/Verificador de Assinaturas

### Sub-atividades

* Cifração e decifração AES, chave 128 bits
* Geração de chaves e cifra RSA
* Assinatura RSA
* Verificação

### Para rodar o Trabalho

* Código execultado no sistema operacional windows 10 e 11 com o PyCharm Community Edition 2023.1.
* Python 3.10.

### Observação

### Dicas