import machine
import utime
import hmc5883

led = machine.Pin(25,machine.Pin.OUT)
#i2c_conn = machine.I2C(id=1,scl=machine.Pin(15),sda=machine.Pin(14))

#devices = i2c_conn.scan()

#if devices:
#    for port in devices:
#        print(hex(port))
        

dev = hmc5883.I2C_DRIVER()

while True:
    dev.calculatetoprinthumanreadable()
    utime.sleep(0.5)





