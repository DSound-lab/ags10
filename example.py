from ags10 import AGS10
import time

sensor = AGS10(busnum=6, address=0x1A, validate_crc=True)

while True:
    if sensor.is_ready:
        voc = sensor.volatile_organic_compounds_ppb
        res = sensor.resistance_kohm
        print(f"VOC: {voc} ppb | Resistance: {res:.2f} kΩ")
    else:
        print("Sensor not ready...")
    time.sleep(1)
