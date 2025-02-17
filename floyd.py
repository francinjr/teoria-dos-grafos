import math  # Importa o módulo math, que fornece funções matemáticas, como 'inf' (infinito)

# Função para o algoritmo de Floyd-Warshall retornando as matrizes finais
def floyd_warshall_matrices(n, dist):
    INF = math.inf  # Define a constante 'INF' como infinito
    # Inicializa a matriz de predecessores (nó anterior) para cada par de nós
    previous_node = [[None] * n for _ in range(n)]  # Inicializa a matriz com 'None' para todos os pares de nós
    nodes = [chr(65 + i) for i in range(n)]  # Mapeia os índices dos nós para letras do alfabeto (A, B, C, ...)

    # Inicializa a matriz de predecessores para as arestas diretas
    for i in range(n):  # Percorre todos os nós
        for j in range(n):  # Percorre todos os nós
            if i != j and dist[i][j] != INF:  # Verifica se não é o mesmo nó e se há uma aresta entre i e j
                previous_node[i][j] = nodes[i]  # O nó anterior de j é o nó de origem i

    # Algoritmo principal de Floyd-Warshall para encontrar os caminhos mínimos entre todos os pares de nós
    for k in range(n):  # Passa por cada nó intermediário k
        for i in range(n):  # Para cada nó de origem i
            for j in range(n):  # Para cada nó de destino j
                # Se o caminho de i para j passando por k for mais curto, atualiza a distância
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]  # Atualiza a distância entre i e j
                    previous_node[i][j] = previous_node[k][j]  # Atualiza o predecessor de j

    # Verifica ciclos negativos
    ciclo_negativo_detectado = False  # Inicializa a variável para verificar ciclos negativos
    for i in range(n):  # Percorre todos os nós
        if dist[i][i] < 0:  # Verifica se há um ciclo negativo (distância de um nó para ele mesmo é negativa)
            ciclo_negativo_detectado = True  # Se encontrar um ciclo negativo, marca como verdadeiro
            break  # Interrompe o loop

    if ciclo_negativo_detectado:  # Se houver ciclo negativo
        log("Houve ciclos negativos.")  # Registra uma mensagem de erro
        return None, None  # Retorna None para as matrizes de distâncias e predecessores
    else:
        log("Não houve ciclos negativos.")  # Se não houver ciclo negativo, registra que tudo está ok

    return dist, previous_node  # Retorna as matrizes de distâncias e predecessores

# Função para reconstruir e imprimir o caminho entre dois nós
def reconstruir_caminho(previous_node, inicio, fim):
    nodes = [chr(65 + i) for i in range(len(previous_node))]  # Mapeia os índices dos nós para letras
    caminho = []  # Lista para armazenar o caminho reconstruído
    atual = fim  # Começa no nó final

    # Reconstrução do caminho, andando para trás, de fim até inicio
    while atual is not None and atual != inicio:  # Enquanto o nó atual não for o nó de origem
        caminho.append(atual)  # Adiciona o nó atual ao caminho
        atual = previous_node[nodes.index(inicio)][nodes.index(atual)]  # Vai para o nó anterior de atual

    if atual is None:  # Se o nó atual for None, significa que não há caminho
        log(f"Sem caminho de {inicio} para {fim}.")  # Registra uma mensagem de erro
        return  # Retorna sem nada

    caminho.append(inicio)  # Adiciona o nó de origem ao caminho
    caminho.reverse()  # Inverte a lista para ter o caminho de inicio até fim
    log(" -> ".join(caminho))  # Registra o caminho como uma string no formato "A -> B -> C"

# Função auxiliar para imprimir matrizes e registrar no arquivo
def log_matriz(matriz, nome):
    log(nome)  # Registra o nome da matriz
    for linha in matriz:  # Para cada linha da matriz
        log(" ".join(str(celula) for celula in linha))  # Registra os valores das células de uma linha

# Função de registro para salvar saída no console e no arquivo
def log(mensagem):
    print(mensagem)  # Imprime a mensagem no console
    with open("resultados.txt", "a") as arquivo:  # Abre o arquivo 'resultados.txt' no modo de anexar
        arquivo.write(mensagem + "\n")  # Escreve a mensagem no arquivo

# Função para ler o grafo de um arquivo e retornar a matriz de distâncias
def ler_grafo_do_arquivo(nome_arquivo):
    matriz_distancia = []  # Lista para armazenar a matriz de distâncias
    with open(nome_arquivo, "r") as arquivo:  # Abre o arquivo para leitura
        for linha in arquivo:  # Para cada linha no arquivo
            # Divide a linha em elementos, converte para inteiros, e substitui 'INF' por infinito
            linha_grafo = linha.split()  # Divide a linha em uma lista de strings
            matriz_distancia.append([math.inf if x == 'INF' else int(x) for x in linha_grafo])  # Substitui INF por infinito
    return matriz_distancia  # Retorna a matriz de distâncias

# Função para gerar formato DOT para Graphviz
def gerar_arquivo_dot(matriz_distancia, previous_node):
    nodes = [chr(65 + i) for i in range(len(matriz_distancia))]  # Mapeia os índices dos nós para letras
    conteudo_dot = "digraph G {\n"  # Inicia a definição do grafo no formato DOT

    # Cria as arestas com base na matriz de distâncias
    for i in range(len(matriz_distancia)):  # Para cada nó de origem
        for j in range(len(matriz_distancia)):  # Para cada nó de destino
            if matriz_distancia[i][j] != math.inf:  # Se houver uma aresta entre os nós i e j
                # Adiciona uma linha no formato DOT para a aresta com o peso
                conteudo_dot += f'  {nodes[i]} -> {nodes[j]} [label="{matriz_distancia[i][j]}"];\n'

    conteudo_dot += "}\n"  # Fecha a definição do grafo no formato DOT

    # Escreve o formato DOT em um arquivo
    with open("grafo.dot", "w") as arquivo:
        arquivo.write(conteudo_dot)  # Escreve o conteúdo no arquivo 'grafo.dot'

    print("Arquivo DOT para o Graphviz foi criado: grafo.dot")  # Imprime uma mensagem informando que o arquivo foi gerado

# Ler o grafo do arquivo entrada.txt
matriz_distancia = ler_grafo_do_arquivo("entrada.txt")  # Chama a função para ler o grafo e obter a matriz de distâncias

# Obter o número de nós
n = len(matriz_distancia)  # Calcula o número de nós (tamanho da matriz)

# Limpar o arquivo antes de escrever
open("resultados.txt", "w").close()  # Apaga o conteúdo anterior do arquivo 'resultados.txt'

# Executar o algoritmo de Floyd-Warshall modificado
dist, previous_node = floyd_warshall_matrices(n, matriz_distancia)  # Chama o algoritmo de Floyd-Warshall

if dist and previous_node:  # Se o algoritmo não encontrou ciclos negativos e retornou as matrizes
    log_matriz(dist, "Matriz Final de Distâncias:")  # Registra a matriz de distâncias
    log_matriz(previous_node, "\nMatriz Final de Nós Anteriores:")  # Registra a matriz de predecessores

    # Exemplo de reconstrução de caminho
    log("\nCaminho Reconstruído:")  # Registra a mensagem de início do caminho
    reconstruir_caminho(previous_node, 'C', 'B')  # Reconstrói e imprime o caminho de C para B
    
    # Gerar o arquivo DOT para o Graphviz
    gerar_arquivo_dot(dist, previous_node)  # Gera o arquivo DOT para representar o grafo