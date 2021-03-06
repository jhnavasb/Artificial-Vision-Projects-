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
include wrappers/python/CMakeFiles/cython3_freenect.dir/depend.make

# Include the progress variables for this target.
include wrappers/python/CMakeFiles/cython3_freenect.dir/progress.make

# Include the compile flags for this target's objects.
include wrappers/python/CMakeFiles/cython3_freenect.dir/flags.make

wrappers/python/freenect3.c:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating freenect3.c"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python && C:\Users\alexn\AppData\Local\Programs\Python\Python36\Lib\site-packages\grpc\_cython\cygrpc.cp36-win_amd64.pyd -3 -o freenect3.c D:/Jhonatan/Documentos/AI/Vision/FINAL/Kinect/libfreenect/wrappers/python/freenect.pyx

wrappers/python/CMakeFiles/cython3_freenect.dir/freenect3.c.obj: wrappers/python/CMakeFiles/cython3_freenect.dir/flags.make
wrappers/python/CMakeFiles/cython3_freenect.dir/freenect3.c.obj: wrappers/python/CMakeFiles/cython3_freenect.dir/includes_C.rsp
wrappers/python/CMakeFiles/cython3_freenect.dir/freenect3.c.obj: wrappers/python/freenect3.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object wrappers/python/CMakeFiles/cython3_freenect.dir/freenect3.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\cython3_freenect.dir\freenect3.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python\freenect3.c

wrappers/python/CMakeFiles/cython3_freenect.dir/freenect3.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/cython3_freenect.dir/freenect3.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python\freenect3.c > CMakeFiles\cython3_freenect.dir\freenect3.c.i

wrappers/python/CMakeFiles/cython3_freenect.dir/freenect3.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/cython3_freenect.dir/freenect3.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python\freenect3.c -o CMakeFiles\cython3_freenect.dir\freenect3.c.s

# Object files for target cython3_freenect
cython3_freenect_OBJECTS = \
"CMakeFiles/cython3_freenect.dir/freenect3.c.obj"

# External object files for target cython3_freenect
cython3_freenect_EXTERNAL_OBJECTS =

wrappers/python/python3/freenect.dll: wrappers/python/CMakeFiles/cython3_freenect.dir/freenect3.c.obj
wrappers/python/python3/freenect.dll: wrappers/python/CMakeFiles/cython3_freenect.dir/build.make
wrappers/python/python3/freenect.dll: lib/libfreenect_sync.dll.a
wrappers/python/python3/freenect.dll: C:/Users/alexn/AppData/Local/Programs/Python/Python36/libs/python3.lib
wrappers/python/python3/freenect.dll: lib/libfreenect.dll.a
wrappers/python/python3/freenect.dll: D:/Jhonatan/Documentos/DriverPackages/libusb-win32-bin-1.2.6.0/lib/gcc/libusb.a
wrappers/python/python3/freenect.dll: D:/Jhonatan/Documentos/DriverPackages/Pre-built.2/lib/libpthreadGC2.a
wrappers/python/python3/freenect.dll: wrappers/python/CMakeFiles/cython3_freenect.dir/linklibs.rsp
wrappers/python/python3/freenect.dll: wrappers/python/CMakeFiles/cython3_freenect.dir/objects1.rsp
wrappers/python/python3/freenect.dll: wrappers/python/CMakeFiles/cython3_freenect.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C shared module python3\freenect.dll"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\cython3_freenect.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
wrappers/python/CMakeFiles/cython3_freenect.dir/build: wrappers/python/python3/freenect.dll

.PHONY : wrappers/python/CMakeFiles/cython3_freenect.dir/build

wrappers/python/CMakeFiles/cython3_freenect.dir/clean:
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python && $(CMAKE_COMMAND) -P CMakeFiles\cython3_freenect.dir\cmake_clean.cmake
.PHONY : wrappers/python/CMakeFiles/cython3_freenect.dir/clean

wrappers/python/CMakeFiles/cython3_freenect.dir/depend: wrappers/python/freenect3.c
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\wrappers\python D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\python\CMakeFiles\cython3_freenect.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : wrappers/python/CMakeFiles/cython3_freenect.dir/depend

