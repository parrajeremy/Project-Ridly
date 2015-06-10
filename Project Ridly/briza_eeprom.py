import mraa as m
import populate_sensor_data as sd
import sys

print 'Address of the boards :', len(sys.argv)-1, 'boards.'
#print 'Address list:', str(sys.argv)

def convert_hex(boardNo):
	board = int(boardNo, 16)
	return board


b1 = sys.argv[1]
board1 = convert_hex(b1)

b2 = sys.argv[2]
board2 = convert_hex(b2)

b3 = sys.argv[3]
board3 = convert_hex(b3)

b4 = sys.argv[4]
board4 = convert_hex(b4)


sd.board1DataInit(board1)
sd.board2DataInit(board2)
sd.board3DataInit(board3)
sd.board4DataInit(board4)

#print board1
#print board2
#print board3
#print board4
