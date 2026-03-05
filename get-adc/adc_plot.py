from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))

    plt.plot(time, voltage, 'b-', linewidth = 1.5, label='Измеренное напряжение')

    plt.title('Зависимость напряжения от времени', fontsize = 14, fontweight = 'bold')
    plt.xlabel('Время (с)', fontsize = 12)
    plt.ylabel('Напряжение (В)', fontsize = 12)

    plt.xlim(min(time), max(time))
    plt.ylim(0, max_voltage * 1.05)

    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.show()