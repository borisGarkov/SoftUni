from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        filtered_hardware = [h for h in System._hardware if h.name == hardware_name]
        if not filtered_hardware:
            return "Hardware does not exist"
        current_hardware = filtered_hardware[0]
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            current_hardware.install(express_software)
            System._software.append(express_software)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        filtered_hardware = [h for h in System._hardware if h.name == hardware_name]
        if not filtered_hardware:
            return "Hardware does not exist"
        current_hardware = filtered_hardware[0]
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            current_hardware.install(light_software)
            System._software.append(light_software)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        filtered_hardware = [h for h in System._hardware if h.name == hardware_name]
        filtered_software = [s for s in System._software if s.name == software_name]

        if not filtered_hardware and not filtered_software:
            return "Some of the components do not exist"
        current_hardware = filtered_hardware[0]
        current_software = filtered_software[0]
        current_hardware.uninstall(current_software)
        System._software.remove(current_software)

    @staticmethod
    def analyze():
        total_memory = sum([h.memory for h in System._hardware])
        total_used_memory = sum([sum([s.memory_consumption for s in h.software_components]) for h in System._hardware])

        total_capacity = sum([h.capacity for h in System._hardware])
        total_used_space = sum([sum([s.capacity_consumption for s in h.software_components]) for h in System._hardware])

        result = f"System Analysis\n" \
                 f"Hardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
                 f"Total Capacity Taken: {total_used_space} / {total_capacity}"
        return result

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            express_software_count = len(
                [s for s in h.software_components if s.__class__.__name__ == "ExpressSoftware"])
            light_software_count = len([s for s in h.software_components if s.__class__.__name__ == "LightSoftware"])
            total_memory_hardware = h.memory
            total_memory_used = sum([s.memory_consumption for s in h.software_components])
            total_capacity_hardware = h.capacity
            total_capacity_used = sum([s.capacity_consumption for s in h.software_components])
            type_hardware = h.type
            if not h.software_components:
                software_components = "None"
            else:
                software_components = ", ".join([s.name for s in h.software_components])

            result += f"Hardware Component - {h.name}\n" \
                      f"Express Software Components: {express_software_count}\n" \
                      f"Light Software Components: {light_software_count}\n" \
                      f"Memory Usage: {total_memory_used} / {total_memory_hardware}\n" \
                      f"Capacity Usage: {total_capacity_used} / {total_capacity_hardware}\n" \
                      f"Type: {type_hardware}\n" \
                      f"Software Components: {software_components}"

        return result
