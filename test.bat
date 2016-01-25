@echo off

set UNITY_PATH="C:\Program Files (x86)\Unity4.6.0f3\Editor\"
set PROJECT_PATH="E:\web_auto_build\client\game\client"
set TOOLS_PATH="E:\web_auto_build\client\tools\tools"
set GAME_PATH="\\10.0.128.3\webclient\auto_web\WebPlayer"
set TABLE_PATH="E:\web_auto_build\common"

cd /D %UNITY_PATH%

if %BuildAssets% EQU true (
    echo UpdateAssets...
    start /wait TortoiseProc.exe /command:update /path:%TOOLS_PATH% /closeonend:1
    echo UpdateAssetsFinish

    echo BuildAssets...
    start /wait Unity.exe -projectPath %TOOLS_PATH% -executeMethod AutoBuild.Build -quit -batchmode
    echo BuildAssetsFinish
)

if %BuildTableAndMsg% EQU true (
    echo UpdateTableAndMsg...
    start /wait TortoiseProc.exe /command:update /path:%TABLE_PATH% /closeonend:1
    echo UpdateTableAndMsgFinish
)

if %PROJECT_PATH% EQU true (
    echo UpdateClient...
    start /wait TortoiseProc.exe /command:update /path:%PROJECT_PATH% /closeonend:1
    echo UpdateClientFinish
)

echo BuildClient...
start /wait Unity.exe -projectPath %PROJECT_PATH% -executeMethod AutoBuild.BuildWeb build_out_path-%GAME_PATH%-%BuildAssets%-%BuildTableAndMsg%-%BuildClient% -quit -batchmode
echo BuildClientFinish

if %BuildTableAndMsg% EQU true (
    echo BuildServerTable...
    start http://10.0.128.3/dev/devtools/dumptable?client=0&server=101&label=rxjb
    echo BuildServerTableFinish
)

echo FinishAll
