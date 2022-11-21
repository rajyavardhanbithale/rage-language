#!/usr/bin/python3.10
# OM Ganesh Shivyaye

import sys
import argparse
import re

from functions import out 

class main:

    def __init__(self, file) -> None:
        self.file = file                        # File
        self.p_out = out.out_text(self.file)    # Loading r printing method
        pass

    def main(self):
        with open(self.file,'r') as p_file:     
            p_line = p_file.readlines()         # Reading file line by line

            line_no = 0

            for read_lines in p_line:           # Reading and Filter Empty Line
                if read_lines.strip() == "":
                    #print("Empty Lines")
                    pass

                elif 'r' in read_lines:         # Preparing for r priting method

                    if 'out' in read_lines:            
                        self.p_out.n_out(read_lines)    # Normal Out
                        #print(read_lines)
                
                    elif 'log' in read_lines:
                        if '.e' in read_lines or '.error' in read_lines:
                            self.p_out.e_out(read_lines)



                        elif '.s' in read_lines or '.success' in read_lines:
                            self.p_out.s_out(read_lines)
             





                    else:
                        pass
                
                line_no = line_no + 1
        



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="RAGE LANG")
    
    #parser.add_argument('file', type=str,dest="ifile")

    #args = parser.parse_args()


    compile = main(sys.argv[1])
    compile.main()