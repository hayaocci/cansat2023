# uart_test.py

import pigpio
import time

pi = pigpio.pi()

if not pi.connected:
   exit()

uart0 = pi.serial_open("/dev/ttyS0", 9600, 0)

# pi.serial_write(uart0, "Hello ! Serial !")

while True:
    time.sleep(1)
    rdy = pi.serial_data_available(uart0)
    if rdy > 0:
        (b, d) = pi.serial_read(uart0, rdy)
        print(d)

pi.serial_close(uart0)
