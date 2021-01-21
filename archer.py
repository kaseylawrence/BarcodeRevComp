import string

barcodefile = open('InputFileNameHere.csv','r')
resultfile = open('OutputFileNameHere.csv','w')

old_chars="ACGT"
replace_chars="TGCA"
tab=str.maketrans(old_chars,replace_chars)


for line in barcodefile:
    barcode = line.split(",")
    barcode[1]=barcode[1].strip()	
    revcomp_result = barcode[1].translate(tab)[::-1]
    print(revcomp_result)
    resultfile.write(barcode[0])
    resultfile.write(",")
    resultfile.write(str(revcomp_result))
    resultfile.write("\n")
    
resultfile.close()
    
