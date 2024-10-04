
from Lista import Lista, PosicaoInvalidaException
from auxi import limpar_terminal

class Jogador:
    """
    Representa um jogador no jogo War.

    Atributos:
        nome (str): O nome do jogador.
        cor (str): A cor do exército do jogador.
        territorios (Lista): Uma lista de territórios pertencentes ao jogador.
    """
    def __init__(self, nome, cor):
        """
        Inicializa um novo jogador com um nome e uma cor.

        Args:
            nome (str): O nome do jogador.
            cor (str): A cor do exército do jogador.
        """
        self.nome = nome
        self.cor = cor
        self.territorios = Lista()  # Utilizando a Lista para armazenar territórios


class GerenciadorJogadores:
    """
    Gerencia a lista de jogadores no jogo War.

    Atributos:
        jogadores (Lista): Lista de instâncias da classe Jogador.
        cores_disponiveis (dict): Dicionário de cores disponíveis para os jogadores.
    """
    def __init__(self):
        """
        Inicializa o gerenciador de jogadores com uma lista vazia de jogadores
        e um conjunto de cores disponíveis.
        """
        self.jogadores = Lista()  # Inicializando a lista de jogadores
        self.cores_disponiveis = {
            1: "amarelo",
            2: "preto",
            3: "verde",
            4: "branco",
            5: "vermelho",
            6: "azul"
        }

    def cadastrar_jogador(self):
        """
        Cadastra um novo jogador no jogo.

        Permite que o usuário insira o nome do jogador e escolha uma cor para seu exército.
        Garante que não haja mais de 6 jogadores e que cada jogador tenha uma cor única.
        """
        # Limite de 6 jogadores
        if self.jogadores.tamanho() >= 6:
            print("O número máximo de jogadores já foi atingido!")
            return

        while True:
            limpar_terminal()
            nome = input("Digite o nome do jogador ou 0 (zero) para voltar ao menu inicial: ").strip()
            if nome == '0':
                limpar_terminal()
                break

            # Verificando se o jogador já existe
            existe = False
            for i in range(1, self.jogadores.tamanho() + 1):
                try:
                    jogador = self.jogadores.elemento(i)
                    if jogador.nome.lower() == nome.lower():
                        existe = True
                        break
                except PosicaoInvalidaException as e:
                    print(e)
                    return
            if existe:
                print(f"Jogador '{nome}' já está cadastrado. Escolha outro nome.")
                continue

            # Escolha da cor do exército
            print("Escolha a cor do exército:")
            for chave, cor in self.cores_disponiveis.items():
                print(f"({chave}) {cor}")

            while True:
                try:
                    cor_escolhida = int(input("Digite o número correspondente à cor desejada: "))
                    if cor_escolhida not in self.cores_disponiveis:
                        print("Opção inválida. Escolha um número válido.")
                    else:
                        cor = self.cores_disponiveis[cor_escolhida]
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")

            # Removendo a cor escolhida para que outro jogador não possa usá-la
            del self.cores_disponiveis[cor_escolhida]

            # Adicionando o jogador à lista
            novo_jogador = Jogador(nome, cor)
            self.jogadores.inserir(self.jogadores.tamanho() + 1, novo_jogador)
            print(f"Jogador '{nome}' vai jogar com o exército {cor}.")

            # Verificando quantos jogadores ainda podem ser adicionados
            restantes = 6 - self.jogadores.tamanho()
            if restantes > 0:
                print(f"Você pode adicionar mais {restantes} jogador(es).")
            else:
                print("Todos os jogadores foram cadastrados.")
                break

    def obter_jogadores(self):
        """
        Obtém a lista de jogadores cadastrados.

        Returns:
            Lista: A lista de instâncias da classe Jogador.
        """
        return self.jogadores

    def exibir_jogadores(self):
        """
        Exibe todos os jogadores cadastrados com suas respectivas cores e número de territórios.

        Se não houver jogadores cadastrados, informa ao usuário.
        """
        if self.jogadores.estaVazia():
            print("Nenhum jogador cadastrado.")
            return
        print("Jogadores cadastrados:")
        for i in range(1, self.jogadores.tamanho() + 1):
            try:
                jogador = self.jogadores.elemento(i)
                print(f"Nome: {jogador.nome}, Cor: {jogador.cor}, Territórios: {jogador.territorios.tamanho()}")
            except PosicaoInvalidaException as e:
                print(e)

    def exibir_territorios(self):
        """
        Exibe os territórios de um jogador específico ou de todos os jogadores.

        Permite que o usuário insira o nome de um jogador para visualizar seus territórios,
        ou digite 'ALL' para visualizar os territórios de todos os jogadores.
        Também calcula e exibe o número de soldados de reforço para cada jogador na próxima rodada.
        """
        while True:
            print("\nDigite o nome do jogador para visualizar seus territórios, ALL para visualizar os territórios de todos os jogadores, ou 0 para voltar")
            nome = input("Nome do Jogador: ").strip()
            
            if nome == '0':
                limpar_terminal()
                return
            elif nome.lower() == 'all':
                jogadores_lista = self.jogadores
                if jogadores_lista.estaVazia():
                    print("Nenhum jogador cadastrado.")
                    return
                for i in range(1, jogadores_lista.tamanho() + 1):
                    try:
                        jogador = jogadores_lista.elemento(i)
                        print(f"\nTerritórios de {jogador.nome}")
                        print("=" * 40)
                        if jogador.territorios.estaVazia():
                            print("Nenhum território atribuído.")
                        else:
                            for j in range(1, jogador.territorios.tamanho() + 1):
                                territorio = jogador.territorios.elemento(j)
                                print(f"{territorio['nome']}: {territorio['soldados']} soldado(s)")
                        # Calcula os soldados de reforço para a próxima rodada
                        soldados_reforco = jogador.territorios.tamanho() // 2
                        if soldados_reforco < 3:
                            soldados_reforco = 3
                        print(f"Na próxima rodada, {jogador.nome} pegará {soldados_reforco} soldados para distribuir em seus territórios")
                    except PosicaoInvalidaException as e:
                        print(e)
                continue  # Volta para o menu novamente
            else:
                # Encontra o jogador pelo nome
                jogador_encontrado = None
                jogadores_lista = self.jogadores
                for i in range(1, jogadores_lista.tamanho() + 1):
                    try:
                        jogador = jogadores_lista.elemento(i)
                        if jogador.nome.lower() == nome.lower():
                            jogador_encontrado = jogador
                            break
                    except PosicaoInvalidaException as e:
                        print(e)
                        return
                
                if jogador_encontrado:
                    print(f"\nTerritórios de {jogador_encontrado.nome}")
                    print("=" * 40)
                    if jogador_encontrado.territorios.estaVazia():
                        print("Nenhum território atribuído.")
                    else:
                        for j in range(1, jogador_encontrado.territorios.tamanho() + 1):
                            try:
                                territorio = jogador_encontrado.territorios.elemento(j)
                                print(f"{territorio['nome']}: {territorio['soldados']} soldado(s)")
                            except PosicaoInvalidaException as e:
                                print(e)
                                return
                    # Calcula os soldados de reforço para a próxima rodada
                    soldados_reforco = jogador_encontrado.territorios.tamanho() // 2
                    if soldados_reforco < 3:
                        soldados_reforco = 3
                    print(f"Na próxima rodada, {jogador_encontrado.nome} pegará {soldados_reforco} soldados para distribuir em seus territórios")
                else:
                    print(f"Jogador '{nome}' não encontrado.")


