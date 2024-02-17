# Fan Speed Controller

This Python script allows you to control the speed of a fan connected to a GPIO pin on a 5v PWM capable board such as a Raspberry Pi or BeagleBone Black.

## Dependencies

This script requires the Adafruit_BBIO library for Python. You can install it using pip:

```bash
pip install Adafruit_BBIO
```
## Usage
The script uses the following parameters:

`fan_pin`: The GPIO pin the fan is connected to. In this script, it’s set to “P9_41”.
`frequency`: The frequency of the PWM signal (in Hz). In this script, it’s set to 1000.
`initial_duty_cycle`: The initial duty cycle of the PWM signal (as a percentage). In this script, it’s set to 100.
To use the script, simply run it with Python:

```bash
python fan_speed_controller.py
```

## Command Line Usage

You can control the fan speed directly from the command line by providing the desired speed as a command line argument when running the script. The speed should be a percentage of the maximum speed (0-100). Here's an example:

```bash
python fan_speed_controller.py 75
```

This will set the fan speed to 75% of the maximum speed. If no argument is provided, the script will print a message asking for a speed.

## Setting Pin Mode to PWM
Before running the script, make sure the GPIO pin is set to PWM mode. You can find more information on how to do this in the BeagleBone Black System Reference Manual or the Raspberry Pi GPIO documentation.

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for the full license text.
