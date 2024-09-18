# Monty Hall Problem Simulation

## Introduction
The Monty Hall problem is a well-known probability puzzle that challenges our intuition about conditional probability. Based on the TV game show "Let's Make a Deal," hosted by Monty Hall, the classic version of this problem involves three doors: behind one door is a car, and behind the others are goats. After the contestant makes an initial choice, the host reveals a goat behind one of the unchosen doors, and the contestant is given the option to switch their choice. Mathematically, switching doors is the best strategy, but this simulation also explores what happens when the contestant chooses **not to switch**.

This simulation generalizes the problem, allowing for a customizable number of doors and doors opened by the host. Additionally, it compares the results when the contestant switches doors and when they stick with their initial choice.

## Mathematical Description
### Generalized Problem:
1. There are \(n\) doors:
   - 1 door with a car (prize).
   - \(n-1\) doors with goats (non-prizes).

2. The contestant picks a door at random. The probability that the car is behind the chosen door is:
   $$\[
   P(\text{Car}) = \frac{1}{n}
   \]$$
   The probability that a goat is behind the chosen door is:
   $$\[
   P(\text{Goat}) = \frac{n-1}{n}
   \]$$

3. The host, who knows what is behind each door, opens \(k\) of the unchosen doors, revealing only goats.

4. The contestant then has the option to:
   - Stick with their initial choice.
   - Switch to one of the remaining unopened doors.

### Probabilistic Analysis:
- **Sticking with the initial choice**: The win rate the car by sticking with the initial choice remains:
   $$\[
   P(\text{Win if no switch}) = \frac{1}{n}
   \]$$
   This is because the contestant's initial guess has a 1 in \(n\) chance of being correct, regardless of any information revealed by the host. This probability does not change after the host opens the doors, as the initial choice remains the same.

- **Switching doors**: The win rate the car by switching involves conditional probability. When the host opens \(k\) doors to reveal goats, the probability mass of $$\( \frac{n-1}{n} \)$$ (initial probability that the car is behind any of the unchosen doors) gets redistributed among the remaining unopened doors.
  - If \(n = 3\) and \(k = 1\) (classic case):
    - Win rate if you switch = $$\( \frac{2}{3} \)$$.

### Formalized Probabilities:
1. **Win rate by not switching**:
   $$\[
   P(\text{Win if no switch}) = \frac{1}{n}
   \]$$

2. **Win rate by switching**:
   $$\[
   P(\text{Win if switch}) = \frac{n-1}{n} \times \frac{1}{n - k - 1}
   \]$$
   
This formula adjusts based on the number of doors \(n\), the number of doors opened \(k\), and whether the contestant chooses to switch.

## Python Simulation
This simulation allows customization of the number of doors and the number of doors the host opens. By running multiple iterations, it estimates the win rate by switching or not switching.

### Files Included
- `monty_hall_simulation.py`: Implements the simulation of the generalized Monty Hall problem, with options to switch doors or keep the initial choice.

### Results
The simulation output shows the number of wins, losses, and the respective probabilities of winning and losing for both strategies:

#### Case 1: Switching Doors
- **Wins**: 666,781 times
- **Losses**: 333,219 times
- **Win rate**: 66.67%
- **Loss rate**: 33.33%
#### Case 2: Not Switching Doors
- **Wins**: 333,054 times
- **Losses**: 666,946 times
- **Win rate**: 33.30%
- **Loss rate**: 66.70%

These results clearly show that switching doors increases the win rate, as predicted by the theoretical probabilities.

### Running the Simulation
To run the simulation, use Python as follows:
```bash
python monty_hall_simulation.py
```

## Conclusion
The Monty Hall problem, in its generalized form, continues to defy intuition. Regardless of the number of doors, the mathematical analysis and simulation consistently demonstrate that switching doors yields a higher win rate the prize, while sticking with the initial choice gives a lower probability of success, defined simply by $$\( \frac{1}{n} \)$$.

## Requirements
- Python 3.x
