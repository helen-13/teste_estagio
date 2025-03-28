import requests
import os

# Diretório para salvar os arquivos
output_dir = "dados_csv"
os.makedirs(output_dir, exist_ok=True)

# URLs e nomes de arquivos de saída
urls = [
    'https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/',
    'https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/'
]
output_files = [
    os.path.join(output_dir, 'demonstracoes_contabeis.csv'),
    os.path.join(output_dir, 'operadoras_ativas.csv')
]

# Função para baixar arquivos
def baixar_arquivo(url, output_file):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"Arquivo {output_file} salvo com sucesso!")
        else:
            print(f"Erro ao acessar {url}. Código de status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar baixar {url}: {e}")

# Baixar cada arquivo
for url, output_file in zip(urls, output_files):
    baixar_arquivo(url, output_file)

'''CREATE TABLE demonstracoes_contabeis (
    id_demonstracao_contabil INT PRIMARY KEY,
    id_operadora INT NOT NULL,
    id_plano_saude INT NOT NULL,
    id_procedimento INT,
    id_atendimento INT,
    id_paciente INT,
    id_profissional INT,
    id_convenio INT,
    data_atendimento DATE,  
    valor_total DECIMAL(10, 2),
    valor_desconto DECIMAL(10, 2),
    valor_liquido DECIMAL(10, 2),
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE operadoras_ativas (
    id_operadora INT PRIMARY KEY,   
    nome_operadora VARCHAR(255) NOT NULL,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);'''
'''LOAD DATA INFILE '/caminho/dados_csv/demonstracoes_contabeis.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/caminho/dados_csv/operadoras_ativas.csv'
INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;'''