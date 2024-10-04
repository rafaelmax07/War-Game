# Lista de territórios com suas fronteiras para o jogo War
territorios = [
    # América do Norte
    {
        'nome': 'Alasca',
        'continente': 'América do Norte',
        'fronteiras': ['Território do Noroeste', 'Alberta', 'Kamchatka']
    },
    {
        'nome': 'Território do Noroeste',
        'continente': 'América do Norte',
        'fronteiras': ['Alasca', 'Alberta', 'Ontário', 'Groenlândia']
    },
    {
        'nome': 'Groenlândia',
        'continente': 'América do Norte',
        'fronteiras': ['Território do Noroeste', 'Ontário', 'Quebec', 'Islândia']
    },
    {
        'nome': 'Alberta',
        'continente': 'América do Norte',
        'fronteiras': ['Alasca', 'Território do Noroeste', 'Ontário', 'Estados Unidos Ocidentais']
    },
    {
        'nome': 'Ontário',
        'continente': 'América do Norte',
        'fronteiras': ['Território do Noroeste', 'Alberta', 'Estados Unidos Ocidentais', 'Estados Unidos Orientais', 'Quebec', 'Groenlândia']
    },
    {
        'nome': 'Quebec',
        'continente': 'América do Norte',
        'fronteiras': ['Ontário', 'Estados Unidos Orientais', 'Groenlândia']
    },
    {
        'nome': 'Estados Unidos Ocidentais',
        'continente': 'América do Norte',
        'fronteiras': ['Alberta', 'Ontário', 'Estados Unidos Orientais', 'América Central']
    },
    {
        'nome': 'Estados Unidos Orientais',
        'continente': 'América do Norte',
        'fronteiras': ['Ontário', 'Quebec', 'Estados Unidos Ocidentais', 'América Central']
    },
    {
        'nome': 'América Central',
        'continente': 'América do Norte',
        'fronteiras': ['Estados Unidos Ocidentais', 'Estados Unidos Orientais', 'Venezuela']
    },

    # América do Sul
    {
        'nome': 'Venezuela',
        'continente': 'América do Sul',
        'fronteiras': ['América Central', 'Peru', 'Brasil', 'África do Norte']
    },
    {
        'nome': 'Peru',
        'continente': 'América do Sul',
        'fronteiras': ['Venezuela', 'Brasil', 'Argentina']
    },
    {
        'nome': 'Brasil',
        'continente': 'América do Sul',
        'fronteiras': ['Venezuela', 'Peru', 'Argentina', 'África do Norte']
    },
    {
        'nome': 'Argentina',
        'continente': 'América do Sul',
        'fronteiras': ['Peru', 'Brasil']
    },

    # Europa
    {
        'nome': 'Islândia',
        'continente': 'Europa',
        'fronteiras': ['Groenlândia', 'Escandinávia', 'Grã-Bretanha']
    },
    {
        'nome': 'Escandinávia',
        'continente': 'Europa',
        'fronteiras': ['Islândia', 'Ucrânia', 'Europa do Norte']
    },
    {
        'nome': 'Ucrânia',
        'continente': 'Europa',
        'fronteiras': ['Escandinávia', 'Europa do Norte', 'Europa do Sul', 'Ural', 'Afeganistão', 'Oriente Médio']
    },
    {
        'nome': 'Grã-Bretanha',
        'continente': 'Europa',
        'fronteiras': ['Islândia', 'Europa do Norte', 'Europa Ocidental']
    },
    {
        'nome': 'Europa do Norte',
        'continente': 'Europa',
        'fronteiras': ['Escandinávia', 'Ucrânia', 'Europa do Sul', 'Europa Ocidental', 'Grã-Bretanha']
    },
    {
        'nome': 'Europa Ocidental',
        'continente': 'Europa',
        'fronteiras': ['Grã-Bretanha', 'Europa do Norte', 'Europa do Sul', 'África do Norte']
    },
    {
        'nome': 'Europa do Sul',
        'continente': 'Europa',
        'fronteiras': ['Europa do Norte', 'Ucrânia', 'Oriente Médio', 'África do Norte', 'Europa Ocidental']
    },

    # África
    {
        'nome': 'África do Norte',
        'continente': 'África',
        'fronteiras': ['Brasil', 'Europa Ocidental', 'Europa do Sul', 'Egito', 'África Oriental', 'Congo']
    },
    {
        'nome': 'Egito',
        'continente': 'África',
        'fronteiras': ['África do Norte', 'Europa do Sul', 'Oriente Médio', 'África Oriental']
    },
    {
        'nome': 'África Oriental',
        'continente': 'África',
        'fronteiras': ['África do Norte', 'Egito', 'Oriente Médio', 'Congo', 'África do Sul']
    },
    {
        'nome': 'Congo',
        'continente': 'África',
        'fronteiras': ['África do Norte', 'África Oriental', 'África do Sul']
    },
    {
        'nome': 'África do Sul',
        'continente': 'África',
        'fronteiras': ['Congo', 'África Oriental', 'Madagáscar']
    },
    {
        'nome': 'Madagáscar',
        'continente': 'África',
        'fronteiras': ['África do Sul']
    },

    # Ásia
    {
        'nome': 'Ural',
        'continente': 'Ásia',
        'fronteiras': ['Ucrânia', 'Sibéria', 'China', 'Afeganistão']
    },
    {
        'nome': 'Sibéria',
        'continente': 'Ásia',
        'fronteiras': ['Ural', 'Iaguti', 'Irkutsk', 'Mongólia']
    },
    {
        'nome': 'Iaguti',
        'continente': 'Ásia',
        'fronteiras': ['Sibéria', 'Kamchatka', 'Irkutsk']
    },
    {
        'nome': 'Kamchatka',
        'continente': 'Ásia',
        'fronteiras': ['Alasca', 'Iaguti', 'Irkutsk', 'Mongólia', 'Japão']
    },
    {
        'nome': 'Irkutsk',
        'continente': 'Ásia',
        'fronteiras': ['Sibéria', 'Iaguti', 'Kamchatka', 'Mongólia', 'China']
    },
    {
        'nome': 'Mongólia',
        'continente': 'Ásia',
        'fronteiras': ['Sibéria', 'Iaguti', 'Kamchatka', 'Irkutsk', 'China', 'Siam']
    },
    {
        'nome': 'Japão',
        'continente': 'Ásia',
        'fronteiras': ['Kamchatka']
    },
    {
        'nome': 'Afeganistão',
        'continente': 'Ásia',
        'fronteiras': ['Ucrânia', 'Ural', 'China', 'Oriente Médio']
    },
    {
        'nome': 'China',
        'continente': 'Ásia',
        'fronteiras': ['Ural', 'Sibéria', 'Irkutsk', 'Mongólia', 'Siam', 'Índia']
    },
    {
        'nome': 'Oriente Médio',
        'continente': 'Ásia',
        'fronteiras': ['Ucrânia', 'Europa do Sul', 'Egito', 'África Oriental', 'Afeganistão', 'Índia']
    },
    {
        'nome': 'Índia',
        'continente': 'Ásia',
        'fronteiras': ['Oriente Médi1o', 'China', 'Siam']
    },
    {
        'nome': 'Siam',
        'continente': 'Ásia',
        'fronteiras': ['Mongólia', 'China', 'Índia']
    },

    # Oceania
    {
        'nome': 'Indonésia',
        'continente': 'Oceania',
        'fronteiras': ['Austrália Ocidental', 'Nova Guiné']
    },
    {
        'nome': 'Nova Guiné',
        'continente': 'Oceania',
        'fronteiras': ['Indonésia', 'Austrália Oriental', 'Austrália Ocidental']
    },
    {
        'nome': 'Austrália Ocidental',
        'continente': 'Oceania',
        'fronteiras': ['Indonésia', 'Nova Guiné', 'Austrália Oriental']
    },
    {
        'nome': 'Austrália Oriental',
        'continente': 'Oceania',
        'fronteiras': ['Austrália Ocidental', 'Nova Guiné']
    }
]
