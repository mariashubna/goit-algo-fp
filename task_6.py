
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            chosen_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']
    
    return f'Обрані позиції: {chosen_items}, загальна калорійність: {total_calories}, вартість страв {total_cost} $ при нашому бюджеті {budget} $'


def dynamic_programming(items, budget):
    n = len(items)
    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'], reverse=True)

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if sorted_items[i - 1][1]['cost'] <= w:
                K[i][w] = max(sorted_items[i - 1][1]['calories'] + K[i - 1][w - sorted_items[i - 1][1]['cost']], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    
    selected_items = []
    total_cost = 0
    total_calories = 0


    i = n
    j = budget
    while i > 0 and j > 0:
        if K[i][j] != K[i - 1][j]:
            selected_items.append(sorted_items[i - 1][0])
            total_cost += sorted_items[i - 1][1]['cost']
            total_calories += sorted_items[i - 1][1]['calories']
            j -= sorted_items[i - 1][1]['cost']
            i -= 1
        else:
            i -= 1
    return f'Обрані позиції: {selected_items}, загальна калорійність: {total_calories}, вартість страв {total_cost} $ при нашому бюджеті {budget} $'




items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


budget = 102

print(greedy_algorithm(items, budget))
print(dynamic_programming(items, budget))



