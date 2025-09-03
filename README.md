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

## 📊 Metodologia e Análise

### Abordagem de Análise de Dados
Nossa metodologia seguiu as melhores práticas de análise exploratória de dados (EDA):

1. **Inspeção Inicial dos Dados**: 
   - Utilizamos `df.info()` e `df.head()` para verificar tipos de dados e estrutura
   - Aplicamos `df.isnull().sum()` para identificar dados ausentes
   - Empregamos `df.describe()` para análise estatística descritiva

2. **Limpeza e Preparação**:
   - Tratamento de valores ausentes identificados no dataset de clientes
   - Criação de grupos etários para análise segmentada
   - Cálculo de BMI e categorização para análise de medidas corporais

3. **Análise Exploratória Focada**:
   - Respondemos às 5 perguntas principais de negócio
   - Utilizamos visualizações específicas (countplot, histplot, heatmaps)
   - Criamos análises de correlação entre variáveis

## 🔍 Principais Insights

### Dataset H&M - Produtos e Clientes

**Categorias de Produtos Mais Populares:**
O gráfico abaixo mostra que as categorias de produtos mais populares são **Jeans** e **Camisetas**, indicando uma alta demanda por itens básicos do vestuário masculino. Essa informação é crucial para priorizar o desenvolvimento do sistema de recomendação de tamanhos.

- **Jeans**: 2 produtos (50% do sample)
- **T-shirts**: 2 produtos (50% do sample)
- **Diversidade**: Cobertura equilibrada entre itens superiores e inferiores do corpo

**Perfil Etário dos Clientes:**
A análise da distribuição de idades revelou um perfil diversificado:
- **Idade média**: 38.0 anos
- **Faixa etária**: 24-54 anos  
- **Distribuição**: Clientes bem distribuídos entre diferentes faixas etárias

**Relação Idade vs Tipo de Produto:**
A análise cruzada mostrou padrões interessantes de consumo por faixa etária, sugerindo que diferentes grupos etários têm preferências específicas de produtos, informação valiosa para personalização do sistema.

### Dataset Rent the Runway - Análise de Caimento

**Distribuição de Avaliações de Caimento:**
- **Perfect (Perfeito)**: 60% das avaliações - indica boa precisão dos tamanhos
- **Small (Pequeno)**: 20% das avaliações - produto ficou pequeno
- **Large (Grande)**: 20% das avaliações - produto ficou grande

**Correlação Tipo de Corpo vs Caimento:**
Identificamos padrões importantes por tipo de corpo:
- **Athletic**: 100% avaliaram como "perfect" - boa adequação de tamanhos
- **Average**: Tendência a avaliar como "small" - pode necessitar ajuste
- **Broad**: Avaliou como "perfect" - tamanhos adequados para esse biótipo
- **Slim**: Avaliou como "large" - tamanhos podem estar grandes para esse perfil

### Implicações para o Sistema de Recomendação

1. **Foco em Produtos Básicos**: Jeans e camisetas devem ser priorizados no algoritmo inicial
2. **Segmentação Etária**: Considerar faixas etárias nas recomendações de estilo
3. **Ajuste por Biótipo**: Implementar correções específicas para diferentes tipos de corpo
4. **Precisão do Caimento**: 60% de avaliações "perfect" é uma base sólida para expandir

## 📈 Próximos Passos

- [x] Download e organização dos datasets
- [x] Análise exploratória inicial  
- [x] Limpeza e preparação dos dados
- [x] **Análise EDA focada nas perguntas de negócio**
- [x] **Identificação de padrões de caimento por tipo de corpo**
- [ ] Adaptação do modelo de caimento para moda masculina
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
