# Apêndice A – Fontes e Formatos de Dados

## 1. Introdução
Este apêndice apresenta o resumo consolidado das fontes utilizadas na elaboração do dicionário de dados.  
O objetivo é garantir **transparência**, **rastreabilidade** e **padronização** das informações, indicando para cada conjunto de dados sua origem, período de cobertura, formato e meio de acesso.

---

## 2. Tabelas de Referência

### Apêndice A – Fontes e Formatos de Dados

| **Fonte** | **Descrição** | **Cobertura Temporal** | **Formato dos Dados** | **URL de Acesso** | **Qtd. Registros** |
|------------|----------------|------------------------|-----------------------|-------------------|---------------------|
| **INEP Alunos** | Dados individuais de alunos avaliados, incluindo presença, proficiência e alfabetização. | 2023–2024 | CSV (exportável) via BigQuery (armazenamento) | [Base dos Dados – INEP Alunos](https://basedosdados.org/dataset/073a39d4-89cf-4068-b1e8-34ed0d9c0b72?table=bb27c746-18df-4ba8-8f98-5110232e2162) | **3.867.999** |
| **INEP Municípios** | Indicadores municipais de alfabetização e desempenho em Língua Portuguesa. | 2023–2024 | CSV (exportável) via BigQuery (armazenamento) | [Base dos Dados – INEP Municípios](https://basedosdados.org/dataset/073a39d4-89cf-4068-b1e8-34ed0d9c0b72?table=60ad97ba-cb4c-42b6-8b3f-a91cbfde3e59) | **23.995** |
| **INEP Meta Alfabetização por Município** | Metas e taxas de alfabetização por município, com projeções até 2030. | 2023–2024 | CSV (exportável) via BigQuery (armazenamento) | [Base dos Dados – INEP Meta Alfabetização por Município](https://basedosdados.org/dataset/073a39d4-89cf-4068-b1e8-34ed0d9c0b72?table=7088028a-f140-4d45-9e2f-7654eda01f38) | **10.704** |
| **INEP Meta Alfabetização por UF** | Metas e taxas de alfabetização por unidade federativa. | 2023–2024 | CSV (exportável) via BigQuery (armazenamento) | [Base dos Dados – INEP Meta Alfabetização por UF](https://basedosdados.org/dataset/073a39d4-89cf-4068-b1e8-34ed0d9c0b72?table=2c9fc9dc-1e77-4ed7-90b2-0bf450e35679) | **81** |
| **INEP Meta Alfabetização Brasil** | Metas e taxas de alfabetização consolidadas nacionalmente. | 2023–2024 | CSV (exportável) via BigQuery (armazenamento) | [Base dos Dados – INEP Meta Alfabetização Brasil](https://basedosdados.org/dataset/073a39d4-89cf-4068-b1e8-34ed0d9c0b72?table=efeb0095-4ad5-4655-820b-4bd1e0a4b7e7) | **3** |
| **INEP UF** | Indicadores estaduais de alfabetização e desempenho em Língua Portuguesa. | 2023–2024 | CSV (exportável) via BigQuery (armazenamento) | [Base dos Dados – INEP UF](https://basedosdados.org/dataset/073a39d4-89cf-4068-b1e8-34ed0d9c0b72?table=e1de7a6a-5038-4e81-89f0-a15f2cc12c9b) | **145** |
| **IBGE Municípios** | Estrutura territorial e hierarquia regional dos municípios brasileiros. | Atual | JSON (via API REST) | [IBGE API – Municípios](https://servicodados.ibge.gov.br/api/v1/localidades/municipios) | **5.571** |
| **IBGE Estados** | Identificação e classificação regional das unidades federativas. | Atual | JSON (via API REST) | [IBGE API – Estados](https://servicodados.ibge.gov.br/api/v1/localidades/estados) | **27** |


---

## Dicionário de dados. 
### Cada tabela contém os campos, suas descrições, tipo de dado, cobertura temporal e observações relevantes.


**INEP Alunos**
| Nome | Descrição | Tipo (BigQuery) | Cobertura Temporal | Dados Sensíveis (LGPD) | Observações |
| --- | --- | --- | --- | --- | --- |
| ano | Ano de aplicação da avaliação estadual | INT64 | 2023–2024 | Não | — |
| id_municipio | ID município de 7 dígitos | STRING | 2023–2024 | Não | — |
| id_escola | Máscara do código da escola (fictício) | STRING | 2023–2024 | Não | — |
| id_aluno | Código do aluno | STRING | 2023–2024 | Não | — |
| caderno | Código do caderno atribuído ao aluno na prova de LP | STRING | 2023–2024 | Não | — |
| serie | Ano escolar | STRING | 2023–2024 | Não | — |
| rede | Dependência administrativa da escola | STRING | 2023–2024 | Não | — |
| presenca | Indicador de presença na prova de LP | STRING | 2023–2024 | Não | — |
| preenchimento_caderno | Indicador de preenchimento da prova de LP | STRING | 2023–2024 | Não | — |
| alfabetizado | Indica se o aluno é considerado alfabetizado | STRING | 2023–2024 | Não | — |
| proficiencia | Proficiência do aluno em LP (escala SAEB) | FLOAT64 | 2023–2024 | Não | — |
| peso_aluno | Peso do aluno na prova de LP | FLOAT64 | 2023-2024 | Não | — |

---

**INEP Municípios**
| Nome | Descrição | Tipo (BigQuery) | Cobertura Temporal | Dados Sensíveis (LGPD) | Observações |
| --- | --- | --- | --- | --- | --- |
| ano | Ano da avaliação estadual | INT64 | 2023–2024 | Não | — |
| id_municipio | ID Município | STRING | 2023–2024 | Não | — |
| serie | Ano escolar | STRING | 2023–2024 | Não | — |
| rede | Rede de ensino | STRING | 2023–2024 | Não | — |
| taxa_alfabetizacao | Percentual de alunos alfabetizados | FLOAT64 | 2023–2024 | Não | — |
| media_portugues | Média ponderada do município em LP (SAEB) | FLOAT64 | 2023–2024 | Não | — |
| proporcao_aluno_nivel_0–8 | Percentual de alunos por nível de desempenho (0–8) | FLOAT64 | 2023–2024 | Não | — |

---

**INEP Meta Alfabetização por Município**
| Nome | Descrição | Tipo (BigQuery) | Cobertura Temporal | Dados Sensíveis (LGPD) | Observações |
| --- | --- | --- | --- | --- | --- |
| ano | Ano da avaliação | INT64 | 2023–2024 | Não | Nomes das colunas variam entre 2023 e 2024 |
| id_municipio | ID município de 7 dígitos | STRING | 2023–2024 | Não | — |
| rede | Rede de ensino | STRING | 2023–2024 | Não | — |
| taxa_alfabetizacao | Taxa de alfabetização | FLOAT64 | 2023–2024 | Não | — |
| meta_alfabetizacao_2024–2030 | Metas anuais de alfabetização | FLOAT64 | 2023–2024 | Não | — |
| nivel_alfabetizacao | Nível de alfabetização | INT64 | 2023–2024 | Não | — |
| percentual_participacao | Percentual de participação no município | FLOAT64 | 2023–2024 | Não | — |

---

**INEP Meta Alfabetização por UF**
| Nome | Descrição | Tipo (BigQuery) | Cobertura Temporal | Dados Sensíveis (LGPD) | Observações |
| --- | --- | --- | --- | --- | --- |
| ano | Ano da avaliação | INT64 | 2023–2024 | Não | — |
| sigla_uf | Sigla da unidade da federação | STRING | 2023–2024 | Não | — |
| rede | Rede de ensino | STRING | 2023–2024 | Não | — |
| taxa_alfabetizacao | Percentual de alunos alfabetizados | FLOAT64 | 2023–2024 | Não | — |
| meta_alfabetizacao_2024–2030 | Metas anuais de alfabetização | FLOAT64 | 2023–2024 | Não | — |
| percentual_participacao | Percentual de participação no estado | FLOAT64 | 2023–2024 | Não | — |

---

**INEP Meta Alfabetização Brasil**
| Nome | Descrição | Tipo (BigQuery) | Cobertura Temporal | Dados Sensíveis (LGPD) | Observações |
| --- | --- | --- | --- | --- | --- |
| ano | Ano da avaliação | INT64 | 2023–2024 | Não | — |
| rede | Rede de ensino | STRING | 2023–2024 | Não | — |
| taxa_alfabetizacao | Percentual de alunos alfabetizados | FLOAT64 | 2023–2024 | Não | — |
| meta_alfabetizacao_2024–2030 | Metas anuais de alfabetização | FLOAT64 | 2023–2024 | Não | — |
| percentual_participacao | Percentual de participação nacional | FLOAT64 | 2023–2024 | Não | — |

---

**INEP UF**
| Nome | Descrição | Tipo (BigQuery) | Cobertura Temporal | Dados Sensíveis (LGPD) | Observações |
| --- | --- | --- | --- | --- | --- |
| ano | Ano da avaliação estadual | INT64 | 2023–2024 | Não | — |
| sigla_uf | Sigla da unidade da federação | STRING | 2023–2024 | Não | — |
| serie | Ano escolar | STRING | 2023–2024 | Não | — |
| rede | Rede de ensino avaliada | STRING | 2023–2024 | Não | — |
| taxa_alfabetizacao | Percentual de alunos alfabetizados | FLOAT64 | 2023–2024 | Não | — |
| media_portugues | Média ponderada em LP (SAEB) | FLOAT64 | 2023–2024 | Não | — |
| proporcao_aluno_nivel_0–8 | Percentual de alunos por nível de desempenho (0–8) | FLOAT64 | 2023–2024 | Não | — |

---

**IBGE Municípios**
| Nome | Descrição | Fonte | Observações |
| --- | --- | --- | --- |
| id | Identificador do município | IBGE API | — |
| nome | Nome do município | IBGE API | — |
| microrregiao.id / nome | Identificação e nome da microrregião | IBGE API | — |
| mesorregiao.id / nome | Identificação e nome da mesorregião | IBGE API | — |
| UF.id / sigla / nome | Identificação e nome da unidade federativa | IBGE API | — |
| regiao.id / sigla / nome | Identificação e nome da região | IBGE API | — |
| regiao-imediata / regiao-intermediaria | Hierarquia regional | IBGE API | — |

---

**IBGE Estados**
| Nome | Descrição | Fonte | Observações |
| --- | --- | --- | --- |
| id | Identificador do estado | IBGE API | — |
| sigla | Sigla da unidade federativa | IBGE API | — |
| nome | Nome do estado | IBGE API | — |
| regiao.id / sigla / nome | Identificação e nome da região | IBGE API | — |

---

## 3. Considerações Técnicas

- As fontes do **INEP** são disponibilizadas por meio da plataforma *Base dos Dados*, com armazenamento em **BigQuery** e opção de exportação em **CSV**, garantindo compatibilidade com ferramentas de análise estatística e sistemas de integração de dados.  
- As fontes do **IBGE** são acessadas via **API REST**, retornando dados em formato **JSON**, o que permite integração direta com aplicações web e scripts automatizados.  
- Todas as fontes são públicas e não contêm dados sensíveis conforme a **Lei Geral de Proteção de Dados (LGPD)**.  
- A cobertura temporal refere-se aos anos de aplicação das avaliações estaduais (2023–2024) ou à atualização contínua das APIs do IBGE.

---

## 4. Finalidade do Apêndice

Este apêndice serve como referência técnica para **auditoria**, **replicação** e **atualização** dos dados utilizados.  
A padronização dos formatos e das fontes assegura a **integridade**, **interoperabilidade** e **transparência** das informações entre diferentes sistemas e equipes de análise.

---

**Fonte:** INEP / IBGE  
**Versão:** Agosto de 2026  
**Autor(es):** 

---
RM374990 - Célia M Tomitsuka

---

RM374983 - Nelson da Silva Paz

---
RM374494 - Nelson T Yamamoto
