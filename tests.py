import io
import sys

import helloWorld
import pangram
import rnaTranscription
import wordCount
import rle
import differenceOfSquare

def test_helloWorld():
    test = "Hello World !"
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    helloWorld.helloWorld()
    sys.stdout = sys.__stdout__
    if test+"\n"== capturedOutput.getvalue():
        print ('HelloWorld succeeded !')
    else:
        print ('HelloWorld failed !')

def test_pangram():
    tests = ["The quick brown fox jumps over the lazy dog.", "The quck brown fox jumps over the lazy dog.", ""]
    outputs = ["True", "False", "False"]
    for idx, test in enumerate(tests):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        pangram.pangram(test)
        print (pangram.pangram(test))
        sys.stdout = sys.__stdout__
        if outputs[idx]+"\n" != capturedOutput.getvalue():
            print ('Pangram failed !')
            return
    print ('Pangram succeeded !')

def test_rnaTranscription():
    tests = ["GCTAA", "AATCG", ""]
    outputs = ["CGAUU", "UUAGC", ""]
    for idx, test in enumerate(tests):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        rnaTranscription.rnaTranscription(test)
        sys.stdout = sys.__stdout__
        if outputs[idx]+"\n" != capturedOutput.getvalue():
            print ('rnaTranscription failed !')
            return
    print ( 'rnaTranscription succeeded !')

def test_wordCount():
    tests = ["olly olly in come free", ""]
    outputs = ["olly: 2\nin: 1\ncome: 1\nfree: 1\n", ""]
    for idx, test in enumerate(tests):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        wordCount.countWord(test)
        sys.stdout = sys.__stdout__
        if outputs[idx] != capturedOutput.getvalue():
            print (capturedOutput.getvalue())
            print ('countWord failed !')
            return
    print ("wordCount succeeded !")

def test_rle():
    tests = ["WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB", "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWW", ""]
    outputs = ["11WB11W2B23WB", "11WB11W2B23W", ""]
    for idx, test in enumerate(tests):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        rle.rle(test)
        sys.stdout = sys.__stdout__
        if outputs[idx]+'\n' != capturedOutput.getvalue():
            print (capturedOutput.getvalue())
            print ('rle failed !')
            return
    print ("rle succeeded !")

def test_differenceOfSquare():
    tests = [10]
    outputs = [2640]
    for idx, test in enumerate(tests):
        if outputs[idx] != differenceOfSquare.differenceOfSquares(test):
            print (differenceOfSquare.differenceOfSquares(test))
            print ("differenceOfSquare failed !")
            return
    print ("differenceOfSquare succeeded !")

test_helloWorld()
test_pangram()
test_rnaTranscription()
test_wordCount()
test_rle()
test_differenceOfSquare()