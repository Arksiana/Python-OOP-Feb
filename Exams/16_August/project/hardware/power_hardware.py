from project.hardware.hardware import Hardware
# from project.software.software import Software


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, 'Power', int(capacity * 0.25), int(memory + memory * 0.75))
