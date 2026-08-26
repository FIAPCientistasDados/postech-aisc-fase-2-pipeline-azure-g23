# =========================
# Secrets
# =========================

import os

from pyspark.dbutils import DBUtils
from pyspark.sql import SparkSession

# =========================
# Databricks
# =========================

spark = SparkSession.getActiveSession()

dbutils = DBUtils(spark)

# =========================
# Key Vault
# =========================

KEYVAULT_SCOPE = "kvfiaptechprod"

# =========================
# Função
# =========================

def get_secret(
    secret_name: str,
    env_name: str = None
):
    """
    Busca primeiro no Databricks Secret Scope.
    Caso não encontre, utiliza variável
    de ambiente local.
    """

    try:

        return dbutils.secrets.get(
            scope=KEYVAULT_SCOPE,
            key=secret_name
        )

    except Exception:

        if env_name:

            value = os.getenv(
                env_name
            )

            if value:
                return value

        return None