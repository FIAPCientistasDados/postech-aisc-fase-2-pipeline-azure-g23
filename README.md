# Alfabetização Brasil — Pipeline de Dados (Camada Gold)
Pipeline de dados em **Databricks + Delta Lake** que consolida indicadores de alfabetização municipal, estadual e nacional, com **qualidade de dados (DQ)**, **rastreabilidade** e **auditoria** em cada etapa.
> Objetivo de negócio: monitorar o cumprimento das metas de alfabetização dos municípios brasileiros entre **2023 e 2024**, identificando onde o Brasil avançou e onde ainda está aquém.
---
### Arquitetura```mermaidflowchart LR    subgraph SILVER["Camada Silver (Delta)"]        S1["silver.indicador_municipio"]        S2["silver.meta_municipio"]        S3["silver.dim_ibge_municipios"]    end
    subgraph GOLD["Camada Gold (Delta)"]        F["gold.fato_alfabetizacao_municipio"]        V1["gold.visao_uf"]        V2["gold.visao_brasil"]        V3["gold.consolidacao_validacao"]    end
    S1 --> F    S2 --> F    S3 --> F    F --> V1    F --> V2    V1 --> V3    V2 --> V3```
**Camada Silver (entrada):** dados já tratados e padronizados por município.**Camada Gold (saída):** dados consolidados, particionados e otimizados para consumo analítico.
---
### Fluxo de Processamento```mermaidflowchart TD    A["Leitura das tabelas Silver"] --> B["Transformações e cálculo de indicadores"]    B --> C["Data Quality: nulos e duplicados na chave"]    C --> D{"Chave íntegra?"}    D -->|"Sim"| E["Gravação via CTAS em Delta"]    D -->|"Não"| H["Registro de falha em monitoring.dq_results"]    E --> F["OPTIMIZE + ZORDER BY"]    F --> G["Validação final e leitura"]    H --> B```
Cada notebook segue o padrão: **leitura → agregação → DQ → CTAS → ZORDER → validação**.
---
### Tabelas Geradas
| Tabela | Granularidade | Registros | Papel ||--------|---------------|-----------|-------|| `gold.fato_alfabetizacao_municipio` | `(ano, id_municipio, rede)` | 10.704 | Base detalhada: resultado × meta por município || `gold.visao_uf` | `(ano, estado_sigla, rede)` | 50 | Comparativo entre estados || `gold.visao_brasil` | `(ano, rede)` | 2 | Painel executivo nacional (2023 e 2024) |
### Estrutura dos Notebooks
| Notebook | Saída | Tipo ||----------|-------|------|| `01_gold_fato_alfabetizacao_municipio` | `gold.fato_alfabetizacao_municipio` | Gravação (CTAS) || `02_gold_visao_uf` | `gold.visao_uf` | Gravação (CTAS) || `03_gold_visao_brasil` | `gold.visao_brasil` | Gravação (CTAS) || `04_gold_consolidacao_validacao` | — | Somente leitura / validação |
---
### Dicionário de Dados
#### `gold.fato_alfabetizacao_municipio`
| Coluna | Descrição ||--------|-----------|| `ano` | Ano de referência (2023, 2024) || `id_municipio` | Código IBGE do município || `estado_sigla` | UF (AC, AL, AM, ...) || `rede` | Código da rede de ensino || `rede_nome` | Nome da rede (ex.: Municipal) || `resultado` | Taxa de alfabetização observada || `meta` | Meta de alfabetização definida (NULL em 2023) || `folga_pp` | Diferença em pontos percentuais (resultado − meta) || `status_meta` | `ATINGIU`, `NAO_ATINGIU` ou `SEM_META` || `ingested_at`, `source`, `version` | Rastreabilidade |
#### `gold.visao_uf` e `gold.visao_brasil`
| Coluna | Descrição ||--------|-----------|| `total_municipios` | Total de registros no grupo || `municipios_distintos` | Municípios únicos (apenas visão Brasil) || `taxa_media` | Média da taxa de alfabetização || `meta_media` | Média das metas || `pct_atingiram_meta` | % de municípios que atingiram a meta || `municipios_atingiram` / `municipios_sem_meta` | Contagens absolutas |
#### Relacionamento entre tabelas```mermaiderDiagram    FATO ||--o{ VISAO_UF : "agrega por (ano, UF, rede)"    FATO ||--o{ VISAO_BRASIL : "agrega por (ano, rede)"    FATO {        int ano        int id_municipio        string estado_sigla        string rede_nome        double resultado        double meta        string status_meta    }    VISAO_UF {        int ano        string estado_sigla        string rede_nome        double taxa_media        double meta_media        double pct_atingiram_meta    }    VISAO_BRASIL {        int ano        string rede_nome        int total_municipios        double taxa_media        double pct_atingiram_meta    }```
---
### Qualidade de Dados
Todas as chaves foram validadas sem nulos e sem duplicados. Cada execução registra o resultado em `monitoring.dq_results` para auditoria.
| Tabela | Chave composta | Nulos | Duplicados ||--------|----------------|-------|------------|| Fato | `(ano, id_municipio, rede)` | 0 | 0 || Visão UF | `(ano, estado_sigla, rede)` | 0 | 0 || Visão Brasil | `(ano, rede)` | 0 | 0 |```mermaidflowchart LR    subgraph DQ["monitoring.dq_results"]        R1["completude_chave"]        R2["unicidade_chave_composta"]    end    FATO --> R1    FATO --> R2    VISAO_UF --> R1    VISAO_UF --> R2    VISAO_BRASIL --> R1    VISAO_BRASIL --> R2```
---
### O que os números contam (análise)
#### Brasil: evolução 2023 → 2024
- Taxa média nacional subiu de **60.48** para **63.04** (+2,56 p.p.).- Em 2024, **5.232 municípios** tinham meta definida e **2.788 atingiram** — **52,09%** de cumprimento.- Isso significa que **47,9% dos municípios ficaram abaixo da meta** em 2024.```mermaidpie showData    title Atingimento de meta — Brasil 2024    "Atingiram a meta (52.09%)" : 52.09    "Abaixo da meta (47.91%)" : 47.91```
#### Disparidade regional
- Destaques positivos: **CE (91,3%)** e **GO (80,0%)** de atingimento.- A variação entre estados mostra que o desafio é **regional e local**, não nacional — sinalizando onde priorizar política pública.
#### 2023 como linha de base
- Sem meta definida naquele ano, serve como referência histórica para medir a evolução a partir de 2024.
---
### Padrões Técnicos
- **Formato:** Delta Lake, `PARTITIONED BY (ano)` + `OPTIMIZE ... ZORDER BY`.- **Gravação:** CTAS (`CREATE OR REPLACE TABLE ... AS SELECT`) — compatível com serverless.- **Rastreabilidade:** colunas `ingested_at`, `source`, `version` em todas as tabelas.- **DQ:** `monitoring.dq_results` registra regra, status, registros verificados e falhas por execução.
---
### ▶Como Executar
1. Garanta as tabelas Silver (`indicador_municipio`, `meta_municipio`, `dim_ibge_municipios`).2. Rode os notebooks em ordem: `01` → `02` → `03`.3. Opcional: `04` para consolidar e validar o conjunto final.
---
### Próximos Passos Sugeridos
- Investigar os municípios abaixo da meta em 2024 (ranking por UF e município).- Acompanhar a evolução 2024 → 2025 para medir o ritmo de avanço.- Cruzar com variáveis socioeconômicas (IDH, renda) para entender os fatores do não cumprimento.- Evoluir para uma camada de visualização (Power BI / Databricks SQL Dashboard).