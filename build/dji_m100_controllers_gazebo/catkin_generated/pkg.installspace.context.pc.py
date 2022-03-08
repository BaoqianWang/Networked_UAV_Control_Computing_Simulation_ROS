# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;std_msgs;sensor_msgs;visualization_msgs;gazebo_ros;gazebo_ros_control;hector_quadrotor_interface;hector_quadrotor_controllers".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-ldji_m100_controller_gazebo_sitl".split(';') if "-ldji_m100_controller_gazebo_sitl" != "" else []
PROJECT_NAME = "dji_m100_controllers_gazebo"
PROJECT_SPACE_DIR = "/home/smile/nac_sim/install"
PROJECT_VERSION = "0.3.5"
