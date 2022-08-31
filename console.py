#!/usr/bin/python3
"""Module for the console"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Creates a console HBNB"""
    prompt = '(hbnb)'

    def quit(self, line):
        """Quit command to exit the program"""
        return True
    def eof(self, line):
        """EOF command to exit the program"""
        return True
    def emptyline(self):
        """Handle empty line when is passed as an argument"""
        pass
if __name__ == '__main__':
            HBNBCommand().cmdloop()

