"""
Consultor de Estilo Virtual - Data Processing Module
==================================================

Este módulo contém funções para limpeza, transformação e preparação
dos dados coletados para análise e modelagem.
"""

import pandas as pd
import numpy as np
import json
import re
from typing import Dict, List, Optional, Tuple, Any
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    """
    Classe responsável pelo processamento e limpeza dos dados.
    """
    
    def __init__(self, processed_dir: str = "data/processed"):
        """
        Inicializa o processador de dados.
        
        Args:
            processed_dir: Diretório onde os dados processados serão salvos
        """
        self.processed_dir = processed_dir
        self.ensure_directories()
    
    def ensure_directories(self) -> None:
        """Garante que os diretórios necessários existam."""
        import os
        os.makedirs(self.processed_dir, exist_ok=True)
    
    def clean_hm_articles(self, articles_df: pd.DataFrame) -> pd.DataFrame:
        """
        Limpa e padroniza os dados de artigos da H&M.
        
        Args:
            articles_df: DataFrame com dados dos artigos
            
        Returns:
            DataFrame limpo e padronizado
        """
        logger.info("Limpando dados de artigos H&M...")
        
        df = articles_df.copy()
        
        # Filtrar apenas produtos masculinos
        if 'department_name' in df.columns:
            df = df[df['department_name'].isin(['Men', 'Menswear'])].copy()
        
        # Limpar nomes de produtos
        if 'prod_name' in df.columns:
            df['prod_name'] = df['prod_name'].str.strip()
            df['prod_name'] = df['prod_name'].str.title()
        
        # Padronizar tipos de produto
        if 'product_type_name' in df.columns:
            df['product_type_name'] = df['product_type_name'].str.strip()
            df['product_category'] = df['product_type_name'].apply(self._categorize_product_type)
        
        # Padronizar cores
        if 'colour_group_name' in df.columns:
            df['colour_group_name'] = df['colour_group_name'].str.strip()
            df['color_category'] = df['colour_group_name'].apply(self._categorize_color)
        
        # Remover duplicatas
        df = df.drop_duplicates(subset=['article_id'])
        
        logger.info(f"Artigos H&M limpos: {len(df)} produtos masculinos")
        return df
    
    def clean_hm_customers(self, customers_df: pd.DataFrame) -> pd.DataFrame:
        """
        Limpa e padroniza os dados de clientes da H&M.
        
        Args:
            customers_df: DataFrame com dados dos clientes
            
        Returns:
            DataFrame limpo e padronizado
        """
        logger.info("Limpando dados de clientes H&M...")
        
        df = customers_df.copy()
        
        # Tratar valores ausentes em idade
        if 'age' in df.columns:
            df['age'] = pd.to_numeric(df['age'], errors='coerce')
            df['age'] = df['age'].fillna(df['age'].median())
            df['age_group'] = df['age'].apply(self._categorize_age)
        
        # Padronizar status do clube
        if 'club_member_status' in df.columns:
            df['is_member'] = df['club_member_status'].notna()
        
        # Padronizar frequência de newsletter
        if 'fashion_news_frequency' in df.columns:
            df['news_frequency'] = df['fashion_news_frequency'].fillna('None')
        
        # Remover duplicatas
        df = df.drop_duplicates(subset=['customer_id'])
        
        logger.info(f"Clientes H&M limpos: {len(df)} registros")
        return df
    
    def clean_fit_data(self, fit_df: pd.DataFrame) -> pd.DataFrame:
        """
        Limpa e padroniza os dados de caimento.
        
        Args:
            fit_df: DataFrame com dados de caimento
            
        Returns:
            DataFrame limpo e padronizado
        """
        logger.info("Limpando dados de caimento...")
        
        df = fit_df.copy()
        
        # Padronizar avaliações de caimento
        if 'fit_rating' in df.columns:
            df['fit_rating'] = df['fit_rating'].str.lower().str.strip()
            df['fit_numeric'] = df['fit_rating'].map({
                'small': -1, 'tight': -1, 'runs small': -1,
                'perfect': 0, 'just right': 0, 'true to size': 0,
                'large': 1, 'loose': 1, 'runs large': 1
            })
        
        # Calcular BMI se altura e peso estiverem disponíveis
        if 'user_height' in df.columns and 'user_weight' in df.columns:
            df['height_m'] = df['user_height'] / 100  # converter cm para m
            df['bmi'] = df['user_weight'] / (df['height_m'] ** 2)
            df['bmi_category'] = df['bmi'].apply(self._categorize_bmi)
        
        # Padronizar tipos de corpo
        if 'body_type' in df.columns:
            df['body_type'] = df['body_type'].str.title().str.strip()
        
        # Padronizar tamanhos
        if 'size_ordered' in df.columns:
            df['size_numeric'] = df['size_ordered'].map({
                'XS': 1, 'S': 2, 'M': 3, 'L': 4, 'XL': 5, 'XXL': 6
            })
        
        logger.info(f"Dados de caimento limpos: {len(df)} registros")
        return df
    
    def create_hybrid_dataset(self, articles_df: pd.DataFrame, 
                            customers_df: pd.DataFrame, 
                            fit_df: pd.DataFrame) -> pd.DataFrame:
        """
        Cria um dataset híbrido combinando as diferentes fontes.
        
        Args:
            articles_df: Dados de artigos H&M limpos
            customers_df: Dados de clientes H&M limpos  
            fit_df: Dados de caimento limpos
            
        Returns:
            DataFrame híbrido combinado
        """
        logger.info("Criando dataset híbrido...")
        
        # Simular associações entre os datasets
        # (Em um cenário real, isso seria baseado em IDs reais)
        hybrid_data = []
        
        for _, customer in customers_df.head(100).iterrows():  # Limitar para exemplo
            # Selecionar alguns artigos aleatoriamente para cada cliente
            customer_articles = articles_df.sample(n=min(5, len(articles_df)))
            
            for _, article in customer_articles.iterrows():
                # Simular dados de caimento baseados nos padrões do fit_df
                fit_sample = fit_df.sample(n=1).iloc[0]
                
                hybrid_record = {
                    'customer_id': customer['customer_id'],
                    'article_id': article['article_id'],
                    'customer_age': customer.get('age', np.nan),
                    'customer_age_group': customer.get('age_group', 'Unknown'),
                    'product_name': article.get('prod_name', 'Unknown'),
                    'product_category': article.get('product_category', 'Unknown'),
                    'product_type': article.get('product_type_name', 'Unknown'),
                    'color_category': article.get('color_category', 'Unknown'),
                    # Simular medidas corporais baseadas no fit_df
                    'estimated_height': fit_sample.get('user_height', 175),
                    'estimated_weight': fit_sample.get('user_weight', 75),
                    'estimated_bmi_category': fit_sample.get('bmi_category', 'Normal'),
                    'predicted_fit': fit_sample.get('fit_rating', 'perfect'),
                    'size_recommendation': fit_sample.get('size_ordered', 'M')
                }
                
                hybrid_data.append(hybrid_record)
        
        hybrid_df = pd.DataFrame(hybrid_data)
        
        logger.info(f"Dataset híbrido criado: {len(hybrid_df)} registros")
        return hybrid_df
    
    def save_processed_data(self, df: pd.DataFrame, filename: str) -> None:
        """
        Salva dados processados em formato CSV e Parquet.
        
        Args:
            df: DataFrame para salvar
            filename: Nome base do arquivo (sem extensão)
        """
        # Salvar em CSV
        csv_path = f"{self.processed_dir}/{filename}.csv"
        df.to_csv(csv_path, index=False)
        
        # Salvar em Parquet (mais eficiente para datasets grandes)
        try:
            parquet_path = f"{self.processed_dir}/{filename}.parquet"
            df.to_parquet(parquet_path, index=False)
            logger.info(f"Dados salvos: {csv_path} e {parquet_path}")
        except Exception as e:
            logger.warning(f"Erro ao salvar em Parquet: {e}")
            logger.info(f"Dados salvos apenas em CSV: {csv_path}")
    
    def _categorize_product_type(self, product_type: str) -> str:
        """Categoriza tipos de produto."""
        if pd.isna(product_type):
            return 'Other'
        
        product_type = product_type.lower()
        
        if any(word in product_type for word in ['shirt', 'tee', 't-shirt', 'blouse', 'top']):
            return 'Tops'
        elif any(word in product_type for word in ['jeans', 'trouser', 'pant', 'short']):
            return 'Bottoms'
        elif any(word in product_type for word in ['jacket', 'coat', 'blazer', 'cardigan']):
            return 'Outerwear'
        elif any(word in product_type for word in ['shoe', 'boot', 'sneaker']):
            return 'Footwear'
        elif any(word in product_type for word in ['accessorie', 'bag', 'belt', 'hat']):
            return 'Accessories'
        else:
            return 'Other'
    
    def _categorize_color(self, color: str) -> str:
        """Categoriza cores."""
        if pd.isna(color):
            return 'Unknown'
        
        color = color.lower()
        
        if any(word in color for word in ['black', 'dark']):
            return 'Dark'
        elif any(word in color for word in ['white', 'light', 'beige']):
            return 'Light'
        elif any(word in color for word in ['blue', 'navy']):
            return 'Blue'
        elif any(word in color for word in ['red', 'burgundy']):
            return 'Red'
        elif any(word in color for word in ['green', 'olive']):
            return 'Green'
        elif any(word in color for word in ['brown', 'tan']):
            return 'Brown'
        else:
            return 'Other'
    
    def _categorize_age(self, age: float) -> str:
        """Categoriza faixas etárias."""
        if pd.isna(age):
            return 'Unknown'
        
        if age < 18:
            return 'Teen'
        elif age < 25:
            return 'Young Adult'
        elif age < 35:
            return 'Adult'
        elif age < 50:
            return 'Middle Age'
        else:
            return 'Senior'
    
    def _categorize_bmi(self, bmi: float) -> str:
        """Categoriza BMI."""
        if pd.isna(bmi):
            return 'Unknown'
        
        if bmi < 18.5:
            return 'Underweight'
        elif bmi < 25:
            return 'Normal'
        elif bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'


def process_all_data(raw_data_dir: str = "data/raw", 
                    processed_data_dir: str = "data/processed") -> None:
    """
    Função principal para processar todos os dados.
    
    Args:
        raw_data_dir: Diretório com dados brutos
        processed_data_dir: Diretório para dados processados
    """
    processor = DataProcessor(processed_data_dir)
    
    try:
        # Carregar dados brutos (usando dados de exemplo)
        articles_df = pd.read_csv(f"{raw_data_dir}/hm/articles_sample.csv")
        customers_df = pd.read_csv(f"{raw_data_dir}/hm/customers_sample.csv")
        fit_df = pd.read_csv(f"{raw_data_dir}/rent_runway/fit_data_sample.csv")
        
        # Processar cada dataset
        articles_clean = processor.clean_hm_articles(articles_df)
        customers_clean = processor.clean_hm_customers(customers_df)
        fit_clean = processor.clean_fit_data(fit_df)
        
        # Criar dataset híbrido
        hybrid_df = processor.create_hybrid_dataset(articles_clean, customers_clean, fit_clean)
        
        # Salvar dados processados
        processor.save_processed_data(articles_clean, "hm_articles_clean")
        processor.save_processed_data(customers_clean, "hm_customers_clean")
        processor.save_processed_data(fit_clean, "fit_data_clean")
        processor.save_processed_data(hybrid_df, "hybrid_dataset")
        
        logger.info("Processamento completo de todos os dados finalizado!")
        
    except FileNotFoundError as e:
        logger.error(f"Arquivo não encontrado: {e}")
        logger.info("Execute o script collect_data.py primeiro para criar os dados de exemplo.")


if __name__ == "__main__":
    # Processar todos os dados
    process_all_data()