# Panama Monte Carlo Simulator

A tiny Python simulation for a dice game we play in bars.

The important question: when you roll, should you keep only `3`s, or should you keep both `1`s and `3`s?

This simulator tests both choices over a large number of games. The result is pleasantly useful bar math: **keeping both `1` and `3` gives the better average score.**

## Game Assumptions

- The game uses `5` six-sided dice.
- A `3` scores `0`.
- Every other die scores its face value.
- Lower total score is better.
- Each turn, you roll the dice you have left and must keep at least one die.
- The game ends once all dice have been kept.

## Strategies Compared

### Strategy 1

Keep all `3`s. If no `3`s are rolled, keep the single lowest die.

### Strategy 2

Keep all `3`s and all `1`s. If no `1`s or `3`s are rolled, keep the single lowest die.

## Result

Example run:

```text
Panama Simulator 1.0
5 dice, 1000000 trials
Average score (strategy 1 - save only 3s, else lowest): 6.801
Average score (strategy 2 - save 3s and 1s): 6.595
```

Because lower scores are better, Strategy 2 wins in the long run.

In other words: **keep the `1`s.**

## Run It

```bash
python3 simulate.py
```

The script runs `1,000,000` simulated games for each strategy by default.

## How It Works

The simulator uses Monte Carlo testing: it plays the game many times with random dice rolls, records the final score for each strategy, and compares the average score.

More trials reduce random noise, but the conclusion is stable: keeping both `1`s and `3`s beats only keeping `3`s.
