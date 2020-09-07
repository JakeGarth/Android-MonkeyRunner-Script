from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands, sys, signal, os, subprocess, re, time
from subprocess import PIPE
print "start"
def runmonkey(item, device, mydevice):
	i = 0
	installed = 0
	while(i< 150):
		pkg = "pm path "+str(item)
		print pkg
		apk_path = device.shell(pkg)
		print apk_path
		if apk_path.startswith('package:'):
			print "myapp already installed."
			installed = 1
			break
		else:
			time.sleep(1)
			i = i + 1
	if installed == 1:
		print "launching myapp..."
		cmd = "/home/muhammad/Android/Sdk/platform-tools/adb -s %s shell  monkey -p "%mydevice+ str(item) +" -v  --throttle 100 -s 1 --pct-appswitch 25 2000"
		print cmd
		result = os.system(cmd)
		print "sleeping now"	
		time.sleep(20)
		print "finishing myapp..."
	else:
		print "not installed"
		return

def fixCertificatePinning(apkName):
    os.system("addSecurityExceptions.sh "+apkName)
        
def getFirstDevice():
    devices = os.popen("adb devices").read()
    print(devices)
    start = devices.find("emulator")
    return devices[start:start+13]

def installAPK(apk):
    cmdInstall  = "adb install "+apk+"_new.apk"
    try:
        os.system(cmdInstall)
        
    except:
        print("some kind install of error?")
        
def uninstallAPK(apk):
    cmdUninstall = "adb uninstall "+apk
    try:
        print("Sleepy boi for 1 sec")
        time.sleep(1)
        print("finish sleep")
        os.system(cmdUninstall)
        print("do we get to end of try")
    except Exception, e:
        print(e)
        print("some kind of uninstall error?")
        

    
	

    
def monkey(item, device, mydevice):
    cmd = "adb -s %s shell  monkey -p "%mydevice+ str(item) +" -v  --throttle 100 -s 1 --pct-appswitch 25 2000"
    print(cmd)
    result = os.system(cmd)
    
def main():	
    
	#devices = os.popen('/home/muhammad/Android/Sdk/platform-tools/adb devices').read().strip().split('\n')[1:]
	#mydevice = devices[0].split('\t')[0]
    apk = "com.lesmillsondemand"
    print("here")
    mydevice = getFirstDevice()
    print("here x2")
    print(mydevice);
    device = MonkeyRunner.waitForConnection('', mydevice);
    print(device)
    apkAddress = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\com.daystrom.fbattery.apk"
    print("here x3")
    #fixCertificatePinning(apk+".apk")
    installAPK(apk)
    print("[info] Starting Mitmdump #########")
    cmd  = ['mitmdump', '-p', '8080', '-w', './mitmdumps_avd1/'+apk]
    p = subprocess.Popen(cmd, shell=False)
    print(p)
    #monkey(apk,device,mydevice)
    #p._process.destroy()
    #uninstallAPK(apk)
    
   
    
    
    

if __name__ == "__main__":
	main()