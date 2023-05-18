import random


def get_random_int():
    return random.randint(1, 6)



def play_risk(attackers, defenders):

    attackers_dice = []
    defenders_dice = []

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
            defenders -= 1
        else:
            attackers -= 1
    return attackers, defenders

def play_risk_2(attackers, defenders):

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



def battle():
    MAX_ATTACKERS = 3
    MAX_DEFENDERS = 2
    attackers = 3
    defenders = 2
    print("Battle!")
    while attackers > 0 and defenders > 0:
        loss_attackers, loss_defenders = play_risk(attackers, defenders)


    print("finished battle!")
    
    loss_attackers = MAX_ATTACKERS - attackers
    loss_defenders = MAX_DEFENDERS - defenders

    return loss_attackers, loss_defenders


def battle_2(attackers, defenders):

    attackers_dices = get_attacker_dices(attackers)
    defenders_dices = get_defender_dices(defenders)
    total_loss_attackers = 0
    total_loss_defenders = 0
    print("Battle 2!")

    while attackers > 0 and defenders > 0:
        loss_attackers, loss_defenders = play_risk_2(attackers_dices, defenders_dices)
        attackers -= loss_attackers
        defenders -= loss_defenders
        total_loss_attackers += loss_attackers
        total_loss_defenders += loss_defenders

        attackers_dices = get_attacker_dices(attackers)
        defenders_dices = get_defender_dices(defenders)
        
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


def generate_battle(num_battles):
    attackers_total_loss = 0
    defenders_total_loss = 0
    for i in range(num_battles):
        loss_attackers, loss_defenders = battle()

        attackers_total_loss += loss_attackers
        defenders_total_loss += loss_defenders
        

    total_loss = attackers_total_loss + defenders_total_loss

    print("Attackers total loss: ", attackers_total_loss)
    print("Defenders total loss: ", defenders_total_loss)
    print("Total loss: ", total_loss)

    print("Average attackers loss: ", attackers_total_loss / total_loss)
    print("Average defenders loss: ", defenders_total_loss / total_loss)
    print("Number of battles: ", num_battles)

    return attackers_total_loss, defenders_total_loss


def generate_battle2(attacker, defender):

    while attacker > 0 and defender > 0:
        group_attack = get_attacker_dices(attacker)
        loss_attackers, loss_defenders = battle_2(group_attack, defender)

        attacker -= loss_attackers
        defender -= loss_defenders

    if (attacker == 0):
        return "Defenders won"
    else:
        return "Attackers won"


def main():

    num_battles = 10000
    defenders_won = 0
    attackers_won = 0
    # attackers_total_loss, defenders_total_loss = generate_battle(num_battles)

    for i in range(num_battles):
        attacker = 3
        defender = 3
        result = generate_battle2(attacker, defender)

        if (result == "Defenders won"):
            defenders_won += 1
        else:
            attackers_won += 1

    print("Attackers won: ", attackers_won)
    print("Defenders won: ", defenders_won)
    print("Prob_attackers: ", attackers_won / num_battles)
    print("Prob_defenders: ", defenders_won / num_battles)




if __name__ == "__main__":
    main()  


