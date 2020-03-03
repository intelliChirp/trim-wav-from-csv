# imports
import scipy.io.wavfile
import numpy

# set input, output
filename = "s2lam001_180707_2018-07-09_20-20.wav"
#outputName = "./output/output.wav"

def trim_and_write( input_file, output_path, start_trim, end_trim, annotation ) :
    # read audio filE
    fs1, y1 = scipy.io.wavfile.read(filename)

    # get seconds to trim
    sec_to_trim = numpy.array( [ start_trim, end_trim ] )
    # get integer indices into the wav file - careful of end of array reading with a check for greater than y1.shape
    sec_to_trim = numpy.ceil( sec_to_trim *fs1 )

    # set start and end, if either is larger than the total file size, set to end of audio file
    start_read = sec_to_trim[0]
    end_read = sec_to_trim[1]
    if start_read >= y1.shape[0] : start_read = y1.shape[0]-1
    if end_read >= y1.shape[0]   :   end_read = y1.shape[0]-1

    output_name = output_path + input_file[:-4] + "_" + annotation + ".wav"
    print(output_name)

    # write to output file
    scipy.io.wavfile.write( output_name, fs1, y1[ int( start_read ) : int( end_read ) ])

trim_and_write( filename, "./output/", 10.2, 20.645, "BBI" )