import time 
import adc_plot as plot
import r2r_adc as adc

dac_range = 3.183

adc_device = adc.R2R_ADC(dynamic_range = dac_range, compare_time = 0.0001, verbose = False)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while (time.time() - start_time) < duration:
        current_time = time.time() - start_time

        voltage = adc_device.get_sc_voltage()

        voltage_values.append(voltage)
        time_values.append(current_time)

        print(f"t = {current_time:.2f} с, U = {voltage:.3f} В")

        time.sleep(0.05)

    if voltage_values and time_values:
        plot.plot_voltage_vs_time(time_values, voltage_values, max_voltage=dac_range)

    if len(time_values) > 1:
        plot.plot_sampling_period_hist(time_values)
        
finally:
    adc_device.deinit()
