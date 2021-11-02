import io
import sys

import pangram as pangram
import rnaTranscription as rnaTranscription
import wordCount as wordCount
import rle as rle
import differenceOfSquare as differenceOfSquare

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
            print ('2 . Pangram failed !')
            return
    print ('2 . Pangram succeeded !')

def test_rnaTranscription():
    tests = ["GCTAA", "AATCG", ""]
    outputs = ["CGAUU", "UUAGC", ""]
    for idx, test in enumerate(tests):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        rnaTranscription.rnaTranscription(test)
        sys.stdout = sys.__stdout__
        if outputs[idx]+"\n" != capturedOutput.getvalue():
            print ('3 . rnaTranscription failed !')
            return
    print ( '3 . rnaTranscription succeeded !')

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
            print ('4 . countWord failed !')
            return
    print ("4 . wordCount succeeded !")

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
            print ('6 . rle failed !')
            return
    print ("6 . rle succeeded !")

def test_differenceOfSquare():
    tests = [10]
    outputs = [2640]
    for idx, test in enumerate(tests):
        if outputs[idx] != differenceOfSquare.differenceOfSquares(test):
            print (differenceOfSquare.differenceOfSquares(test))
            print ("7 . differenceOfSquare failed !")
            return
    print ("7 . differenceOfSquare succeeded !")

test_pangram()
test_rnaTranscription()
test_wordCount()
test_rle()
test_differenceOfSquare()