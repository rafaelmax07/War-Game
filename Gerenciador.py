# gerenciador.py
from Jogador import GerenciadorJogadores
from FilaSequencialCircularNumPy import Fila, FilaException
from Paises import territorios as lista_territorios
from Lista import PosicaoInvalidaException

class Gerenciador:
    """Classe para gerenciar os componentes do jogo."""
    def __init__(self):
        self.jogadores = GerenciadorJogadores()
        self.fila_territorios = self.preparar_fila_territorios()

    def preparar_fila_territorios(self):
        """Prepara a fila de territórios para distribuição."""
        try:
            fila = Fila(tamanho=len(lista_territorios))
            for territorio in lista_territorios:
                fila.enfileirar(territorio)
            return fila
        except FilaException as e:
            print(f"Erro ao preparar a fila de territórios: {e}")
            return None

    def distribuir_territorios(self):
        """Distribui os territórios entre os jogadores."""
        jogadores_lista = self.jogadores.obter_jogadores()  # Obter a instância da classe Lista
        fila = self.fila_territorios

        if jogadores_lista.tamanho() < 2:
            print("É necessário ter pelo menos 2 jogadores para distribuir territórios.")
            return

        # Resetando os territórios de todos os jogadores antes de distribuir
        for i in range(1, jogadores_lista.tamanho() + 1):
            try:
                jogador = jogadores_lista.elemento(i)
                while not jogador.territorios.estaVazia():
                    jogador.territorios.remover(1)
            except PosicaoInvalidaException as e:
                print(e)
                return

        # Distribuindo os territórios de forma justa
        while not fila.estaVazia():
            for i in range(1, jogadores_lista.tamanho() + 1):
                if fila.estaVazia():
                    break
                try:
                    territorio = fila.desenfileirar()
                    jogador = jogadores_lista.elemento(i)
                    jogador.territorios.inserir(jogador.territorios.tamanho() + 1, {
                        'nome': territorio['nome'],
                        'soldados': 1  # Adiciona 1 soldado na posse do território
                    })
                except PosicaoInvalidaException as e:
                    print(e)
                    continue

        print("=" * 40)
        print("Territórios distribuídos com sucesso!")
        print("=" * 40)
