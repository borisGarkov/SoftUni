from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        filtered_hardware = [h for h in System._hardware if h.name == hardware_name]
        if not filtered_hardware:
            return "Hardware does not exist"
        try:
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            filtered_hardware[0].install(software)
            System._software.append(software)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        filtered_hardware = [h for h in System._hardware if h.name == hardware_name]
        if not filtered_hardware:
            return "Hardware does not exist"
        try:
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            filtered_hardware[0].install(software)
            System._software.append(software)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            filtered_hardware = [h for h in System._hardware if h.name == hardware_name][0]
            filtered_software = [s for s in System._software if s.name == software_name][0]
            filtered_hardware.uninstall(filtered_software)
            System._software.remove(filtered_software)
        except:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_used_memory = sum([h.memory_taken for h in System._hardware])
        total_memory = sum([h.memory for h in System._hardware])
        total_used_capacity = sum([h.capacity_taken for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])
        result = ["System Analysis", f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}",
                  f"Total Operational Memory: {total_used_memory} / {total_memory}",
                  f"Total Capacity Taken: {total_used_capacity} / {total_capacity}"]
        return "\n".join(result)

    @staticmethod
    def system_split():
        return "\n".join([h.__repr__() for h in System._hardware])
