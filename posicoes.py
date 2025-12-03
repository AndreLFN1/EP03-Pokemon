import math
DELTA_T = 0.1

def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
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
    xy_atualizado.append(y_atualizado)
    return xy_atualizado


def atualizaVelocidade(vx, vy, dt=DELTA_T):
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


#atualizaVelocidade(vx, vy, dt)

#atualizaPosicao(x, y, vx, vy, dt)



import math

velocidade_inicial = float(input('Digite a velocidade de lançamento inicial (m/s): '))
theta = grau2Radiano(int(input('Digite o ângulo de lançamento inicial (em graus): ')))
g = 2.0   # gravidade na Lua

Vx = round(velocidade_inicial * math.cos(theta), 2)
Vy = round(velocidade_inicial * math.sin(theta), 2)

floor_position = 0
left_grid = -100
right_grid = 100

x_atualizado = 0
y_atualizado = 0

while left_grid <= x_atualizado <= right_grid and y_atualizado >= floor_position:
    # Atualiza posição com base no passo discreto
    xy_posicao = (atualizaPosicao(x_atualizado, y_atualizado, Vx, Vy, dt=DELTA_T))
    x_atualizado = xy_posicao[0]
    y_atualizado = xy_posicao[1]

    # Arredondando para desenhar o gráfico
    x_grafico = round(x_atualizado, 0)
    y_grafico = round(y_atualizado, 0)
    # Atualiza velocidade vertical
    
    vxvy_atualizado = atualizaVelocidade(Vx, Vy, dt=DELTA_T)
    Vy = vxvy_atualizado[1]


