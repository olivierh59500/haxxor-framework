#!/usr/bin/env python 
import os
import sys
import commands
import getpass
from subprocess import call
try:
	from termcolor import colored
except ImportError:
	print("[!] You are missing termcolor")
	print("[!] Type pip install termcolor to install it")
	sys.exit(0)
# VARIABLES #
user = getpass.getuser()
uid = os.getuid
apache_check = commands.getoutput("ps -A")
# MISC #
finished_haxxor = ("/usr/bin/haxxor")
ipath = ("/usr/haxxor")
# LIST #
fuzzer1 = call("ls -1 /usr/haxxor/fuzzers/windows/browser | wc -l > /dev/null", shell=True)
fuzzer2 = call("ls -1 /usr/haxxor/fuzzers/windows/os | wc -l > /dev/null", shell=True)
fuzzer3 = call("ls -1 /usr/haxxor/fuzzers/mac_os/browser | wc -l > /dev/null", shell=True)
fuzzer4 = call("ls -1 /usr/haxxor/fuzzers/mac_os/os | wc -l > /dev/null", shell=True)
fuzzer5 = call("ls -1 /usr/haxxor/fuzzers/linux/browser | wc -l > /dev/null", shell=True)
fuzzer6 = call("ls -1 /usr/haxxor/fuzzers/linux/os | wc -l > /dev/null", shell=True)
fuzzer7 = call("ls -1 /usr/haxxor/fuzzers/misc/browser | wc -l > /dev/null", shell=True)
fuzzer8 = call("ls -1 /usr/haxxor/fuzzers/misc/os | wc -l > /dev/null", shell=True)
module1 = call("ls -1 /usr/haxxor/modules/scanning | wc -l > /dev/null", shell=True)
module2 = call("ls -1 /usr/haxxor/modules/dns | wc -l > /dev/null", shell=True)
module3 = call("ls -1 /usr/haxxor/modules/enumeration | wc -l > /dev/null", shell=True)
list_fuzzers = (fuzzer1 + fuzzer2 + fuzzer3 + fuzzer4 + fuzzer5 + fuzzer6 + fuzzer7 + fuzzer8)
list_modules = (module1 + module2 + module3)
list_scanners = call("ls -1 /usr/haxxor/scanners |wc -l > /dev/null", shell=True)
list_privesc = call("ls -1 /usr/haxxor/privesc |wc -l > /dev/null", shell=True)

if(user == "root"):
	print colored("[*] Running as root", "yellow")
else:
	print colored("[!] MUST RUN AS ROOT", "red")
	sys.exit(0)
if(os.path.exists(ipath)):
	print colored("[*] Directories exist", "yellow")
else:
	print colored("[!] Directories not found", "red")
	sys.exit(0)

if("apache2" in apache_check):
	print colored("[*] Apache2 started", "yellow")
else:
	print colored("[*] Starting apache2", "yellow")
	incase = commands.getoutput("service apaceh2 start")
	if("service not found" in incase):
		print colored("[!] You are missing apache2, please install it by typing apt-get install apache2", "red")
		sys.exit(0)
	else:
		print colored("[*] Apache2 started with no error", "yellow")
call("clear", shell=True)
#
#
#
#
#
#
#

def banner():
	print colored("------------------------------------", "blue")
	print colored(" _                                  ", "blue")
	print colored("| |                                 ", "blue")
	print colored("| |__  _____ _   _ _   _ ___   ____ ", "blue")
	print colored("|  _ \(____ ( \ / | \ / ) _ \ / ___)", "blue")
	print colored("| | | / ___ |) X ( ) X ( |_| | |    ", "blue")
	print colored("|_| |_\_____(_/ \_|_/ \_)___/|_|    ", "blue")
	print colored("------------------------------------", "blue")
	print colored("[ [{}] fuzzers  [{}] modules ]".format(list_fuzzers, list_modules), "red")
	print colored("[ [{}] scanners [{}] privesc ]".format(list_scanners, list_privesc), "red")
banner()
print colored("[1] fuzzers", "blue")
print colored("[2] modules", "blue")
print colored("[3] scanners", "blue")
print colored("[4] privesc", "blue")
print colored("[5] help", "blue")
print colored("[6] donate", "blue")
print colored("[7] exit", "blue")
def haxxor_main():
	try:	
		
		haxxor_input = raw_input("[haxxor] => ")
		if(haxxor_input == '1'):
			print colored("[1] Windows", "blue")
			print colored("[2] Linux", "blue")
			print colored("[3] Mac OS", "blue")
			print colored("[4] Misc", "blue")
			choice_1 = raw_input("[fuzzers] => ")
			if(choice_1 == '1'):
				print colored("[1] Browser","blue")
				print colored("[2] Misc", "blue")
				choice_1_1 = raw_input("[fuzzers/Windows] => ")
				if(choice_1_1 == '1'):
					print colored("", "white")
				elif(choice_1_1 == '2'):
					print colored("", "white")
				else:
					print colored("\n[!] Unknown choice", "red")
			elif(choice_1 == '2'):
				print("")
			elif(choice_1 == '3'):
				print("")
			elif(choice_1 == '4'):
				print("")
			else:
				print colored("\n[!] Unknown choice", "red")
		elif(haxxor_input == '2'):
			print("")
		elif(haxxor_input == '3'):
			print("")
		elif(haxxor_input == '4'):
			print("")
		elif(haxxor_input == '5'):
			print("")
		elif(haxxor_input == '6'):
			print("")
		elif(haxxor_input == '7'):
			print colored("\n[*] Exiting", "red")
			sys.exit(0)
		else:
			print("\n[!] Unknown choice")
	except KeyboardInterrupt:
		print colored("\n[!] Type exit to exit", "red")
while True:
	haxxor_main()	