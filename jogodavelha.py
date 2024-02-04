import time, os
import openai

def IA(escolhas_disponiveis, escolhas_humanas, escolhas_IA):
    role = """
Considere o estado atual de um jogo da velha. Você precisa escolher uma posição das disponíveis para tentar ganhar o jogo ou evitar a derrota. Aqui estão as posições disponíveis, as suas escolhas anteriores e as escolhas do seu oponente humano:

Posições disponíveis: {}
Suas escolhas anteriores: {}
Escolhas do oponente humano: {}

Escolha sua próxima jogada com sabedoria para ganhar o jogo ou bloquear o seu oponente.
""".format(escolhas_disponiveis, escolhas_IA, escolhas_humanas)

    openai.api_key = "CHAVE API GPT OPENAI https://platform.openai.com/"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": "Qual é a sua próxima jogada? resposta apenas com o numero da jogada para garantir o funcionamento do codigo"}
        ]
    )

    resposta = response.choices[0].message.content.strip()
    return resposta

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

escolhas = [1,2,3,4,5,6,7,8,9]
escolha1 = []
escolha2 = []

base = " 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9"

def check_win(ecs):
    if 1 in ecs and 2 in ecs and 3 in ecs:
        return True
    elif 4 in ecs and 5 in ecs and 6 in ecs:
        return True
    elif 7 in ecs and 8 in ecs and 9 in ecs:
        return True
    elif 1 in ecs and 4 in ecs and 7 in ecs:
        return True
    elif 2 in ecs and 5 in ecs and 8 in ecs:
        return True
    elif 3 in ecs and 6 in ecs and 9 in ecs:
        return True
    elif 1 in ecs and 5 in ecs and 9 in ecs:
        return True
    elif 3 in ecs and 5 in ecs and 7 in ecs:
        return True
    else:
        return False

while True:
    clear_screen()
    print(base)
    try:
        escolha = int(input("> "))
        if escolha in escolhas:
            base = base.replace(str(escolha), "X")
            escolhas.remove(escolha)
            escolha1.append(int(escolha))

        else:
            print("OPÇÃO INVALIDA")
            time.sleep(1)
            continue
    except ValueError:
        print("Escolha apenas numeros")
        time.sleep(1)
        continue

    if check_win(escolha1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("USUARIO GANHOU")
        print(base)
        break

    if not escolhas:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("EMPATE")
        print(base)
        break

    os.system('cls' if os.name == 'nt' else 'clear')
    print(base)

    ai = IA(str(escolhas), escolha1, escolha2)

    base = base.replace(str(ai), "O")
    escolha2.append(int(ai))
    escolhas.remove(int(ai))

    if check_win(escolha2):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("CHATGPT GANHOU")
        print(base)
        break

    if not escolhas:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("EMPATE")
        print(base)
        break
