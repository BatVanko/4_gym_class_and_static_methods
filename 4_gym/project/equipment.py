class Equipment:
    equipment_id = 1

    def __init__(self, name: str):
        self.id = self.get_next_id()
        self.name = name


    @staticmethod
    def get_next_id():
        result = Equipment.equipment_id
        Equipment.equipment_id += 1
        return result

    def __repr__(self):

        return f"Equipment <{self.id}> {self.name}"







