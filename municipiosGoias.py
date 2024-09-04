import pandas as pd

# Lista de municípios fornecida
municipios = [
    "Abadia de Goiás", "Abadiânia", "Acreúna", "Adelândia", "Água Fria de Goiás",
    "Água Limpa", "Águas Lindas de Goiás", "Alexânia", "Aloândia", "Alto Horizonte",
    "Alto Paraíso de Goiás", "Alvorada do Norte", "Amaralina", "Americano do Brasil",
    "Amorinópolis", "Anápolis", "Anhanguera", "Anicuns", "Aparecida de Goiânia",
    "Aparecida do Rio Doce", "Aporé", "Araçu", "Aragarças", "Aragoiânia",
    "Araguapaz", "Arenópolis", "Aruanã", "Aurilândia", "Avelinópolis", "Baliza",
    "Barro Alto", "Bela Vista de Goiás", "Bom Jardim de Goiás", "Bom Jesus de Goiás",
    "Bonfinópolis", "Bonópolis", "Brazabrantes", "Britânia", "Buriti Alegre",
    "Buriti de Goiás", "Buritinópolis", "Cabeceiras", "Cachoeira Alta", "Cachoeira de Goiás",
    "Cachoeira Dourada", "Caçu", "Caiapônia", "Caldas Novas", "Caldazinha",
    "Campestre de Goiás", "Campinaçu", "Campinorte", "Campo Alegre de Goiás",
    "Campo Limpo de Goiás", "Campos Belos", "Campos Verdes", "Carmo do Rio Verde",
    "Castelândia", "Catalão", "Caturaí", "Cavalcante", "Ceres", "Cezarina",
    "Chapadão do Céu", "Cidade Ocidental", "Cocalzinho de Goiás", "Colinas do Sul",
    "Córrego do Ouro", "Corumbá de Goiás", "Corumbaíba", "Cristalina", "Cristianópolis",
    "Crixás", "Cromínia", "Cumari", "Damianópolis", "Damolândia", "Davinópolis",
    "Diorama", "Divinópolis de Goiás", "Doverlândia", "Edealina", "Edéia",
    "Estrela do Norte", "Faina", "Fazenda Nova", "Firminópolis", "Flores de Goiás",
    "Formosa", "Formoso", "Gameleira de Goiás", "Goianápolis", "Goiandira",
    "Goianésia", "Goiânia", "Goianira", "Goiás", "Goiatuba", "Gouvelândia",
    "Guapó", "Guaraíta", "Guarani de Goiás", "Guarinos", "Heitoraí", "Hidrolândia",
    "Hidrolina", "Iaciara", "Inaciolândia", "Indiara", "Inhumas", "Ipameri",
    "Ipiranga de Goiás", "Iporá", "Israelândia", "Itaberaí", "Itaguari", "Itaguaru",
    "Itajá", "Itapaci", "Itapirapuã", "Itapuranga", "Itarumã", "Itauçu", "Itumbiara",
    "Ivolândia", "Jandaia", "Jaraguá", "Jataí", "Jaupaci", "Jesúpolis", "Joviânia",
    "Jussara", "Lagoa Santa", "Leopoldo de Bulhões", "Luziânia", "Mairipotaba",
    "Mambaí", "Mara Rosa", "Marzagão", "Matrinchã", "Maurilândia", "Mimoso de Goiás",
    "Minaçu", "Mineiros", "Moiporá", "Monte Alegre de Goiás", "Montes Claros de Goiás",
    "Montividiu", "Montividiu do Norte", "Morrinhos", "Morro Agudo de Goiás", "Mossâmedes",
    "Mozarlândia", "Mundo Novo", "Mutunópolis", "Nazário", "Nerópolis", "Niquelândia",
    "Nova América", "Nova Aurora", "Nova Crixás", "Nova Glória", "Nova Iguaçu de Goiás",
    "Nova Roma", "Nova Veneza", "Novo Brasil", "Novo Gama", "Novo Planalto", "Orizona",
    "Ouro Verde de Goiás", "Ouvidor", "Padre Bernardo", "Palestina de Goiás", "Palmeiras de Goiás",
    "Palmelo", "Palminópolis", "Panamá", "Paranaiguara", "Paraúna", "Perolândia",
    "Petrolina de Goiás", "Pilar de Goiás", "Piracanjuba", "Piranhas", "Pirenópolis",
    "Pires do Rio", "Planaltina", "Pontalina", "Porangatu", "Porteirão", "Portelândia",
    "Posse", "Professor Jamil", "Quirinópolis", "Rialma", "Rianápolis", "Rio Quente",
    "Rio Verde", "Rubiataba", "Sanclerlândia", "Santa Bárbara de Goiás", "Santa Cruz de Goiás",
    "Santa Fé de Goiás", "Santa Helena de Goiás", "Santa Isabel", "Santa Rita do Araguaia",
    "Santa Rita do Novo Destino", "Santa Rosa de Goiás", "Santa Tereza de Goiás",
    "Santa Terezinha de Goiás", "Santo Antônio da Barra", "Santo Antônio de Goiás",
    "Santo Antônio do Descoberto", "São Domingos", "São Francisco de Goiás", "São João d'Aliança",
    "São João da Paraúna", "São Luís de Montes Belos", "São Luíz do Norte", "São Miguel do Araguaia",
    "São Miguel do Passa-Quatro", "São Patrício", "São Simão", "Senador Canedo", "Serranópolis",
    "Silvânia", "Simolândia", "Sítio d'Abadia", "Taquaral de Goiás", "Teresina de Goiás",
    "Terezópolis de Goiás", "Três Ranchos", "Trindade", "Trombas", "Turvânia", "Turvelândia",
    "Uirapuru", "Uruaçu", "Uruana", "Urutaí", "Valparaíso de Goiás", "Varjão", "Vianópolis",
    "Vicentinópolis", "Vila Boa", "Vila Propício"
]

# Cria um DataFrame com a lista de municípios
df_municipios = pd.DataFrame(municipios, columns=['Municipio'])

# Adiciona uma nova coluna com o valor 'Goiás' para todas as linhas
df_municipios['dmun_uf_nome'] = 'Goiás'

# Salva o DataFrame em um arquivo CSV
df_municipios.to_csv('municipios_goias.csv', index=False)

print("Tabela criada e salva como 'municipios_goias.csv'")
