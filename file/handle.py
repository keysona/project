import MySQLdb as db
import requests as req
import struct 
import cv2
import numpy as np
from StringIO import StringIO
from pyimagesearch.colordescriptor import ColorDescriptor
def handle_upload_file(f):
    fobj = open('test.file','w')
    for chunk in f.chunks():
	fobj.write(chunk)
    fobj.close()
    conn = db.connect(host='localhost',user='root',passwd='123',db='test2')
    cur = conn.cursor()
    cd = ColorDescriptor((8, 12, 3))
    cur.execute('select url,width,height,time,type,hist from image') 
    a = cur.fetchall()
    img1 = cv2.imread('test.file')
    feature = cd.describe(img1) 
    print type(feature)
    result = {}
    for i in range(len(a)):
        hist = a[i][5].split(' ')
        hist = [float(item) for item in hist]
        d = chi2_distance(hist,feature)
        result[d] = a[i]
	if d < 3:
	    print d
    items = result.items()
    result = sorted(items)[:20]
    final = {}
    for i in range(20):
        temp = {}
        temp['name'] = 'item'+str(i)
	temp['url'] = result[i][1][0]
	temp['width'] = result[i][1][1]
	temp['height'] = result[i][1][2]
	temp['time'] = result[i][1][3]
	temp['type'] = result[i][1][4]
	final[str(i)] = temp
	print final[str(i)]
   # final = {}
   # for i in range(20):
   #     temp = {}
   #     temp['url'] = result[i][1]
   #	temp['name'] = 'item'+str(i)
   #	final[str(i)]=temp
    return final
def chi2_distance(histA, histB, eps = 1e-10):
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
        for (a, b) in zip(histA, histB)])
    return d
      

