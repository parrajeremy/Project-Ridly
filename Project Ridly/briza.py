import mraa as m
import pca9557 as pca
import briza_eeprom as b_eeprom 
import hdc1000 as hdc
import LPS25H as lph
import data_calc as dc
import lmp91000 as lmp
import ads1220 as ads
import populate_sensor_data as sd
import EEPROM as eeprom
import sensor_init as s
import time as t
import Board as board

#initilization of the eeprom is done usinf file briza_eerpom.py
board_addr = [b_eeprom.board1,b_eeprom.board2,b_eeprom.board3,b_eeprom.board4]
#print board_addr

#sen1 ='1' 
#sen2 ='2'


board.board_init(board_addr[0])
board.board_init(board_addr[1])
board.board_init(board_addr[2])
board.board_init(board_addr[3])

#configuring other sensors on the board like : humidity, tem, pressure
lph.configure()
def other_sensor():
    humidity = hdc.readHDC_humidity()
    temperature = hdc.readHDC_temp()
    pressure = lph.getPressure()

#configuring the on board sensor configuration
def sensor1(s1):
    pca.pca_config(1,0,0)
    s.init(s1)
    lmp.lmp_init()
    ads.spi_init()
    pca.pca_config(1,1,1) 


def conf_sensor1():
#    print("sensor 1:")
    pca.pca_config(1,0,0)
    dc.s1_avg_data()
    sensor1Data = ads.get_readData()
    s1_avg = dc.get_s1Avg()
    pca.pca_config(1,1,1)

def sensor2(s2):
    pca.pca_config(0,1,0)
    s.init(s2)
    lmp.lmp_init()
    ads.spi_init()
    pca.pca_config(1,1,1)

def conf_sensor2():
#    print("sensor 2:")
    pca.pca_config(0,1,0)
    dc.s2_avg_data()
    sensor2Data = ads.get_readData()
    s2_avg = dc.get_s2Avg()
    pca.pca_config(1,1,1)

def load_board(boardAdr):
	board.call_pca(boardAdr)
        t.sleep(0.4)
        ts = t.time()
        t.sleep(0.4)
        print ts,
        t.sleep(0.4)
        ads.get_ads_config0(0x70)
        t.sleep(0.4)
        #print "sensor 1"
        conf_sensor1()
        t.sleep(0.4)
        ads.get_ads_config0(0x60)
        t.sleep(0.4)
        #print "sensor2"
        conf_sensor2()
        t.sleep(0.4)
        t.sleep(0.39)
 


while 1==1:
#     other_sensor()
#    t.sleep(0.1)
     print "\n Board 1"
     load_board(board_addr[0])
     print "\n Board 2"
     load_board(board_addr[1])
     print "\n Board 3"
     load_board(board_addr[2])
     print "\n Board 4"
     load_board(board_addr[3])