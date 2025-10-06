# Análise Descritiva de Músicas do Spotify (2010-2019)

**Universidade Positivo**
**Curso:** Tópicos Especiais em Software
**Professor:** Tiago Batista Pedra
**Integrantes:** [Seu Nome Completo] e [Nome Completo da Dupla]

---

## 1. Descrição do Projeto

Este projeto foi desenvolvido para a Atividade Avaliativa A1 e consiste em um sistema em Python que realiza uma análise descritiva de dados. [cite_start]O sistema utiliza a biblioteca `pandas` para leitura e manipulação de um dataset do Kaggle e `matplotlib`/`seaborn` para a visualização gráfica dos dados[cite: 11, 24].

## 2. Dataset Escolhido

O dataset utilizado foi o **"Top Spotify Songs from 2010-2019"**, obtido no Kaggle. [cite_start]Ele contém informações sobre as músicas mais populares da década, incluindo características como gênero, artista, batidas por minuto (BPM), energia, e popularidade.

- **Formato:** `.csv`
- **Link:** [https://www.kaggle.com/datasets/leonardopena/top50spotify2010-2019](https://www.kaggle.com/datasets/leonardopena/top50spotify2010-2019)

## 3. Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado.

### Instalação

1.  Clone este repositório:
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd seu-repositorio-final
    ```
3.  Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

### Execução

Para rodar a análise, execute o script principal:
```bash
python analise_spotify.py
```
O script irá imprimir o relatório de análise no console e salvará um gráfico de barras chamado `top_10_artistas.png` no diretório.

## 4. Resumo da Análise

O script executa as seguintes etapas:

1.  [cite_start]**Leitura dos Dados:** Carrega o arquivo `top10s.csv` usando pandas[cite: 15].
2.  **Tratamento e Limpeza:**
    -   [cite_start]Padroniza os nomes das colunas (para minúsculas e sem espaços).
    -   [cite_start]Verifica a existência de valores nulos (neste dataset, não foram encontrados).
    -   [cite_start]Confirma se os tipos de dados de cada coluna estão adequados para a análise.
3.  **Análise Exploratória:**
    -   [cite_start]Calcula as estatísticas descritivas (média, mediana, desvio padrão, etc.) para as colunas numéricas[cite: 22].
    -   Identifica os artistas e gêneros mais frequentes.
4.  **Visualização:**
    -   [cite_start]Gera um gráfico de barras com os 10 artistas que mais apareceram na lista de sucessos, salvando-o como uma imagem PNG[cite: 24].