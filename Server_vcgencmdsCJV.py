import socket
import os
import json

s = socket.socket()
host = '0.0.0.0'  # Localhost
port = 5000
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    # Get core temperature
    temperature = os.popen('vcgencmd measure_temp').readline().strip()

    # Get CPU core speed
    cpu_speed = os.popen('vcgencmd measure_clock arm').readline().strip()

    # Get 3D block speed
    v3d_speed = os.popen('vcgencmd measure_clock v3d').readline().strip()

    # Get pixel values
    pixel_speed = os.popen('vcgencmd measure_clock pixel').readline().strip()

    pi_info = {
        "Temperature": temperature,
        "CPU core speed": cpu_speed,
        "3D block speed": v3d_speed,
        "Pixel values": pixel_speed
    }

    # Convert the dictionary to a JSON string
    json_string = json.dumps(pi_info)

    res = bytes(json_string, 'utf-8')  # needs to be a byte
    c.send(res)  # sends data as a byte type
    c.close()
