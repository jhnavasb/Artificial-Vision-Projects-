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
include examples/CMakeFiles/freenect-camtest.dir/depend.make

# Include the progress variables for this target.
include examples/CMakeFiles/freenect-camtest.dir/progress.make

# Include the compile flags for this target's objects.
include examples/CMakeFiles/freenect-camtest.dir/flags.make

examples/CMakeFiles/freenect-camtest.dir/camtest.c.obj: examples/CMakeFiles/freenect-camtest.dir/flags.make
examples/CMakeFiles/freenect-camtest.dir/camtest.c.obj: examples/CMakeFiles/freenect-camtest.dir/includes_C.rsp
examples/CMakeFiles/freenect-camtest.dir/camtest.c.obj: ../examples/camtest.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object examples/CMakeFiles/freenect-camtest.dir/camtest.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect-camtest.dir\camtest.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\examples\camtest.c

examples/CMakeFiles/freenect-camtest.dir/camtest.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect-camtest.dir/camtest.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\examples\camtest.c > CMakeFiles\freenect-camtest.dir\camtest.c.i

examples/CMakeFiles/freenect-camtest.dir/camtest.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect-camtest.dir/camtest.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\examples\camtest.c -o CMakeFiles\freenect-camtest.dir\camtest.c.s

# Object files for target freenect-camtest
freenect__camtest_OBJECTS = \
"CMakeFiles/freenect-camtest.dir/camtest.c.obj"

# External object files for target freenect-camtest
freenect__camtest_EXTERNAL_OBJECTS =

bin/freenect-camtest.exe: examples/CMakeFiles/freenect-camtest.dir/camtest.c.obj
bin/freenect-camtest.exe: examples/CMakeFiles/freenect-camtest.dir/build.make
bin/freenect-camtest.exe: lib/libfreenect.dll.a
bin/freenect-camtest.exe: D:/Jhonatan/Documentos/DriverPackages/libusb-win32-bin-1.2.6.0/lib/gcc/libusb.a
bin/freenect-camtest.exe: examples/CMakeFiles/freenect-camtest.dir/linklibs.rsp
bin/freenect-camtest.exe: examples/CMakeFiles/freenect-camtest.dir/objects1.rsp
bin/freenect-camtest.exe: examples/CMakeFiles/freenect-camtest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ..\bin\freenect-camtest.exe"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\freenect-camtest.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/CMakeFiles/freenect-camtest.dir/build: bin/freenect-camtest.exe

.PHONY : examples/CMakeFiles/freenect-camtest.dir/build

examples/CMakeFiles/freenect-camtest.dir/clean:
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples && $(CMAKE_COMMAND) -P CMakeFiles\freenect-camtest.dir\cmake_clean.cmake
.PHONY : examples/CMakeFiles/freenect-camtest.dir/clean

examples/CMakeFiles/freenect-camtest.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\examples D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\examples\CMakeFiles\freenect-camtest.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : examples/CMakeFiles/freenect-camtest.dir/depend
