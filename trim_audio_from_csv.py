import scipy.io.wavfile
import numpy

filename = "s2lam001_180707_2018-07-09_20-20.wav"
outputName = "output.wav"

fs1, y1 = scipy.io.wavfile.read(filename)
l1 = numpy.array([  [7.2,19.8] ])
l1 = numpy.ceil(l1*fs1)#get integer indices into the wav file - careful of end of array reading with a check for greater than y1.shape
newWavFileAsList = []
for elem in l1:
  startRead = elem[0]
  endRead = elem[1]
  if startRead >= y1.shape[0]:
    startRead = y1.shape[0]-1
  if endRead >= y1.shape[0]:
    endRead = y1.shape[0]-1
  newWavFileAsList.extend( y1[ int(startRead) : int(endRead) ] )

newWavFile = numpy.array(newWavFileAsList)

scipy.io.wavfile.write(outputName, fs1, newWavFile)
