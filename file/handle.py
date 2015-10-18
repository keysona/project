#coding:utf-8
from multiprocessing import Process,Queue,Lock,Pool
import MySQLdb as db
import requests as req
import cv2
import numpy as np
from StringIO import StringIO
from pyimagesearch.colordescriptor import ColorDescriptor
import os

def comp(operand):
    data,feature = operand
    print 'start:',os.getpid(),id(data),id(feature)
    result = {}
    for i in range(len(data)):
        hist = [float(item) for item in data[i][5].split(' ')]
        d = chi2_distance(hist,feature)
        result[d] = data[i]
    items = result.items()
    result = sorted(items)[:2]
    return result

def handle_upload_file(f):
    #存储文件
    fobj = open('test.file','w')
    for chunk in f.chunks():
	   fobj.write(chunk)
    fobj.close()
    #初始化工作
    conn = db.connect(host='localhost',user='root',passwd='123',db='test2')
    cur = conn.cursor()
    cd = ColorDescriptor((8, 12, 3))
    rows = cur.execute('select url,width,height,time,type,hist from image') 
    dataset = cur.fetchall()
    img1 = cv2.imread('test.file')
    feature = cd.describe(img1) 
    #多进程
    start,end,step= 0,0,100
    processes = rows/step + 1 if rows%step else 0
    pool = Pool(processes)
    operand = []
    for i in range(processes):
        end = (end + step) if (rows - end > step) else (rows + 1)
	operand.append([dataset[start:end],feature[:]])
        start = end
    result = []
    for item in pool.imap(comp,operand):
        result.extend(item)

    result = sorted(result)
    final = {}
    for i in range(processes):
        temp = {}
        temp['name'] = 'item'+str(i)
        temp['url'] = result[i][1][0]
        temp['width'] = result[i][1][1]
        temp['height'] = result[i][1][2]
        temp['time'] = result[i][1][3]
        temp['type'] = result[i][1][4]
        final[str(i)] = temp
    return final

def chi2_distance(histA, histB, eps = 1e-10):
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
        for (a, b) in zip(histA, histB)])
    return d
      

