# =========================
# Secrets
# =========================

import os

# =========================
# Configuração
# =========================

KEYVAULT_SCOPE = "kvfiaptechprod"

# =========================
# Inicialização Databricks
# =========================

dbutils = None

try:

    from pyspark.sql import SparkSession
    from pyspark.dbutils import DBUtils

    spark = SparkSession.getActiveSession()

    if spark is not None:

        dbutils = DBUtils(spark)

        print(
            "✅ Databricks detectado. "
            "Secret Scope habilitado."
        )

except Exception:

    print(
        "⚠️ Ambiente local detectado. "
        "Utilizando variáveis de ambiente."
    )

# =========================
# Função
# =========================

def get_secret(
    secret_name: str,
    env_name: str = None
):
    """
    Busca primeiro no Databricks Secret Scope.

    Caso não encontre ou esteja em ambiente local,
    utiliza variável de ambiente.
    """

    # -------------------------
    # Databricks Secret Scope
    # -------------------------

    if dbutils is not None:

        try:

            return dbutils.secrets.get(
                scope=KEYVAULT_SCOPE,
                key=secret_name
            )

        except Exception:

            pass

    # -------------------------
    # Variável de ambiente
    # -------------------------

    if env_name:

        value = os.getenv(
            env_name
        )

        if value:

            return value

    # -------------------------
    # Não encontrado
    # -------------------------

    return None