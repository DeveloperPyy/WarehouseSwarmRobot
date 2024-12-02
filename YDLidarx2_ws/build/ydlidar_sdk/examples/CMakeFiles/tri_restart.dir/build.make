# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/src/YDLidar-SDK"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk"

# Include any dependencies generated for this target.
include examples/CMakeFiles/tri_restart.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include examples/CMakeFiles/tri_restart.dir/compiler_depend.make

# Include the progress variables for this target.
include examples/CMakeFiles/tri_restart.dir/progress.make

# Include the compile flags for this target's objects.
include examples/CMakeFiles/tri_restart.dir/flags.make

examples/CMakeFiles/tri_restart.dir/tri_restart.cpp.o: examples/CMakeFiles/tri_restart.dir/flags.make
examples/CMakeFiles/tri_restart.dir/tri_restart.cpp.o: /home/shashank/ROS2\ Projects/Major\ Project/YDLidarx2_ws/src/YDLidar-SDK/examples/tri_restart.cpp
examples/CMakeFiles/tri_restart.dir/tri_restart.cpp.o: examples/CMakeFiles/tri_restart.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/CMakeFiles/tri_restart.dir/tri_restart.cpp.o"
	cd "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/examples" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT examples/CMakeFiles/tri_restart.dir/tri_restart.cpp.o -MF CMakeFiles/tri_restart.dir/tri_restart.cpp.o.d -o CMakeFiles/tri_restart.dir/tri_restart.cpp.o -c "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/src/YDLidar-SDK/examples/tri_restart.cpp"

examples/CMakeFiles/tri_restart.dir/tri_restart.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tri_restart.dir/tri_restart.cpp.i"
	cd "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/examples" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/src/YDLidar-SDK/examples/tri_restart.cpp" > CMakeFiles/tri_restart.dir/tri_restart.cpp.i

examples/CMakeFiles/tri_restart.dir/tri_restart.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tri_restart.dir/tri_restart.cpp.s"
	cd "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/examples" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/src/YDLidar-SDK/examples/tri_restart.cpp" -o CMakeFiles/tri_restart.dir/tri_restart.cpp.s

# Object files for target tri_restart
tri_restart_OBJECTS = \
"CMakeFiles/tri_restart.dir/tri_restart.cpp.o"

# External object files for target tri_restart
tri_restart_EXTERNAL_OBJECTS =

tri_restart: examples/CMakeFiles/tri_restart.dir/tri_restart.cpp.o
tri_restart: examples/CMakeFiles/tri_restart.dir/build.make
tri_restart: libydlidar_sdk.a
tri_restart: examples/CMakeFiles/tri_restart.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../tri_restart"
	cd "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/examples" && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tri_restart.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/CMakeFiles/tri_restart.dir/build: tri_restart
.PHONY : examples/CMakeFiles/tri_restart.dir/build

examples/CMakeFiles/tri_restart.dir/clean:
	cd "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/examples" && $(CMAKE_COMMAND) -P CMakeFiles/tri_restart.dir/cmake_clean.cmake
.PHONY : examples/CMakeFiles/tri_restart.dir/clean

examples/CMakeFiles/tri_restart.dir/depend:
	cd "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/src/YDLidar-SDK" "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/src/YDLidar-SDK/examples" "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk" "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/examples" "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/examples/CMakeFiles/tri_restart.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : examples/CMakeFiles/tri_restart.dir/depend

