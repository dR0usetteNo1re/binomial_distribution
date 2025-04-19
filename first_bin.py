from datetime import datetime

start_time = datetime.now()

# Imports
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

# ANSI - for console colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"  # Сброс цвета

# Для примера можно ввести n = 10; p = 0.5
x = np.linspace(-1, 10, 100)
n, p = int(input("Введите кол-во испытаний n = ")), float(
    input("Введите вероятность успеха p = "))  # n - Кол-во испытаний; p - Вероятность успеха

# График значения дискретной плотности в точке x (Probability Density Function)
pdf = binom.pmf(x, n, p)

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(15, 9))
ax[0].bar(x, pdf, color='red')
ax[0].set_title("График значения дискретной плотности")

# График функции распределения (Cumulative Distribution Function)
cdf = binom.cdf(x, n, p)

ax[1].plot(x, cdf)
ax[1].scatter([1], [binom.cdf(1, n, p)], color='red') # Красная точка показывает F(1)
ax[1].set_title("Кумулятивная функция распределения")

plt.show()


sample = binom(n, p).rvs(size=200)
print(
    f"\nПервые 10 значений случайной выборки = {sample[:10]},"
    f" \nКвадратичное отклонение = {np.sqrt(sample.var())}\n"
    f"Математическое ожидание = {binom(n, p).expect()}"
    f"\nДисперсия = {sample.var()}"
)

print(
    f"Дискретная плотность = {[float(i) for i in binom(n, p).pmf([-1, 0, 5, 5.5, 10])]}"
    f" \nФункция распределения = {[float(i) for i in binom(n, p).cdf([-1, 0, 5, 5.5, 10])]}"
)

print('Квантили:', [float(i) for i in binom(n, p).ppf([0.05, 0.1, 0.5, 0.9, 0.95])] )

for k in range(0, n + 1):
    print(f"\nВероятность пройти {CYAN}{k}{RESET} собеседований из {YELLOW}{n}{RESET} = {GREEN}{float(binom.pmf(k, n, p))}{RESET}")
print(f"\nВероятность пройти хотя бы {CYAN}одно{RESET} собеседование = {GREEN}{float(1 - binom.cdf(0, n, p))}{RESET}")



end_time = datetime.now()
execution_time = end_time - start_time

print(f"Время выполнения программы = {execution_time}")
