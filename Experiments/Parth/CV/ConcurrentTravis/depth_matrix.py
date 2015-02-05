from PIL import Image
from numpy import *
import math
from multiprocessing import Process, Queue

def retrieveRow(inputFile, rowToCheck, outputRow):
	# Open the images
	inputArray = array(Image.open(inputFile),'f');
	row = empty([1, inputArray.shape[1], inputArray.shape[2]])
	for i in range (0, inputArray.shape[1]):
	        for j in range (0, inputArray.shape[2]):
			row[0][i][j] = inputArray[rowToCheck][i][j]
	outputRow.put(row)

def save(leftRow, rightRow, leftStartingPoint, leftEndPoint, rightStartingPoint, rightEndPoint, outputArray, returnValue):
	# Calculate the values of the disparity matrix
	for i in range(leftStartingPoint, leftEndPoint):
		for j in range(rightStartingPoint, rightEndPoint):
			outputArray[i][j] = math.sqrt((leftRow[0][i][0]-rightRow[0][j][0])**2+(leftRow[0][i][1]-rightRow[0][j][1])**2+(leftRow[0][i][2]-rightRow[0][j][2])**2)
	print '[',leftStartingPoint,'-',leftEndPoint,'],[',rightStartingPoint,'-',rightEndPoint,']', outputArray
	returnValue.put(outputArray)

if __name__ == '__main__':
	right_result_queue = Queue()
	left_result_queue = Queue()
	rightProcess = Process(target=retrieveRow, args=('right2.png', 256, right_result_queue))
	leftProcess = Process(target=retrieveRow, args=('left2.png', 256, left_result_queue))

	rightProcess.start()
	leftProcess.start()
	rightProcess.join()
	leftProcess.join()

	save1 = Queue()
	save2 = Queue()
	save3 = Queue()
	save4 = Queue()

	leftStrip = left_result_queue.get()
	rightStrip = right_result_queue.get()

	leftSize = leftStrip.shape[1]
	rightSize = leftStrip.shape[1]

	m = zeros([leftSize, rightSize])

	proc1 = Process(target=save, args=(leftStrip, rightStrip, 0, leftSize/2, 0, rightSize/2, m, save1))
	proc2 = Process(target=save, args=(leftStrip, rightStrip, (leftSize/2)+1, leftSize, 0, rightSize/2, m, save2))
	proc3 = Process(target=save, args=(leftStrip, rightStrip, 0, leftSize/2, (rightSize/2)+1, rightSize, m, save3))
	proc4 = Process(target=save, args=(leftStrip, rightStrip, (leftSize/2)+1,leftSize,(rightSize/2)+1, rightSize, m, save4))
	
	proc1.start()
	proc2.start()
	proc3.start()
	proc4.start()

	m1 = save1.get()
	m2 = save2.get()
	m3 = save3.get()
	m4 = save4.get()
		
	m[0:leftSize/2][0:rightSize/2] = m1[0:leftSize/2][0:rightSize/2] 
	m[(leftSize/2)+1:leftSize][0:rightSize/2] = m2[(leftSize/2)+1:leftSize][0:rightSize/2]
	m[0:leftSize/2][(rightSize/2)+1:rightSize] = m3[0:leftSize/2][(rightSize/2)+1:rightSize]
	m[(leftSize/2)+1:leftSize][(rightSize/2)+1:rightSize] = m4[(leftSize/2)+1:leftSize][(rightSize/2)+1:rightSize]

	out = Image.fromarray(uint8(m))
	out.save('matrix3.png')
