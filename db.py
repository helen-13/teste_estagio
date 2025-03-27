import requests

# URLs dos arquivos
urls = [
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/",
    "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"
]

# Nomes dos arquivos que serão salvos localmente
files = ["demonstracoes_contabeis.zip", "operadoras_ativas.csv"]

# Fazer download dos arquivos
for url, file in zip(urls, files):
    print(f"Baixando {file} de {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(file, "wb") as f:
            f.write(response.content)
        print(f"Arquivo {file} salvo com sucesso!")
    else:
        print(f"Erro ao baixar {file}: {response.status_code}")
'''LOAD DATA INFILE '/caminho/demonstracoes_contabeis.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/caminho/operadoras_ativas.csv'
INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
'''