from matplotlib import pyplot as plt
import numpy as np

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))

    plt.plot(time, voltage, 'b-', linewidth = 1.5, label='Измеренное напряжение')

    plt.title('Зависимость напряжения от времени', fontsize = 14, fontweight = 'bold')
    plt.xlabel('Время (с)', fontsize = 12)
    plt.ylabel('Напряжение (В)', fontsize = 12)

    plt.xlim(min(time), max(time))
    plt.ylim(0, max_voltage * 1.05)

    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.show(block=False)

def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(1, len(time)):
        period = time[i] - time[i-1]
        sampling_periods.append(period)

    plt.figure(figsize=(10,6))

    plt.hist(sampling_periods, bins = 30, edgecolor = 'black', alpha = 0.7, color = 'green')

    plt.title('Распределение периодов дискретизации', fontsize = 14, fontweight = 'bold')
    plt.xlabel('Период измерения (с)', fontsize = 12)
    plt.ylabel('Количество измерений', fontsize = 12)

    plt.xlim(0, 0.06)

    plt.grid(True, linestyle = '--', alpha = 0.7)

    if sampling_periods:
        mean_period = np.mean(sampling_periods)
        std_period = np.std(sampling_periods)
        min_period = np.min(sampling_periods)
        max_period = np.max(sampling_periods)

    plt.axvline(mean_period, color = 'red', linestyle = '--', linewidth = 2, label = f'Среднее: {mean_period:.4f} с')
    plt.legend()

    print(f"\nСтатистика периодов дискретизации:")
    print(f"Среднее значение: {mean_period:.6f} с")
    print(f"Стандартное отклонение: {std_period:.6f} с")
    print(f"Минимальное значение: {min_period:.6f} с")
    print(f"Максимальное значение {max_period:.6f} с")

    plt.tight_layout()
    plt.show() 

