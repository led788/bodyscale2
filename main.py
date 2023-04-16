import asyncio
import binascii

from bleak import BleakScanner

address = "D0:3E:7D:48:C9:52"


async def main(address: str):
    stop_event = asyncio.Event()

    def callback(device, advertising_data):
        if device.address.lower() == address.lower():
            data = binascii.b2a_hex(advertising_data.service_data['0000181b-0000-1000-8000-00805f9b34fb']).decode(
                'ascii')
            byte12 = data[-2:]  # weight
            byte11 = data[-4:-2]  # weight
            weight = round((int(byte12 + byte11, 16)) / 200, 2)
            print(f"{weight=} kg", end="\t")
            byte09 = data[-6:-4]  # impedance
            byte10 = data[-8:-6]  # impedance
            impedance = int(byte09 + byte10, 16)
            print(f"{impedance=}")

    async with BleakScanner(callback) as scanner:
        await stop_event.wait()


asyncio.run(main(address))
