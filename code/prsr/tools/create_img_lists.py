"""Create image-list file
Example:
python tools/create_img_lists.py 
"""
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--dataset", dest="dataset",  
                  help="dataset path")
parser.add_option("--trainfile", dest="trainfile",  
                  help="trainfile path")
parser.add_option("--testfile", dest="testfile",  
                  help="testfile path")

(options, args) = parser.parse_args()

f1 = open(options.trainfile, 'w')
f2 = open(options.testfile, 'w')
dataset_basepath = options.dataset

for p1 in os.listdir(dataset_basepath):
	l2 = os.listdir(dataset_basepath + '/' + p1)
	l2.sort(key=lambda f: int(filter(str.isdigit, f)))
	l2_tr = l2[:1000]
	for p2 in l2_tr:
		l3 = os.listdir(dataset_basepath + '/' + p1 + '/' + p2)
		l3.sort(key=lambda f: int(filter(str.isdigit, f)))
		for p3 in l3:
  			image = os.path.abspath(dataset_basepath + '/' + p1 + '/' + p2 + '/' + p3)
  			f1.write(image + '\n')
	l2_te = l2[1000:1010]
	for p2 in l2_te:
		l3 = os.listdir(dataset_basepath + '/' + p1 + '/' + p2)
		l3.sort(key=lambda f: int(filter(str.isdigit, f)))
		for p3 in l3:
  			image = os.path.abspath(dataset_basepath + '/' + p1 + '/' + p2 + '/' + p3)
  			f2.write(image + '\n')

f1.close()
f2.close()