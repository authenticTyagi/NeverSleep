def main():
	try:
		# Import required modules
		from operator import truediv
		from pickle import TRUE
		import pyautogui
		import time
		import sys
		import os, shutil
		from os import system
		import ctypes
		import keyboard

		# FAILSAFE to FALSE feature is enabled by default
		# so that you can easily stop execution of
		# your pyautogui program by manually moving the
		# mouse to the upper left corner of the screen.
		# Once the mouse is in this location,
		# pyautogui will throw an exception and exit.
		pyautogui.FAILSAFE = False

		# Setting the Title of the Console App
		ctypes.windll.kernel32.SetConsoleTitleW("Never Sleep: Version 1.0")

		# Welcome Message
		print("Design & Development by: Abhishek Tyagi || [GitHub Handle: authenticTyagi]")
		print("**************************************************************************\n")
		time.sleep(1)

		# Counter for interrupts and other variables
		inCounter = 0
		pretext = "scn"
		exten = ".jpg"

		# Capture current screen size
		currScreenSize = pyautogui.size()

		# Create a directory to save the screenshots
		directFolder = "Never Sleep"
		existingPath = "C:/Users/Public/Downloads/"
		targetPath = "C:/Users/Public/Downloads/Never Sleep/"

		finalPath = os.path.join(existingPath, directFolder)

		# Checking if the directory exists already
		isExists = os.path.exists(targetPath) # Will return True or False

		# Creating the directory if it doesn't exist yet
		if isExists == False:
			os.mkdir(finalPath)
			print("Directory '% s' has been created to save the screenshots." % directFolder)
		else:
			print("The required directory 'Never Sleep' to save the screenshots already exists.")

		print("Folder Path of the directory: {}\n".format(targetPath))
		# We need to set the pointer to the middle of the screen during the interrupt
		setWidth = (currScreenSize.width)/2
		setHeight = (currScreenSize.height)/2

		# Important Message
		print("-------------------------------------------------------------------------------------")
		print("Press & Hold 'Q' to terminate the program anytime and keep the catured screenshots.")
		print("Press & Hold 'D' to terminate the program anytime and delete the captured screenshots.")
		print("-------------------------------------------------------------------------------------\n")

		# To check whether user agrees to our conditions
		rcvInput = pyautogui.confirm(text='This program will capture the PRINTSCREENs of your primary display in every 15 seconds to let you analyze them later if needed. The previously stored data in the directory will be overwritten by the application. This will consume approximately 1 MB per minute from your drive storage.', title='Notice & Disclaimer', buttons=['I Agree', 'No, I changed my mind'])

		if rcvInput == "I Agree":
			while True:
				# Checking everytime the loop runs if the target directory has been deleted manually or mising for any reason
				isExists = os.path.exists(targetPath)
				if isExists == True:
					fileName = targetPath + pretext + str(inCounter) + exten
					fN = fileName
					pyautogui.screenshot(fN)	
					pyautogui.moveTo(x=setWidth, y=setHeight)
					pyautogui.press('right')

					print("Interrupt(s) executed so far: {}.".format(inCounter))
					print("Interrupting again in ")
	
					for remaining in range(15, 0, -1):
						# Checking regularly if the user wants to quit the program using D or Q
						qPressSmall = keyboard.is_pressed("q")
						qPressBig = keyboard.is_pressed("Q")
						dPressSmall = keyboard.is_pressed("d")
						dPressBig = keyboard.is_pressed("D")
				
						if  qPressSmall == True or qPressBig == True: # Checking if the user pressed q or Q
							print("\nOk, Bye!")
							time.sleep(1)
							return "Successful Exit"
						elif dPressSmall == True or dPressBig == True: # Checking if the user pressed d or D
							for files in os.listdir(targetPath):
								path = os.path.join(targetPath, files)
								try:
									shutil.rmtree(path) # Deleting all the files while looping through them one by one
								except OSError:
									os.remove(path)
							print("\nFiles have been deleted successfully. The program will exit now.")
							time.sleep(1)
							return "Successful Exit"
						else:
							sys.stdout.write("\r")
							sys.stdout.write("{:2d} ...".format(remaining))
							sys.stdout.flush()
							time.sleep(1)
					print("\n")
					inCounter += 1
				else:
					pyautogui.alert(text="Unable to save the captured screenshot. Please check the directory path and go again. The program will exit now.", title="Oops!", button="Cool")
					return "Error Exit"
		else:
			print("\nYou have not agreed to the disclaimer. The program will exit now.")
			time.sleep(1)
			return "User Exit"
	except:
		print("Program is exiting due to multiple issues with the environment.")
# Calling the main function
main()
