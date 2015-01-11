PWBC - Packaged Windows Build Code

	This project contains prebuilt executables for Mac OSX and Windows which will run any 
arbitrary python code you hook into them. It allows development on whatever platform you
develop on without you having to concern yourself with releasing your game to multiple
platforms, whether yo use py2exe or pyinstaller, and even just the boring manual labor
of zipping up files. 

The executables come complete with these libraries:
	* python2.6
	  * a large portion of python standard library, though not everything
	  * sockets, urllib, zipfile, unicode, etc are included
	  * certain more special case library files which had larger file size are not included
	* pygame 1.9.1
	* numpy
	* ctypes

Instructions
	Ensure core/libengine.py contains a run() function.
	Use provided base code if desired, or delete other files in core to use your own.
	Use provided art/fonts directories for assets if desired, or design your own layout.
	A core/libengine.py file with a run() function is only strict requirement.
	
	Edit build_settings.py.
	Change appname to the name of your app. 
	Release files will be {appname}_{platform}.zip.
	Release zip files will contain a top level folder {appname}.
	Add files to ignore list, with relative paths to base directory. Folders listed
		will not be traversed at all.
	Configure build and release directories as needed.
	Run build.py
	Distribute zip files to their destination platforms.

Base Code:
	Base code is provided which:
	* Separates display resolution from game resolution
	* Handles drawing sprites
	* Draws a framerate
	* Sets the program's icon
	* Use it or don't!

Changelog:
	2 - Contains mac osx exe, build script to package releaseable zips quickly.
	1 - First release. Only windows exe. No build scripts.


-saluk (saluk64007@gmail.com)