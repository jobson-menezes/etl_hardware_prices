# 🚀 ETL Architecture: Automated Price Monitoring (Hardware)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## 📌 Business Problem
Financial planning for building a high-performance computer requires precision and market tracking. With a strict budget cap of R$ 8,600, price fluctuations of critical components — specifically the RTX 5060 GPU — posed a risk to the project. 

The solution was to develop an autonomous **ETL (Extract, Transform, Load) Pipeline**. The bot monitors the Kabum e-commerce, bypasses dynamic page loading to capture data at its root, and creates a structured historical database, enabling temporal analysis of price drops and promotions.

---

## ⚙️ Project Architecture

The pipeline was modularized following corporate Data Engineering best practices, separating responsibilities to ensure scalability and resilience.

* **Extract (`extract.py`):** * Uses `requests` and `BeautifulSoup`.
    * *Reverse Engineering:* Conventional HTML extraction fails due to dynamic JavaScript rendering. The script bypasses this by directly intercepting the hidden tag containing the structured payload in **JSON-LD** (`application/ld+json`).
* **Transform (`transform.py`):** * The `pandas` library handles raw data in memory.
    * Filters noise, isolates the `offers` dictionary, and structures the list into a clean relational DataFrame containing the product name and decimalized price.
* **Load (`load.py`):** * Integration via `sqlalchemy`.
    * Data is not overwritten. The goal is to build a **Historical Data Warehouse (OLAP)**. On each execution, a timestamp is appended, and rows are incrementally inserted (`append`) into a local **SQLite** database, enabling analytical "time travel".
* **Orchestration (`main.py` & Task Scheduler):** * The flow is coordinated by the maestro script.
    * Automation was implemented at the OS level (Windows Task Scheduler + `.bat` file pointing to the virtual environment), ensuring daily execution in the background without human intervention.

---

## 🛠️ How to Run Locally

### Prerequisites
* Python 3.x installed.
* Active internet connection.

### Step by Step

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jobson-menezes/etl_hardware_prices.git
cd etl_hardware_prices

2. **Create and activate the virtual environment:**
    ```bash
    python -m venv venv

source venv/Scripts/activate  # On Windows

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run the Pipeline Manually:**
    ````bash
    python main.py

After execution, the hardware_db.sqlite file will be automatically generated in the project root with the day's data.

📊 SQL Queries & Data Analysis
With the database populated over several days, you can connect tools like DBeaver or Power BI to consume the data. Example of a query used to fetch only the most recent price of each GPU to avoid duplicates on the screen:

  ```bash
    SELECT 
    Produto, 
    "Preço (R$)", 
    MAX(Data_Coleta) as Ultima_Atualizacao
    FROM historico_precos
    GROUP BY Produto
    ORDER BY "Preço (R$)" ASC;
