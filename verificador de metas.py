import pandas as pd
from twilio.rest import Client


account_sid ='AC878cb8a181157482160649dee4ee0070'
auth_token = 'd9f6a69fdaa03c776eeeaf30dcd7c70d'
client = Client(account_sid, auth_token)

# abrir arquivos em excel
lista_meses = ['janeiro', 'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' ]

for mes in lista_meses:
   tabela_vendas = pd.read_excel(f'{mes}.xlsx')

   if (tabela_vendas['Vendas'] > 55000).any():
      vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
      vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
      print(f'no mês de  {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
      message = client.messages.create(
                     to='+5511998463503',
                     from_ = '+14158554714',
                     body = f'no mês de  {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'
      )
      print(message.sid)





