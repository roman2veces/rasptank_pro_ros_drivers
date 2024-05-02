FROM ros:foxy

RUN sudo apt update 
RUN sudo apt install -y ros-foxy-teleop-twist-keyboard

# Install our source code 
RUN mkdir -p /home/romantwice/rasptank_pro_ws/src/
WORKDIR /home/romantwice/rasptank_pro_ws/src/
RUN git clone https://github.com/roman2veces/rasptank_pro_ros_drivers.git

WORKDIR /home/romantwice/rasptank_pro_ws/
RUN . /opt/ros/foxy/setup.sh && colcon build
