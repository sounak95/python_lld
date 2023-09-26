'''
+-----------------------+         +-----------------------+
|  PaymentGatewayManager|         |     PaymentGateway   |
+-----------------------+         +-----------------------+
| - _instance: PaymentGatewayManager |                   |
| - _lock: Lock              |         |                   |
|                          |         |                   |
| + __new__(): PaymentGatewayManager |                   |
| + _initialize(): None     |         |                   |
| + process_payment(amount: float): None |                |
+-----------------------+         +-----------------------+

      |                           |
      |                           |
      |                           |
      |                          |
      |                            |
      |                            |

+-------------------------+   +---------------------------+
|        Main Program    |   |        Threading Module    |
+-------------------------+   +---------------------------+
|                         |   |                           |
| - payment_gateway: PaymentGatewayManager |              |
| - another_payment_gateway: PaymentGatewayManager |    |
|                         |   |                           |
|                         |   |                           |
| + main(): None          |   |                           |
|                         |   |                           |
+-------------------------+   +---------------------------+

This textual representation outlines the classes PaymentGatewayManager and PaymentGateway, along with their attributes and methods. It also includes the Main Program section, which interacts with these classes, and mentions the Threading Module used for thread safety.
'''

import threading

class PaymentGatewayManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(PaymentGatewayManager, cls).__new__(cls)
                    cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        print("Payment Gateway Manager initialized.")

    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through the payment gateway.")

if __name__ == "__main__":
    payment_gateway = PaymentGatewayManager()

    payment_gateway.process_payment(100.0)

    # Attempt to create another instance (should return the existing instance)
    another_payment_gateway = PaymentGatewayManager()

    # Check if both instances are the same.
    if payment_gateway is another_payment_gateway:
        print("Both instances are the same. Singleton pattern is working.")
    else:
        print("Singleton pattern is not working correctly.")
