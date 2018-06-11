# Author: Adam Roch
import io
import sys
import unittest
import json
import os

def get_path():
    # special python variable, is the current file name    
    current_file = __file__
    
    #gets the current directory path
    current_directory = os.path.dirname(current_file)

    #gets us to testx_python directory
    up_one_directory = os.path.dirname(current_directory)

    return up_one_directory

path_to_testx_python = get_path()

sys.path.append(path_to_testx_python)

from scripts import cpu_test as ct

class TestMemoryTest(unittest.TestCase):

    def test_memory_test(self):

        for i in range(2):  ## it will run the test i times
            captured_out = io.StringIO()
            og_out = sys.stdout
            sys.stdout = captured_out
            ct.run()
            sys.stdout = og_out
        
            test_output = captured_out.getvalue()
            json_format_output = json.loads(test_output)
            output_dict = dict(json_format_output)

            #print(output_dict['testStartDateTime'])
        
            self.assertEqual(output_dict['result'], 'SUCCESS')


if __name__ == '__main__':
    unittest.main()





    
