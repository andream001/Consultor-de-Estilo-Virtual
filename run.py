#!/usr/bin/env python
"""
Consultor de Estilo Virtual - CLI Interface
==========================================

Interface de linha de comando para executar as principais funcionalidades do projeto.

Usage:
    python run.py --help
    python run.py collect-data
    python run.py process-data
    python run.py analyze-data
    python run.py run-all
"""

import argparse
import sys
import os
from pathlib import Path

# Adicionar src ao path
sys.path.append('src')

from data.collect_data import DataCollector
from data.process_data import DataProcessor, process_all_data

def collect_data():
    """Coleta e organiza os dados de exemplo."""
    print("🔧 Iniciando coleta de dados...")
    
    collector = DataCollector()
    
    # Mostrar informações dos datasets
    datasets = collector.download_datasets_info()
    print("\n📊 Datasets disponíveis:")
    for name, info in datasets.items():
        print(f"   📋 {info['name']}")
        print(f"      Tamanho: {info['size']}")
        print(f"      URL: {info['url']}")
    
    # Criar dados de exemplo
    collector.create_sample_data()
    
    # Verificar dados criados
    articles, customers, fit_data = collector.load_sample_data()
    print(f"\n✅ Dados coletados:")
    print(f"   👔 Artigos H&M: {len(articles)} registros")
    print(f"   👥 Clientes H&M: {len(customers)} registros")
    print(f"   📐 Dados de caimento: {len(fit_data)} registros")
    
    print("\n📝 Para datasets completos, consulte:")
    print(collector.get_dataset_instructions())

def process_data():
    """Processa e limpa os dados coletados."""
    print("🔄 Iniciando processamento de dados...")
    
    try:
        process_all_data()
        print("\n✅ Processamento concluído com sucesso!")
        print("📁 Arquivos gerados em data/processed/")
        
        # Listar arquivos processados
        processed_dir = Path("data/processed")
        if processed_dir.exists():
            files = list(processed_dir.glob("*.csv"))
            print(f"\n📋 Arquivos processados ({len(files)}):")
            for file in files:
                size_kb = file.stat().st_size / 1024
                print(f"   📄 {file.name} ({size_kb:.1f} KB)")
        
    except FileNotFoundError:
        print("❌ Dados brutos não encontrados.")
        print("Execute primeiro: python run.py collect-data")

def analyze_data():
    """Executa análise básica dos dados."""
    print("📊 Iniciando análise de dados...")
    
    try:
        import pandas as pd
        
        # Carregar dados híbridos
        hybrid_path = "data/processed/hybrid_dataset.csv"
        if not os.path.exists(hybrid_path):
            print("❌ Dataset híbrido não encontrado.")
            print("Execute primeiro: python run.py process-data")
            return
        
        df = pd.read_csv(hybrid_path)
        
        print(f"\n📋 Dataset Híbrido - {len(df)} registros:")
        print(f"   👥 Clientes únicos: {df['customer_id'].nunique()}")
        print(f"   👔 Produtos únicos: {df['article_id'].nunique()}")
        
        print(f"\n📊 Distribuição por categoria:")
        category_counts = df['product_category'].value_counts()
        for category, count in category_counts.items():
            percentage = (count / len(df)) * 100
            print(f"   {category}: {count} ({percentage:.1f}%)")
        
        print(f"\n📏 Distribuição de tamanhos:")
        size_counts = df['size_recommendation'].value_counts()
        for size, count in size_counts.items():
            percentage = (count / len(df)) * 100
            print(f"   Tamanho {size}: {count} ({percentage:.1f}%)")
        
        print(f"\n✅ Distribuição de caimento:")
        fit_counts = df['predicted_fit'].value_counts()
        for fit, count in fit_counts.items():
            percentage = (count / len(df)) * 100
            print(f"   {fit.title()}: {count} ({percentage:.1f}%)")
            
    except ImportError:
        print("❌ Pandas não encontrado. Instale com: pip install pandas")

def run_all():
    """Executa todo o pipeline completo."""
    print("🚀 Executando pipeline completo...\n")
    
    print("1️⃣ Coleta de dados:")
    collect_data()
    
    print("\n2️⃣ Processamento de dados:")
    process_data()
    
    print("\n3️⃣ Análise de dados:")
    analyze_data()
    
    print("\n🎉 Pipeline completo executado com sucesso!")
    print("📓 Para análise detalhada, execute os notebooks em notebooks/")

def main():
    parser = argparse.ArgumentParser(
        description="Consultor de Estilo Virtual - Sistema de Recomendação de Tamanhos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python run.py collect-data     # Coleta dados de exemplo
  python run.py process-data     # Processa e limpa dados
  python run.py analyze-data     # Análise básica dos dados
  python run.py run-all          # Executa pipeline completo

Para análise detalhada:
  jupyter notebook               # Execute os notebooks em notebooks/
        """
    )
    
    parser.add_argument(
        'command', 
        choices=['collect-data', 'process-data', 'analyze-data', 'run-all'],
        help='Comando a ser executado'
    )
    
    args = parser.parse_args()
    
    # Garantir que diretórios existem
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    
    if args.command == 'collect-data':
        collect_data()
    elif args.command == 'process-data':
        process_data()
    elif args.command == 'analyze-data':
        analyze_data()
    elif args.command == 'run-all':
        run_all()

if __name__ == '__main__':
    main()