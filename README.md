# Algoritmo de Floyd-Warshall - Projeto de Cálculo de Caminhos Mínimos

Este projeto implementa o algoritmo de Floyd-Warshall para encontrar os caminhos mínimos entre todos os pares de nós em um grafo orientado. O programa também suporta a detecção de ciclos negativos, a reconstrução de caminhos e a geração de arquivos no formato DOT para visualização no Graphviz.

## Funcionalidades

- **Cálculo de caminhos mínimos:** Utiliza o algoritmo de Floyd-Warshall para calcular as menores distâncias entre todos os pares de nós.
- **Detecção de ciclos negativos:** Verifica se há ciclos com pesos negativos no grafo.
- **Reconstrução de caminhos:** Reconstrói o caminho de um nó inicial para um nó final.
- **Geração de arquivos DOT:** Cria uma representação do grafo no formato DOT, que pode ser visualizada usando ferramentas como o Graphviz.
- **Log de resultados:** Salva os resultados das matrizes de distâncias, predecessores e reconstrução de caminhos em um arquivo `resultados.txt`.

## Pré-requisitos

Certifique-se de que você tenha instalado:

- Python 3.12.9 ou superior
- Um editor de texto ou IDE para Python
- Graphviz (opcional, para visualizar o arquivo DOT gerado)

## Estrutura do Projeto

- `entrada.txt`: Arquivo de entrada que contém a matriz de adjacência do grafo.
- `floyd.py`: Código principal contendo a implementação do algoritmo.
- `resultados.txt`: Arquivo de saída onde os resultados são salvos.
- `grafo.dot`: Arquivo gerado para visualização no Graphviz.

## Formato do Arquivo de Entrada

O arquivo `entrada.txt` deve conter a matriz de adjacência do grafo, onde:

- Cada linha representa os pesos das arestas entre os nós.
- `INF` é usado para indicar que não há aresta entre dois nós.

### Exemplo de Entrada

```txt
0 3 INF 7
8 0 2 INF
5 INF 0 1
2 INF INF 0
```

Após escrever sua matriz de entrada, rode a aplicação para gerar os resultados no arquivo resultados.txt, e o código Graphviz no arquivo grafo.dot

## Gerando a imagem do grafo da matriz final de distâncias usando o Graphviz
### No diretório em que se encontra o arquivo floyd.py, exceute o comando:
```bash
 dot -Tpng grafo.dot -o grafo.png
```
Após executar esse comando uma imagem grafo.png será criada

## Contribuidores
- Francinaldo Manoel dos Anjos Junior
- José Mikael da Silva Alves
- Lucas Rock da Silva Cardoso
- Lucas Vinicius Fernandes da Silva
- Samuel Rógenes Carvalho Freire




