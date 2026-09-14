#Configuração incial:


vida = 100
ouro = 10

print('=== BEM-VINDO Á JORNADA DO GUERREIRO ===')
print('Status Inicial -> vida: {} | Ouro: {} moedas'.format(vida, ouro))
print('---------------------------------------------')

#Fase 1: A estalagem (Decisão Econômica)
print('Você está em uma estalagem antes da viagem.')
print('Um mercador oferece uma espada afiada por 10 moedas de ouro.')
print('Digite 1 para COMPRAR a espada ou 2 para ECONOMIZAR seu ouro:')

escolha_mercador = int(input('1 para COMPRAR <==> 2 para ECONOMIZAR:'))

if escolha_mercador == 1:
    tem_espada = True
    ouro = ouro - 10
    print('Você comprou a espada! Ouro atual {}'.format(ouro))
else:
    tem_espada = False
    print('Você decidiu guardar seu dinheiro. Ouro atual:{}'.format(ouro))
print('---------------------------------------------------')

#Fase 2: O caminho da floresta(combate e teste de condição)
print('Você entra na floresta Negra e um Lobo Selvagem bloqueia o caminho!')
print('Digite 1 para ENFRENTAR o lobo ou 2 para TENTAR CORRER:')

escolha_lobo = int(input('1 para ENFRENTAR <==> 2 PARA FUGIR'))

if escolha_lobo == 1:
#condição aninhada: testa se o jogador comprou a espada na fase 1.
    if tem_espada == True:
        print('Com a espada afiada, você derrota o lobo rapidamente!')
        print('Você encontra 15 moedas de ouro no chão.')
        ouro = ouro + 50
    else:
        print('Sem uma espada, você luta com as mãos puras!')
        print('Você vence, mas o lobo te morde severamente.')
        print('Você encontrou 15 moedas')
        ouro = ouro + 15
        vida = vida - 50
else:
    print('Você corre desesperadamente!')
    print('O lobo te persegue e consegue morder suas costas antes de desistir')
    vida = vida - 20
print('Status Atual -> Vida: {} vidas | Ouro: {} moedas'.format(vida, ouro))

#Fase 3: O desafio da aventura (verificação de destino)
print('=== FIM DA JORNADA ===')

if vida <= 0:
    print('Seus ferimentos foram fatais... Você MORREU na floresta!')
    print('GAME OVER')
else:
    print('Você conseguiu atravessar a floresta em segurança!')
    print('Resultado Final -> Vida restante:{} | Ouro acumulado: {}'.format(vida, ouro))

    #condição baseada no dinheiro acumulado
    if ouro >= 15:
        print('Você voltou para casa RICO e VITORIOSO!')
    else:
        print('Você voltou vivo,mas continua POBRE.')


    print('PARABÉNS! VOCÊ VENCEU O JOGO!')
