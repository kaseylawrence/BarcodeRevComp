import os
import subprocess
from subprocess import Popen, PIPE
barcodefile = open('/home/pi/Documents/Acher_MBCs_MiSeq.csv','r')
resultfile = open('/home/pi/Documents/Archer_MBCs_NextSeq.csv','w')

import string
old_chars="ACGT"
replace_chars="TGCA"
tab=str.maketrans(old_chars,replace_chars)


for line in barcodefile:
    barcode = line.split(",")
    #print(barcode[1])
    #revcomp = str("""echo \'%s\' | tr \'ATCG\' \'TAGC\' | rev""" % barcode[1])
    #print(revcomp)
    #revcomp_result = os.popen(revcomp,'r',1)
    #revcomp_result = subprocess.Popen([revcomp], stdout=subprocess.PIPE,stderr=subprocess.PIPE, universal_newlines=True,shell=True)
   # revcomp_result = subprocess.run(revcomp, capture_output=True,text=True).stdout
    #revcomp_result =  check_output(revcomp)
    #revcomp_read = revcomp.read()
    barcode[1]=barcode[1].strip()	
    revcomp_result = barcode[1].translate(tab)[::-1]
    print(revcomp_result)
    resultfile.write(barcode[0])
    resultfile.write(",")
    resultfile.write(str(revcomp_result))
    resultfile.write("\n")
    
resultfile.close()
    
