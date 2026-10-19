import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddServiceClient(Node):
	def __init__(self):
		super().__init__('add_service_client')
		self.client=self.create_client(AddTwoInts,'add_two_numbers')
		while not self.client.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('waiting for service ...')
	
	def send_request(self,a,b):
		request=AddTwoInts.Request()
		request.a=a
		request.b=b
		return self.client.call_async(request)

def main(args=None):
	rclpy.init(args=args)
	node=AddServiceClient()
	future=node.send_request(15,25)
	try:
		rclpy.spin_until_future_complete(node,future)
		if future.result is not None:
			node.get_logger().info(f'Result: {future.result().sum}')
		else:
			node.get_logger().error('Service call failed')
	except KeyboardInterrupt:
		pass
	finally:
		node.destroy_node()
		if rclpy.ok():
			rclpy.shutdown()

if __name__=='__main__':
	main()
