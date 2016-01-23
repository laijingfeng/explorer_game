@echo off

set /p IsHome=是否家里环境?(y/n)
if /i %IsHome% EQU y (
	set UNITY_PATH="E:\Program Files\Unity4.6.0\Editor\"
	set PROJECT_PATH="D:\GitHub\explorer_client"
	set GAME_PATH="D:\GitHub\explorer_game"
) else (
	set UNITY_PATH="D:\Program Files\Unity3D\Editor"
	set PROJECT_PATH="D:\GitHub\explorer_client"
	set GAME_PATH="D:\GitHub\explorer_game"
)
::注释要另起一行，地址带空格要加引号，PROJECT_PATH后面不要加/
set FTP_PATH="\\10.0.128.3\ipa\auto_build\"

set TOOLS_PATH=%cd%

cd /D %UNITY_PATH%
::/D是跨磁盘

echo Packing...

start /wait Unity.exe -projectPath %PROJECT_PATH% -executeMethod Build.BuildWeb build_out_path-%GAME_PATH% -quit -batchmode

echo Packed

echo Finish.

start /wait python qr.py lai jing 

copy /y %GAME_PATH%\qr.png %FTP_PATH%\qr.png
copy /y %GAME_PATH%\explorer_game.html %FTP_PATH%\explorer_game.html
copy /y %GAME_PATH%\explorer_game.unity3d %FTP_PATH%\explorer_game.unity3d

pause