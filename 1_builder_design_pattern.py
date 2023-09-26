'''
+---------------------+        +------------------+
|      Desktop        |        |  DesktopBuilder  |
+---------------------+        +------------------+
| - motherboard: str |        |                  |
| - processor: str    |        |                  |
| - memory: str       |        |                  |
| - storage: str      |        |                  |
| - graphics_card: str|        |                  |
+---------------------+        |                  |
| + display(): None  |        |                  |
| + get_motherboard(): str |  |                  |
| + set_motherboard(motherboard: str): None |    |
| + get_processor(): str |     |                  |
| + set_processor(processor: str): None |       |
| + get_memory(): str |         |                  |
| + set_memory(memory: str): None |              |
| + get_storage(): str |        |                  |
| + set_storage(storage: str): None |            |
| + get_graphics_card(): str |  |                  |
| + set_graphics_card(graphics_card: str): None | |
+---------------------+        +------------------+
         |                               |
         |                               |
         |                               |
         |            +------------------+|
         |            | DellDesktopBuilder||
         |            +------------------+|
         |            |                  ||
         |            | + build_motherboard(): None |
         |            | + build_processor(): None  |
         |            | + build_memory(): None     |
         |            | + build_storage(): None    |
         |            | + build_graphics_card(): None |
         |            |                      ||
         |            +----------------------+
         |
         |            +----------------------+
         |            | HpDesktopBuilder   |
         |            +----------------------+
         |            |                  |
         |            | + build_motherboard(): None |
         |            | + build_processor(): None  |
         |            | + build_memory(): None     |
         |            | + build_storage(): None    |
         |            | + build_graphics_card(): None |
         |            |                      |
         |
         |            +----------------------+
         |            | DesktopDirector   |
         |            +----------------------+
         |            |                  |
         |            | + build_desktop(builder: DesktopBuilder): Desktop |
         |            |                  |
         |
         |            +-----------------------+
         |            | DesktopBuilderDemo    |
         |            +-----------------------+
         |            |                       |
         |            | main(args: list): None |
         |            |                       |
         +-----------------------------------+

'''
class Desktop:
    def __init__(self):
        self.motherboard = ""
        self.processor = ""
        self.memory = ""
        self.storage = ""
        self.graphics_card = ""

    def display(self):
        print("Desktop Specs:")
        print("Motherboard:", self.motherboard)
        print("Processor:", self.processor)
        print("Memory:", self.memory)
        print("Storage:", self.storage)
        print("Graphics Card:", self.graphics_card)

    def get_motherboard(self):
        return self.motherboard

    def set_motherboard(self, motherboard):
        self.motherboard = motherboard

    def get_processor(self):
        return self.processor

    def set_processor(self, processor):
        self.processor = processor

    def get_memory(self):
        return self.memory

    def set_memory(self, memory):
        self.memory = memory

    def get_storage(self):
        return self.storage

    def set_storage(self, storage):
        self.storage = storage

    def get_graphics_card(self):
        return self.graphics_card

    def set_graphics_card(self, graphics_card):
        self.graphics_card = graphics_card


class DesktopBuilder:
    def __init__(self):
        self.desktop = Desktop()

    def build_motherboard(self):
        pass

    def build_processor(self):
        pass

    def build_memory(self):
        pass

    def build_storage(self):
        pass

    def build_graphics_card(self):
        pass

    def get_desktop(self):
        return self.desktop


class DellDesktopBuilder(DesktopBuilder):
    def build_motherboard(self):
        self.desktop.set_motherboard("Dell Motherboard")

    def build_processor(self):
        self.desktop.set_processor("Dell Processor")

    def build_memory(self):
        self.desktop.set_memory("32GB DDR4 RAM")

    def build_storage(self):
        self.desktop.set_storage("1TB SSD + 2TB HDD")

    def build_graphics_card(self):
        self.desktop.set_graphics_card("NVIDIA RTX 3080")


class HpDesktopBuilder(DesktopBuilder):
    def build_motherboard(self):
        self.desktop.set_motherboard("HP Motherboard")

    def build_processor(self):
        self.desktop.set_processor("Intel Core i5")

    def build_memory(self):
        self.desktop.set_memory("16GB DDR4 RAM")

    def build_storage(self):
        self.desktop.set_storage("512GB SSD")

    def build_graphics_card(self):
        self.desktop.set_graphics_card("Integrated Graphics")


class DesktopDirector:
    def build_desktop(self, builder):
        builder.build_motherboard()
        builder.build_processor()
        builder.build_memory()
        builder.build_storage()
        builder.build_graphics_card()
        return builder.get_desktop()


if __name__ == "__main__":
    director = DesktopDirector()

    dell_builder = DellDesktopBuilder()
    dell_desktop = director.build_desktop(dell_builder)

    hp_builder = HpDesktopBuilder()
    hp_desktop = director.build_desktop(hp_builder)

    dell_desktop.display()
    hp_desktop.display()
