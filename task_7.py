import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість продукту А
B = pulp.LpVariable('B', lowBound=0, upBound=10, cat='Integer')  # Кількість продукту Б

# Функція цілі (Максимізація прибутку)
model += 50 * A + 40 * B, "Profit"

# Додавання обмежень
model += 5 * A + 2 * B <= 80  # Обмеження для машини №1
model += 3 * A + 2 * B <= 40  # Обмеження для машини №2

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти продуктів А:", A.varValue)
print("Виробляти продуктів Б:", B.varValue)
