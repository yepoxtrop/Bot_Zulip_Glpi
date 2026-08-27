@echo off

:: Acces to folder RustDesk
pushd "C:\Program Files\RustDesk"

:: Get Id
echo **************************** > %TEMP%\Codigo_Rustdesk.txt
rustdesk.exe --get-id | more >> %TEMP%\Codigo_Rustdesk.txt
echo **************************** >> %TEMP%\Codigo_Rustdesk.txt
popd 

:: Open notepad with rustdesk code
notepad %TEMP%\Codigo_Rustdesk.txt

:: Copy rustdesk code to clipboard
rustdesk.exe --get-id | more | clip

::pause