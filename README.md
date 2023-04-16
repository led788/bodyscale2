
## XIAOMI Mi Body Composition Scale 2
Small Python script for getting weight and impedance from XIAOMI Mi Body Composition Scale 2 via BLE


### How to use:

```pip install -r requirements.txt```

modify address variable in main.py to your value 

```python main.py```


### Data format

| Byte | Description |
|------|-------------|
| 00   |             |
| 01   |             |
| 02   | Year        |
| 03   | Year        |
| 04   | Month       |
| 05   | Date        |
| 06   | Hour        |
| 07   | Minutes     |
| 08   | Seconds     |
| 09   | Impedance   |
| 10   | Impedance   |
| 11   | Weight      |
| 12   | Weight      |

Impedance and Weight in little-endian format\
Weight value = [byte_12 byte_11] / 200

additional information about this BLE service in specification \
`https://www.bluetooth.com/specifications/specs/body-composition-service-1-0/`

