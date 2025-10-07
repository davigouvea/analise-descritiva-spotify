# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analisar_dados_spotify():
    """
    Função principal que executa a leitura, tratamento, análise
    e visualização dos dados do Spotify.
    """
    
    # --- 1. Leitura do Dataset ---
    try:
        # Usando a codificação 'latin1' serve para ler o arquivo
        df = pd.read_csv('top10s.csv', encoding='latin1')
        print(">>> 1. Leitura de dados concluída com sucesso!")
        print("   - Colunas originais encontradas:", df.columns.tolist())
        print("-" * 50)

    except FileNotFoundError:
        print("Erro: O arquivo 'top10s.csv' não foi encontrado. Verifique se ele está na mesma pasta do script.")
        return
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return

    # --- 2. Tratamento e Padronização (A CORREÇÃO FINAL) ---
    print(">>> 2. Iniciando tratamento e padronização dos dados...")
    
    # Dicionário para renomear as colunas EXATAS do arquivo para nomes limpos
    rename_dict = {
        'Track.Name': 'track_name',
        'Artist.Name': 'artist',
        'Genre': 'genre',
        'Beats.Per.Minute': 'bpm',
        'Energy': 'energy',
        'Danceability': 'danceability',
        'Loudness..dB..': 'loudness_db',
        'Liveness': 'liveness',
        'Valence.': 'valence',
        'Length.': 'duration',
        'Acousticness..': 'acousticness',
        'Speechiness.': 'speechiness',
        'Popularity': 'popularity'
    }
    df.rename(columns=rename_dict, inplace=True)
    print("   - Colunas renomeadas para um formato limpo e padronizado.")

    # Remove a primeira coluna 'Numeracao' que é apenas um índice
    if 'Numeracao' in df.columns:
        df = df.drop('Numeracao', axis=1)
        print("   - Coluna de índice 'Numeracao' removida.")
    
    print("   - Verificando valores nulos...")
    if df.isnull().sum().sum() > 0:
        df.dropna(inplace=True)
        print("   - Linhas com valores nulos foram removidas.")
    else:
        print("   - Nenhum valor nulo foi encontrado.")

    print(">>> Tratamento de dados concluído!")
    print("-" * 50)

    # --- 3. Exploração Inicial (Estatísticas Descritivas) ---
    print(">>> 3. Gerando estatísticas descritivas...")
    
    # Agora podemos usar a lista de nomes limpos com segurança
    colunas_descritivas = [
        'bpm', 'energy', 'danceability', 'loudness_db', 'liveness',
        'valence', 'duration', 'acousticness', 'speechiness', 'popularity'
    ]
    
    estatisticas = df[colunas_descritivas].describe()
    
    print("   - Estatísticas Descritivas das Músicas:")
    print(estatisticas.to_string())
    print("-" * 50)

    # --- 4. Relatório Simples e Insights ---
    print(">>> 4. Gerando insights e visualizações...")
    
    # Usando as colunas com os nomes limpos ('artist', 'popularity', 'genre')
    artista_mais_popular = df.groupby('artist')['popularity'].sum().idxmax()
    musicas_do_artista = df['artist'].value_counts()[artista_mais_popular]
    print(f"\n   - Insight 1: O artista com a maior soma de popularidade é '{artista_mais_popular}' com {musicas_do_artista} músicas na lista.")

    genero_mais_comum = df['genre'].mode()[0]
    contagem_genero = df['genre'].value_counts()[genero_mais_comum]
    print(f"   - Insight 2: O gênero mais frequente é '{genero_mais_comum}', aparecendo {contagem_genero} vezes.")

    # --- Visualização Básica (Gráfico de Barras) ---
    top_10_artistas = df['artist'].value_counts().head(10)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_10_artistas.index, y=top_10_artistas.values, palette='viridis')
    
    plt.title('Top 10 Artistas com Mais Músicas de Sucesso', fontsize=16)
    plt.xlabel('Artista', fontsize=12)
    plt.ylabel('Número de Músicas', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    plt.savefig('top_10_artistas.png')
    
    print("\n   - Gráfico 'top_10_artistas.png' gerado com sucesso!")
    print("-" * 50)
    print(">>> Análise concluída!")

if __name__ == '__main__':
    analisar_dados_spotify()
