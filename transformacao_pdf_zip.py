import os
import zipfile
import pdfplumber  # Para extração de texto de PDFs
import requests

# URLs dos PDFs
urls = [
    'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf',
    'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf'
]

# Criar diretórios para PDFs e TXT, caso não existam
os.makedirs("pdf", exist_ok=True)
os.makedirs("txt", exist_ok=True)

# Baixar PDFs e extrair texto
for i, url in enumerate(urls):
    print(f"Baixando: {url}")
    response = requests.get(url)
    
    # Verificar se o download foi bem-sucedido
    if response.status_code == 200:
        pdf_path = f'pdf/{i}.pdf'
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        print(f"PDF {i} salvo em {pdf_path}")
        
        # Abrir PDF e extrair texto
        with pdfplumber.open(pdf_path) as pdf:
            all_text = ""
            for page in pdf.pages:
                all_text += page.extract_text() + "\n"  # Extrai o texto de todas as páginas
            
        # Salvar texto extraído em arquivo TXT
        txt_path = f'txt/{i}.txt'
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(all_text)
        print(f"Texto do PDF {i} salvo em {txt_path}")
    else:
        print(f"Erro ao baixar PDF {i}: {response.status_code}")

# Compactar PDFs em um arquivo ZIP
zip_filename = "arquivos_pdf.zip"
with zipfile.ZipFile(zip_filename, mode='w') as zipf:
    for file in os.listdir("pdf"):  # Itera pelos arquivos na pasta de PDFs
        zipf.write(f"pdf/{file}", os.path.basename(file))  # Adiciona PDFs ao ZIP
print(f"Arquivo ZIP criado: {zip_filename}")

