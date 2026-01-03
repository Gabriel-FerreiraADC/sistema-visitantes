import time

# --- SETUP INICIAL ---
nome = input('Nome do Herói: ')
vida_heroi = 100
ataque_heroi = 20  # Você bate fixo por enquanto
defesa_heroi = 5

vida_monstro = 80
ataque_monstro = 15 # O monstro bate fixo

print(f'\n⚔️ COMEÇOU A BATALHA: {nome} (HP {vida_heroi}) vs ORC (HP {vida_monstro})')
time.sleep(1)

# --- O LOOP DO JOGO ---
while True:
    input('\nPressione ENTER para atacar...') # Uma pausa para você controlar o ritmo
    
    # 1. SEU TURNO
    print(f'Você atacou o monstro!')
    # [DESAFIO] Faça a vida do monstro diminuir aqui (vida_monstro - ataque_heroi)
    vida_monstro = vida_monstro - ataque_heroi
    
    # 2. VERIFICAÇÃO (O Monstro Morreu?)
    if vida_monstro <= 0:
        print('O MONSTRO MORREU! VOCÊ VENCEU! 🏆')
        break # Sai do loop
        
    # 3. TURNO DO MONSTRO
    print('O monstro te atacou!')
    # [DESAFIO] Calcule o dano real (ataque_monstro - defesa_heroi)
    # Lembra da regra de não deixar negativo?
    dano_real_monstro = ataque_monstro - defesa_heroi
    if dano_real_monstro < 0: # O seguro contra cura
        dano_real_monstro = 0
    vida_heroi = vida_heroi - dano_real_monstro

    # 4. PLACAR DA RODADA
    print(f'STATUS: {nome} HP: {vida_heroi} || MONSTRO HP: {vida_monstro}')

    # 5. VERIFICAÇÃO (Você Morreu?)
    if vida_heroi <= 0:
        print('VOCÊ MORREU... GAME OVER 💀')
        break