# ags10
AGS10 — TVOC Sensor library for python


## 📦 Overview
This Python module provides a clean, Linux-compatible driver for the **AGS10 volatile organic compound (VOC) sensor**. It was originally ported from the MicroPython implementation by Gavesha Labs, and uses **smbus2** for I²C communication. It was tested to run on **Raspberry Pi 3/4** under **Raspbian Bullseye/Bookworm** with Python 3.

---

## 🧩 Features
- Full AGS10 sensor support (VOC concentration + sensor resistance)
- CRC-8 validation (optional)
- Baseline calibration write support
- Tested on Raspberry Pi 3 Model B


## 🛠️ Installation
```
git clone https://github.com/yourusername/AGS10_RPi.git
cd AGS10_RPi
pip install .
```
Or install directly from source:
```
python setup.py install
```

## 🧪 Example Usage
```
from ags10_rpi import AGS10
import time

sensor = AGS10(busnum=1, address=0x1A, validate_crc=True)

while True:
    if sensor.is_ready:
        voc = sensor.volatile_organic_compounds_ppb
        res = sensor.resistance_kohm
        print(f"VOC: {voc} ppb | Resistance: {res:.2f} kO")
    else:
        print("Sensor not ready...")
    time.sleep(1)

```

## 🧾 License
MIT License
Original MicroPython version © 2023 Gavesha Labs
Ported to Python (Raspbian) 2026 by DSound-labs
