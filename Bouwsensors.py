import glob
import time

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir+'28*')[0]
device_file = device_folder + 'w1_slave'

def lees_temp_ruw ():
    f = open(device_folder, 'r')
    lijnen = f.readlines()
    f.close()
    return lijnen

def lees_temp ():
    lijnen = lees_temp_ruw()

    while lijnen[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lijnen = lees_temp_ruw()

    gelijk_pos = lijnen[1].find('t=')

    if gelijk_pos != -1:
        temp_string = lijnen[1][gelijk_pos+2:]
        temp = float(temp_string) / 1000
        return temp

while True:
    LOL = lees_temp()
    print(LOL)
    time.sleep(1)