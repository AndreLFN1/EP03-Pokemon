import math
import copy

DELTA_T = 0.1
g = 2

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


def populaMatriz(matriz, pokemons): #DONE
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
        
        i += 1
    return matriz_populada


def preenchePokemon(matriz, id, x, y, raio): #DONE
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


def removePokemon(matriz, id, pokemons): #DONE
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
    # matriz_pokemons = removePokemon(matriz_pokemons, id, lista_arquivo[1:])
    car_pokemon = str(pokemons[id])[2:][:-2].split()
    inicial_pokemon = car_pokemon[0][0] + "  "
    print(inicial_pokemon)
    
    '''
    para cada linha
    para cada letra na linha
        verificar se a letra é igual ao pokemon
            se sim, substituir
        se nao, nao fazer nada
    '''
    i = 0
    for linha in matriz:
        p = 0 
        for elemento in matriz[i]:
            if elemento == inicial_pokemon:
                matriz[i][p] = '.  '
            else:  
                pass
            p += 1
        i += 1

    return matriz


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


def atualizaPosicao(x, y, vx, vy, dt=DELTA_T): #DONE
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    # Podia ser um dicionario? Podia, mas eu to meio de saco cheio dessa parte. Aqui eu retorno x e y numa lista, foda-se
    xy_atualizado = []

    x_atualizado = round(x + vx * DELTA_T, 2)
    y_atualizado = round(y + vy * DELTA_T - 0.5 * g * DELTA_T**2, 2)
    xy_atualizado.append(x_atualizado)
    xy_atualizado.append(-y_atualizado)
    return xy_atualizado


def atualizaVelocidade(vx, vy, dt=DELTA_T): #DONE
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    vxvy_atualizado = []

    Vy = vy - g * DELTA_T
    vxvy_atualizado.append(vx)
    vxvy_atualizado.append(Vy)

    return vxvy_atualizado


def grau2Radiano(theta): #DONE
    '''
    Esta função converte o ângulo theta em graus para radianos.
    Entrada: ângulo theta.
    Saída: ângulo theta em radianos.
    '''

    grau_radiano = math.radians(theta)
    return grau_radiano

def posicionaJogador(matriz, x): #DONE
    '''
    [FUNÇÃO CRIADA]

    Entrada: Essa função recebe a posição x e a matriz 
    Saída: Modifica a matriz
    '''
    matriz[-1][x] = 'T  '

    return matriz

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

    # Função que recebe o lista do grid e a informação dos pokemons e popula com pokemons
    matriz_pokemons = populaMatriz(matriz_vazia,lista_arquivo[1:])
    
    # A matriz com pokemons é populada com a posicao inicial do jogador
    matriz_inicial = posicionaJogador(matriz_pokemons,T)

    # Loop de impressão da matriz em um plano 2d
    imprimeMatriz(matriz_inicial)

    velocidade_inicial = float(input('Digite a velocidade de lançamento inicial (m/s): '))
    theta = grau2Radiano(int(input('Digite o ângulo de lançamento inicial (em graus): ')))

    Vx = round(velocidade_inicial * math.cos(theta), 2)
    Vy = round(velocidade_inicial * math.sin(theta), 2)
    
    floor_position = 0
    left_grid = 0
    right_grid = len(matriz_vazia)

    x_atualizado = 0
    y_atualizado = 0

    while left_grid <= x_atualizado <= right_grid and y_atualizado >= floor_position:
        # Atualiza posição com base no passo discreto
        xy_posicao = (atualizaPosicao(x_atualizado, y_atualizado, Vx, Vy, dt=DELTA_T))
        x_atualizado = xy_posicao[0]
        y_atualizado = xy_posicao[1]

        

        # Arredondando para desenhar o gráfico
        x_grafico = int(round(x_atualizado, 0))
        y_grafico = int(round(y_atualizado, 0))
        # Atualiza velocidade vertical

        
        vxvy_atualizado = atualizaVelocidade(Vx, Vy, dt=DELTA_T)
        Vy = vxvy_atualizado[1]

        # Atualiza valores no gráfico 
        matriz_inicial[y_grafico][x_grafico] = 'o  '
        print(x_grafico)
        print(y_grafico)

    imprimeMatriz(matriz_inicial)
   

 
main()
