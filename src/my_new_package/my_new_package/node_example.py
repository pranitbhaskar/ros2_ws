import rclpy
from rclpy.node import Node 

class CustomNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.timer=self.create_timer(
            1.0,
            self.timer_callback
        )
        self.get_logger().info("Node Started!")

    def timer_callback(self):
        self.get_logger().info("Hello from ros2!")

def main(args=None):
    rclpy.init(args=args)
    node=CustomNode("example_node_name")
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()
