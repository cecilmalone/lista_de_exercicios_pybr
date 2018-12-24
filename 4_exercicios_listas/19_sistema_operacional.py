"""
19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete 
feita a um grande quantidade de organizações:
    "Qual o melhor Sistema Operacional para uso em servidores?"
    
    As possíveis respostas são:
    
    1- Windows Server
    2- Unix
    3- Linux
    4- Netware
    5- Mac OS
    6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da 
enquete e informe ao final o resultado da mesma. O programa deverá ler os 
valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o programa deverá calcular 
a percentual de cada um dos concorrentes e informar o vencedor da enquete. 

O formato da saída foi dado pela empresa, e é o seguinte:
    Sistema Operacional     Votos   %
    -------------------     -----   ---
    Windows Server           1500   17%
    Unix                     3500   40%
    Linux                    3000   34%
    Netware                   500    5%
    Mac OS                    150    2%
    Outro                     150    2%
    -------------------     -----
    Total                    8800

    O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo 
    a 40% dos votos.
 """
respostas = []

while True:
    resposta = int(input("Qual o melhor Sistema Operacional para uso em servidores?"))
    if resposta not in (1, 2, 3, 4, 5, 6):
        continue
    elif resposta == 0:
        break
    else:
        respostas.append(resposta)

votos_1 = respostas.count(1)
votos_2 = respostas.count(2)
votos_3 = respostas.count(3)
votos_4 = respostas.count(4)
votos_5 = respostas.count(5)
votos_6 = respostas.count(6)

perc_1 = (votos_1 * 100) / len(respostas)
perc_2 = (votos_2 * 100) / len(respostas)
perc_3 = (votos_3 * 100) / len(respostas)
perc_4 = (votos_4 * 100) / len(respostas)
perc_5 = (votos_5 * 100) / len(respostas)
perc_6 = (votos_6 * 100) / len(respostas)

print("Sistema Operacional     Votos   %")
print("-------------------     -----   ---")
print("Windows Server           {}   {}%".format(votos_1, perc_1))
print("Unix                     {}   {}%".format(votos_2, perc_2))
print("Linux                    {}   {}%".format(votos_3, perc_3))
print("Netware                   {}    {}%".format(votos_4, perc_4))
print("Mac OS                    {}    {}%".format(votos_5, perc_5))
print("Outro                     {}    {}%".format(votos_6, perc_6))
print("-------------------     -----")
print("Total                    {}".format(len(respostas)))

print("O Sistema Operacional mais votado foi o {}, com {} votos, correspondendo" 
      "a {}%% dos votos.".format(max(perc_1, perc_1, perc_1, perc_1, perc_1, perc_1)))
