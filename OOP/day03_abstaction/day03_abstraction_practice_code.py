from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Lamp(Appliance):
    def turn_on(self):
        print("Lamp is glowing")

    def turn_off(self):
        print("Lamp is off")

class Fan(Appliance):
    def turn_on(self):
        print("Fan is spinning")

    def turn_off(self):
        print("Fan stopped")

lamp = Lamp()
lamp.turn_on()
lamp.turn_off()

fan = Fan()
fan.turn_on()
fan.turn_off()


from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} using PayPal.")

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} using Stripe.")

def checkout(processor: PaymentProcessor, amount: float):
    processor.process_payment(amount)

paypal = PayPalProcessor()
stripe = StripeProcessor()

checkout(paypal, 100)
checkout(stripe, 200)


from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[Console] {message}")

class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a") as file:
            file.write(f"[File] {message}\n")

class RemoteLogger(Logger):
    def log(self, message):
        print(f"[Remote] Sending log: {message}")

class LogManager:
    def __init__(self, logger: Logger):
        self.logger = logger

    def do_log(self, message):
        self.logger.log(message)

# Example usage
console_log = LogManager(ConsoleLogger())
file_log = LogManager(FileLogger())
remote_log = LogManager(RemoteLogger())

console_log.do_log("User signed in")
file_log.do_log("File uploaded")
remote_log.do_log("Error sent to server")


class Engine(ABC):
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def re_charge(self):
        pass
    
class Motorbik(Engine):
    def run(self):
        print("Vilocity max is 250 km/h")
        
    def re_charge(self):
        print("Maximum 25 galons")
        
class Car(Engine):
    def run(self):
        print("Volocity max is 350km")
        
    def re_charge(self):
        print("Maximum 35 galons")
        
class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def change_channel(self, channel: int):
        pass
    
class SamsungRemote(RemoteControl):
    def turn_on(self):
        print("Samsun TV is now On.")
        
    def turn_off(self):
        print("Samsun TV is now off.")
        
    def change_channel(self, channel: int):
        print(f"Samsung TV changed to channel {channel}.")
        

class SonyRemote(RemoteControl):
    def turn_on(self):
        print("Sony TV is powering up.")
        
    def turn_off(self):
        print("Sony TV is now shutting down.")
        
    def change_channel(self, channel: int):
        print(f"Sony TV switched to channel {channel}.")
        
class User:
    def __init__(self, remote: RemoteControl):
        self.remote = remote
        
    def watch_tv(self):
        self.remote.turn_on()
        self.remote.change_channel(5)
        self.remote.turn_off()
        
samsung = SamsungRemote()
sony = SonyRemote()

user1 = User(samsung)
user2 = User(sony)

print("=== User with Samsum ===")
user1.watch_tv()

print("\n=== User with Sony ===")
user2.watch_tv()