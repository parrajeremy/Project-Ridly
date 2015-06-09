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

#initilization of the eeprom is done usinf file briza_eerpom.py
board_addr = [b_eeprom.board1,b_eeprom.board2,b_eeprom.board3,b_eeprom.board4]
#print board_addr

sen1 ='1' 
sen2 ='2'
s1 = ''
s2 = ''
def reading_eeprom(boardAdr):
       global sen1, sen2
       eeprom.init_EEPROM(boardAdr)

#reading the data from eeprom sensor 1
       se1 = eeprom.readSensorQRData(1)
       sen1 = eeprom.data[7:10]

#reading the data from eeprom for sensor2
       se2 = eeprom.readSensorQRData(2)
       sen2 = eeprom.data[7:10]

#reading_eeprom(board_addr[0])

#print sen1
#print sen2


#PCA initilization.

def call_pca(boardAdr):
    if boardAdr == board_addr[0]:
        pca.pca_init(0x1B)
        print "ON PCA : 0x1B"
    elif boardAdr == board_addr[1]:
        pca.pca_init(0x1D)
        print "ON PCA : 0x1D"
    elif boardAdr == board_addr[2]:
        pca.pca_init(0x1E)
        print "ON PCA : 0x1E"
    elif boardAdr == board_addr[3]:
        pca.pca_init(0x1F)
        print "ON PCA : 0x1F"
    else:
        print("please initialize the board in populate_sensor_board.py")


#configuring other sensors on the board like : humidity, tem, pressure
lph.configure()
def other_sensor():
    humidity = hdc.readHDC_humidity()
    temperature = hdc.readHDC_temp()
    pressure = lph.getPressure()

#configuring the on board sensor configuration
def sensor1():
    s.init(s1)
    pca.pca_config(1,0,0)
    lmp.lmp_init()
    ads.spi_init()    
    #print("SENSOR1 : %s", s1)

def sensor1_conf():
    dc.s1_avg_data()
    sensor1Data = ads.get_readData()
    s1_avg = dc.get_s1Avg()

def sensor2():
    s.init(s2)
    pca.pca_config(0,1,0)
    #print("SENSOR2  : %s", s2)
    lmp.lmp_init()
    ads.spi_init()

def sensor2_conf():
    dc.s2_avg_data()
    sensor2Data = ads.get_readData()
    s2_avg = dc.get_s2Avg()


   

#for driving one board configuration at a time
def load_board():
    
    for i in range (0,4):
        addr = board_addr[i]
        reading_eeprom(addr)
        t.sleep(1)
        global s1,s2
        s1 = str(sen1)
        s2 = str(sen2)
        #ts is the time stamp in seconds for each sensor value.
        ts = time.time()
        print ts
        print "\n\n SENSOR 1 is : "
        print s1
        print "\n\n SENSOR 2 is :"
        print s2
        call_pca(addr)
        sensor1()
        sensor1_conf()
        t.sleep(1)
        sensor2()
        sensor2_conf()
        t.sleep(1)


while 1==1:
    #other_sensor()
    t.sleep(0.1)
    load_board()
