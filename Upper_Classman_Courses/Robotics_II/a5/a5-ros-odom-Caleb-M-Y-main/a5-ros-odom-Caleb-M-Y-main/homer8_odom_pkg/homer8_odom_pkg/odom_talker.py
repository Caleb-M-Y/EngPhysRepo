import rclpy
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry

from tf_transformations import quaternion_from_euler
from math import sin, cos

from homer8_odom_pkg.homer_figure8 import Homer8Node


class OdomAnnouncerNode(Homer8Node):
    def __init__(self):
        super().__init__()
        ### START CODEING HERE ### ~3 lines
        # Init /odom publisher and tf broadcaster `odom` -> `base_link`
        self.odom_base_broadcaster = TransformBroadcaster(self)
        self.odom_publisher = self.create_publisher(
            topic="odom",
            msg_type=Odometry,
            qos_profile=1,
        )
        self.odom_talker_timer = self.create_timer(0.02, self.publish_odom)  # 50Hz
        ### END CODING HERE ###
        # Init variables
        self.x = 0.0  # in odom frame
        self.y = 0.0
        self.z = 0.033
        self.th = 0.0
        self.prev_ts = self.get_clock().now()
        self.curr_ts = self.get_clock().now()
        self.get_logger().info("Odometry is ready.")

    def announce_odometry(self):
        """Callback function for odom_talker_timer
        Totally 3 steps:
            1. Calculate pose change at every instance.
            2. Broadcast transformation: "odom" -> "base_link".
            3. Publish "/odom" topic.
        """

        ### START CODEING HERE ### ~30 lines

        # Calculate time and pose change
        self.curr_ts = self.get_clock().now()
        dt = (self.curr_ts - self.prev_ts).nanoseconds * 1e-9
        dx = self.lin_vel * cos(self.th) * dt
        dy = self.lin_vel * sin(self.th) * dt
        dth = self.ang_vel * dt
        self.x = dx
        self.y = dy
        self.th = dth
        quat = quaternion_from_euler(self.th, (0,0, 1))
        self.prev_ts = self.curr_ts  # update previous time stamp

        # Broadcast `odom` to `base_link` transformation
        odom_base_tf = TransformStamped()
        odom_base_tf.header.stamp = self.curr_ts.to_msg()
        odom_base_tf.header.frame_id = "odom"
        odom_base_tf.child_frame_id = "base_link"
        odom_base_tf.transform.translation.x = self.x
        odom_base_tf.transform.translation.y = self.y
        odom_base_tf.transform.translation.z = self.GROUND_CLEARANCE
        odom_base_tf.transform.rotation.x = quat[0]
        odom_base_tf.transform.rotation.y = quat[1]
        odom_base_tf.transform.rotation.z = quat[2]
        odom_base_tf.transform.rotation.w = quat[3]
        self.odom_base_broadcaster.sendTransform(odom_base_tf)  # broadcast tf

        # publish odom topic
        odom_msg = Odometry()
        odom_msg.header.stamp = self.curr_ts.to_msg()
        odom_msg.header.frame_id = "odom"
        odom_msg.child_frame_id = "base_link"
        odom_msg.pose.pose.position.x = self.x
        odom_msg.pose.pose.position.y = self.y
        odom_msg.pose.pose.position.z = self.GROUND_CLEARANCE
        odom_msg.pose.pose.orientation.x = quat[0]
        odom_msg.pose.pose.orientation.y = quat[1]
        odom_msg.pose.pose.orientation.z = quat[2]
        odom_msg.pose.pose.orientation.w = quat[3]
        odom_msg.twist.twist.linear.x = self.real_lin_vel
        odom_msg.twist.twist.angular.z = self.real_ang_vel
        self.odom_publisher.publish(odom_msg)  # publish "/odom" topic
        ### END CODING HERE ###


def main():
    rclpy.init()
    odom_node = OdomAnnouncerNode()
    rclpy.spin(odom_node)
    odom_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
