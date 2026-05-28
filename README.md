# 🚀 Arquitetura ETL: Monitoramento Automatizado de Preços (Hardware)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## 📌 O Problema de Negócio
O planejamento financeiro para a montagem de um computador de alta performance exige precisão e acompanhamento de mercado. Com um teto de orçamento estritamente fixado em R$ 8.600, a flutuação de preços de componentes críticos — especificamente a placa de vídeo RTX 5060 — representava um risco ao projeto. 

A solução foi desenvolver um **Pipeline ETL (Extract, Transform, Load)** autônomo. O robô monitora o e-commerce Kabum, burla o carregamento dinâmico da página para capturar os dados em sua raiz, e cria um banco de dados histórico estruturado, permitindo análises temporais de quedas de preço e promoções.

---

## ⚙️ Arquitetura do Projeto

O pipeline foi modularizado seguindo as melhores práticas de Engenharia de Dados corporativa, separando responsabilidades para garantir escalabilidade e resiliência.

* **Extract (`extract.py`):** * Utiliza `requests` e `BeautifulSoup`.
    * *Engenharia Reversa:* A extração via HTML convencional falha devido à renderização dinâmica via JavaScript. O script contorna isso interceptando diretamente a tag oculta contendo o payload estruturado em **JSON-LD** (`application/ld+json`).
* **Transform (`transform.py`):** * A biblioteca `pandas` recebe os dados brutos em memória.
    * Filtra ruídos, isola o dicionário de ofertas (`offers`) e estrutura a lista em um DataFrame relacional limpo contendo o nome do produto e o preço decimalizado.
* **Load (`load.py`):** * Integração via `sqlalchemy`.
    * Os dados não são sobrescritos. O objetivo é criar um **Data Warehouse Histórico (OLAP)**. A cada execução, um timestamp é anexado e as linhas são inseridas de forma incremental (`append`) no banco de dados local **SQLite**, permitindo "viagens no tempo" analíticas.
* **Orquestração (`main.py` e Task Scheduler):** * O fluxo é coordenado pelo script maestro.
    * A automação foi implementada a nível de Sistema Operacional (Windows Task Scheduler + arquivo `.bat` apontando para o ambiente virtual), garantindo a execução diária em background sem intervenção humana.

---

## 🛠️ Como Executar Localmente

### Pré-requisitos
* Python 3.x instalado.
* Conexão ativa com a internet.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/etl_hardware_prices.git](https://github.com/SEU-USUARIO/etl_hardware_prices.git)
   cd etl_hardware_prices