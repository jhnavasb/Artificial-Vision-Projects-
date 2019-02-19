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
include wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/depend.make

# Include the progress variables for this target.
include wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/progress.make

# Include the compile flags for this target's objects.
include wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/flags.make

wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/cpp_pc_view.cpp.obj: wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/flags.make
wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/cpp_pc_view.cpp.obj: wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/includes_CXX.rsp
wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/cpp_pc_view.cpp.obj: ../wrappers/cpp/cpp_pc_view.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/cpp_pc_view.cpp.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\cpp && C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\freenect-cpp_pcview.dir\cpp_pc_view.cpp.obj -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\wrappers\cpp\cpp_pc_view.cpp

wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/cpp_pc_view.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/freenect-cpp_pcview.dir/cpp_pc_view.cpp.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\cpp && C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\wrappers\cpp\cpp_pc_view.cpp > CMakeFiles\freenect-cpp_pcview.dir\cpp_pc_view.cpp.i

wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/cpp_pc_view.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/freenect-cpp_pcview.dir/cpp_pc_view.cpp.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\cpp && C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\wrappers\cpp\cpp_pc_view.cpp -o CMakeFiles\freenect-cpp_pcview.dir\cpp_pc_view.cpp.s

# Object files for target freenect-cpp_pcview
freenect__cpp_pcview_OBJECTS = \
"CMakeFiles/freenect-cpp_pcview.dir/cpp_pc_view.cpp.obj"

# External object files for target freenect-cpp_pcview
freenect__cpp_pcview_EXTERNAL_OBJECTS =

bin/freenect-cpp_pcview.exe: wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/cpp_pc_view.cpp.obj
bin/freenect-cpp_pcview.exe: wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/build.make
bin/freenect-cpp_pcview.exe: lib/libfreenect.dll.a
bin/freenect-cpp_pcview.exe: D:/Jhonatan/Documentos/DriverPackages/glut-3.7.6-bin/glut32.lib
bin/freenect-cpp_pcview.exe: D:/Jhonatan/Documentos/DriverPackages/Pre-built.2/lib/libpthreadGC2.a
bin/freenect-cpp_pcview.exe: D:/Jhonatan/Documentos/DriverPackages/libusb-win32-bin-1.2.6.0/lib/gcc/libusb.a
bin/freenect-cpp_pcview.exe: wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/linklibs.rsp
bin/freenect-cpp_pcview.exe: wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/objects1.rsp
bin/freenect-cpp_pcview.exe: wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ..\..\bin\freenect-cpp_pcview.exe"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\cpp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\freenect-cpp_pcview.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/build: bin/freenect-cpp_pcview.exe

.PHONY : wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/build

wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/clean:
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\cpp && $(CMAKE_COMMAND) -P CMakeFiles\freenect-cpp_pcview.dir\cmake_clean.cmake
.PHONY : wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/clean

wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\wrappers\cpp D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\cpp D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\cpp\CMakeFiles\freenect-cpp_pcview.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : wrappers/cpp/CMakeFiles/freenect-cpp_pcview.dir/depend

