import os

KEYVAULT_SCOPE = "kvfiaptechprod"


def get_secret(secret_name: str,
               env_name: str = None):
    """
    Busca primeiro no Secret Scope do Databricks.
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
            return os.getenv(env_name)

        return None