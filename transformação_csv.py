import requests
import os
import zipfile
import pdfplumber
import csv

# URL do PDF
url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

# Criar diretórios para PDFs e CSVs, caso não existam
os.makedirs("pdf", exist_ok=True)
os.makedirs("csv", exist_ok=True)

# Função para baixar PDFs e extrair texto
def process_pdf(url, index):
    print(f"Baixando: {url}")
    response = requests.get(url)
    
    # Verificar se o download foi bem-sucedido
    if response.status_code == 200:
        pdf_path = f'pdf/{index}.pdf'
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        print(f"PDF {index} salvo em {pdf_path}")
        
        # Abrir PDF e extrair texto
        csv_path = f'csv/{index}.csv'
        with pdfplumber.open(pdf_path) as pdf:
            with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                for page in pdf.pages:
                    # Extraia as linhas da página como texto separado por tabulações ou espaços
                    for line in page.extract_text().split('\n'):
                        # Divida as linhas em colunas, se necessário
                        row = line.split()  # Ajuste conforme o formato do PDF
                        writer.writerow(row)
        print(f"Dados extraídos do PDF {index} e salvos em {csv_path}")
        return True
    else:
        print(f"Erro ao baixar o PDF {index}: {response.status_code}")
        return False

# Processar o PDF
if process_pdf(url, 0):
    # Compactar arquivos CSV em um arquivo ZIP
    zip_filename = "Teste_HelenFreire_csv.zip"
    with zipfile.ZipFile(zip_filename, mode='w') as zipf:
        for file in os.listdir("csv"):  # Itera pelos arquivos na pasta "csv"
            zipf.write(f"csv/{file}", os.path.basename(file))  # Adiciona CSVs ao ZIP
    print(f"Arquivos CSV compactados em: {zip_filename}")
else:
    print("Falha no processo de download ou extração.")