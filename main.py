import machine
import utime
import hmc5883

led = machine.Pin(25,machine.Pin.OUT)
i2c_conn = machine.I2C(1,scl=machine.Pin(15),sda=machine.Pin(14))

devices = i2c_conn.scan()

if devices:
    for port in devices:
        print(hex(port))
        

dev = hmc5883.HMC5883L




