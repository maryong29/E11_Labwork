import adafruit_bme680
import time
import board

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25
start_time = time.time()

while True:
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.relative_humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)
    data = [time.time(), bme680.temperature]
    print(data)
    time.sleep(1)
while i < 2:
    print(i)
    i += 1
else: 
    print('Finish')
