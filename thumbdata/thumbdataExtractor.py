import sys

if len(sys.argv)!=2:
	print("Usage : python " + sys.argv[0] + " <full file path of thumbdata file>")
	exit(0)

f=open(sys.argv[1],'rb')
thumbdata = f.read()
f.close()

streamStart = b'\xff\xd8'
streamEnd = b'\xff\xd9'

count = 0
start = 0

while True:
    x1 = thumbdata.find(streamStart,start)
    if x1 < 0:
        break
    x2 = thumbdata.find(streamEnd,x1)
    jpg = thumbdata[x1:x2+1]
    count += 1
    fname = 'ExtractedPic-%d.jpg' % (count)
    fw = open(fname,'wb')
    fw.write(jpg)
    fw.close()
    print("Extracted " + str(count) + " picture(s)")
    start = x2+2