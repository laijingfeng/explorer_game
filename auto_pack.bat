@echo off

set /p IsHome=�Ƿ���ﻷ��?(y/n)
if /i %IsHome% EQU y (
	set UNITY_PATH="E:\Program Files\Unity4.6.0\Editor\"
	set PROJECT_PATH="D:\GitHub\explorer_client"
) else (
	set UNITY_PATH="D:\Program Files\Unity3D\Editor"
	set PROJECT_PATH="D:\GitHub\explorer_client"
)

cd /D %UNITY_PATH%
::/D�ǿ����

echo Packing...

::start /wait Unity.exe -projectPath %PROJECT_PATH% -executeMethod Pack.Build -quit -batchmode

echo Finish.

start /wait python qr.py lai jing 

pause