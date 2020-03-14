Luke Zambella and Gregory Yezhov
This program assumes that machine definitions and their text files are stored in their own directories so multiple ones can be tested.

To run the program, go to the base directory where __main__.py is and run the command:

python __main__.py {machine directory name} {"input string"}


it was developed with python 3.8 but should work for all versions of python3.

The input string must be enclosed in quotations.

It has 2 outputs, the first one assumes that the input string is either entirely an accept string or not such that if there is a possible match but other characters it will reject.
The second output fixes this by working on strings where the match may have text before or after it. This implementation works by resetting the machine instead of rejecting and accepting the first match.

The code for the machine is stored in state_machine.py and is well documented.
The example machine is alpha_email_recognizer and accepts input that is an email that consists of only lower case letters, the period and @ symbol.
It is defined by the REGEX /[a-z\.]+@[a-z]+\.[a-z\.]

alternatively, run `python test.py` to run a unit test suite that tests each of the FSA matching functions, and the file loading functions against a wide variety of inputs. 
if successful, it should output OK if everything was successful