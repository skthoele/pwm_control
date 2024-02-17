import sys
import Adafruit_BBIO.PWM as PWM

# The GPIO pin the fan is connected to
fan_pin = "P9_41"

# The frequency of the PWM signal (in Hz)
frequency = 1000

# The initial duty cycle of the PWM signal (as a percentage)
initial_duty_cycle = 100

# Start the PWM signal
PWM.start(fan_pin, initial_duty_cycle, frequency)

def set_fan_speed(speed):
    """
    Set the speed of the fan.

    :param speed: The desired speed as a percentage of the maximum
    speed (0-100).
    """
    # Check if the speed is within the valid range
    if 0 <= speed <= 100:
        PWM.set_duty_cycle(fan_pin, speed)
    else:
        print("Error: Speed must be a value between 0 and 100")

# Get the speed from the command line arguments
if len(sys.argv) > 1:
    speed = int(sys.argv[1])
    set_fan_speed(speed)
else:
    print("Please provide a speed as a command line argument.")
