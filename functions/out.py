

# OM Ganesh Shivyaye
import re

class out_text():

    def __init__(self,infile) -> None:
        self.out = 0;
        self.file = infile
        pass

    def n_out(self, content):
        rx = re.search(';(.*);', content)
        print(rx.group(1))
        return rx

    def e_out(self,content):
        rx = re.search(';(.*);', content)
        print('\033[31m' + rx.group(1)+ '\033[39m')
        

    def s_out(self,content):
        rx = re.search(';(.*);', content)
        print('\033[32m' + rx.group(1)+ '\033[39m')
     