#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    
    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello World!")
        self.create_timer(timer_period_sec=1.,
                          callback=self.timer_callback)
        
    def timer_callback(self):
        self.get_logger().info("Hello! Time: " + str(self.counter_))
        self.counter_+=1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()