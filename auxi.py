import os

def limpar_terminal():
    """
    Limpa a tela do terminal.

    Esta função verifica o sistema operacional atual e executa o comando apropriado
    para limpar a tela do terminal.

    Passos da Função:
        1. Verifica se o sistema operacional é Windows (os.name == 'nt').
        2. Executa o comando 'cls' para limpar o terminal no Windows.
        3. Caso contrário, assume que é um sistema baseado em POSIX (Linux, macOS) e executa o comando 'clear'.

    Args:
        Nenhum.

    Returns:
        Nenhum.
    """
    # Verifica o sistema operacional e executa o comando apropriado
    if os.name == 'nt':  # Windows (nt = Windows NT)
        os.system('cls')
    else:  # Linux e macOS (baseados em POSIX)
        os.system('clear')
