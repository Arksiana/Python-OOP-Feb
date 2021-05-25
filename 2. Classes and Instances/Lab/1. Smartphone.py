class Smartphone:
    apps = []
    is_on = False

    def __init__(self, memory):
        self.memory = memory

    def power(self):
        if not Smartphone.is_on:
            Smartphone.is_on = True
            return Smartphone.is_on
        Smartphone.is_on = False

    def install(self, app, app_memory):
        if app_memory <= self.memory and Smartphone.is_on:
            Smartphone.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif app_memory <= self.memory and not Smartphone.is_on:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(Smartphone.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())

