from google.cloud import bigquery
from azure.storage.blob import BlobServiceClient

from datetime import datetime
from dotenv import load_dotenv

import pandas as pd
import os

load_dotenv()

# GCP
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = (
    r'F:\tough-medley-505300-k1-164371097431.json'
)

# Azure
AZURE_CONNECTION_STRING = os.getenv(
    'AZURE_STORAGE_CONNECTION_STRING'
)

# BigQuery
bq_client = bigquery.Client(
    project='tough-medley-505300-k1'
)

# Consulta
query = '''
SELECT *
FROM `basedosdados.br_inep_avaliacao_alfabetizacao.uf`
'''

df = bq_client.query(query).to_dataframe()

# Data de ingestão
dt_ingestao = datetime.now().strftime('%Y-%m-%d')

# Salva parquet
arquivo_local = 'dados.parquet'

df.to_parquet(
    arquivo_local,
    index=False
)

# Azure
blob_service = BlobServiceClient.from_connection_string(
    AZURE_CONNECTION_STRING
)

blob_path = (
    f'uf/'
    f'dt_ingestao={dt_ingestao}/'
    f'dados.parquet'
)

blob_client = blob_service.get_blob_client(
    container='bronze',
    blob=blob_path
)

with open(arquivo_local, 'rb') as data:
    blob_client.upload_blob(
        data,
        overwrite=True
    )

print(
    f'✅ bronze/{blob_path}'
)