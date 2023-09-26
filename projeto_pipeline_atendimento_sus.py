import pandas as pd
import requests

# PARTE 1 - Obter arquivo e extrair os dados
arquivo_atendimento_sus = 'AtendimentoSus_RegiaoBrotasSSA.xlsx'

df = pd.read_excel(arquivo_atendimento_sus)

# PARTE 2 - Efetuar algum processo de transformação
# consulta de informação georeferencial na api do Google 
endereco_completo = {}

API_KEY = 'sua_api_key'

for linha in df.itertuples():
    
    #leitura dos dados
    endereco = linha.Logradouro+', '+linha.Bairro+' SALVADOR BA BRASIL'
    unidade = linha.Unidade

    #busca na api
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={endereco}&key={API_KEY}'

    response = requests.get(url)
    data = response.json()

    #extrai as coordenadas geográficas
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        endereco_completo[linha.Index] = {'Unidade': unidade, 'Logradouro': endereco, 'Latitude': latitude, 'Longitude': longitude}
    else:
        endereco_completo[linha.Index] = {'Unidade': unidade, 'Logradouro': endereco, 'Latitude': 'não encontrada', 'Longitude': 'não encontrada'}

# PARTE 3 - Carga em um arquivo de saida

df_final = pd.DataFrame.from_dict(endereco_completo, orient='index')
df_final.to_excel('AtendimentoSus_RegiaoBrotasSSA_Georeferencia.xlsx', index_label='ID', engine='openpyxl')
