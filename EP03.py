import math
import copy

DELTA_T = 0.1
GRAVIDADE = 2

# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP3.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================

def leArquivo(file_name): #DONE
    '''
    Esta função lê um arquivo ('entrada.txt' por default) e
    retorna uma lista de listas.
    Entrada: arquivo cujo nome está armazenado em nomeArquivo.
             Por default, é 'entrada.txt'
    Saída: uma lista de listas, onde o primeiro elemento é uma
           lista de inteiros [m, n] (dimensões da matriz) e os
           elementos subsequentes são listas que representam as
           característica lidas dos Pokémons na forma:
                [nome, raio, x, y]
    '''

    # Criando lista vazia para inserção de parâmetros
    parametros_arquivo = []
    # Adicionando linha a linha em uma nova lista
    parameters_file = (open(file_name, 'r').readlines())

    for line in parameters_file:
        parametros_arquivo.append((line.split("\n")))

    # A ideia aqui é remover o '' que ficou nas listas de um jeito porco, porém funcional
    i = 0
    for item in parameters_file:
        if len(parametros_arquivo[i]) > 1:
            del parametros_arquivo[i][-1]
            i += 1

    return parametros_arquivo


def criaMatriz(m, n): #DONE
    '''
    Esta função cria e retorna uma lista de listas.
    Entrada: dois inteiros que representam o número de linhas e
             o número de colunas da matriz.
    Saída: uma lista de m listas, cada uma com n elementos, todos
           inicializados com zeros.
    '''
    lista_n_elementos = []
    lista_n_listas = []

    for i in range(n):
        lista_n_elementos.append('.  ') # A matriz é populada com pontos

    for l in range(m):
        lista_n_listas.append(lista_n_elementos)
        # Reserva cada lista em um local da memória
        lista_n_listas = copy.deepcopy(lista_n_listas)

    return lista_n_listas


def populaMatriz(matriz, pokemons):
    '''
    Esta função recebe uma matriz e uma lista contendo listas que
    representam os pokémons na forma [nome, raio, x, y] e preenche-a
    os pokémons conforme a representação retangular considerando os
    raios da representação.
    Entrada: matriz representada por uma lista de listas
    Saída: A matriz fornecida é modificada.
    '''

    lista_arquivo = pokemons
    matriz_vazia = matriz
    i = 0
    for pokemon in lista_arquivo:
    # Ex: ['Nidoran', '1', '14', '13']
        
        car_pokemon = str(lista_arquivo[i])[2:][:-2].split()
        inicial_pokemon = car_pokemon[0][0] + "  "
        raio = int(car_pokemon[1])
        x = int(car_pokemon[2])
        y = -(int(car_pokemon[3]) + 1)
        # Definindo o ponto central do pokemon
        matriz_vazia[y][x] = inicial_pokemon

        matriz_populada = preenchePokemon(matriz_vazia, inicial_pokemon, x, y, raio)
        '''
        # Preenchendo o raio para a esquerda e direita no grid
        
        #Preenchendo a coluna com o raio do pokemon para baixo
        h = y + 1
        for linha in range(raio):
            matriz_vazia[h][x] = inicial_pokemon
            h += 1
        
        #Preenchendo a coluna com o raio do pokemon para cima 
        l = y - 1
        for linha in range(raio):
            matriz_vazia[l][x] = inicial_pokemon
            l -= 1
        
        
        # Preenchendo diagonais para cima/esquerda
        h = y
        for linha in range(raio + 1): 
            # Preenchendo o raio para esquerda
            p = x - 1
            for k in range(raio):
                matriz_vazia[h][p] = inicial_pokemon
                p -= 1
            h -= 1

        # Preenchendo diagonais para cima/direita
        h = y
        for linha in range(raio + 1):
            # Preenchendo o raio para direita
            p = x + 1
            for k in range(raio):
                matriz_vazia[h][p] = inicial_pokemon
                p += 1
            h -= 1
        
        # Preenchendo diagonais para baixo/esquerda
        h = y
        for linha in range(raio + 1): 
            # Preenchendo o raio para esquerda
            p = x - 1
            for k in range(raio):
                matriz_vazia[h][p] = inicial_pokemon
                p -= 1
            h += 1

        # Preenchendo diagonais para baixo/direita
        h = y
        for linha in range(raio + 1):
            # Preenchendo o raio para direita
            p = x + 1
            for k in range(raio):
                matriz_vazia[h][p] = inicial_pokemon
                p += 1
            h += 1

        
        '''
        i += 1
    return matriz_populada


def preenchePokemon(matriz, id, x, y, raio):
    '''
    Esta função é auxiliar da função populaMatriz. Ela insere
    um Pokémon na matriz de acordo com sua representação retangular
    baseada no raio ao redor do ponto central (x,y)
    Entrada: matriz representada por uma lista de listas
             id é o número a preencher a matriz; para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente.
             x,y são as coordenadas do ponto central
             raio é a distância a ser guardada a partir do
             ponto central.
    Saída: A matriz fornecida é modificada.
    '''

    # Preenchendo o raio para a esquerda e direita no grid
        
        #Preenchendo a coluna com o raio do pokemon para baixo
    h = y + 1
    for linha in range(raio):
        matriz[h][x] = id
        h += 1
    
    #Preenchendo a coluna com o raio do pokemon para cima 
    l = y - 1
    for linha in range(raio):
        matriz[l][x] = id
        l -= 1
    
    
    # Preenchendo diagonais para cima/esquerda
    h = y
    for linha in range(raio + 1): 
        # Preenchendo o raio para esquerda
        p = x - 1
        for k in range(raio):
            matriz[h][p] = id
            p -= 1
        h -= 1

    # Preenchendo diagonais para cima/direita
    h = y
    for linha in range(raio + 1):
        # Preenchendo o raio para direita
        p = x + 1
        for k in range(raio):
            matriz[h][p] = id
            p += 1
        h -= 1
    
    # Preenchendo diagonais para baixo/esquerda
    h = y
    for linha in range(raio + 1): 
        # Preenchendo o raio para esquerda
        p = x - 1
        for k in range(raio):
            matriz[h][p] = id
            p -= 1
        h += 1

    # Preenchendo diagonais para baixo/direita
    h = y
    for linha in range(raio + 1):
        # Preenchendo o raio para direita
        p = x + 1
        for k in range(raio):
            matriz[h][p] = id
            p += 1
        h += 1

    return matriz


def removePokemon(matriz, id, pokemons):
    '''
    Esta função recebe uma matriz, o numeral que representa o pokémon
    a ser removido da matriz (id) e a lista contendo as listas que
    representam pokémons, substituindo os numerais id por zero
    Entrada: matriz representada por uma lista de listas;
             id é o número a preencher a matriz, para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente;
             pokemons lista contendo as listas que representam pokémons.
    Saída: A matriz fornecida é modificada.
    '''
    return None


def imprimeMatriz(matriz): #DONE
    '''
    Esta função imprime a matriz dada.
    Note que a matriz deve ser impressa com espelhamento vertical, 
    pois a primeira linha representa o chão.
    Entrada: matriz representada por uma lista de listas.
    '''
    p = 0
    for l in matriz:
        for i in matriz[p]:
            print(i,end="")
        print("")
        p += 1

    return None


def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    return None


def atualizaVelocidade(vx, vy, dt=DELTA_T):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    return None


def grau2Radiano(theta):
    '''
    Esta função converte o ângulo theta em graus para radianos.
    Entrada: ângulo theta.
    Saída: ângulo theta em radianos.
    '''
    return None



def main():
    nome = input("Digite o nome do arquivo: ")
    N = int(input("Digite o numero N de pokebolas: "))
    T = int(input('Digite a posição inicial no eixo x do jogador: '))
    
    # Variável que guarda as dimensões da matriz e as informações dos pokemons
    lista_arquivo = leArquivo(nome)
    
    # Guarda as dimensoes da matriz em uma lista
    dimensoes_matriz = str(lista_arquivo[0])[2:][:-2].split()
    
    # Retorna uma lista de listas com m linhas (numero de elementos) e n colunas (numero de elementos em cada elemento)
    matriz_vazia = criaMatriz(int(dimensoes_matriz[0]),int(dimensoes_matriz[1]))

    # Função que recebe o lista do grid e a informação dos pokemons
    matriz_pokemons = populaMatriz(matriz_vazia,lista_arquivo[1:])
    '''
    i = 1
    for pokemon in lista_arquivo[1:]:
    # Ex: ['Nidoran', '1', '14', '13']
        
        car_pokemon = str(lista_arquivo[i])[2:][:-2].split()
        inicial_pokemon = car_pokemon[0][0] + "  "
        raio = int(car_pokemon[1])
        x = int(car_pokemon[2])
        y = -(int(car_pokemon[3]) + 1)
        # Definindo o ponto central do pokemon
        matriz_vazia[y][x] = inicial_pokemon

        # Preenchendo o raio para a esquerda e direita no grid
        
        #Preenchendo a coluna com o raio do pokemon para baixo
        h = y + 1
        for linha in range(raio):
            matriz_vazia[h][x] = inicial_pokemon
            h += 1
        
        #Preenchendo a coluna com o raio do pokemon para cima 
        l = y - 1
        for linha in range(raio):
            matriz_vazia[l][x] = inicial_pokemon
            l -= 1
        
        
        # Preenchendo diagonais para cima/esquerda
        h = y
        for linha in range(raio + 1): 
            # Preenchendo o raio para esquerda
            p = x - 1
            for k in range(raio):
                matriz_vazia[h][p] = inicial_pokemon
                p -= 1
            h -= 1

        # Preenchendo diagonais para cima/direita
        h = y
        for linha in range(raio + 1):
            # Preenchendo o raio para direita
            p = x + 1
            for k in range(raio):
                matriz_vazia[h][p] = inicial_pokemon
                p += 1
            h -= 1
        
        # Preenchendo diagonais para baixo/esquerda
        h = y
        for linha in range(raio + 1): 
            # Preenchendo o raio para esquerda
            p = x - 1
            for k in range(raio):
                matriz_vazia[h][p] = inicial_pokemon
                p -= 1
            h += 1

        # Preenchendo diagonais para baixo/direita
        h = y
        for linha in range(raio + 1):
            # Preenchendo o raio para direita
            p = x + 1
            for k in range(raio):
                matriz_vazia[h][p] = inicial_pokemon
                p += 1
            h += 1

        i += 1
    '''
    # Loop de impressão da matriz em um plano 2d
    imprimeMatriz(matriz_pokemons)

 
main()
