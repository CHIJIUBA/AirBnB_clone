#!/usr/bin/python3
"""
The console for AirBnb project
Contains the entry point of the command interpreter
"""
from ast import arg
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    custom console class
    """

    prompt = '(hbnb) '

    classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

    def do_quit(self, line):
        """Handles the 'quit' command

        Args:
            line(args): input argument for quiting
            the terminal

        """
        return True

    def help_quit(self):
        """
        Help instructions for the quit command
        """
        print('Quit command to exit the program\n')

    def do_EOF(self, line):
        """Quits command interpreter with ctrl+d

         Args:
            line(args): input argument for quiting
            the terminal

        """
        return True

    def emptyline(self):
        """
        Eliminates empty lines
        """
        pass

    def do_show(self, line):
        """Prints a string representation of an instance.

        Args:
            line(line): to enter with command <class name> <id>
            Example: 'show User 1234-1234-1234'

        """
        args = line.split(" ")
        if not line:
            print('** class name missing **')
            return False
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        elif len(args) != 2:
            print("** instance id missing **")
            return False

        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if obj_id == args[0]+'.'+args[1]:
                obj = all_objs[obj_id]
                print(obj)
                return False
        print('** no instance found **')

    def do_create(self, line):
        """Creates a new instance of @cls_name class,
        and prints the new instance's ID.

        Args:
            line(args): Arguments to enter with command: <class name>
            Example: 'create User'

        """
        args = line.split(" ")
        if not line:
            print('** class name missing **')
            return False
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        """
        args[0] contains class name, create new instance
        of that class updates 'updated_at' attribute,
        and saves into JSON file
        """
        obj = eval(args[0])()
        obj.save()
        print(obj.id)

    def do_destroy(self, line):
        """Prints a string representation of an instance.

        Args:
            line(line): to enter with command <class name> <id>
            Example: 'show User 1234-1234-1234'

        """
        args = line.split(" ")
        if not line:
            print('** class name missing **')
            return False
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False

        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if obj_id == args[0]+'.'+args[1]:
                storage.all().pop(obj_id)
                storage.save()
                return False
        print('** no instance found **')

    def do_all(self, line):
        """Prints a string representation of all instance.

        Args:
            line(line): to enter with command <class name> <id>
            Example: 'all BaseModel 1234-1234-1234'

        """
        args = line.split(" ")
        if not line:
            print('** class name missing **')
            return False
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return False

        all_objs = storage.all()
        lis = []
        for obj_id in all_objs.keys():
            sp = obj_id.split('.')
            if args[0] in sp:
                lis.append(str(all_objs[obj_id]))
        print(lis)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating an attribute

        Args:
            line(args): receives the commands:
            <class name> <id> <attribute name> "<attribute value>"
            Example: 'update User 1234-1234-1234 my_name "Bob"'

        """
        args = line.split(" ")
        if not line:
            print('** class name missing **')
            return False
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        elif len(args) < 3:
            print('** attribute name missing **')
            return False
        elif len(args) < 4:
            print('** value missing **')
            return False

        all_objs = storage.all()
        attr_k = args[2]
        attr_v = args[3]
        sp = attr_v.split('"')
        try:
            if attr_v.isdigit():
                attr_v = int(attr_v)
            elif float(attr_v):
                attr_v = float(attr_v)
        except ValueError:
            pass
        if isinstance(attr_v, str):
            if len(sp) < 2:
                return False
            for obj_id in all_objs.keys():
                if obj_id == args[0]+'.'+args[1]:
                    setattr(all_objs[obj_id], attr_k, sp[1])
                    storage.save()
                    return False
        if isinstance(attr_v, int) or isinstance(attr_v, float):
            for obj_id in all_objs.keys():
                if obj_id == args[0]+'.'+args[1]:
                    setattr(all_objs[obj_id], attr_k, attr_v)
                    storage.save()
                    return False
        print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
