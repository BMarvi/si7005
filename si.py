import smbus
import time

## Silicon LABS Si7005 ########################################################

class Si7005():

    """
    Silicon Labs Si7005
    DIGITAL i2c HUMIDITY AND TEMPERATURE SENSOR
    http://www.silabs.com/Support%20Documents/TechnicalDocs/Si7005.pdf
    by marvi@marvi.it
    """

    i2c_bus = -1
    address = 0x40

    A0 = -4.7844
    A1 =  0.4008
    A2 = -0.00393
    
    Q0 =  0.1973
    Q1 =  0.00237

    def __init__(self,bus_id=0):
        self.i2c_bus = smbus.SMBus(bus_id)

    def __sendcommand(self,value):
        self.i2c_bus.write_byte_data(self.address,0x03,value)

    def readdata(self,reg):
        return self.i2c_bus.read_byte_data(self.address,reg)

    def readTemperature(self):
        self.__sendcommand(0x11)
        while not self.__conversionReady():
            time.sleep(0.01)
        datah = self.readdata(0x01)
        datal = self.readdata(0x02)
        datat = (datah << 6) + (datal >>2)
        temp  = (datat/32.0) - 50
        self.temp = temp
        return self.temp

    def readHumidity(self):
        self.readTemperature()
        self.__sendcommand(0x01)
        while not self.__conversionReady():
            time.sleep(0.01)
        datah = self.readdata(0x01)
        datal = self.readdata(0x02)
        datat = (datah << 4) + (datal >> 4)
        self.notLinHum = (datat/16.0) - 24
        self.notComHum = self.notLinHum - (self.notLinHum**2 * self.A2 + self.notLinHum * self.A1 + self.A0)
        self.hum = self.notComHum + (self.temp - 30) * (self.notComHum * self.Q1 + self.Q0)
        return self.hum

    def readHumidityTemperature(self):
        self.readHumidity()
        return (self.hum, self.temp)

    def setHeater(self):
        pass

    def __conversionReady(self):
        status = self.readdata(0x00)
        return (( status & 1 ) == 0)

    def __str__(self):
        self.readHumidity()
        return 'Umidity: %.2f, Temperature: %.2f' % (self.hum, self.temp)

    getT  = readTemperature
    getH  = readHumidity
    getHT = readHumidityTemperature

