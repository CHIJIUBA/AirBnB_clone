#!/usr/bin/python3
"""
The console for AirBnb project
Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    custom console class
    """

    prompt = '(hbnb) '

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
        elif args[0] != "BaseModel":
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
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif  len(args) != 2:
            print("** instance id missing **")
            return False
        
        args = line.split()
        d = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        print(d[key])
            

if __name__ == '__main__':
    cli = HBNBCommand()
    cli.cmdloop()
