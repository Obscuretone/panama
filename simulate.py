import random

# Roll n dice
def roll_dice(n):
    return [random.randint(1, 6) for _ in range(n)]

# Score rule: 3 counts as 0, others face value
def score_die(d):
    return 0 if d == 3 else d

# Strategy 1: always save all 3s, otherwise save the single lowest non-3
# Strategy 2: always save all 3s, and also save 1s

def play_game(n, strategy):
    dice_left = n
    saved = []

    while dice_left > 0:
        roll = roll_dice(dice_left)

        if strategy == 1:
            # Save all 3s
            saves = [d for d in roll if d == 3]
            if not saves:
                # If no 3s, save the lowest die
                saves = [min(roll)]
        elif strategy == 2:
            # Save all 3s and all 1s
            saves = [d for d in roll if d in (1, 3)]
            if not saves:
                # If no 1s or 3s, save the lowest die
                saves = [min(roll)]
        else:
            raise ValueError("Unknown strategy")

        saved.extend(saves)
        dice_left -= len(saves)

    return sum(score_die(d) for d in saved)

# Run simulations
def simulate(n=5, strategy=1, trials=100000):
    return sum(play_game(n, strategy) for _ in range(trials)) / trials

if __name__ == "__main__":
    trials = 1000000
    num_dice = 5

    

    print(f"Panama Simulator 1.0")
    print(f"{num_dice:.0f} dice, {trials:.0f} trials")

    avg1 = simulate(n=num_dice, strategy=1, trials=trials)
    print(f"Average score (strategy 1 - save only 3s, else lowest): {avg1:.3f}")

    avg2 = simulate(n=num_dice, strategy=2, trials=trials)
    print(f"Average score (strategy 2 - save 3s and 1s): {avg2:.3f}")