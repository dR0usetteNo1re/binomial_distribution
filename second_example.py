import numpy as np  
from scipy.stats import binom  
import matplotlib.pyplot as plt  
  
x = np.linspace(-1, 10, 100)  
n, p = 20, 0.05  # n - Кол-во испытаний; p - Вероятность успеха  
  
# График значения дискретной плотности в точке x (Probability Density Function)  
pdf = binom.pmf(x, n, p)  
  
plt.title(f"Кол-во испытаний = {n}, Вероятность успеха = {p}")  
plt.title(f"График значения дискретной плотности")  
plt.bar(x, pdf, color='green')  
plt.show()  
  
# График функции распределения (Cumulative Distribution Function)  
cdf = binom.cdf(x, n, p)  
  
plt.title(f"Кумулятивная функция распределения")  
plt.plot(x, cdf)  
  
## Красная точка показывает F(1)  
plt.scatter([1], [binom.cdf(1, n, p)], color="red");  
  
sample = binom(n, p).rvs(size=200)  
print(  
    f"\nПервые 10 значений случайной выборки = {sample[:10]}\nКвадратичное отклонение = {np.sqrt(sample.var())}\nМатематическое ожидание = {binom(n, p).expect()}\nДисперсия = {sample.var()}")  
print(  
    f"Дискретная плотность = {binom(n, p).pmf([-1, 0, 5, 5.5, 10])}\nФункция распределения = {binom(n, p).cdf([-1, 0, 5, 5.5, 10])}")  
print('Квантили:', binom(n, p).ppf([0.05, 0.1, 0.5, 0.9, 0.95]))  
  
print("Проверяем 20 изделий на предмет дефектов и хотим узнать вероятность того, что ровно 2 из них окажутся дефектными.")  
  
for k in range(0, n + 1): print(f"\nШанс того, что {k} изделий из {n} - бракованные = {binom.pmf(k, n, p)}")  
print(f"\nВероятность того, что ровно 2 изделия - брак = {2 - binom.cdf(0, n, p)}")  
plt.show()
