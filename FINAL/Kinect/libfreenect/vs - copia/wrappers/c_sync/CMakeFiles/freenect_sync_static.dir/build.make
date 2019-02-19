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
include wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/depend.make

# Include the progress variables for this target.
include wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/progress.make

# Include the compile flags for this target's objects.
include wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/flags.make

wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/libfreenect_sync.c.obj: wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/flags.make
wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/libfreenect_sync.c.obj: wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/includes_C.rsp
wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/libfreenect_sync.c.obj: ../wrappers/c_sync/libfreenect_sync.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/libfreenect_sync.c.obj"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\c_sync && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\freenect_sync_static.dir\libfreenect_sync.c.obj   -c D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\wrappers\c_sync\libfreenect_sync.c

wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/libfreenect_sync.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/freenect_sync_static.dir/libfreenect_sync.c.i"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\c_sync && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\wrappers\c_sync\libfreenect_sync.c > CMakeFiles\freenect_sync_static.dir\libfreenect_sync.c.i

wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/libfreenect_sync.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/freenect_sync_static.dir/libfreenect_sync.c.s"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\c_sync && C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\wrappers\c_sync\libfreenect_sync.c -o CMakeFiles\freenect_sync_static.dir\libfreenect_sync.c.s

# Object files for target freenect_sync_static
freenect_sync_static_OBJECTS = \
"CMakeFiles/freenect_sync_static.dir/libfreenect_sync.c.obj"

# External object files for target freenect_sync_static
freenect_sync_static_EXTERNAL_OBJECTS =

lib/libfreenect_sync.a: wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/libfreenect_sync.c.obj
lib/libfreenect_sync.a: wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/build.make
lib/libfreenect_sync.a: wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C static library ..\..\lib\libfreenect_sync.a"
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\c_sync && $(CMAKE_COMMAND) -P CMakeFiles\freenect_sync_static.dir\cmake_clean_target.cmake
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\c_sync && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\freenect_sync_static.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/build: lib/libfreenect_sync.a

.PHONY : wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/build

wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/clean:
	cd /d D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\c_sync && $(CMAKE_COMMAND) -P CMakeFiles\freenect_sync_static.dir\cmake_clean.cmake
.PHONY : wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/clean

wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\wrappers\c_sync D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\c_sync D:\Jhonatan\Documentos\AI\Vision\FINAL\Kinect\libfreenect\vs\wrappers\c_sync\CMakeFiles\freenect_sync_static.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : wrappers/c_sync/CMakeFiles/freenect_sync_static.dir/depend
