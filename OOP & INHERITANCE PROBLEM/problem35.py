"""Traffic light class - simulate signal timing & controll flow privately."""
class Trafficlight:
    def __init__(self):
        self.__signal = "Red"
    def change_signal(self, signal):
        self.__signal = signal
    def display(self):
        print(f"Current signal : {self.__signal}")
obj = Trafficlight()
obj.display()
obj.change_signal("Green")
obj.display()