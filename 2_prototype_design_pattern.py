'''
+-------------------+         +----------------+
|   NetworkDevice  |         |     Router     |
+-------------------+         +----------------+
| <<abstract>>      |         | - name: str    |
| - name: str       |         | - ip: str      |
+-------------------+         | - securityPolicy: str |
| + clone(): NetworkDevice | | + Router(name: str, ip: str, securityPolicy: str) |
| + display(): None |         | + clone(): NetworkDevice |
| + update(new_name: str): None| + display(): None |
+-------------------+         | + update(new_name: str): None |
                             +----------------+
                             |
                             |
+-------------------+         +----------------+
|     Switch        |         |    RouterDemo   |
+-------------------+         +----------------+
| - protocol: str   |
+-------------------+
| + clone(): NetworkDevice |
| + display(): None |
| + update(new_name: str): None |
+-------------------+


'''
from abc import ABC, abstractmethod

class NetworkDevice(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def update(self, new_name):
        pass

class Router(NetworkDevice):
    def __init__(self, name, ip, security_policy):
        self.name = name
        self.ip = ip
        self.security_policy = security_policy

    def clone(self):
        return Router(self.name, self.ip, self.security_policy)

    def display(self):
        print(f"Router - Name: {self.name}, IP: {self.ip}, Security Policy: {self.security_policy}")

    def update(self, new_name):
        self.name = new_name

class Switch(NetworkDevice):
    def __init__(self, name, protocol):
        self.name = name
        self.protocol = protocol

    def clone(self):
        return Switch(self.name, self.protocol)

    def display(self):
        print(f"Switch - Name: {self.name}, Protocol: {self.protocol}")

    def update(self, new_name):
        self.name = new_name

if __name__ == "__main__":
    # Create prototype instances of a router and a switch
    router_prototype = Router("Router A", "192.168.1.1", "Firewall Enabled")
    switch_prototype = Switch("Switch X", "Ethernet")

    # Clone and display router and switch devices
    router_clone = router_prototype.clone()
    switch_clone = switch_prototype.clone()

    print("Router Clone:")
    router_clone.display()

    print("\nSwitch Clone:")
    switch_clone.display()

    # Update the names of the clones
    router_clone.update("Router B")
    switch_clone.update("Switch Y")

    print("\nUpdated Router Clone:")
    router_clone.display()

    print("\nUpdated Switch Clone:")
    switch_clone.display()
