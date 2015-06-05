import mraa as m
#import lmp91000 as lmp
#import pca9557 as pca
#import ads1220 as ads
import populate_sensor_data as sd


board1 = 0x53
board2 = 0x55
board3 = 0x56
board4 = 0x57


sd.board1DataInit(board1)
sd.board2DataInit(board2)
sd.board3DataInit(board3)
sd.board4DataInit(board4)


#eeprom has been written, to chnage the eeprom values,
#first plug the board1, board2, board3 on to the edison,
#run i2cdetect -y -r 1 
#check the address and fill in the corresponding addresses in the file.
#and, run this file only once. using command python briza_eeprom.py


