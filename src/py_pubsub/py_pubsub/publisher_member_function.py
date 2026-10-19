# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import rclpy 
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from std_msgs.msg import String
from rclpy.parameter import Parameter 
from rcl_interfaces.msg import SetParametersResult

class MinimalPublisher(Node):
	def __init__(self):
		super().__init__('minimal_publisher')
		self.declare_parameter('publish_period', 0.2)
		self.publisher_=self.create_publisher(String,'topic',10)
		period=self.get_parameter('publish_period').value
		self.timer=self.create_timer(float(period),self.timer_callback)
		self.i=0
		self.add_on_set_parameters_callback(self.parameter_callback)
	def parameter_callback(self,parameters):
		for parameter in parameters:
			if parameter.name=='publish_period':
				if parameter.type_!=Parameter.Type.DOUBLE:
					return SetParametersResult(successful=False,reason='publish_period must be a number')
				if parameter.value<=0.0:
					return SetParameterResult(successful=False,reason='publish_period must be greater than zero')
				self.timer.timer_period_ns=int(parameter.value*1_000_000_000)
				return SetParametersResult(successful=True)

	def timer_callback(self):
		msg=String()
		msg.data=f'Hello World: {self.i}'
		self.publisher_.publish(msg)
		self.get_logger().info(f'Publishing: "{msg.data}"')
		self.i+=1

def main(args=None):
	try:
		with rclpy.init(args=args):
			node=MinimalPublisher()
			rclpy.spin(node)
	except (KeyboardInterrupt,ExternalShutdownException):
		pass

if __name__=='__main__':
	main()
