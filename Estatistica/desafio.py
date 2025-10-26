"""Nesse desafio trataremos um dicionário utilizando as bibliotecas Pandas e MatplotLib 
   para obter a média de vendas de uma loja e trazer visualizações mais objetivas utilizando gráficos de barra e linhas.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Melhorar a visualização dos valores
def formatar_milhares(valor, pos):
    return f'{int(valor/1000)}'

# Dicionário de faturamento
dict_faturamento = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
        ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
        ]
}

df_faturamento = pd.DataFrame.from_dict(dict_faturamento) 
df_faturamento['data_ref'] = pd.to_datetime(df_faturamento['data_ref'])
df_faturamento = df_faturamento.sort_values('data_ref')
print(df_faturamento)

media_vendas = df_faturamento['valor'].mean()
print(f"\nA média das vendas foram R${media_vendas:.2f}")

# Para plotar o gráfico
df_faturamento['mes_ano'] = df_faturamento['data_ref'].dt.strftime('%m/%Y') # No primeiro gráfico estavam aparecendo as horas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5)) # Plota os dois gráficos lado a lado e aumenta a visualização para mostrar todas as datas
df_faturamento.plot.bar(x="mes_ano",y='valor', ax=ax1)
ax1.set_xlabel('Mês/Ano')
ax1.set_ylabel('Valor (R$1000,00)')
ax1.set_title('Gráfico de barras verticais')
ax1.yaxis.set_major_formatter((formatar_milhares))


df_faturamento.plot.line(x='mes_ano',y="valor", ax=ax2)
ax2.set_xlabel('Mês/Ano')
ax2.set_ylabel('Valor (R$1000,00)')
ax2.set_title('Gráfico de linha')
ax2.yaxis.set_major_formatter((formatar_milhares))


plt.tight_layout() #Melhora a visualização
plt.show()
