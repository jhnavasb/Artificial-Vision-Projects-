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
include examples/CMakeFiles/freenect-tiltdemo.dir/depend.make

# Include the progress variables for this target.
include examples/CMakeFiles/freenect-tiltdemo.dir/progress.make

# Include the compile flags for this target's objects.
include examples/CMakeFiles/freenect-tiltdemo.dir/flags.make

examples/CMakeFiles/freenect-tiltdemo.dir/tiltdemo.c.obj: examples/CMakeFiles/freenect-tiltdemo.dir/flags.make
examples/CMakeFiles/freenect-tiltdemo.dir/tiltdemo.c.obj: examples/CMakeFiles/freenect-tiltdemo.dir/includes_C.rsp
examples/CMakeFiles/freenect-tiltdemo.dir/tiltdemo.c.obj: ../examples/tiltdemo.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object examples/CMakeFiles/freenect-tiltdemo.dir/tiltdemo.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect-tiltdemo.dir\tiltdemo.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\examples\tiltdemo.c

examples/CMakeFiles/freenect-tiltdemo.dir/tiltdemo.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect-tiltdemo.dir/tiltdemo.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\examples\tiltdemo.c > CMakeFiles\freenect-tiltdemo.dir\tiltdemo.c.i

examples/CMakeFiles/freenect-tiltdemo.dir/tiltdemo.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect-tiltdemo.dir/tiltdemo.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\examples\tiltdemo.c -o CMakeFiles\freenect-tiltdemo.dir\tiltdemo.c.s

# Object files for target freenect-tiltdemo
freenect__tiltdemo_OBJECTS = \
"CMakeFiles/freenect-tiltdemo.dir/tiltdemo.c.obj"

# External object files for target freenect-tiltdemo
freenect__tiltdemo_EXTERNAL_OBJECTS =

bin/freenect-tiltdemo.exe: examples/CMakeFiles/freenect-tiltdemo.dir/tiltdemo.c.obj
bin/freenect-tiltdemo.exe: examples/CMakeFiles/freenect-tiltdemo.dir/build.make
bin/freenect-tiltdemo.exe: lib/libfreenect_sync.dll.a
bin/freenect-tiltdemo.exe: lib/libfreenect.dll.a
bin/freenect-tiltdemo.exe: D:/Jhonatan/Documentos/DriverPackages/libusb-win32-bin-1.2.6.0/lib/gcc/libusb.a
bin/freenect-tiltdemo.exe: D:/Jhonatan/Documentos/DriverPackages/Pre-built.2/lib/libpthreadGC2.a
bin/freenect-tiltdemo.exe: examples/CMakeFiles/freenect-tiltdemo.dir/linklibs.rsp
bin/freenect-tiltdemo.exe: examples/CMakeFiles/freenect-tiltdemo.dir/objects1.rsp
bin/freenect-tiltdemo.exe: examples/CMakeFiles/freenect-tiltdemo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ..\bin\freenect-tiltdemo.exe"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\freenect-tiltdemo.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/CMakeFiles/freenect-tiltdemo.dir/build: bin/freenect-tiltdemo.exe

.PHONY : examples/CMakeFiles/freenect-tiltdemo.dir/build

examples/CMakeFiles/freenect-tiltdemo.dir/clean:
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples && $(CMAKE_COMMAND) -P CMakeFiles\freenect-tiltdemo.dir\cmake_clean.cmake
.PHONY : examples/CMakeFiles/freenect-tiltdemo.dir/clean

examples/CMakeFiles/freenect-tiltdemo.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\examples D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples\CMakeFiles\freenect-tiltdemo.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : examples/CMakeFiles/freenect-tiltdemo.dir/depend
