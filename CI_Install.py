#! /usr/bin/env python3
#coding:utf8

######################################
##									##
##		Collective Industries		##
##		 Tools Installation			##
##									##
##		  By: Levi & Andrew			##
##				©2018				##
######################################



#############
## Imports ##
#############
from sys import platform
from subprocess import Popen, PIPE
import shutil
import distutils.spawn
import os
import subprocess
import getpass
import pwd
import getpass
import time

###############
## Variables ##
###############
user = pwd.getpwuid(os.getuid())[4]
uname = getpass.getuser()
os_name	= os.name
user = user.replace(',', '')


# Text output color definitions
class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def Debug(var1, var2, TF):
	DEBUG = True
	if DEBUG == True and TF == True:
		print(var1 +' = ' + var2)	
	
def prog_check(program):
	return shutil.which(program) is not None
	#p = Popen(['which', program], stdout=PIPE, stderr=PIPE)
	#p.communicate()
	#return p.returncode == 0
	
	
if user == '':
	users = uname
else:
	users = user

def init():
	os.system('clear')
	if platform == 'linux' or platform == 'linux2':
		# linux
		with open('/etc/os-release') as file:
			global oper
			oper = file.readlines()
			oper = oper[5].split('=')
			oper = oper[1]
			
def main():
	init()
	Debug('oper', oper, False)
	print('######################')
	print('##                  ##')
	print('##   CI INSTALLER   ##')
	print('##                  ##')
	print('######################')
	print('')
	print('')
	print("Welcome " + users + " to the Collective Industries Tools Installation.")
	print("Please select what program(s) you would like to install.")
	print("")
	print("")
	print('1. GitHUB    - ' + str(prog_check('git')))
	print('2. GCC       - ' + str(prog_check('gcc')))
	print('3. Teamspeak - ' + str(prog_check('teamspeak')))
	
	choice = input('Choice: ')
	
	if choice == 1:
		git()
		
def git():
	# GitHub Installation
	os.system('clear')
	if str(prog_check('git')) == False:
		print('Getting ready to install GitHub.')
		os.system('wget https://github.com/hammerzaine/CI-Tools-Install/blob/master/git_install.py')
		os.system('./git_install.py')
		print('GitHub is now installed')
		time.sleep(5)
		os.system('sudo rm git_install.py')
		main()
	else:
		print('Are you sure you want to remove GitHub from your machine. \nYou can always Reinstall it later.')
		yn = input('Y/N: ')
		if yn.lower() == 'y':
			print('Remove github here')
		else:
			main()
		
main()
