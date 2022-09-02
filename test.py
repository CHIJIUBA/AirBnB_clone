# import json

# all_objs = {"BaseModel.f26e97b7-feef-40e8-9223-d92f0fd55657": {"id": "f26e97b7-feef-40e8-9223-d92f0fd55657", "created_at": "2022-09-01T20:28:23.517539", "updated_at": "2022-09-01T20:28:23.517539", "name": "My_First_Model", "my_number": 89, "__class__": "BaseModel"},
#             "BaseModel.f26e97b7-feef-40e8-9223-d92f0fd55655": {"id": "f26e97b7-feef-40e8-9223-d92f0fd55657", "created_at": "2022-09-01T20:28:23.517539", "updated_at": "2022-09-01T20:28:23.517539", "name": "My_First_Model", "my_number": 89, "__class__": "BaseModel"},
#             "BaseModel.f26e97b7-feef-40e8-9223-d92f0fd55656": {"id": "f26e97b7-feef-40e8-9223-d92f0fd55657", "created_at": "2022-09-01T20:28:23.517539", "updated_at": "2022-09-01T20:28:23.517539", "name": "My_First_Model", "my_number": 89, "__class__": "BaseModel"}}


# # for obj_id in all_objs.keys():
# #     obj = all_objs[obj_id]
# #     print(obj)

# if 'BaseModel.f26e97b7-feef-40e8-9223-d92f0fd55655' in all_objs:
#     print("[{}] ({}) {}".format('BaseModel', 'BaseModel.f26e97b7-feef-40e8-9223-d92f0fd55655', all_objs['BaseModel.f26e97b7-feef-40e8-9223-d92f0fd55655']))
# else:
#     print("not in this dictionary")

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for k, v in car.items():
    print("{} = {}".format(k, v))

x = car.keys()
print(x[0])