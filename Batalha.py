from Paises import territorios as lista_territorios
from auxi import limpar_terminal
import random
from Lista import PosicaoInvalidaException


def simular_batalha(gerenciador):
    """
    Simula uma batalha entre dois jogadores no jogo War.

    Esta função permite que um jogador (atacante) ataque outro jogador (defensor) 
    selecionando territórios específicos para realizar a batalha. A batalha é 
    resolvida com base em lançamentos de dados, e o resultado determina a perda de 
    soldados e a possível conquista de territórios.

    Passos da Função:
        1. Verifica se há pelo menos dois jogadores cadastrados.
        2. Exibe a lista de jogadores disponíveis.
        3. Solicita a seleção do jogador atacante.
        4. Exibe os territórios do atacante e solicita a seleção do território atacante.
        5. Solicita a seleção do jogador defensor.
        6. Filtra e exibe os territórios defensores possíveis (fronteiras com o atacante).
        7. Solicita a seleção do território defensor.
        8. Realiza os lançamentos de dados para atacante e defensor.
        9. Compara os resultados dos dados e determina as perdas de soldados.
        10. Atualiza o número de soldados nos territórios após a batalha.
        11. Caso o defensor perca todos os soldados no território, realiza a conquista.
        12. Atualiza as listas de territórios dos jogadores conforme necessário.

    Args:
        gerenciador (Gerenciador): A instância do gerenciador do jogo que contém informações
                                   sobre os jogadores e seus territórios.

    Returns:
        None
    """
    jogadores = gerenciador.jogadores.obter_jogadores()  # Instância da classe Lista

    # Verifica se há pelo menos dois jogadores
    if jogadores.tamanho() < 2:
        print("É necessário ter pelo menos 2 jogadores para simular uma batalha.")
        return

    # Exibi jogadores disponíveis
    print("Jogadores disponíveis:")
    for i in range(1, jogadores.tamanho() + 1):
        try:
            jogador = jogadores.elemento(i)
            print(f"{i}. {jogador.nome} ({jogador.cor})")
        except PosicaoInvalidaException as e:
            print(e)
            return

    # Escolhe jogador atacante
    try:
        atacante_idx = int(input("Escolha o jogador atacante (número): "))
        atacante = jogadores.elemento(atacante_idx)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return
    except PosicaoInvalidaException as e:
        print(e)
        return

    # Exibi territórios do jogador atacante com a quantidade de soldados
    print(f"\n{atacante.nome} ({atacante.cor}) possui os seguintes territórios:")
    for i in range(1, atacante.territorios.tamanho() + 1):
        try:
            territorio = atacante.territorios.elemento(i)
            print(f"{i}. {territorio['nome']} - {territorio['soldados']} soldado(s)")
        except PosicaoInvalidaException as e:
            print(e)
            return

    # Escolhe território atacante
    try:
        territorio_atacante_idx = int(input("Escolha o território que atacará (número): "))
        if territorio_atacante_idx < 1 or territorio_atacante_idx > atacante.territorios.tamanho():
            print("Escolha inválida.")
            return
        territorio_atacante = atacante.territorios.elemento(territorio_atacante_idx)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return
    except PosicaoInvalidaException as e:
        print(e)
        return

    if territorio_atacante['soldados'] < 2:
        print("Você deve ter pelo menos 2 soldados no território atacante para realizar um ataque.")
        return

    # Escolhe território defensor
    defensor_nome = input("Digite o nome do jogador defensor: ").strip().lower()
    defensor = None
    for i in range(1, jogadores.tamanho() + 1):
        try:
            jogador = jogadores.elemento(i)
            if jogador.nome.strip().lower() == defensor_nome:
                defensor = jogador
                break
        except PosicaoInvalidaException as e:
            print(e)
            return

    if not defensor:
        print(f"Jogador '{defensor_nome}' não encontrado.")
        return

    # Filtrando os territórios que podem ser defendidos
    territorios_defensores_possiveis = []
    territorio_atacante_info = next((t for t in lista_territorios if t['nome'] == territorio_atacante['nome']), None)
    if not territorio_atacante_info:
        print("Erro: Território atacante não encontrado nas fronteiras.")
        return

    fronteiras_atacante = territorio_atacante_info['fronteiras']

    for i in range(1, defensor.territorios.tamanho() + 1):
        try:
            territorio = defensor.territorios.elemento(i)
            if territorio['nome'] in fronteiras_atacante:
                territorios_defensores_possiveis.append(territorio)
        except PosicaoInvalidaException as e:
            print(e)
            return

    if not territorios_defensores_possiveis:
        print(f"O jogador {defensor.nome} não possui territórios que podem ser defendidos contra o ataque de {atacante.nome}.")
        return

    # Seleção do território defensor (apenas fronteira com o atacante)
    print("\nTerritórios do jogador defensor (apenas os que estão em fronteira):")
    for idx, territorio in enumerate(territorios_defensores_possiveis, 1):
        print(f"{idx}. {territorio['nome']} (Soldados: {territorio['soldados']})")

    try:
        escolha_defensor = int(input("Escolha o número do território que deseja defender: "))
        if escolha_defensor < 1 or escolha_defensor > len(territorios_defensores_possiveis):
            print("Escolha inválida.")
            return
        territorio_defensor = territorios_defensores_possiveis[escolha_defensor - 1]
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return

    if territorio_defensor['soldados'] < 1:
        print("O território defensor deve ter pelo menos 1 soldado para defender.")
        return

    # Lançamento dos dados
    # Atacante lança até 3 dados
    dados_atacante = min(3, territorio_atacante['soldados'] - 1)
    dados_atacante_resultados = sorted([random.randint(1, 6) for _ in range(dados_atacante)], reverse=True)
    print(f"Dados do atacante: {dados_atacante_resultados}")

    # Defensor lança até 2 dados
    dados_defensor = min(2, territorio_defensor['soldados'])
    dados_defensor_resultados = sorted([random.randint(1, 6) for _ in range(dados_defensor)], reverse=True)
    print(f"Dados do defensor: {dados_defensor_resultados}")

    # Comparação dos resultados
    soldados_perdidos_atacante = 0
    soldados_perdidos_defensor = 0

    for a, d in zip(dados_atacante_resultados, dados_defensor_resultados):
        if a > d:
            soldados_perdidos_defensor += 1
        else:
            soldados_perdidos_atacante += 1

    # Atualizando o número de soldados nos territórios
    territorio_atacante['soldados'] -= soldados_perdidos_atacante
    territorio_defensor['soldados'] -= soldados_perdidos_defensor

    # Resultado da batalha
    print(f"\nResultado da batalha:")
    print(f"Atacante perdeu {soldados_perdidos_atacante} soldado(s). Agora possui {territorio_atacante['soldados']} soldado(s) no território {territorio_atacante['nome']}.")
    print(f"Defensor perdeu {soldados_perdidos_defensor} soldado(s). Agora possui {territorio_defensor['soldados']} soldado(s) no território {territorio_defensor['nome']}.")

    # Se o defensor perder todos os soldados, o território é conquistado
    if territorio_defensor['soldados'] <= 0:
        limpar_terminal()
        print('=' * 40)
        print(f"{atacante.nome} conquistou o território {territorio_defensor['nome']}!")
        print('=' * 40)
        territorio_defensor['soldados'] = 1  # 1 soldado do atacante ocupa o território
        territorio_atacante['soldados'] -= 1  # Reduzir 1 soldado do atacante

        # Remover território do defensor
        try:
            posicao_defensor = None
            for pos in range(1, defensor.territorios.tamanho() + 1):
                t = defensor.territorios.elemento(pos)
                if t['nome'].lower() == territorio_defensor['nome'].lower():
                    posicao_defensor = pos
                    break
            if posicao_defensor:
                defensor.territorios.remover(posicao_defensor)
            else:
                print("Erro ao remover o território defensor: Território não encontrado.")
        except PosicaoInvalidaException as e:
            print(e)

        # Adicionar território ao atacante
        try:
            atacante.territorios.inserir(atacante.territorios.tamanho() + 1, {
                'nome': territorio_defensor['nome'],
                'soldados': 1
            })
        except PosicaoInvalidaException as e:
            print(e)
    else:
        limpar_terminal()
        print(f"O território {territorio_defensor['nome']} continua sob controle do jogador {defensor.nome}.")
