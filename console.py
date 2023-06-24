#!/usr/bin/python3
"""This module defines the entry point of the command interpreter."""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter class."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handles the EOF signal to exit the program."""
        print()
        return True

    def emptyline(self):
        """Handles empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class.
        Usage: create <class name>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        Usage: show <class name> <instance id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all().keys():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        Usage: destroy <class name> <instance id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all().keys():
            storage.all().pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances.
        Usage: all [<class name>]
        """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_list = list(storage.all().values())
        elif args[0] in storage.classes.keys():
            obj_list = [obj for obj in storage.all().values()
                        if type(obj).__name__ == args[0]]
        else:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in obj_list])

    def do_update(self, arg):
        """Updates an instance based on the class name and id.
        Usage: update <class name> <instance id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = storage.all()[key]
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_count(self, arg):
        """Retrieves the count of instances of a class.
        Usage: count <class name>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        obj_list = [obj for obj in storage.all().values() if type(obj).__name__ == args[0]]
        print(len(obj_list))

    def default(self, arg):
        """Called on an input line when the command prefix is not recognized."""
        cmd_parts = arg.split('.')
        if len(cmd_parts) >= 2:
            class_name = cmd_parts[0]
            if class_name in storage.classes.keys():
                cmd = "{} {}".format(class_name, '.'.join(cmd_parts[1:]))
                self.onecmd(cmd)
                return
        print('*** Unknown syntax: {}'.format(arg))

    def help_quit(self):
        """Displays help message for quit command."""
        print("Quit command usage: quit")

    def help_EOF(self):
        """Displays help message for EOF command."""
        print("EOF command usage: EOF")

    def help_create(self):
        """Displays help message for create command."""
        print("Create command usage: create <class name>")

    def help_show(self):
        """Displays help message for show command."""
        print("Show command usage: show <class name> <instance id>")

    def help_destroy(self):
        """Displays help message for destroy command."""
        print("Destroy command usage: destroy <class name> <instance id>")

    def help_all(self):
        """Displays help message for all command."""
        print("All command usage: all [<class name>]")

    def help_update(self):
        """Displays help message for update command."""
        print("Update command usage: update <class name> <instance id> <attribute name> \"<attribute value>\"")

    def help_count(self):
        """Displays help message for count command."""
        print("Count command usage: count <class name>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
