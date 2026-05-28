@echo off
echo Iniciando o Pipeline ETL da Kabum...

:: 1. Navega ate a pasta do projeto
cd C:\Users\Jobso\Documents\etl_hardware_prices

:: 2. Executa o main.py chamando DIRETAMENTE o Python do venv
venv\Scripts\python.exe main.py