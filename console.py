#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""
import cmd


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
    
if __name__ == '__main__':
    cli = HBNBCommand()
    cli.cmdloop()
    