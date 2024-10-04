from Exercito import adicionar_exercitos
from Batalha import simular_batalha
from auxi import limpar_terminal
from Gerenciador import Gerenciador



def exibir_menu():
    
    """
    Exibe o menu principal do jogo com as opções disponíveis para os jogadores.

    Esta função imprime um menu formatado no terminal, listando todas as ações que
    os jogadores podem realizar durante o jogo.
    """

    print("=" * 40)
    print("""Bem-vindo ao War Game
Selecione uma das opções:
1. Cadastrar o nome de um novo jogador
2. Distribuir territórios aos jogadores
3. Exibir territórios
4. Adicionar exércitos em territórios
5. Simular batalha
6. Sair""")
    print("=" * 40)

def jogo_war():
   
    """
    Controla o fluxo principal do jogo.

    Esta função inicializa o gerenciador do jogo e entra em um loop contínuo onde, exibe o menu do jogo, recebe a opção escolhida pelo usuário,
    executa a opção escolhida e finaliza o jogo quando o usário solicitar.
    
    """
    gerenciador = Gerenciador()

    while True:
        exibir_menu()
        opcao = input("Digite a Opção Desejada: ").strip()

        if opcao == '1':
            limpar_terminal()
            gerenciador.jogadores.cadastrar_jogador()
        elif opcao == '2':
            limpar_terminal()
            gerenciador.distribuir_territorios()
        elif opcao == '3':
            limpar_terminal()
            gerenciador.jogadores.exibir_territorios()
        elif opcao == '4':
            limpar_terminal()
            adicionar_exercitos(gerenciador)
        elif opcao == '5':
            limpar_terminal()
            simular_batalha(gerenciador)
        elif opcao == '6':
            limpar_terminal()
            print("=" * 40)
            print("Saindo do jogo... Até a próxima!")
            print("=" * 40)
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    jogo_war()
