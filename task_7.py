import random
import matplotlib.pyplot as plt

def play_result(value):
    result = {i: 0 for i in range(2, 13)}
    
    for _ in range(value):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        sum = first + second        
        result[sum] += 1
    
    probabilities = {s: (count / value) * 100 for s, count in result.items()}    
    return probabilities

def plot_results(simulated_probabilities, theoretical_probabilities, value):
    sums = list(simulated_probabilities.keys())
    simulated_probs = [simulated_probabilities[sum_dice] for sum_dice in sums]
    theoretical_probs = [theoretical_probabilities[sum_dice] for sum_dice in sums]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sums, simulated_probs, label='Simulated Probabilities', marker='o')
    plt.plot(sums, theoretical_probs, label='Theoretical Probabilities', marker='x')
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability (%)')
    plt.title(f'Simulated vs Theoretical Probabilities of Dice Sums (number of dice tosses {value})')
    plt.legend()
    plt.grid(True)
    plt.show()


theoretical_probabilities = {
    2: 1/36 * 100,
    3: 2/36 * 100,
    4: 3/36 * 100,
    5: 4/36 * 100,
    6: 5/36 * 100,
    7: 6/36 * 100,
    8: 5/36 * 100,
    9: 4/36 * 100,
    10: 3/36 * 100,
    11: 2/36 * 100,
    12: 1/36 * 100
}

experement_play = [100, 1000, 100000, 500000]
for exp in experement_play:
    simulated_probabilities = play_result(exp)
    plot_results(simulated_probabilities, theoretical_probabilities, exp)