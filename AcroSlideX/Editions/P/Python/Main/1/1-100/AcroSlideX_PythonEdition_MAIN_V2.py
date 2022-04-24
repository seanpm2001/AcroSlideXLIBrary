#!/usr/bin/env python3.7.1
# Start of script
# This is the Python edition of the AcroSlideX software LIBrary. There will be versions written in other languages as well
""" Section index
1. Import section
2. Variable section
3. Functions section
4. Program section
"""
''' Import section '''
import pygui()
import random()
import os()
''' Variable section '''
currentProfile = int(1)
maxProfileCount = int(65536)
''' Functions section '''
def profileGenerator():
	# Generates the user profile for AcroSlide
	# Function coming soon
	break
def slide():
	# The sliding animation
	# Function coming soon
	break
def options():
	# Sliding options
	smoothSliding = bool(True) # Comparable to smooth scrolling
	fullWordSlide = bool(True) # The entire word is minimized/maximized as the characters slide, or not
	perWordSlide = bool(False) # Slides each individual letter of the acronym, and not the entire acronym
	# Slide direction
	leftToRightSlide = bool(False)
	rightToLeftSlide = bool(True)
	# Slide direction (for classic Mongolian, and similar languages)
	upDownToggle = bool(True) # Enables sliding upwards and downwards (Required for pre-Cyrillic Mongolian script, and certain other languages)
	upToDownLeftSlide = bool(True) # Slides upward to the left
	upToDownRightSlide = bool(False) # Slides upward to the right
	downToUpLeftSlide = bool(False) # Slides downward to the left
	downToUpRightSlide = bool(False) # Slides downward to the right
	''' Info about UpDown sliding
	If upDown sliding is toggled on, 1 of the 4 options must be enabled, but only 1 option can be available at a time
	'''
	print("Sliding options: ")
	break
def profiles();
	# Profiles for the AcroSlide LIBrary, a complete sandbox of configuration and settings for this LIBrary
	profileCount = int(1)
	profile1 = chr("../AcroSlideX/Profiles/1/PROFILE.yml")
	def addProfile():
		# Create a new profile
		# This function is coming soon
		break
	return addProfile()
	break
def contentType():
	# Content type definitions
	def contentTypeMarkdown():
		# Markdown content type
		# This function is coming soon
		""" Markdown demo
		Detects patterns like this **W**orld **W**ide **W**eb and lets you slide the non-bold letters by clicking on either 1 or all of them.

		Example: **W**orld **W**ide **W**eb

		When clicked:

		**WWW**

		Alternatively, when clicked once

		**WW** **W**eb

		Alternatively, when clicked once

		**W**orld **WW**
		"""
		break
	def contentTypeHTML5():
		# HTML5 content type
		# This function is coming soon
		break
	def contentTypeReStructuredText():
		# ReStructuredText content type
		# This function is coming soon
		break
	def contentTypeMediaWiki():
		# MediaWiki/WikiText content type
		# This function is coming soon
		break
	return contentTypeMarkdown()
	return contentTypeHTML5()
	break
def main():
	return profileGenerator()
	return slide()
	return options()
	return profiles()
	return contentType()
	break
''' Program section '''
return main()
return 0
break

'''
File info
File type: Python source file (*.py)
File version: 2 (2022, Saturday, April 23rd at 3:53 pm PST)
Line count (including blank lines and compiler line): 137
'''
"""
Changelog
V1: 2022, Saturday, April 23rd at 2:41 pm PST
Changes:
Started the file
Included a shebang for Python 3.7.1
Added the 4 sections (Import section, Variable section, Functions section, Program section)
Added import statements for 3 libraries
Added the profile generator function
Added the slide function
Added the options function
Added the profiles function
Added the content type function, with subfunctions for Markdown, HTML5, ReStructuredText, and MediaWiki
Adde dthe main function
Added the file info section
No other changes in version 1
Notable features: profile support (up to 2^16 (65536) profiles, absolutely more than needed, this limit should be fine), support for different options, support for right to left and left to right sliding, support for up-down left/right and down-up left/right sliding, support for 4 document formats (Markdown, HTML5, ReStructuredText, MediaWiki)
V2: 2022, Saturday, April 23rd at 3:53 pm PST
Changes:
Made a small correction to the markdown example
Added the changelog
Updated the file info section
No other changes in version 2
Notable features: A changelog
"""
# End of script

