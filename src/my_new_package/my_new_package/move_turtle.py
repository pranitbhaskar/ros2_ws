import random

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim_msgs.srv import TeleportAbsolute
from functools import partial

class CustomTurtleOperator(Node):
    def __init__ (self,name):
        super().__init__(name)
        self.publisher=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_timer(1,callback=self.callback)

    def callback(self):
        message=Twist()

        message.linear.x=random.random()
        message.linear.y=random.random()
        message.linear.z=random.random()

        message.angular.x=random.random()
        message.angular.y=random.random()
        message.angular.z=random.random()
        # self.get_logger().info(message)
        self.publisher.publish(message)

    def call_set_teleport_service(self,x,y,theta):
        client =self.create_client(TeleportAbsolute,'/turtle1/teleport_absolute')
        request=TeleportAbsolute.Request()
        request.x=x
        request.y=y
        request.theta=theta

        future=client.call_async(request)
        future.add_done_callback(partial(self.callback_set_teleport))

def  main(args=None):
    rclpy.init(args=args)
    node=CustomTurtleOperator("example_node_name")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()