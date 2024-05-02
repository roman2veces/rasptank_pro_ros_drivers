from rasptank_pro_ros_drivers.move_test import moveTest

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class RasptankProControl(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    print('Hi from rasptank_pro_ros_drivers.')
    moveTest()

    rclpy.init(args=args)

    control_node = RasptankProControl()

    rclpy.spin(control_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()