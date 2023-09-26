Exemplo simples de pipeline de ETL em Python.

1: Extração e leitura de dados
Fonte utilizada: arquivo excel. Como exemplo foi utilizada uma base de rede de atendimento do SUS

2: Transformação
A partir do endereço de cada unidade foi verificada na API do Google as informações de Latitude e Longitude, para uma possível aplicação com georeferência

3: É feita a carga de uma nova base de dados com informações atualizadas a partir da busca na API.