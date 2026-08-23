#### 🚀 Tech Challenge FIAP - Fase 2

Metodologia: PIPELINE / ARQUITETURA MEDALHÃO

🧑‍🤝‍🧑 **Integrantes do Grupo 23**:

 ✅ Célia Maria Tomitsuka - RM374490

 ✅ Nelson da Silva Paz - RM374983

 ✅ Nelson Toshikazu Yamamoto - RM374494

---

📊 Projeto de Ingestão e Pipeline de Dados — FIAP Cientistas de Dados
🎯 Objetivo
Este projeto tem como finalidade construir um pipeline de ingestão batch que exporta dados do BigQuery para o Azure Blob Storage, organizando-os em camadas (bronze, silver e gold) e permitindo que sejam processados posteriormente no Databricks.

A arquitetura segue boas práticas de Data Lakehouse, garantindo escalabilidade, versionamento e governança dos dados.

🏗️ Arquitetura
🔎 Visão Geral
BigQuery (Fonte de Dados)

Dados públicos e institucionais são consultados diretamente no BigQuery.

Exportação realizada em formato Parquet para otimizar leitura e compressão.

Azure Blob Storage (Data Lake)

Camada Bronze: dados brutos exportados do BigQuery.

Camada Silver: dados tratados e normalizados no Databricks.

Camada Gold: dados prontos para consumo analítico e dashboards.

Databricks (Processamento)

Notebooks versionados no Repos (integrados ao GitHub).

Transformações PySpark/Pandas para limpeza e enriquecimento dos dados.

Uso do Auto Loader para ingestão contínua de novos arquivos.

GitHub Actions (Orquestração)

Automatiza a execução do pipeline de ingestão.

Configurado para rodar a cada 1 hora, garantindo atualização periódica dos dados.

⚙️ Infraestrutura com Bicep
A infraestrutura é provisionada via Bicep, linguagem declarativa nativa do Azure para IaC (Infrastructure as Code).

🔎 Recursos criados
Storage Account

Containers: bronze, silver, gold.

Configuração de chaves de acesso e integração com Databricks.

Databricks Workspace

Cluster configurado para processamento distribuído.

Integração com GitHub Repos.

Key Vault

Armazena credenciais sensíveis (BigQuery Service Account, Storage Keys).

Automation/Jobs

Orquestração do pipeline via GitHub Actions ou Azure Data Factory.

✅ Exemplo de trecho Bicep
bicep
resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: 'stfiapoin4ci2kb4w7c'
  location: resourceGroup().location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

resource bronzeContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2022-09-01' = {
  name: '${storageAccount.name}/default/bronze'
  properties: {
    publicAccess: 'None'
  }
}
🚀 Fluxo de Dados
Ingestão

Script Python exporta tabelas do BigQuery → Blob (camada bronze).

Nome dos arquivos versionado com sufixo de data (AAA-MM-DD_tabela.parquet).

Transformação

Databricks lê os Parquets da bronze.

Aplica limpeza, normalização e enriquecimento.

Grava resultados na camada silver.

Consumo

Dados gold disponíveis para dashboards, relatórios e análises avançadas.

📌 Conclusão
Este projeto demonstra uma arquitetura moderna de Data Lakehouse integrada entre Google BigQuery e Azure Databricks, com Blob Storage como camada de persistência e Bicep para provisionamento de infraestrutura.

A combinação de GitHub Actions e Databricks Jobs garante automação e escalabilidade, permitindo que os dados sejam atualizados continuamente sem intervenção manual.

## Estrutura de pastas no GitHub (CORRIGIR)

tech-challenge/
├── data/
│   ├── raw/                                        # Dados originais
│   └── processed/                                  # Dados processados 
|__ docs
|   |__ tech_challenge_fase1
|        |__ 1IAST - Fase 1 - Tech Challenge1.pdf   # Arquivo PDF
├── notebooks/
│   ├── 1. Entendimento do negócio.ipynb            # Entendimento do negócio
|   ├── 2. Definição da Target.ipynb                # Target
|   ├── 3. Análise_Exploratória_dos_Dados.ipynb     # EDA
|   ├── 4. Modelo preditivo.ipynb                   # Modelo preditivo
├── reports/
│   ├── NPS_Apresentacao_Fase1.pptx                 # Apresentação executiva
│   └── Video_link_aprresentacao.md                 # Apresentação executiva
├── src/
├── README.md
└── environment.yml


## Como Reproduzir os resultados

### 1. Clone o repositório

git clone git clone https://github.com/FIAPCientistasDados/postech-aisc-fase-2-pipeline-azure-g23
cd postech-aisc-fase-2-pipeline-azure-g23

### 2. No PowerShell, crie e ative o ambiente virtual

conda env create -f environment.yml

# Ativar o ambiente

conda activate fase2

---

Ou com o Python:
git clone git clone https://github.com/FIAPCientistasDados/postech-aisc-fase-2-pipeline-azure-g23
cd postech-aisc-fase-2-pipeline-azure-g23
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

---

### 3. Suba o projeto e execute o notebook com o código de ingestao

1. make deploy
2. main.ipynb

---

## Apresentação executiva (material e link)

- **Apresentação executiva:** [`reports/ALFABETIZACAO_Apresentacao_Fase2.pptx`]
- **Vídeo executivo (5 min):** (https://www.loom.com/share/42f2a8fe7d0c45008f4cf486e4812d7f???????????????)

--- Dados IBGE
IBGE_BR_ESTADOS = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
IBGE_BR_MUNICIPIOS = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

ANOS = (2024, 2025)
META_BRASIL = {2023: 54.0, 2024: 60.0, 2025: 64.0}
