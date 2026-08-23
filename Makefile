# =========================
# Azure Bicep - Tech Challenge Fase 2
# =========================

include .env
export

RESOURCE_GROUP=rg-fiap-techchallenge-prod
LOCATION=eastus
MAIN_BICEP=infra/main.bicep
PARAMETERS=infra/parameters/prod.bicepparam
STORAGE_ACCOUNT=stfiaptechchallenge
#KEYVAULT_NAME=kvfiaptechprod
SUBSCRIPTION_ID=e4285dee-2708-4d00-b7a5-9c45f1f37e89
SP_APPID=3686488a-04fc-4d8a-b967-61f98ec41efe

.PHONY: help login rg-create rg-show validate what-if deploy destroy storage-key kv-role-assign list-resources deploy-pipeline run-job

help:
	@echo 'Comandos disponíveis:'
	@echo '  make login          -> Faz login com Service Principal'
	@echo '  make rg-create      -> Cria o Resource Group'
	@echo '  make rg-show        -> Mostra o Resource Group'
	@echo '  make validate       -> Valida o Bicep'
	@echo '  make what-if        -> Simula o deploy'
	@echo '  make deploy         -> Executa o deploy e atribui permissões'
	@echo '  make destroy        -> Remove o Resource Group'
	@echo '  make storage-key    -> Mostra a chave do Storage Account'
	@echo '  make list-resources -> Lista recursos do Resource Group'
	@echo '  make deploy-pipeline-> Cria pipeline ADF que chama job Python no Databricks'
	@echo '  make run-job        -> Executa manualmente o job Python no Databricks (teste)'

login:
	az login \
		--service-principal \
		-u $(AZURE_CLIENT_ID) \
		-p $(AZURE_CLIENT_SECRET) \
		--tenant $(AZURE_TENANT_ID)

	az account set \
		--subscription $(AZURE_SUBSCRIPTION_ID)

rg-create:
	az group create \
		--name $(RESOURCE_GROUP) \
		--location $(LOCATION)

rg-show:
	az group show \
		--name $(RESOURCE_GROUP)

validate:
	az bicep build \
		--file $(MAIN_BICEP)

what-if:
	az deployment group what-if \
		--resource-group $(RESOURCE_GROUP) \
		--parameters $(PARAMETERS)

deploy: login rg-create validate
	az deployment group create \
		--resource-group $(RESOURCE_GROUP) \
		--parameters $(PARAMETERS)
	$(MAKE) kv-role-assign

kv-role-assign:
    az role assignment create \
        --role 'Key Vault Secrets Officer' \
        --assignee $(SP_APPID) \
        --scope '/subscriptions/$(SUBSCRIPTION_ID)/resourceGroups/$(RESOURCE_GROUP)/providers/Microsoft.KeyVault/vaults/$(KEYVAULT_NAME)'

storage-key: login
	@az storage account keys list \
		--resource-group $(RESOURCE_GROUP) \
		--account-name $(STORAGE_ACCOUNT) \
		--query '[0].value' \
		-o tsv

# destroy: login
#	az group delete \
#		--name $(RESOURCE_GROUP) \
#		--yes \
#		--no-wait

list-resources:
	az resource list \
		--resource-group $(RESOURCE_GROUP) \
		-o table

# =========================
# Databricks + Pipeline Python
# =========================

deploy-pipeline: login rg-create validate
	az deployment group create \
		--resource-group $(RESOURCE_GROUP) \
		--template-file $(MAIN_BICEP) \
		--parameters \
			dataFactoryName=$(DATAFACTORY_NAME) \
			databricksHost=$(AZURE_DATABRICKS_HOST) \
			databricksToken=$(AZURE_DATABRICKS_TOKEN) \
			sparkJob=$(SPARK_JOB) \
			googleApplicationCredentials=$(GOOGLE_APPLICATION_CREDENTIALS) \
			bronzeContainer=$(AZURE_CONTAINER_BRONZE)

run-job:
	databricks jobs run-now \
		--host $(AZURE_DATABRICKS_HOST) \
		--token $(AZURE_DATABRICKS_TOKEN) \
		--job-id $(SPARK_JOB)

upload-job:
	databricks workspace import \
		--host $(AZURE_DATABRICKS_HOST) \
		--token $(AZURE_DATABRICKS_TOKEN) \
		./jobs/main.py \
		$(SPARK_JOB) \
		-l PYTHON \
		-o
