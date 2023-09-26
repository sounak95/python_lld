'''
+---------------------+        +------------------+
|      Desktop        |        |   DesktopBuilder |
+---------------------+        +------------------+
| - motherboard: str |        |                |
| - processor: str    |        |                |
| - memory: str       |        |                |
| - storage: str      |        |                |
| - graphics_card: str|        |                |
+---------------------+        |                |
| + display(): None  |        |                |
+---------------------+        |                |
                               |                |
+----------------------+        |                |
|    DesktopBuilder    |        |                |
+----------------------+        |                |
| - desktop: Desktop  |<>------|                |
+----------------------+        |                |
| + build_motherboard(): None |                |
| + build_processor(): None   |                |
| + build_memory(): None      |                |
| + build_storage(): None     |                |
| + build_graphics_card(): None|                |
| + get_desktop(): Desktop   |                |
+----------------------+        +------------------+
         |                                      |
         |                                      |
         |                                      |
         |            +------------------+      |
         |            | DellDesktopBuilder|      |
         |            +------------------+      |
         |            |                  |      |
         |            | + build_motherboard(): None |    |
         |            | + build_processor(): None  |    |
         |            | + build_memory(): None     |    |
         |            | + build_storage(): None    |    |
         |            | + build_graphics_card(): None |  |
         |            |                      |         |
         |            +----------------------+         |
         |                                          |
         |                                          |
         |            +----------------------+        |
         |            | HpDesktopBuilder   |          |
         |            +----------------------+        |
         |            |                  |            |
         |            | + build_motherboard(): None |  |
         |            | + build_processor(): None  |  |
         |            | + build_memory(): None     |  |
         |            | + build_storage(): None    |  |
         |            | + build_graphics_card(): None | |
         |            |                      |        |
         |            +----------------------+        |
         |                                          |
         |                                          |
         |            +----------------------+        |
         |            | DesktopDirector   |          |
         |            +----------------------+        |
         |            |                  |            |
         |            | + build_desktop(builder: DesktopBuilder): Desktop |
         |            |                  |            |
         |            +------------------+            |
         |                                          |
         |                                          |
         |            +-----------------------+      |
         |            | DesktopBuilderDemo    |       |
         |            +-----------------------+      |
         |            |                       |      |
         |            | main(args: list): None |     |
         |            |                       |      |
         |            +-----------------------+      |
         +------------------------------------------+
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
        self.desktop.motherboard = "Dell Motherboard"

    def build_processor(self):
        self.desktop.processor = "Dell Processor"

    def build_memory(self):
        self.desktop.memory = "32GB DDR4 RAM"

    def build_storage(self):
        self.desktop.storage = "1TB SSD + 2TB HDD"

    def build_graphics_card(self):
        self.desktop.graphics_card = "NVIDIA RTX 3080"


class HpDesktopBuilder(DesktopBuilder):
    def build_motherboard(self):
        self.desktop.motherboard = "HP Motherboard"

    def build_processor(self):
        self.desktop.processor = "Intel Core i5"

    def build_memory(self):
        self.desktop.memory = "16GB DDR4 RAM"

    def build_storage(self):
        self.desktop.storage = "512GB SSD"

    def build_graphics_card(self):
        self.desktop.graphics_card = "Integrated Graphics"


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
