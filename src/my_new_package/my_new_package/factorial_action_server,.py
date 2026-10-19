import rclpy
from rclpy import Node
from rclpy.action import ActionServer
from my_new_interface.action import Factorial

class FactoriaActionServer(Node):
    def __init__(self,name):
        super().__init__(name)

        self.action_server=ActionServer(self, Factorial, 'factorial', self.execute_callback)

    def execute_callback(self, goal_handle):
        feedback = Factorial.Feedback()
        feedback.sequence_factorial_from_1_to_n=[1]

        for j in range(1, goal_handle.request.n):  



def main(args=None):
    rclpy.init(args=args)

    factorial_action_server = FactoriaActionServer('factorial_action_server_node')

    rclpy.spin(factorial_action_server)
    rclpy.shutdown()  


if __name__=='__main__':
    main()