import scipy.io.wavfile
fs1, y1 = scipy.io.wavfile.read(filename)
l1 = numpy.array([  [7.2,19.8], [35.3,67.23], [103,110 ] ])
l1 = ceil(l1*fs1)#get integer indices into the wav file - careful of end of array reading with a check for greater than y1.shape
newWavFileAsList = []
for elem in l1:
  startRead = elem[0]
  endRead = elem[1]
  if startRead >= y1.shape[0]:
    startRead = y1.shape[0]-1
  if endRead >= y1.shape[0]:
    endRead = y1.shape[0]-1
  newWavFileAsList.extend(y1[startRead:endRead])


newWavFile = numpy.array(newWavFileAsList)

scipy.io.wavfile.write(outputName, fs1, newWavFile)
