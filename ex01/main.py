import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a, b = 0, 2

def monte_carlo_integration(f, a, b, n=100000):
    x_random = np.random.uniform(a, b, n)
    y_random = np.random.uniform(0, f(b), n)

    under_curve = y_random <= f(x_random)

    area = (b - a) * f(b) * np.sum(under_curve) / n
    
    return area, x_random, y_random, under_curve

mc_result, x_rand, y_rand, under = monte_carlo_integration(f, a, b, 100000)
analytical_result = (b**3 - a**3) / 3
quad_result, quad_error = spi.quad(f, a, b)

print(f"{'Метод':<20} {'Результат':<15} {'Похибка'}")
print("-" * 50)
print(f"{'Монте-Карло':<20} {mc_result:<15.10f} {abs(mc_result - analytical_result):.10f}")
print(f"{'Аналітичний':<20} {analytical_result:<15.10f} -")
print(f"{'quad (SciPy)':<20} {quad_result:<15.10f} {quad_error:.2e}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

x = np.linspace(-0.5, 2.5, 400)
ax1.plot(x, f(x), 'r', linewidth=2, label='f(x) = x²')
ix = np.linspace(a, b, 100)
ax1.fill_between(ix, f(ix), color='gray', alpha=0.3, label='Площа')
ax1.axvline(a, color='gray', linestyle='--', alpha=0.5)
ax1.axvline(b, color='gray', linestyle='--', alpha=0.5)
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_title('Інтегрування f(x) = x²')
ax1.legend()
ax1.grid(alpha=0.3)

ax2.scatter(x_rand[under], y_rand[under], s=1, c='green', alpha=0.3, label='Під кривою')
ax2.scatter(x_rand[~under], y_rand[~under], s=1, c='red', alpha=0.3, label='Над кривою')
ax2.plot(ix, f(ix), 'b', linewidth=2)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title(f'Метод Монте-Карло ({len(x_rand)} точок)')
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()

print(f"\n{'='*50}")
print("ВИСНОВОК:")
print(f"{'='*50}")
print(f"Різниця Монте-Карло vs Аналітичний: {abs(mc_result - analytical_result):.10f}")
print(f"Точність: {(1 - abs(mc_result - analytical_result)/analytical_result)*100:.4f}%")