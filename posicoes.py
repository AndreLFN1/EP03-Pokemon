import math

def atualizaPosicao(x, y, vx, vy, dt):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    return None


def atualizaVelocidade(vx, vy, dt):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    
    return None


def grau2Radiano(theta): #DONE
    '''
    Esta função converte o ângulo theta em graus para radianos.
    Entrada: ângulo theta.
    Saída: ângulo theta em radianos.
    '''

    grau_radiano = math.radians(theta)
    return grau_radiano
    
velocidade_inicial = float(input('Digite a velocidade de lançamento inicial (m/s): '))
theta = grau2Radiano(int(input('Digite o ângulo de lançamento inicial (em graus): ')))
g = 2
DELTA_T = 0.1
V0_x = round(velocidade_inicial*math.cos(theta),2)
V0_y = round(velocidade_inicial*math.sin(theta),2)

floor_position = 0
left_grid = -100
right_grid = 100

x_atualizado = 0
y_atualizado = 1
while left_grid <= x_atualizado <= right_grid and y_atualizado > floor_position:
    x_atualizado = round(V0_x * DELTA_T,0)
    y_atualizado = round(V0_y * DELTA_T - 0.5 * g * DELTA_T**2,0)
    DELTA_T += 0.1

    print(f'X: {x_atualizado}')
    print(f'Y: {y_atualizado}')

