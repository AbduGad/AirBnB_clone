#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            ins = eval(arg)()
            ins.save()
            print(ins.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            ins = storage.all()
            if key in ins:
                print(ins[key])
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            ins = storage.all()
            if key not in ins:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = ins[key]
                attr = args[2]
                if hasattr(obj, attr):
                    value = args[3]
                    try:
                        value = eval(value)
                    except (NameError, SyntaxError):
                        pass
                    setattr(obj, attr, value)
                    storage.save()

    def do_destroy(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            ins = storage.all()
            if key in ins:
                del ins[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_
        """


if __name__ == "__main__":
    HBNBCommand().cmdloop()
