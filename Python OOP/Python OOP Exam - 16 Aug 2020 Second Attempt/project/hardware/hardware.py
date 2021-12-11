from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def __repr__(self):
        express_length = len([s for s in self.software_components if s.__class__.__name__ == 'ExpressSoftware'])
        light_length = len([s for s in self.software_components if s.__class__.__name__ == 'LightSoftware'])

        if self.software_components:
            software_components_names = ", ".join([s.name for s in self.software_components])
        else:
            software_components_names = "None"

        result = [f"Hardware Component - {self.name}", f"Express Software Components: {express_length}",
                  f"Light Software Components: {light_length}",
                  f"Memory Usage: {self.memory_taken} / {self.memory}",
                  f"Capacity Usage: {self.capacity_taken} / {self.capacity}",
                  f"Type: {self.type}",
                  f"Software Components: {software_components_names}"]

        return "\n".join(result)

    def install(self, software: Software):
        if self.capacity_taken + software.capacity_consumption > self.capacity \
                or self.memory_taken + software.memory_consumption > self.memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    @property
    def capacity_taken(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def memory_taken(self):
        return sum([s.memory_consumption for s in self.software_components])
