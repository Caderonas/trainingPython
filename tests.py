import io
import sys

import helloWorld
import pangram

def test_helloWorld():
    test = "Hello World !"
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    helloWorld.helloWorld()
    sys.stdout = sys.__stdout__
    if test+"\n"== capturedOutput.getvalue():
        print ('HelloWorld succed !')
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
    print ('Pangram succed !')
"""
def test_wordCount():
    tests = [""]
"""


test_helloWorld()
test_pangram()