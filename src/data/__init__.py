"""
Consultor de Estilo Virtual - __init__.py
=========================================

Módulo de dados para coleta e processamento.
"""

from .collect_data import DataCollector
from .process_data import DataProcessor, process_all_data

__all__ = ['DataCollector', 'DataProcessor', 'process_all_data']