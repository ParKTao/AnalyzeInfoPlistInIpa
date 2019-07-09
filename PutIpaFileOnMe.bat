@set currentPath=%~dp0
@set ipaFile=%1

@echo %currentPath%
@echo %ipaFile%

@call %currentPath%\Python-3.7.0\python.exe %currentPath%/IpaToolSource/AnalyzeInfoPlistInIpa.py %ipaFile%

@echo if you want to look out the another info.plist,please see the open Source

pause