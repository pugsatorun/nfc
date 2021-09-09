#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii
import nfc
import time

# 学生証のサービスコード
service_code = 0x200B

def on_connect_nfc(tag):
  # タグのIDなどを出力する
  # print tag
  
  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
        sc = nfc.tag.tt3.ServiceCode(service_code >> 6 ,service_code & 0x3f)
        bc = nfc.tag.tt3.BlockCode(0,service=0)
        data = tag.read_without_encryption([sc],[bc])
        print("sc= ", sc)
        print("bc= ", bc)
        print("data= " , data)

        sid =  "s" + str(data)
        print(sid)
    except Exception as e:
      print("error: %s",e)
  else:
    print("error: tag isn't Type3Tag")
  
def main():
  clf = nfc.ContactlessFrontend('usb')
  while True:
    clf.connect(rdwr={'on-connect': on_connect_nfc})
    time.sleep(3)
  
if __name__ == "__main__":
  main()
"""
import os
import sys
sys.path.insert(1, os.path.split(sys.path[0])[0])
 
import binascii
import nfc
   
service_code = 0x090f
   
def connected(tag):
  # タグのIDなどを出力する
  print(tag)
   
  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
      # 内容を16進数で出力する
      print('  ' + '\n  '.join(tag.dump()))
    except Exception as e:
      print( "error: %s",e)
  else:
    print("error: tag isn't Type3Tag")
   
# タッチ時のハンドラを設定して待機する
clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
"""
