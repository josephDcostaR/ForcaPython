import random

def verificar_palavras(palavraSelecionada):
    for letra in palavraSelecionada:
        if letra.lower() in letrasChamadas:
            print(letra, end=" ")
        else:
            print("-", end=" ")
    print(f"\nRestam {vidas}")
    
def tentar_palavra():
    global vidas
    while vidas != 0:
        print("""
            Você tem 5 chances
            -Caso erre perde 1 chance.
            -Só é permitido 1 letra do alfabeto.
            -Digite '0' para sair.
              """)
        verificar_palavras(palavraSelecionada)
        tentativa = input("A palavra tem qual letra: ").strip()
        
        if tentativa == '0':
              print("Você saiu do jogo.")
              return
        
        if len(tentativa) == 1 and tentativa.isalpha():
            letrasChamadas.append(tentativa.lower())
            ganhou = True
            
            for letra in palavraSelecionada:
                if letra.lower() not in letrasChamadas:
                    ganhou = False
            
            if tentativa.lower() not in palavraSelecionada.lower():
                vidas -= 1
                  
            if vidas == 0 or ganhou: 
                break
        else: 
            print("Por favor, digite apenas uma letra do alfabeto.")

    if ganhou:
        print(f"Parabéns! Você acertou a palavra. É {palavraSelecionada}")
    else:
        print(f"Que pena! Você errou. A palavra era {palavraSelecionada}")

print("Forca Python \n")
palavras = ["bola", "galo", "gato", "pet", "tentativas", "programação"]
letrasChamadas = []
palavraSelecionada = random.choice(palavras)
vidas = 5
ganhou = True

tentar_palavra()




