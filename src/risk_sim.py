import random
import numpy as np
import math
import os

def remove_file(path):

    if os.path.exists(path):
        os.remove(path)
        print(path + " eliminado exitosamente.")
    else:
        print("El archivo no existe.")


def get_random_int():
    return random.randint(1, 6)


def play_risk(attackers, defenders):

    attackers_dice = []
    defenders_dice = []
    loss_attackers = 0
    loss_defenders = 0

    for i in range(attackers):
        attackers_dice.append(get_random_int())
    for i in range(defenders):
        defenders_dice.append(get_random_int())

    attackers_dice.sort(reverse=True)
    defenders_dice.sort(reverse=True)
    print("Attackers: ", attackers_dice)
    print("Defenders: ", defenders_dice)
    for i in range(min(attackers, defenders)):
        if attackers_dice[i] > defenders_dice[i]:
            loss_defenders += 1
        else:
            loss_attackers += 1
    return loss_attackers, loss_defenders


def battle_sim(attackers, defenders):

    total_loss_attackers = 0
    total_loss_defenders = 0

    print("Battle 2!")

    while attackers > 0 and defenders > 0:
        attackers_dices = get_attacker_dices(attackers)
        defenders_dices = get_defender_dices(defenders)
        loss_attackers, loss_defenders = play_risk(attackers_dices, defenders_dices)
        attackers -= loss_attackers
        defenders -= loss_defenders
        total_loss_attackers += loss_attackers
        total_loss_defenders += loss_defenders

    print("finished battle!")
    
    return total_loss_attackers, total_loss_defenders


def get_attacker_dices(attackers):
    if (attackers >= 3):
        attackers_dices = 3
    elif (attackers == 2):
        attackers_dices = 2
    elif (attackers == 1):
        attackers_dices = 1
    else:
        attackers_dices = 0
    
    return attackers_dices


def get_defender_dices(defenders):
    if (defenders >= 2):
        defenders_dices = 2
    elif (defenders == 1):
        defenders_dices = 1
    else:
        defenders_dices = 0
    
    return defenders_dices


def battle_sim_only_3_attackers(attacker, defender, TOTAL_BATTLES):

    defenders_won = 0
    attackers_won = 0

    array_attackers = []
    array_defenders = []

    for battle in range(TOTAL_BATTLES):

        attacker_survivors = attacker
        defender_survivors = defender

        while attacker_survivors > 0 and defender_survivors > 0:
            group_attack = get_attacker_dices(attacker_survivors)
            loss_attackers, loss_defenders = battle_sim(group_attack, defender_survivors)

            attacker_survivors -= loss_attackers
            defender_survivors -= loss_defenders


        if (attacker_survivors == 0):
            array_defenders.append(defender_survivors)
            defenders_won += 1
        else:
            array_attackers.append(attacker_survivors)
            attackers_won += 1

    np_array_attackers = np.array(array_attackers)
    np_array_defenders = np.array(array_defenders)

    return (np_array_attackers, np_array_defenders, attackers_won, defenders_won)
    

def battle_sim_Risk_conventional(attacker, defender, TOTAL_BATTLES):

    defenders_won = 0
    attackers_won = 0

    array_attackers = []
    array_defenders = []

    for battle in range(TOTAL_BATTLES):
            
        attacker_survivors = attacker
        defender_survivors = defender

        loss_attackers, loss_defenders = battle_sim(attacker, defender)

        attacker_survivors -= loss_attackers
        defender_survivors -= loss_defenders

        if (attacker_survivors == 0):
            array_defenders.append(defender_survivors)
            defenders_won += 1
        else:
            array_attackers.append(attacker_survivors)
            attackers_won += 1

    np_array_attackers = np.array(array_attackers)
    np_array_defenders = np.array(array_defenders)

    return (np_array_attackers, np_array_defenders, attackers_won, defenders_won)



def risk_simulator(TOTAL_BATTLES, attacker, defender, type_of_battle):


    if(type_of_battle == "conventional"):
        (np_array_attackers, np_array_defenders, attackers_won, defenders_won) = battle_sim_Risk_conventional(attacker, defender, TOTAL_BATTLES)
    elif(type_of_battle == "only_3_attackers"):
        (np_array_attackers, np_array_defenders, attackers_won, defenders_won) = battle_sim_only_3_attackers(attacker, defender, TOTAL_BATTLES)


    mean_attackers = np.mean(np_array_attackers)
    mean_defenders = np.mean(np_array_defenders)

    print()

    print("Battle summary: Attackers", attacker, " defenders: ", defender, " battle simulations: ", TOTAL_BATTLES, "\n")

    print("Mean attackers: ", format(mean_attackers, ".2f"))
    print("Mean defenders: ", format(mean_defenders, ".2f"))

    print("Attackers won: ", attackers_won)
    print("Defenders won: ", defenders_won)

    prob_attackers = attackers_won / TOTAL_BATTLES
    prob_defenders = defenders_won / TOTAL_BATTLES

    print("Prob_attackers: ", prob_attackers)
    print("Prob_defenders: ", prob_defenders)

    

    return (np_array_attackers, np_array_defenders, attackers_won, defenders_won, prob_attackers, prob_defenders)


def main():
    TOTAL_BATTLES = 50000
    attacker = 10
    defender = 10
    type_of_battle = "only_3_attackers"

    RESULT_CVS_FILE_PROB = "results_cvs_prob.txt"
    RESULT_MEAN_ATTACKERS_FILE = "results_mean_attackers.txt"
    RESULT_MEAN_DEFENDERS_FILE = "results_mean_defenders.txt"
    RESULT_ALL_STATISTICS = "results_all_statistics.txt"




    remove_file(RESULT_CVS_FILE_PROB)
    remove_file(RESULT_MEAN_ATTACKERS_FILE) 
    remove_file(RESULT_MEAN_DEFENDERS_FILE) 
    remove_file(RESULT_ALL_STATISTICS)


    for at in range(1, attacker + 1): 
        for de in range(1, defender + 1): 
            result = risk_simulator(TOTAL_BATTLES, at, de, type_of_battle)

            mean_attackers = np.mean(result[0])
            if math.isnan(mean_attackers):
                mean_attackers = 0
            mean_defenders = np.mean(result[1])
            if math.isnan(mean_defenders):
                mean_defenders = 0
            std_attackers = np.std(result[0])
            if math.isnan(std_attackers):
                std_attackers = 0
            std_defenders = np.std(result[1])    
            if math.isnan(std_defenders):
                std_defenders = 0


            with open(RESULT_ALL_STATISTICS, "a") as myfile:
                myfile.write("Attackers: " + str(at) + " Defenders: " + str(de) + " Prob_attackers: " + str(result[4]) + " Prob_defenders: " + str(result[5]) + " Mean_attackers: " + str(mean_attackers) + " Mean_defenders: " + str(mean_defenders) + " Std_attackers: " + str(std_attackers) + " Std_defenders: " + str(std_defenders) + "\n")
                myfile.close()


            with open(RESULT_CVS_FILE_PROB, "a") as myfile:
                myfile.write(str(result[4]) + ", ")
                myfile.close()

            with open(RESULT_MEAN_ATTACKERS_FILE, "a") as myfile:
                myfile.write(str(mean_attackers) + ", ")
                myfile.close()

            with open(RESULT_MEAN_DEFENDERS_FILE, "a") as myfile:
                myfile.write(str(mean_defenders) + ", ")
                myfile.close()

        with open(RESULT_CVS_FILE_PROB, "a") as myfile:
            myfile.write("\n")
            myfile.close()

        with open(RESULT_MEAN_ATTACKERS_FILE, "a") as myfile:
            myfile.write("\n")
            myfile.close()
    
        with open(RESULT_MEAN_DEFENDERS_FILE, "a") as myfile:
            myfile.write("\n")
            myfile.close()

    result = risk_simulator(TOTAL_BATTLES, attacker, defender, type_of_battle)

    print(result)


if __name__ == "__main__":
    main()  


