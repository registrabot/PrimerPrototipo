import RPi.GPIO as GPIO
from keypad_module.keypad_class import KeypadController
from buzzer_module.buzzer_class import BuzzerController

def main():

    buzzer_controller = BuzzerController()
    keypad_controller = KeypadController()
    price_value_str = ""

    while(True):
        try:
            price, price_value_str = keypad_controller.enter_price(price_value_str)
            print('Precio:', price)
            buzzer_controller.finish_sound()
        except KeyboardInterrupt:
            print("\nSaliendo del programa...")
            GPIO.cleanup()
            break

if __name__ == '__main__':     #Program start from here
    print ("Program is starting ... ")
    main()

