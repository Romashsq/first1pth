import json
import os 


FILE_NAME = "devices.json"

class SmartDevice:
    def __init__(self, id, name, process, is_on, access):
        self.id = id
        self.name = name
        self.process = process
        self.is_on = is_on
        self.__access = access
    @classmethod
    def get_new_device(cls):
        print('=== ADD NEW DEVICE ===')
        input_id = input('Enter ID:').strip()
        input_name = input('Enter Name:').strip()
        input_process = input('Enter Process:').strip()
        input_is_on = input('Enter on/off - yes/no:').strip().lower == 'yes'
        input_access = input('Enter password access:').strip()

        new_device = cls(
            id =  input_id,
            name = input_name,
            process = input_process,
            is_on  = input_is_on,
            access = input_access,
        )
        cls.w_json(new_device)
        return new_device

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "process": self.process,
            "is_on": self.is_on,
            "access": self.__access
        }
    
    @classmethod
    def r_json(cls):
        if os.path.exists(FILE_NAME):
            try:
                with open(FILE_NAME, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(data)
                    return data
            except json.JSONDecodeError:
                print('Not json')
        else:
            print('Wrong path')

    def w_json(cls, new_device):
        if os.path.exists(FILE_NAME):
            new_device_dict = new_device.to_dict()
            data = cls.r_json()
            data['Devices']
            with open(FILE_NAME, 'w', encoding='utf-8'):
                new_device_dict = new_device.to_dict()
                

