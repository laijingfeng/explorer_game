# -*- encoding: UTF-8 -*-

import sys, os, time

UNITY_PATH = "D:\Program Files\Unity3D\Editor\Unity.exe"

if __name__=="__main__":

    if len(sys.argv)!=3:
        print "need 2 argvs: is_windows is_home"
        sys.exit(-1)

    is_windows=int(sys.argv[1])
    is_home=int(sys.argv[2])
    
    if is_windows==1:
        if is_home==1:
            UNITY_PATH = "E:\Program Files\Unity4.6.0\Editor\Unity.exe"
        else:
            UNITY_PATH = "D:\Program Files\Unity3D\Editor\Unity.exe"
    else:
        UNITY_PATH = "ios"

    if(not( is_windows==1 and is_home!=1 )):
        print "wait!"
        sys.exit(0)

    print "hi"

    os.system('"D:\Program Files\Unity3D\Editor\Unity.exe"')
'''
    os.system('"D:\Program Files\Unity3D\Editor\Unity.exe" -projectPath "D:\GitHub\explorer_client" -executeMethod Pack.Build -quit -batchmode')
''' 


    


    

