#python esptool.py --port COM4 erase_flash
python esptool.py --port COM4 --baud 460800 write_flash --flash_size=detect 0 esp8266-20190125-v1.10.bin