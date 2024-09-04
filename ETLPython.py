import pandas as pd
from pandas.tseries.offsets import MonthEnd 

# Carregar os dados
df_fOrigem = pd.read_csv('origem.csv')
df_dMunicipio = pd.read_csv('d_municipio.csv')
df_dTempo = pd.read_csv('d_tempo.csv')

# Renomear colunas
df_origem_renomear = df_fOrigem.rename(columns={'co_municipio_residencia_atual': 'dmun_codibge', 'dt_diagnostico_sintoma':'dte_id'})

# Conversao
df_origem_renomear['dte_id'] = pd.to_datetime(df_origem_renomear['dte_id'], errors='coerce')
df_dTempo['dte_id'] = pd.to_datetime(df_dTempo['dte_id'], errors='coerce')

# Merge 
df_origem_municipio = pd.merge(df_origem_renomear, df_dMunicipio, how='left', on='dmun_codibge')
df_origem = pd.merge(df_origem_municipio, df_dTempo, how='left', on='dte_id')

# Filtrar somente datas após 2021 e apenas municípios de Goiás
df_origem_filtro = df_origem[(df_origem['dte_id'] > '2021-01-01') & (df_origem['dmun_uf_nome'] == 'Goiás')]

# Dicionário de meses em português
meses_portugues = {
    'January': 'Janeiro',
    'February': 'Fevereiro',
    'March': 'Março',
    'April': 'Abril',
    'May': 'Maio',
    'June': 'Junho',
    'July': 'Julho',
    'August': 'Agosto',
    'September': 'Setembro',
    'October': 'Outubro',
    'November': 'Novembro',
    'December': 'Dezembro'
}

# Função para converter o mês para português
def mes_para_portugues(data):
    mes_ingles = data.strftime('%B')
    return meses_portugues.get(mes_ingles, mes_ingles) + ' De ' + data.strftime('%Y')

# Criar a coluna formatada usando a função personalizada
df_origem_filtro['dte_id_formatado'] = df_origem_filtro['dte_id'].apply(mes_para_portugues)

# Selecionar apenas colunas necessárias e filtrar apenas casos novos de tuberculose pulmonar
# Assumindo que 'tp_forma' indica que é tuberculose pulmonar e 'tp_entrada' indica casos novos
cte1 = df_origem_filtro[
    (df_origem_filtro['tp_entrada'].isin([1, 6])) & 
    (df_origem_filtro['tp_forma'].isin([1, 3])) & 
    (df_origem_filtro['tp_situacao_encerramento'] != 6)
][[
    'dmun_municipio',
    'dte_id_formatado'
]]

# Contar o número de casos novos por município e data
resultado = cte1.groupby(['dmun_municipio', 'dte_id_formatado']).size().reset_index(name='Quantidade_Tuberculose')

# Salvar o resultado em um arquivo CSV
resultado.to_csv('saida.csv', index=False)
