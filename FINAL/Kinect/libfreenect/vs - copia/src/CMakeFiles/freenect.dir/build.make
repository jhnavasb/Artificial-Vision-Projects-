# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\CMake\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\CMake\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs

# Include any dependencies generated for this target.
include src/CMakeFiles/freenect.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/freenect.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/freenect.dir/flags.make

src/CMakeFiles/freenect.dir/core.c.obj: src/CMakeFiles/freenect.dir/flags.make
src/CMakeFiles/freenect.dir/core.c.obj: src/CMakeFiles/freenect.dir/includes_C.rsp
src/CMakeFiles/freenect.dir/core.c.obj: ../src/core.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object src/CMakeFiles/freenect.dir/core.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect.dir\core.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\core.c

src/CMakeFiles/freenect.dir/core.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect.dir/core.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\core.c > CMakeFiles\freenect.dir\core.c.i

src/CMakeFiles/freenect.dir/core.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect.dir/core.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\core.c -o CMakeFiles\freenect.dir\core.c.s

src/CMakeFiles/freenect.dir/tilt.c.obj: src/CMakeFiles/freenect.dir/flags.make
src/CMakeFiles/freenect.dir/tilt.c.obj: src/CMakeFiles/freenect.dir/includes_C.rsp
src/CMakeFiles/freenect.dir/tilt.c.obj: ../src/tilt.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object src/CMakeFiles/freenect.dir/tilt.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect.dir\tilt.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\tilt.c

src/CMakeFiles/freenect.dir/tilt.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect.dir/tilt.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\tilt.c > CMakeFiles\freenect.dir\tilt.c.i

src/CMakeFiles/freenect.dir/tilt.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect.dir/tilt.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\tilt.c -o CMakeFiles\freenect.dir\tilt.c.s

src/CMakeFiles/freenect.dir/cameras.c.obj: src/CMakeFiles/freenect.dir/flags.make
src/CMakeFiles/freenect.dir/cameras.c.obj: src/CMakeFiles/freenect.dir/includes_C.rsp
src/CMakeFiles/freenect.dir/cameras.c.obj: ../src/cameras.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object src/CMakeFiles/freenect.dir/cameras.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect.dir\cameras.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\cameras.c

src/CMakeFiles/freenect.dir/cameras.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect.dir/cameras.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\cameras.c > CMakeFiles\freenect.dir\cameras.c.i

src/CMakeFiles/freenect.dir/cameras.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect.dir/cameras.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\cameras.c -o CMakeFiles\freenect.dir\cameras.c.s

src/CMakeFiles/freenect.dir/flags.c.obj: src/CMakeFiles/freenect.dir/flags.make
src/CMakeFiles/freenect.dir/flags.c.obj: src/CMakeFiles/freenect.dir/includes_C.rsp
src/CMakeFiles/freenect.dir/flags.c.obj: ../src/flags.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object src/CMakeFiles/freenect.dir/flags.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect.dir\flags.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\flags.c

src/CMakeFiles/freenect.dir/flags.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect.dir/flags.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\flags.c > CMakeFiles\freenect.dir\flags.c.i

src/CMakeFiles/freenect.dir/flags.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect.dir/flags.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\flags.c -o CMakeFiles\freenect.dir\flags.c.s

src/CMakeFiles/freenect.dir/usb_libusb10.c.obj: src/CMakeFiles/freenect.dir/flags.make
src/CMakeFiles/freenect.dir/usb_libusb10.c.obj: src/CMakeFiles/freenect.dir/includes_C.rsp
src/CMakeFiles/freenect.dir/usb_libusb10.c.obj: ../src/usb_libusb10.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object src/CMakeFiles/freenect.dir/usb_libusb10.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect.dir\usb_libusb10.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\usb_libusb10.c

src/CMakeFiles/freenect.dir/usb_libusb10.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect.dir/usb_libusb10.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\usb_libusb10.c > CMakeFiles\freenect.dir\usb_libusb10.c.i

src/CMakeFiles/freenect.dir/usb_libusb10.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect.dir/usb_libusb10.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\usb_libusb10.c -o CMakeFiles\freenect.dir\usb_libusb10.c.s

src/CMakeFiles/freenect.dir/registration.c.obj: src/CMakeFiles/freenect.dir/flags.make
src/CMakeFiles/freenect.dir/registration.c.obj: src/CMakeFiles/freenect.dir/includes_C.rsp
src/CMakeFiles/freenect.dir/registration.c.obj: ../src/registration.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building C object src/CMakeFiles/freenect.dir/registration.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect.dir\registration.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\registration.c

src/CMakeFiles/freenect.dir/registration.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect.dir/registration.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\registration.c > CMakeFiles\freenect.dir\registration.c.i

src/CMakeFiles/freenect.dir/registration.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect.dir/registration.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\registration.c -o CMakeFiles\freenect.dir\registration.c.s

src/CMakeFiles/freenect.dir/audio.c.obj: src/CMakeFiles/freenect.dir/flags.make
src/CMakeFiles/freenect.dir/audio.c.obj: src/CMakeFiles/freenect.dir/includes_C.rsp
src/CMakeFiles/freenect.dir/audio.c.obj: ../src/audio.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building C object src/CMakeFiles/freenect.dir/audio.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect.dir\audio.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\audio.c

src/CMakeFiles/freenect.dir/audio.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect.dir/audio.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\audio.c > CMakeFiles\freenect.dir\audio.c.i

src/CMakeFiles/freenect.dir/audio.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect.dir/audio.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\audio.c -o CMakeFiles\freenect.dir\audio.c.s

src/CMakeFiles/freenect.dir/loader.c.obj: src/CMakeFiles/freenect.dir/flags.make
src/CMakeFiles/freenect.dir/loader.c.obj: src/CMakeFiles/freenect.dir/includes_C.rsp
src/CMakeFiles/freenect.dir/loader.c.obj: ../src/loader.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building C object src/CMakeFiles/freenect.dir/loader.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect.dir\loader.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\loader.c

src/CMakeFiles/freenect.dir/loader.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect.dir/loader.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\loader.c > CMakeFiles\freenect.dir\loader.c.i

src/CMakeFiles/freenect.dir/loader.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect.dir/loader.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src\loader.c -o CMakeFiles\freenect.dir\loader.c.s

# Object files for target freenect
freenect_OBJECTS = \
"CMakeFiles/freenect.dir/core.c.obj" \
"CMakeFiles/freenect.dir/tilt.c.obj" \
"CMakeFiles/freenect.dir/cameras.c.obj" \
"CMakeFiles/freenect.dir/flags.c.obj" \
"CMakeFiles/freenect.dir/usb_libusb10.c.obj" \
"CMakeFiles/freenect.dir/registration.c.obj" \
"CMakeFiles/freenect.dir/audio.c.obj" \
"CMakeFiles/freenect.dir/loader.c.obj"

# External object files for target freenect
freenect_EXTERNAL_OBJECTS =

lib/libfreenect.dll: src/CMakeFiles/freenect.dir/core.c.obj
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/tilt.c.obj
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/cameras.c.obj
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/flags.c.obj
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/usb_libusb10.c.obj
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/registration.c.obj
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/audio.c.obj
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/loader.c.obj
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/build.make
lib/libfreenect.dll: D:/Jhonatan/Documentos/DriverPackages/libusb-win32-bin-1.2.6.0/lib/gcc/libusb.a
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/linklibs.rsp
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/objects1.rsp
lib/libfreenect.dll: src/CMakeFiles/freenect.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Linking C shared library ..\lib\libfreenect.dll"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\freenect.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/freenect.dir/build: lib/libfreenect.dll

.PHONY : src/CMakeFiles/freenect.dir/build

src/CMakeFiles/freenect.dir/clean:
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src && $(CMAKE_COMMAND) -P CMakeFiles\freenect.dir\cmake_clean.cmake
.PHONY : src/CMakeFiles/freenect.dir/clean

src/CMakeFiles/freenect.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\src D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\src\CMakeFiles\freenect.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/freenect.dir/depend

