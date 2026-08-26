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
BASE_DADOS_INEP = "https://basedosdados.org/dataset/073a39d4-89cf-4068-b1e8-34ed0d9c0b72?table=e1de7a6a-5038-4e81-89f0-a15f2cc12c9b"

ANOS = (2024, 2025)
META_BRASIL = {2023: 54.0, 2024: 60.0, 2025: 64.0}

Dado o código que puxa os dados do Google BigQuery com sucesso para o container do Azure. Código no GitHub https://github.com/FIAPCientistasDados/postech-aisc-fase-2-pipeline-azure-g23/blob/main/jobs/main.ipynb ​‌
Preciso criar uma rotina que dispare esse notebook .ypnb (também tenho o mesmo código em Python) no Azure para rodar todos os dias 06h00. Qual o melhor jeit, veja que para conexão no Google só tenho o ID da Base de Dados BigQuery e o json "tough-medley".

Estou executando o pipeline "no Azure" de forma automatizada; você está executando localmente pelo VS Code, usando o JSON da Service Account do GCP para acessar o BigQuery.

Teste compartilhando GitHub no Databricks

Seguem as pastas compartilhadas do código no Databricks Azure, só para edição. A codificação segue no GitHub, mas ao salvar no GitHub atualiza aitomaticamente no Azure Databricks.

O que esse notebook faz
Usa Parquet em vez de CSV (mais eficiente e otimizado para leitura em Big Data).

Mostra o df.head() em cada lote para você visualizar os dados simulados diretamente no notebook.

Funciona tanto localmente (via .env) quanto em Databricks (via Key Vault).

Grava os dados no container bronze, organizados em partições por data/hora.

Simula streaming contínuo com lotes de dados chegando em intervalos regulares.

👉 Agora você tem dados simulados chegando no bronze em formato Parquet e consegue inspecionar cada lote no notebook.

A diferença entre os diretórios simulado e streaming no notebook é conceitual:

📂 inep_alunos_simulado

Representa um lote único de dados gerados de forma estática.

É como se fosse uma carga inicial ou um batch de teste.

Útil para validar o pipeline, checar schema, testar ingestão e garantir que o formato (Parquet) está correto.

Normalmente usado como “snapshot” de dados fictícios.

📂 inep_alunos_streaming

Representa dados chegando em tempo contínuo, em pequenos lotes.

Cada execução do loop gera um novo arquivo particionado por data/hora (YYYY/MM/DD/HHMMSS).

Simula o comportamento de um fluxo real de eventos, como se viessem de um Event Hub ou Kafka.

Útil para testar cenários de ingestão incremental, monitoramento e consumo em tempo real.

👉 Em resumo:

Simulado = carga única, estática, para teste inicial.

Streaming = múltiplos lotes em sequência, simulando fluxo contínuo de dados.

Isso te dá flexibilidade: você pode usar o simulado para validar o pipeline e o streaming para testar como o sistema reage a dados chegando em tempo real.


1 - Entrar no Portal Azure com o RM da Fiap e senha da Microsoft (igual à do Teams), talvez precisa que o celular tenha o app Microsoft Authenticator instalado.
https://portal.azure.com/

2- Baixar o projeto do GitHub 
> git clone https://github.com/FIAPCientistasDados/postech-aisc-fase-2-pipeline-azure-g23

3 - Utilizar o VSCode com WSL Ubuntu preferencialmente

4 - Abrir um ambiente virtual VENV
4.1 -  criar uma VENV
> python3.13 -m venv venv

4.2 - ativar a VENV
> venv\Scripts\activate.bat

4.3 - instalar o requirements.txt

5 - Dentro da pasta do projeto "postech-aisc-fase-2-pipeline-azure-g23" rodar com
> make deploy 

# 6 - Depois, com a ajuda do CoPilot procure todas as variáveis necessárias do ENV abaixo.

# =========================
# GOOGLE
# =========================
GCP_PROJECT_ID="????????????"
GOOGLE_APPLICATION_CREDENTIALS=???????????????????????.json
# =========================
# AZURE
# =========================
AZURE_STORAGE_ACCOUNT="stfiapoin4ci2kb4w7c" 
# AZURE-STORAGE-ACCOUNT
AZURE_STORAGE_CONTAINER="bronze"

#KEY1
AZURE_STORAGE_KEY="????????????????????????"
AZURE_STORAGE_CONNECTION = "??????????????????????????????????????????????????????????"

# 
AZURE_TENANT_ID="??????????????????????"
AZURE-CLIENT-ID="?????????????????????????"
AZURE_CLIENT_SECRET="??????????????????????????????"
AZURE_SUBSCRIPTION_ID="?????????????????????"

AZURE_RESOURCE_GROUP=rg-fiap-techchallenge-prod
AZURE_LOCATION=eastus

# =========================
# Databricks
# =========================
AZURE_DATABRICKS_HOST=??????????????
AZURE_DATABRICKS_TOKEN="????????????????"
# Caminho do job Spark (Notebook ou script Python)
SPARK_JOB=/Repos/fiap-techchallenge/jobs/main.py
# Arquivo de logs
SPARK_LOG=logs/spark_output.log
# Containers
AZURE_CONTAINER_BRONZE=bronze
AZURE_CONTAINER_SILVER=silver
AZURE_CONTAINER_GOLD=gold
AZURE_KEYVAULT_NAME=kvfiaptechprod

RESOURCE_GROUP="rg-fiap-techchallenge-prod"
STORAGE_ACCOUNT="?????????"
EVENTHUB_NAMESPACE="evh-fiap-techchallenge"
DATABRICKS_WORKSPACE="dbw-fiap-techchallenge"
LOG_ANALYTICS_WORKSPACE="law-fiap-techchallenge"

Teste

Teste2


