from ags10 import AGS10
import time

sensor = AGS10(busnum=6, address=0x1A, validate_crc=True)
version = sensor.version
print(f"version: {version}")
sensor.set_baseline_factorydefault()
time.sleep(1.5)

while True:
    if sensor.is_ready:
        voc = sensor.volatile_organic_compounds_ppb
        time.sleep(1.5)
        res = sensor.resistance_kohm
        print(f"VOC: {voc} ppb | Resistance: {res:.2f} kΩ")
        time.sleep(1.5)
    else:
        print("Sensor not ready...")
        time.sleep(1.5)
