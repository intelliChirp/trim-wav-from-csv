# imports
import scipy.io.wavfile
import numpy
import csv
import os,binascii
import soundfile as sf
import shutil

# set input, output
#filename = "s2lam001_180604_2018-06-09_08-00.wav"
#outputName = "./output/output.wav"

def trim_and_write( input_file, input_path, output_path, start_trim, end_trim, annotation ) :
    print("[WORKING] Attempting to trim audio file and write to directory")
    # read audio filE
    y1, fs1 = sf.read(input_path)

    # get seconds to trim
    #print(start_trim)
    #print(end_trim)
    sec_to_trim = numpy.array( [ float(start_trim), float(end_trim) ] )
    # get integer indices into the wav file - careful of end of array reading with a check for greater than y1.shape
    sec_to_trim = numpy.ceil( sec_to_trim *fs1 )

    # set start and end, if either is larger than the total file size, set to end of audio file
    start_read = sec_to_trim[0]
    end_read = sec_to_trim[1]
    if start_read >= y1.shape[0] : start_read = y1.shape[0]-1
    if end_read >= y1.shape[0]   :   end_read = y1.shape[0]-1

    # create output file name
    random_hex = binascii.b2a_hex(os.urandom(5))
    output_name = output_path + "\\" + input_file[:-4] + "_" + str(random_hex) + "_" + annotation + ".wav"

    # write to output file
    scipy.io.wavfile.write( output_name, fs1, y1[ int( start_read ) : int( end_read ) ])
    print("[SUCESS] Wrote new audio file to", output_name)

def create_folders() :
    csv_file = os.path.join( ".\data_collection.csv")
    # location of files
    existing_path_prefix = "E:\\recordings"

    # creates new folder in for location of resulting folders w/ files and sets path
    try:
        os.mkdir(os.path.join(existing_path_prefix, "audio_folders"))
    except OSError as error:  # if file already exists
        print(error)
    new_path_prefix = os.path.join(existing_path_prefix, "audio_folders")

    # open csv
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                pass  # Skip header row
            else:
                # -!!!- Match this with columns from csv file -!!!-
                File_name, Selection, View, Channel, Begin_Time, End_Time, Low_Freq, High_Freq, Annotation = row

                try:
                    os.mkdir(os.path.join(new_path_prefix, Annotation))
                except OSError as error:  # if file already exists
                    print(error)

                # copy files into new folders
                new_filedir = os.path.join(new_path_prefix, Annotation)
                existing_filedir = os.path.join(existing_path_prefix, File_name)

                try:
                    trim_and_write( File_name, existing_filedir, new_filedir, Begin_Time, End_Time, Annotation )
                except ValueError:
                    print("CSV row entered incorrectly for ", File_name)

create_folders()