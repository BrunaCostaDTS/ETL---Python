import pandas as pd
from pandas.tseries.offsets import MonthEnd 

# Carregar os dados
df_fOrigem = pd.read_csv('origem.csv')
df_dMunicipio = pd.read_csv('d_municipio.csv')
df_dTempo = pd.read_csv('d_tempo.csv')
df_mungoias = pd.read_csv('municipios_goias.csv')

# Renomear colunas
df_origem_renomear = df_fOrigem.rename(columns={'co_municipio_residencia_atual': 'dmun_codibge', 'dt_diagnostico_sintoma':'dte_id'})

# Conversao
df_origem_renomear['dte_id'] = pd.to_datetime(df_origem_renomear['dte_id'], errors='coerce')
df_dTempo['dte_id'] = pd.to_datetime(df_dTempo['dte_id'], errors='coerce')

# Merge 
df_origem_municipio = pd.merge(df_origem_renomear, df_dMunicipio, how='left', on='dmun_codibge')
df_origem = pd.merge(df_origem_municipio, df_dTempo, how='left', on='dte_id')

# Filtrar somente datas após 2021
df_origem_filtro = df_origem[df_origem['dte_id'] > '2021-01-01']

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

# Selecionar colunas desejadas
cte1 = df_origem_filtro[[
    'dmun_uf_nome',
    'dmun_municipio',
    'nu_notificacao',
    'tp_entrada',
    'tp_forma',
    'tp_situacao_encerramento',
    'dte_id_formatado'
]]

# Criar um DataFrame com todos os estados e meses possíveis
estados = df_origem_filtro['dmun_uf_nome'].unique()
meses = df_origem_filtro['dte_id_formatado'].unique()
estados_meses = pd.MultiIndex.from_product([estados, meses], names=['dmun_uf_nome', 'dte_id_formatado']).to_frame(index=False)

# Realizar a agregação
aggregado = cte1.groupby(['dmun_uf_nome', 'dmun_municipio', 'dte_id_formatado']).agg(
    Quantidade_Tuberculose=pd.NamedAgg(
        column='tp_entrada',
        aggfunc=lambda x: (
            ((x.isin([1, 6])) & 
            (cte1['tp_forma'].isin([1, 3])) & 
            (cte1['tp_situacao_encerramento'] != 6))
        ).sum()
    ),
    Quantidade_Tuberculose_Goias=pd.NamedAgg(
        column='tp_entrada',
        aggfunc=lambda x: (
            ((x.isin([1, 6])) & 
            (cte1['tp_forma'].isin([1, 3])) & 
            (cte1['tp_situacao_encerramento'] != 6) & 
            (cte1['dmun_uf_nome'] == 'Goiás'))
        ).sum()
    )
).reset_index()

# Juntar com o DataFrame com todos os estados e meses possíveis
resultado = pd.merge(estados_meses, agregada, on=['dmun_uf_nome', 'dte_id_formatado'], how='left')

# Substituir NaN por 0
resultado.fillna(0, inplace=True)

# Salvar o resultado em um arquivo CSV
resultado.to_csv('saida.csv', index=False)
