# Consultor de Estilo Virtual

Um sistema inteligente de recomendação de tamanhos e estilo para moda masculina, utilizando análise de dados e machine learning.

## 🎯 Objetivo

Resolver a **"Incerteza do Caimento Perfeito"** na moda masculina online. Este projeto desenvolve um protótipo de recomendador de tamanho e estilo, transformando dados brutos em uma solução prática que melhora a experiência de compra do cliente.

## 💡 A Solução: Da Análise à Recomendação

Construímos uma jornada completa, desde a exploração dos dados até a criação de um protótipo funcional.

### 1. Análise e Insights

Nossa análise revelou insights cruciais sobre os clientes e produtos:

**Perfil do Público (H&M):**
A maioria dos nossos clientes está na faixa etária de **21 a 30 anos**, indicando um público jovem e conectado.

![Gráfico de Idade](https://i.imgur.com/your_age_chart_image.png) 
*(Nota: Substituir por imagem real do gráfico gerado no notebook)*

**Categorias Mais Populares (H&M):**
**Tops (camisetas, blusas)** e **Bottoms (calças, shorts)** dominam as preferências, mostrando a importância de acertar o tamanho nesses itens básicos.

![Gráfico de Categorias](https://i.imgur.com/your_category_chart_image.png)
*(Nota: Substituir por imagem real do gráfico gerado no notebook)*

**O Problema do Caimento (Rent the Runway):**
A análise do 'fit' quantifica o problema: uma parcela significativa dos clientes não encontra o caimento ideal, resultando em uma experiência de compra frustrante.

![Gráfico de Fit](https://i.imgur.com/your_fit_chart_image.png)
*(Nota: Substituir por imagem real do gráfico gerado no notebook)*

### 2. Solução Proposta: O Recomendador Inteligente

Com base nos padrões encontrados, desenvolvemos um **protótipo de recomendador de tamanho**. Ele utiliza regras simples, extraídas da análise de dados, para sugerir o tamanho mais adequado com base na altura e peso do cliente.

**Como Funciona?**
Criamos uma função em Python que serve como o cérebro do nosso recomendador:

```python
def recomendar_tamanho(altura, peso):
  # ... lógica baseada em regras ...
  if 175 <= altura <= 185 and 70 <= peso <= 80:
    return "Tamanho M é provavelmente o ideal para você."
  else:
    return "Não temos uma recomendação clara com base nos dados."
```

Esta função é o primeiro passo para um sistema que pode reduzir devoluções, aumentar a satisfação do cliente e, consequentemente, impulsionar as vendas.

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

## 🔍 Principais Insights e Próximos Passos

Nossa análise aprofundada revelou padrões claros que direcionam nossa solução.

### Análise de Preferências (H&M)
- **Jovens Adultos (Young Adult)**: Preferem **Tops** e **Outerwear**, indicando um foco em moda casual e de sobreposição.
- **Adultos (Adult)**: Mostram uma preferência maior por **Bottoms**, sugerindo uma necessidade de variedade e bom caimento em calças e shorts.

### Relação Medidas vs. Caimento (Rent the Runway)
O gráfico de dispersão mostra uma concentração de caimentos **'Perfeito' (azul)** em determinadas faixas de peso e altura. As áreas com pontos **'Apertado' (vermelho)** e **'Largo' (amarelo)** representam as "zonas de risco" onde nosso recomendador pode atuar para evitar uma má experiência.

*(Nota: Adicionar imagem do scatter plot gerado)*

### Implicações para o Sistema de Recomendação

1. **Foco em Produtos Básicos**: O recomendador deve ser excelente para Tops e Bottoms.
2. **Segmentação por Idade e Estilo**: As recomendações podem ser personalizadas. Um "Young Adult" pode receber sugestões de 'Outerwear', enquanto um 'Adult' pode ver mais opções de 'Bottoms'.
3. **Refinamento com Base no 'Fit'**: A função `recomendar_tamanho` é o nosso MVP (Minimum Viable Product). Os próximos passos envolvem refinar as regras com base nas "zonas de risco" identificadas no gráfico de dispersão.

## 📈 Próximos Passos

- [x] Análise exploratória aprofundada
- [x] Criação do protótipo da função de recomendação
- [x] Atualização do README com novos insights
- [ ] **Refinar a função `recomendar_tamanho`** com mais regras extraídas da análise.
- [ ] **Integrar os gráficos gerados** no README para visualização.
- [ ] Desenvolver um modelo de Machine Learning simples (ex: Regressão Logística) para prever o 'fit'.
- [ ] Criar uma interface de usuário simples para o recomendador.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

---

**Autor**: Andrea M.  
**Contato**: [GitHub](https://github.com/andream001)
