# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:48:54 2018

@author: haoyu
"""

import hashlib
if __name__=='__main__':
    
    md5=hashlib.md5()
    md5.update('this is a sentence.'.encode('utf-8'))
    md5.update('This is a second sentence.'.encode('utf-8'))
    print('不出意外，这将是个乱码：',md5.digest())
    print('MD5:',md5.hexdigest())
    
    md5=hashlib.md5()
    md5.update('This is a sentence.This is a second sentence.'.encode('utf-8'))
    print('MD5:',md5.hexdigest())
    print(md5.digest_size,md5.block_size)
    print('-------------------')
    
    sha1=hashlib.sha1()
    sha1.update('this is a sentence.'.encode('utf-8'))
    sha1.update('this is a second sentence.'.encode('utf-8'))
    print('不出意外，这将是乱码：',sha1.digest())
    print('SHA1:',sha1.hexdigest())
    
    sha1=hashlib.sha1()
    sha1.update('This is a sentence.this a second sentence.'.encode('utf-8'))
    print('SHA1:',sha1.hexdigest())
    print(sha1.digest_size,sha1.block_size)
    print('=====================')


    md5=hashlib.new('md5','this is a sentence.This a second sentence.'.encode('utf-8'))
    print(md5.hexdigest()) 
    sha1=hashlib.new('sha1','This is a sentence.This is a second sentence.'.encode('utf-8'))
    print(sha1.hexdigest())
    
    print(hashlib.algorithms_available)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    