import RPi.GPIO as GPIO
from weightsensor_module.weightsensor_conf import *
import time

weight_sensor = WeightSensor()

try:
    while True:
        peso = weight_sensor.get_weight(0.5)
        print(f"Peso: {peso} kg")
        time.sleep(1)

except KeyboardInterrupt:
    # Limpiar los pines GPIO al salir
    weight_sensor.clean_and_exit()