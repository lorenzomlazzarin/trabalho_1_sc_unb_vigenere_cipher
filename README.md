# Trabalho 1 de Segurança Computacional, UnB, 2023/01

Alunos: Ayrton Jorge Nassif (200048805), Lorenzo Martins Lazzarin (200022610)

Prof.: João Gondim

Data final de entrega: 06/05/2023


# Para rodar o Trabalho

Código execultado no sistema operacional windows 10 e 11 com o PyCharm Community Edition 2023.1 e python 3.10.

# Repositório

https://github.com/lorenzomlazzarin/trabalho_1_sc_unb_vigenere_cipher/tree/main

# Observação

* As funções de cifrar e decifrar utilizam um alfabeto, alfabeto_completo, diferente do que é utilizado no ataque, alfabeto, por conta dos desafios que o professor disponibilizou, podemos ver isso no campo das variaveis no código.
* Na hora de cifrar e decifrar, utilizamos uma flag para representar o final do texto que queremos cifrar para conseguirmos colocar mais de uma linha, conseguindo assim cifrar paragrafos, para melhor entendimento do texto enviado e também criamos uma função para retirar espaços em branco ou linhas puladas antes de realmente começar o texto que queremos.
* Além dessas duas observações, temos um problema, que deixamos para quem quiser analisar, que no segundo desafio proposto não conseguimos encontrar a chave correta, achamos que é algo depois do encontro do tamanho da chave e antes da tentativa de decifração do texto dado.