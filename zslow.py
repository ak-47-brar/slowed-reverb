#!/usr/bin/env python
#===============================================================================
# Author: Will Fenton
# Date: October 17 2019
#===============================================================================

from pysndfx import AudioEffectsChain
import os
import sys
import getopt

#===============================================================================

def print_usage():
    sys.stderr.write(
"""Usage: python3 process-audio.py [options]
Options:
    (-a | --audio)         <audio file>   the audio file to use
    (-o | --output-path)   <path>         where to save the output
    (-h | --help)                         display this message
Example: python3 process-audio.py -a song.mp3 -o processed-audio.mp3
""")

def main():
    # quit if no arguments provided
    if len(sys.argv) == 1:
        print_usage()
        sys.exit(1)

    # read options
    try:
        options = "a:o:h"
        longOptions = ["audio=", "output-path=", "help"]
        opts, args = getopt.getopt(sys.argv[1:], options, longOptions)
    except getopt.GetoptError:
        print_usage()
        sys.exit(1)

    audio_path = ""
    output_path = "output/processed-audio.mp3"

    # parse options
    for o, v in opts:
        if o in ("-a", "--audio"):
            audio_path = v
        if o in ("-o", "--output-path"):
            output_path = v
        if o in ("-h", "--help"):
            print_usage()
            sys.exit()

    # make sure audio is provided
    if audio_path == "":
        raise Exception("Need to specify an audio file.")

    # make output directory
    try:
        os.mkdir("output")
    except FileExistsError:
        pass

    # chain of effects to apply to the audio
    fx = (
        AudioEffectsChain()
        .speed(0.9)
        .reverb()
    )

    # path to temporarily store the audio
    temp_audio_path = "output/temp.mp3"

    print("Processing audio...")

    # apply the effects, save file
    fx(audio_path, temp_audio_path)

    print("Saving processed audio...")

    # move the processed audio to the desired output path
    os.rename(temp_audio_path, output_path)

#===============================================================================

if __name__ == "__main__":
    main()

#===============================================================================
