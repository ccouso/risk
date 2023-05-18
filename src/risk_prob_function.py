import numpy as np
import itertools

def prob_3_attackers_2_defenders():

    ataque_gana_2 = 0
    defensa_gana_2 = 0
    ataque_gana_1_defensa_gana_1 = 0
    total = 0

    N_CARAS = 6

    # Genera todas las combinaciones posibles de tiradas de dados
    dados_ataque = list(itertools.product(range(1, N_CARAS + 1), repeat=3))
    dados_defensa = list(itertools.product(range(1, N_CARAS + 1), repeat=2))

    # Convierte las listas en matrices NumPy para un cálculo eficiente
    dados_ataque = np.array(dados_ataque)
    dados_defensa = np.array(dados_defensa)

    for tirada_ataque in dados_ataque:
        for tirada_defensa in dados_defensa:
            tirada_ataque = np.sort(tirada_ataque, axis=None)[::-1]
            tirada_defensa = np.sort(tirada_defensa, axis=None)[::-1]

            if (tirada_ataque[0] > tirada_defensa[0]) and (tirada_ataque[1] > tirada_defensa[1]):
                ataque_gana_2 += 1
            elif((tirada_ataque[0] <= tirada_defensa[0]) and (tirada_ataque[1] > tirada_defensa[1]) or 
                 (tirada_ataque[0] > tirada_defensa[0]) and (tirada_ataque[1] <= tirada_defensa[1])):
                ataque_gana_1_defensa_gana_1 += 1
            else:
                defensa_gana_2 += 1

            total += 1


    print(ataque_gana_1_defensa_gana_1)
    print(ataque_gana_2)
    print(defensa_gana_2)

    prob_ataque_gana_2 = calculate_simple_prob(ataque_gana_2, total)
    prob_ataque_gana_1_defensa_gana_1 = calculate_simple_prob(ataque_gana_1_defensa_gana_1, total)
    prob_defensa_gana_2 = calculate_simple_prob(defensa_gana_2, total)

    print(prob_ataque_gana_2)
    print(prob_ataque_gana_1_defensa_gana_1)
    print(prob_defensa_gana_2)

    return(prob_ataque_gana_2, prob_ataque_gana_1_defensa_gana_1, prob_defensa_gana_2)


def prob_2_attackers_2_defenders():

    ataque_gana_2 = 0
    defensa_gana_2 = 0
    ataque_gana_1_defensa_gana_1 = 0
    total = 0

    N_CARAS = 6

    # Genera todas las combinaciones posibles de tiradas de dados
    dados_ataque = list(itertools.product(range(1, N_CARAS + 1), repeat=2))
    dados_defensa = list(itertools.product(range(1, N_CARAS + 1), repeat=2))

    # Convierte las listas en matrices NumPy para un cálculo eficiente
    dados_ataque = np.array(dados_ataque)
    dados_defensa = np.array(dados_defensa)

    for tirada_ataque in dados_ataque:
        for tirada_defensa in dados_defensa:
            tirada_ataque = np.sort(tirada_ataque, axis=None)[::-1]
            tirada_defensa = np.sort(tirada_defensa, axis=None)[::-1]

            if (tirada_ataque[0] > tirada_defensa[0]) and (tirada_ataque[1] > tirada_defensa[1]):
                ataque_gana_2 += 1
            elif((tirada_ataque[0] <= tirada_defensa[0]) and (tirada_ataque[1] > tirada_defensa[1]) or 
                 (tirada_ataque[0] > tirada_defensa[0]) and (tirada_ataque[1] <= tirada_defensa[1])):
                ataque_gana_1_defensa_gana_1 += 1
            else:
                defensa_gana_2 += 1

            total += 1


    print(ataque_gana_1_defensa_gana_1)
    print(ataque_gana_2)
    print(defensa_gana_2)

    prob_ataque_gana_2 = calculate_simple_prob(ataque_gana_2, total)
    prob_ataque_gana_1_defensa_gana_1 = calculate_simple_prob(ataque_gana_1_defensa_gana_1, total)
    prob_defensa_gana_2 = calculate_simple_prob(defensa_gana_2, total)

    print(prob_ataque_gana_2)
    print(prob_ataque_gana_1_defensa_gana_1)
    print(prob_defensa_gana_2)

    return(prob_ataque_gana_2, prob_ataque_gana_1_defensa_gana_1, prob_defensa_gana_2)


def prob_1_attackers_2_defenders():
    ataque_gana_1 = 0
    defensa_gana_1 = 0
    total = 0

    N_CARAS = 6

    # Genera todas las combinaciones posibles de tiradas de dados
    dados_ataque = list(itertools.product(range(1, N_CARAS + 1), repeat=1))
    dados_defensa = list(itertools.product(range(1, N_CARAS + 1), repeat=2))

    # Convierte las listas en matrices NumPy para un cálculo eficiente
    dados_ataque = np.array(dados_ataque)
    dados_defensa = np.array(dados_defensa)

    for tirada_ataque in dados_ataque:
        for tirada_defensa in dados_defensa:
            tirada_ataque = np.sort(tirada_ataque, axis=None)[::-1]
            tirada_defensa = np.sort(tirada_defensa, axis=None)[::-1]

            if (tirada_ataque[0] > tirada_defensa[0]):
                ataque_gana_1 += 1
            else:
                defensa_gana_1 += 1

            total += 1


    print(ataque_gana_1)
    print(defensa_gana_1)


    prob_ataque_gana_1 = calculate_simple_prob(ataque_gana_1, total)
    prob_defensa_gana_1 = calculate_simple_prob(defensa_gana_1, total)

    print(prob_ataque_gana_1)
    print(prob_defensa_gana_1)

    return(prob_ataque_gana_1, prob_defensa_gana_1)


def prob_3_attackers_1_defenders():

    ataque_gana_1 = 0
    defensa_gana_1 = 0
    total = 0

    N_CARAS = 6

    # Genera todas las combinaciones posibles de tiradas de dados
    dados_ataque = list(itertools.product(range(1, N_CARAS + 1), repeat=3))
    dados_defensa = list(itertools.product(range(1, N_CARAS + 1), repeat=1))

    # Convierte las listas en matrices NumPy para un cálculo eficiente
    dados_ataque = np.array(dados_ataque)
    dados_defensa = np.array(dados_defensa)

    for tirada_ataque in dados_ataque:
        for tirada_defensa in dados_defensa:
            tirada_ataque = np.sort(tirada_ataque, axis=None)[::-1]
            tirada_defensa = np.sort(tirada_defensa, axis=None)[::-1]

            if (tirada_ataque[0] > tirada_defensa[0]):
                ataque_gana_1 += 1
            else:
                defensa_gana_1 += 1

            total += 1


    print(ataque_gana_1)
    print(defensa_gana_1)


    prob_ataque_gana_1 = calculate_simple_prob(ataque_gana_1, total)
    prob_defensa_gana_1 = calculate_simple_prob(defensa_gana_1, total)

    print(prob_ataque_gana_1)
    print(prob_defensa_gana_1)

    return(prob_ataque_gana_1, prob_defensa_gana_1)


def prob_2_attackers_1_defenders():

    ataque_gana_1 = 0
    defensa_gana_1 = 0
    total = 0

    N_CARAS = 6

    # Genera todas las combinaciones posibles de tiradas de dados
    dados_ataque = list(itertools.product(range(1, N_CARAS + 1), repeat=2))
    dados_defensa = list(itertools.product(range(1, N_CARAS + 1), repeat=1))

    # Convierte las listas en matrices NumPy para un cálculo eficiente
    dados_ataque = np.array(dados_ataque)
    dados_defensa = np.array(dados_defensa)

    for tirada_ataque in dados_ataque:
        for tirada_defensa in dados_defensa:
            tirada_ataque = np.sort(tirada_ataque, axis=None)[::-1]
            tirada_defensa = np.sort(tirada_defensa, axis=None)[::-1]

            if (tirada_ataque[0] > tirada_defensa[0]):
                ataque_gana_1 += 1
            else:
                defensa_gana_1 += 1

            total += 1


    print(ataque_gana_1)
    print(defensa_gana_1)


    prob_ataque_gana_1 = calculate_simple_prob(ataque_gana_1, total)
    prob_defensa_gana_1 = calculate_simple_prob(defensa_gana_1, total)

    print(prob_ataque_gana_1)
    print(prob_defensa_gana_1)

    return(prob_ataque_gana_1, prob_defensa_gana_1)


def prob_1_attackers_1_defenders():

    ataque_gana_1 = 0
    defensa_gana_1 = 0
    total = 0

    N_CARAS = 6

    # Genera todas las combinaciones posibles de tiradas de dados
    dados_ataque = list(itertools.product(range(1, N_CARAS + 1), repeat=1))
    dados_defensa = list(itertools.product(range(1, N_CARAS + 1), repeat=1))

    # Convierte las listas en matrices NumPy para un cálculo eficiente
    dados_ataque = np.array(dados_ataque)
    dados_defensa = np.array(dados_defensa)

    for tirada_ataque in dados_ataque:
        for tirada_defensa in dados_defensa:
            tirada_ataque = np.sort(tirada_ataque, axis=None)[::-1]
            tirada_defensa = np.sort(tirada_defensa, axis=None)[::-1]

            if (tirada_ataque[0] > tirada_defensa[0]):
                ataque_gana_1 += 1
            else:
                defensa_gana_1 += 1

            total += 1


    print(ataque_gana_1)
    print(defensa_gana_1)


    prob_ataque_gana_1 = calculate_simple_prob(ataque_gana_1, total)
    prob_defensa_gana_1 = calculate_simple_prob(defensa_gana_1, total)

    print(prob_ataque_gana_1)
    print(prob_defensa_gana_1)

    return(prob_ataque_gana_1, prob_defensa_gana_1)


def calculate_simple_prob(event_A, total):
    return format(event_A / total, ".4f")


prob_1_attackers_1_defenders()