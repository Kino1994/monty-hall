import random

def monty_hall_simulation(iterations=1000000, doors=3, open_doors=1, switch=True):
    wins = 0

    for _ in range(iterations):
        car_position = random.randint(0, doors - 1)
        player_choice = random.randint(0, doors - 1)
        
        possible_doors_to_open = [i for i in range(doors) if i != player_choice and i != car_position]
        doors_to_open = random.sample(possible_doors_to_open, open_doors)
        remaining_closed_doors = [i for i in range(doors) if i not in doors_to_open and i != player_choice]

        if switch:
            new_choice = remaining_closed_doors[0] if remaining_closed_doors[0] != player_choice else remaining_closed_doors[1]
        else:
            new_choice = player_choice

        if new_choice == car_position:
            wins += 1

    win_probability = wins / iterations
    return wins, iterations - wins, win_probability, 1 - win_probability

results_with_switch = monty_hall_simulation(switch=True)
results_without_switch = monty_hall_simulation(switch=False)

print(results_with_switch)
print(results_without_switch)
