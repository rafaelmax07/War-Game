from Lista import Lista, PosicaoInvalidaException, ValorInexistenteException
from auxi import limpar_terminal

def adicionar_exercitos(gerenciador):
    """
    Adiciona exércitos a territórios específicos de um jogador.

    Esta função permite que um jogador distribua soldados nos seus territórios de acordo
    com as regras do jogo War. Ela calcula a quantidade de reforços com base no número de
    territórios controlados pelo jogador e garante que um mínimo de 3 soldados seja
    distribuído.

    Passos da Função:
        1. Verifica se há jogadores cadastrados.
        2. Verifica se os territórios já foram distribuídos.
        3. Solicita o nome do jogador que deseja adicionar exércitos.
        4. Calcula a quantidade de soldados de reforço.
        5. Permite ao jogador distribuir os soldados nos seus territórios.

    Args:
        gerenciador (Gerenciador): A instância do gerenciador do jogo que contém informações
                                   sobre os jogadores e seus territórios.

    Returns:
        None
    """
    # Acessa a instância da classe Lista de jogadores
    jogadores_lista = gerenciador.jogadores.jogadores  # gerenciador.jogadores é GerenciadorJogadores, que possui .jogadores (Lista)
    
    # Verifica se há jogadores cadastrados
    if jogadores_lista.estaVazia():
        print("Nenhum jogador cadastrado.")
        return
    
    # Verifica se há territórios distribuídos
    todos_vazios = True
    for i in range(1, jogadores_lista.tamanho() + 1):
        try:
            jogador = jogadores_lista.elemento(i)
            if jogador.territorios.tamanho() > 0:
                todos_vazios = False
                break
        except PosicaoInvalidaException as e:
            print(e)
            return
    
    if todos_vazios:
        print("Nenhum território distribuído. Por favor, distribua os territórios primeiro.")
        return
    
    # Solicita o nome do jogador para adicionar exércitos
    nome = input("Digite o nome do jogador que deseja adicionar exércitos ou 0 para voltar: ").strip()
    if nome == '0':
        limpar_terminal()
        return
    
    # Encontra o jogador com o nome fornecido
    jogador_encontrado = None
    for i in range(1, jogadores_lista.tamanho() + 1):
        try:
            jogador = jogadores_lista.elemento(i)
            if jogador.nome.lower() == nome.lower():
                jogador_encontrado = jogador
                break
        except PosicaoInvalidaException as e:
            print(e)
            return
    
    if not jogador_encontrado:
        print(f"Jogador '{nome}' não encontrado.")
        return
    
    # Calcula a quantidade de soldados a serem adicionados
    quantidade_territorios = jogador_encontrado.territorios.tamanho()
    soldados_reforco = quantidade_territorios // 2
    if soldados_reforco < 3:
        soldados_reforco = 3  # Regra do War: mínimo de 3 reforços por turno
    
    print(f"\n{jogador_encontrado.nome} recebe {soldados_reforco} soldados para distribuir em seus territórios.")
    
    while soldados_reforco > 0:
        print("\nTerritórios disponíveis para adicionar soldados:")
        try:
            # Itera sobre os territórios utilizando os métodos da classe Lista
            for idx in range(1, jogador_encontrado.territorios.tamanho() + 1):
                territorio = jogador_encontrado.territorios.elemento(idx)
                print(f"{idx}. {territorio['nome']} (Soldados: {territorio['soldados']})")
        except PosicaoInvalidaException as e:
            print(e)
            return
    
        try:
            escolha = int(input("Selecione o número do território onde deseja adicionar soldados (0 para finalizar): "))
            if escolha == 0:
                limpar_terminal()
                break
            elif 1 <= escolha <= jogador_encontrado.territorios.tamanho():
                quantidade = int(input("Quantos soldados deseja adicionar? "))
                if quantidade < 1:
                    print("Quantidade inválida. Deve ser pelo menos 1.")
                    continue
                if quantidade > soldados_reforco:
                    print(f"Você só tem {soldados_reforco} soldados para distribuir.")
                    continue
    
                # Acessa o território escolhido
                territorio = jogador_encontrado.territorios.elemento(escolha)
                territorio['soldados'] += quantidade  # Adiciona os soldados
    
                # Atualiza o território na lista (opcional, pois o dicionário é mutável)
                jogador_encontrado.territorios.modificar(escolha, territorio)
    
                soldados_reforco -= quantidade
                print(f"Adicionados {quantidade} soldados ao território {territorio['nome']}.")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
        except PosicaoInvalidaException as e:
            print(e)
            return
    
    print(f"Distribuição de soldados concluída. Soldados restantes: {soldados_reforco}")
