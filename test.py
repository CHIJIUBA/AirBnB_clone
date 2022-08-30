import uuid
import datetime
# # Printing random id using uuid4()
# today = datetime.datetime.now()
# today = datetime.datetime.isoformat(today)
# print(today)

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            if value == "Enugu":
                continue
            print("{} == {}".format(key, value))


if __name__ == "__main__":
    # dicto = {name = 'chijiuba', age:17, school:'UNN', state:'Enugu'}
    greet_me(name = 'chijiuba', age = 17, school = 'UNN', state = 'Enugu')