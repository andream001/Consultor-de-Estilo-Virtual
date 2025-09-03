"""
Consultor de Estilo Virtual - Data Collection Module
==================================================

Este módulo contém funções para coleta e organização dos datasets
utilizados no projeto de recomendação de tamanhos para moda masculina.

Datasets utilizados:
1. H&M Personalized Fashion Recommendations (Kaggle)
2. Rent the Runway Fit Data (Kaggle)
"""

import pandas as pd
import numpy as np
import os
import requests
from typing import Dict, List, Optional, Tuple
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataCollector:
    """
    Classe responsável pela coleta e organização inicial dos datasets.
    """
    
    def __init__(self, data_dir: str = "data/raw"):
        """
        Inicializa o coletor de dados.
        
        Args:
            data_dir: Diretório onde os dados brutos serão armazenados
        """
        self.data_dir = data_dir
        self.ensure_directories()
    
    def ensure_directories(self) -> None:
        """Garante que os diretórios necessários existam."""
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(f"{self.data_dir}/hm", exist_ok=True)
        os.makedirs(f"{self.data_dir}/rent_runway", exist_ok=True)
    
    def download_datasets_info(self) -> Dict[str, str]:
        """
        Retorna informações sobre os datasets a serem utilizados.
        
        Returns:
            Dict com informações dos datasets
        """
        datasets_info = {
            "hm_fashion": {
                "name": "H&M Personalized Fashion Recommendations",
                "url": "https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data",
                "description": "Dataset com produtos, clientes e transações da H&M",
                "files": [
                    "articles.csv",
                    "customers.csv", 
                    "transactions_train.csv"
                ],
                "size": "~31GB total",
                "key_features": [
                    "Informações detalhadas de produtos",
                    "Dados demográficos de clientes",
                    "Histórico de transações"
                ]
            },
            "rent_runway": {
                "name": "Rent the Runway Fit Data",
                "url": "https://www.kaggle.com/datasets/rmisra/rent-the-runway",
                "description": "Dataset com avaliações de caimento de roupas femininas",
                "files": [
                    "renttherunway_final_data.json"
                ],
                "size": "~192MB",
                "key_features": [
                    "Medidas corporais dos usuários",
                    "Tamanhos alugados",
                    "Avaliações de caimento (fit)"
                ]
            }
        }
        
        return datasets_info
    
    def create_sample_data(self) -> None:
        """
        Cria dados de exemplo para desenvolvimento e testes.
        Útil quando os datasets completos não estão disponíveis.
        """
        logger.info("Criando dados de exemplo...")
        
        # Sample H&M Articles Data
        articles_sample = pd.DataFrame({
            'article_id': ['108775015', '108775044', '111565001', '111565002'],
            'product_code': ['108775', '108775', '111565', '111565'],
            'prod_name': ['Ston Washed Jeans', 'Ston Washed Jeans', 'Cotton T-shirt', 'Cotton T-shirt'],
            'product_type_name': ['Jeans', 'Jeans', 'T-shirt', 'T-shirt'],
            'product_group_name': ['Garment Lower body', 'Garment Lower body', 'Garment Upper body', 'Garment Upper body'],
            'colour_group_name': ['Dark Blue', 'Light Blue', 'White', 'Black'],
            'department_name': ['Men', 'Men', 'Men', 'Men'],
            'index_name': ['Menswear', 'Menswear', 'Menswear', 'Menswear'],
            'section_name': ['Men', 'Men', 'Men', 'Men']
        })
        
        # Sample H&M Customers Data
        customers_sample = pd.DataFrame({
            'customer_id': ['00000dbacae5abe5e23885899a1fa44253a17956c6d1c3d25f88aa139fdfc657',
                          '0000423b00ade91418cceaf3b26c6af3dd342b51fd051eec9c12fb36984420fa',
                          '000058a12d5b43e67d225668fa1f8d618c13dc232df0cad8ffe7ad4a250a7a',
                          '00007d2de826758b65a93dd24ce629ed66842531df6699338c5570910a014cc2'],
            'FN': [1.0, 1.0, np.nan, 1.0],
            'Active': [1.0, 1.0, 1.0, 1.0],
            'club_member_status': ['ACTIVE', 'ACTIVE', 'PRE_CREATE', 'ACTIVE'],
            'fashion_news_frequency': ['Regularly', 'Regularly', np.nan, 'Monthly'],
            'age': [49, 25, 24, 54],
            'postal_code': ['52043ee2162cf5aa7ee79974281641c6f11a68d276ece30c9c9d34d1', 
                          '2973abc54daa8a5f8ccfe9362140c63247c5eee03f35f0875a5ad5e', 
                          'ca75339134f4b9dcc58a3eb3e56e6e4e5b7d0a1f3f96a4d3c7e5b8f', 
                          '474cc7c952fb2725c16b1e95d6ca2c727a0a3f4d8b5e3a3c8f2e7d1']
        })
        
        # Sample Rent the Runway inspired data (adapted for men's clothing)
        fit_data_sample = pd.DataFrame({
            'user_id': [1, 2, 3, 4, 5],
            'item_id': [1001, 1002, 1003, 1004, 1005],
            'user_age': [28, 35, 42, 31, 26],
            'user_height': [180, 175, 185, 172, 178],  # cm
            'user_weight': [75, 82, 90, 68, 70],       # kg
            'body_type': ['Athletic', 'Average', 'Broad', 'Slim', 'Athletic'],
            'size_ordered': ['M', 'L', 'XL', 'S', 'M'],
            'fit_rating': ['perfect', 'small', 'perfect', 'large', 'perfect'],
            'category': ['shirt', 'jeans', 'jacket', 'pants', 'shirt'],
            'brand': ['Brand A', 'Brand B', 'Brand C', 'Brand D', 'Brand E']
        })
        
        # Salvar dados de exemplo
        articles_sample.to_csv(f"{self.data_dir}/hm/articles_sample.csv", index=False)
        customers_sample.to_csv(f"{self.data_dir}/hm/customers_sample.csv", index=False)
        fit_data_sample.to_csv(f"{self.data_dir}/rent_runway/fit_data_sample.csv", index=False)
        
        logger.info("Dados de exemplo criados com sucesso!")
    
    def load_sample_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Carrega os dados de exemplo criados.
        
        Returns:
            Tuple com os DataFrames: (articles, customers, fit_data)
        """
        try:
            articles = pd.read_csv(f"{self.data_dir}/hm/articles_sample.csv")
            customers = pd.read_csv(f"{self.data_dir}/hm/customers_sample.csv")
            fit_data = pd.read_csv(f"{self.data_dir}/rent_runway/fit_data_sample.csv")
            
            logger.info("Dados de exemplo carregados com sucesso!")
            return articles, customers, fit_data
            
        except FileNotFoundError:
            logger.warning("Dados de exemplo não encontrados. Execute create_sample_data() primeiro.")
            return None, None, None
    
    def get_dataset_instructions(self) -> str:
        """
        Retorna instruções para download dos datasets completos.
        
        Returns:
            String com instruções detalhadas
        """
        instructions = """
        INSTRUÇÕES PARA DOWNLOAD DOS DATASETS COMPLETOS
        =============================================
        
        Para obter acesso aos datasets completos, siga os passos abaixo:
        
        1. H&M Personalized Fashion Recommendations:
           - Acesse: https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data
           - Faça login no Kaggle (ou crie uma conta)
           - Aceite as regras da competição
           - Baixe os arquivos: articles.csv, customers.csv, transactions_train.csv
           - Coloque os arquivos em: data/raw/hm/
        
        2. Rent the Runway Fit Data:
           - Acesse: https://www.kaggle.com/datasets/rmisra/rent-the-runway
           - Faça login no Kaggle
           - Baixe o arquivo: renttherunway_final_data.json
           - Coloque o arquivo em: data/raw/rent_runway/
        
        3. Instalação da API do Kaggle (opcional):
           - pip install kaggle
           - Configure suas credenciais: https://www.kaggle.com/docs/api
           - Use os comandos abaixo para download automático:
           
           kaggle competitions download -c h-and-m-personalized-fashion-recommendations
           kaggle datasets download -d rmisra/rent-the-runway
        
        NOTA: Enquanto os datasets completos não estiverem disponíveis,
        utilize os dados de exemplo criados por create_sample_data().
        """
        
        return instructions


if __name__ == "__main__":
    # Exemplo de uso
    collector = DataCollector()
    
    # Mostrar informações dos datasets
    datasets = collector.download_datasets_info()
    print("Datasets disponíveis:")
    for name, info in datasets.items():
        print(f"\n{info['name']}:")
        print(f"  URL: {info['url']}")
        print(f"  Descrição: {info['description']}")
        print(f"  Tamanho: {info['size']}")
    
    # Criar dados de exemplo
    collector.create_sample_data()
    
    # Mostrar instruções
    print(collector.get_dataset_instructions())