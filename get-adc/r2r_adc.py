import RPi.GPIO as GPIO
import time 

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.setup(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def number_to_dac(self, number):
        max_value = (1 << len(self.bits_gpio)) - 1

        for i in range(len(self.bits_gpio)):
            bit = (number >> i) & 1
            GPIO.output(self.bits_gpio[i], bit)

    def sequential_counting_adc(self):
        max_value = (1 << len(self.bits_gpio)) - 1

        for dac_value in range(max_value + 1):
            self.number_to_dac(dac_value)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 1:
                return dac_value

        return max_value

    def get_sc_voltage(self):
        digital_value = self.sequential_counting_adc()

        bit_count = len(self.bits_gpio)
        max_digital = (1 << len(self.bits_gpio)) - 1

        voltage = (digital_value / max_digital) * self.dynamic_range

        return voltage

    def successive_approximation_adc(self):
        low = 0
        high = 2**(len(self.bits_gpio)) - 1


        for _ in range(len(self.bits_gpio)):
            mid = (low+high) // 2

            self.number_to_dac(mid)

            time.sleep(0.001)

            comp_output = GPIO.input(self.comp_gpio)

            if comp_output == 1:
                low = mid + 1
            else:
                high = mid - 1

        return (low + high) // 2

    def get_sar_voltage(self):
        digital_value = self.successive_approximation_adc()

        voltage = (digital_value / (2**(len(self.bits_gpio)) - 1)) * self.dynamic_range
        return voltage 
    

if __name__ == "__main__":
    try:
        dac_range = 3.183
        adc = R2R_ADC(dynamic_range=dac_range, verbose=False) 

        while True:
            voltage = adc.get_sar_voltage()
            print(f"Измеренное напряжение: {voltage:.3f} В")
            time.sleep(0.5)

##        while True:
##           voltage = adc.get_sc_voltage()           
##           print(f"Напряжение: {voltage:.3f} В")
##           time.sleep(0.5) 

    finally:
        adc.deinit()
