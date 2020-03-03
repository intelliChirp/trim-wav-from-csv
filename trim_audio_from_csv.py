# imports
import scipy.io.wavfile
import numpy

# set input, output
filename = "s2lam001_180707_2018-07-09_20-20.wav"
outputName = "output.wav"

# read audio file
fs1, y1 = scipy.io.wavfile.read(filename)

# get seconds to trim
sec_to_trim = numpy.array([7.2,19.8])
# get integer indices into the wav file - careful of end of array reading with a check for greater than y1.shape
sec_to_trim = numpy.ceil( sec_to_trim *fs1 )

# set start and end, if either is larger than the total file size, set to end of audio file
startRead = sec_to_trim[0]
endRead = sec_to_trim[1]
if startRead >= y1.shape[0] : startRead = y1.shape[0]-1
if endRead >= y1.shape[0]   :   endRead = y1.shape[0]-1

# write to output file
scipy.io.wavfile.write(outputName, fs1, y1[ int(startRead) : int(endRead) ])
