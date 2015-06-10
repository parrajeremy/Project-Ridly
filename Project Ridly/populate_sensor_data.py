import EEPROM as e
#import pca9557 as pca

sensor1board1 = "TR,2,-37.38"
sensor1board1raw = "100901-TOR-1501/ 2/-37.38"

sensor2board1 = "TX,95,11.93"
sensor2board1raw ="100801-TOX-1501/ 95/11.93"

sensor1board2 = "H2S,425,162.58"
sensor1board2raw = "100302-H2S-150/ 425/162.58"

sensor2board2 = "SO2,99,32.9"
sensor2board2raw = "100601-SO2-150/ 99/32.9"

sensor1board3 = "O3,111,-20.74"
sensor1board3raw = "100401-O3-1501/ 111/-20.74"

sensor2board3 = "NO2,26,-49.04"
sensor2board3raw = "100501-NO2-1411/ 26/-49.04"

sensor1board4 = "CO,33,9.89"
sensor1board4raw = "100106-CO-1410/ 33/9.89"

sensor2board4 = "TX,120,13.13"
sensor2board4raw = "100801-TOX-1501/ 120/13.13"

def board1DataInit(board1):
	e.init_EEPROM(board1)
	e.writeSensorQRData(1,sensor1board1,sensor1board1raw)
	e.writeSensorQRData(2,sensor2board1,sensor2board1raw)
#    pca.pca_init(board1 <<3)

def board2DataInit(board2):
	e.init_EEPROM(board2)
	e.writeSensorQRData(1,sensor1board2,sensor1board2raw)
	e.writeSensorQRData(2,sensor2board2,sensor2board2raw)
#   pca.pca_init(board2<<3)

def board3DataInit(board3):
	e.init_EEPROM(board3)
	e.writeSensorQRData(1,sensor1board3,sensor1board3raw)
	e.writeSensorQRData(2,sensor2board3,sensor2board3raw)
#    pca.pca_init(board3<<3)


def board4DataInit(board4):
	e.init_EEPROM(board4)
	e.writeSensorQRData(1,sensor1board4,sensor1board4raw)
	e.writeSensorQRData(2,sensor2board4,sensor2board4raw)
#    pca.pca_init(board4<<3)
