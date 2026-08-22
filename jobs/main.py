# Databricks notebook script
# BigQuery → Azure Blob usando Service Account JSON
# Exporta tabelas do BigQuery em formato Parquet para o Azure Blob Storage

import os
import datetime as dt
from google.cloud import bigquery
from azure.storage.blob import BlobServiceClient

# =========================
# Parâmetros vindos do Databricks (widgets)
# =========================
GOOGLE_APPLICATION_CREDENTIALS = dbutils.widgets.get('GOOGLE_APPLICATION_CREDENTIALS')  # caminho do JSON no DBFS
BRONZE_CONTAINER = dbutils.widgets.get('BRONZE_CONTAINER')  # nome do container no Blob (ex: bronze)

# Configura variável de ambiente para BigQuery
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS

# Cliente BigQuery
project_id = os.getenv('GCP_PROJECT_ID', 'tough-medley-505300-k1')
bq_client = bigquery.Client(project=project_id)

# Cliente Azure Blob
storage_account = os.getenv('AZURE_STORAGE_ACCOUNT')
storage_key = os.getenv('AZURE_STORAGE_KEY')

blob_service_client = BlobServiceClient(
    f'https://{storage_account}.blob.core.windows.net',
    credential=storage_key
)

# =========================
# Função de exportação
# =========================
def export_bigquery_table_to_blob(source_table: str, blob_container: str, blob_name: str):
    '''
    Exporta uma tabela do BigQuery direto para Azure Blob em formato Parquet.
    '''
    try:
        query = f'SELECT * FROM `{source_table}`'
        query_job = bq_client.query(query, location='US')

        # Converte resultado para DataFrame Pandas
        df = query_job.to_dataframe()

        # Adiciona colunas de auditoria
        ingested_at = dt.datetime.now(dt.timezone.utc).isoformat()
        df['_ingested_at'] = ingested_at
        df['_source_table'] = source_table

        # Salva localmente em Parquet (no DBFS)
        local_file = '/dbfs/tmp/temp.parquet'
        df.to_parquet(local_file, index=False)

        # Upload para Blob
        blob_client = blob_service_client.get_blob_client(container=blob_container, blob=blob_name)
        with open(local_file, 'rb') as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f'✅ Exportado {source_table} direto para azure://{blob_container}/{blob_name}')

    except Exception as e:
        print(f'❌ Erro ao exportar {source_table} para Blob: {e}')

# =========================
# Lista de tabelas para exportar
# =========================
sources = [
    ('basedosdados.br_inep_avaliacao_alfabetizacao.uf', 'uf.parquet'),
    ('basedosdados.br_inep_avaliacao_alfabetizacao.meta_alfabetizacao_brasil', 'meta_alfabetizacao_brasil.parquet'),
    ('basedosdados.br_inep_avaliacao_alfabetizacao.meta_alfabetizacao_uf', 'meta_alfabetizacao_uf.parquet'),
    ('basedosdados.br_inep_avaliacao_alfabetizacao.meta_alfabetizacao_municipio', 'meta_alfabetizacao_municipio.parquet'),
    ('basedosdados.br_inep_avaliacao_alfabetizacao.municipio', 'municipio.parquet')
]

# =========================
# Executa exportação
# =========================
for source_table, blob_name in sources:
    export_bigquery_table_to_blob(source_table, BRONZE_CONTAINER, blob_name)
