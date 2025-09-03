# Consultor de Estilo Virtual

Um sistema inteligente de recomendação de tamanhos e estilo para moda masculina, utilizando análise de dados e machine learning.

## 🎯 Objetivo

Desenvolver um projeto de análise de dados que culmine na criação de um protótipo de recomendador de tamanho e estilo para resolver o problema crítico da inconsistência de tamanhos na moda masculina online.

## 🚀 Fase 1: Coleta e Estruturação de Dados (1-2 semanas)

### O Desafio
Identificamos que a inconsistência de tamanhos é um problema crítico na moda masculina online, mas notamos a ausência de um dataset público completo que contenha simultaneamente:
- Medidas detalhadas de roupas masculinas
- Medidas corporais dos clientes  
- Avaliações de caimento

### A Solução Criativa
Para superar essa limitação, construímos uma **solução híbrida**:

1. **Base de Produtos e Clientes**: [H&M Personalized Fashion Recommendations](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data)
   - Dataset massivo com informações detalhadas sobre produtos (tipo de peça, cor, etc.)
   - Dados de clientes (idade) e histórico completo de transações
   - Base realista para análise de padrões de compra por perfil de cliente

2. **Estrutura de Medidas e Avaliação**: [Rent the Runway Fit Data](https://www.kaggle.com/datasets/rmisra/rent-the-runway)
   - Informações de clientes (altura, peso, tipo de corpo)
   - Tamanhos utilizados e avaliações de caimento (pequeno, perfeito, grande)
   - Modelo para entender a relação entre biotipos e caimento das peças

### O Resultado
Uma análise que não só explora padrões de compra, mas também propõe um sistema de recomendação de tamanho que poderia ser aplicado a um e-commerce real, adaptando a lógica de moda feminina para o universo masculino.

## 📁 Estrutura do Projeto

```
Consultor-de-Estilo-Virtual/
│
├── data/                          # Dados do projeto
│   ├── raw/                       # Dados originais (não versionados)
│   ├── processed/                 # Dados processados (não versionados)
│   └── external/                  # Dados de referência externa
│
├── src/                           # Código fonte
│   ├── data/                      # Scripts de coleta e processamento
│   ├── features/                  # Engenharia de features
│   ├── models/                    # Modelos de ML
│   └── visualization/             # Scripts de visualização
│
├── notebooks/                     # Jupyter notebooks
│   ├── 01-data-exploration/       # Exploração inicial dos dados
│   ├── 02-data-cleaning/          # Limpeza e preparação
│   └── 03-modeling/               # Modelagem e análises
│
├── models/                        # Modelos treinados (não versionados)
├── docs/                          # Documentação
├── tests/                         # Testes automatizados
├── requirements.txt               # Dependências Python
└── README.md                      # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal
- **Pandas**: Manipulação e análise de dados
- **NumPy**: Computação científica
- **Scikit-learn**: Machine learning
- **Matplotlib/Seaborn**: Visualização de dados
- **Jupyter Notebooks**: Análise exploratória
- **Plotly**: Visualizações interativas

## 🚀 Como Começar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/andream001/Consultor-de-Estilo-Virtual.git
   cd Consultor-de-Estilo-Virtual
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute os notebooks**:
   ```bash
   jupyter notebook
   ```

## 📊 Datasets

### 1. H&M Personalized Fashion Recommendations
- **Fonte**: [Kaggle Competition](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data)
- **Conteúdo**: Produtos, clientes, transações
- **Uso**: Base de produtos e comportamento de compra

### 2. Rent the Runway Fit Data  
- **Fonte**: [Kaggle Dataset](https://www.kaggle.com/datasets/rmisra/rent-the-runway)
- **Conteúdo**: Medidas corporais e avaliações de caimento
- **Uso**: Modelo para sistema de recomendação de tamanhos

## 🔄 Pipeline de Dados

1. **Coleta**: Download e organização dos datasets
2. **Limpeza**: Tratamento de valores ausentes e padronização
3. **Transformação**: Adaptação do modelo feminino para masculino
4. **Integração**: Criação de dataset híbrido coeso
5. **Análise**: Exploração de padrões e insights
6. **Modelagem**: Desenvolvimento do sistema de recomendação

## 📈 Próximos Passos

- [ ] Download e organização dos datasets
- [ ] Análise exploratória inicial
- [ ] Limpeza e preparação dos dados
- [ ] Adaptação do modelo de caimento
- [ ] Desenvolvimento do algoritmo de recomendação
- [ ] Validação e testes do sistema
- [ ] Criação de interface/protótipo

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

---

**Autor**: Andrea M.  
**Contato**: [GitHub](https://github.com/andream001)
