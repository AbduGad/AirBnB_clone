#!/usr/bin/python3

import cmd
import models
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
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            ins = models.storage.all()
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
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            ins = models.storage.all()
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
                    models.storage.save()

    def do_destroy(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            ins = models.storage.all()
            if key in ins:
                del ins[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        # instances = storage.all()

        if not arg:
            print([str(inst) for inst in models.storage.all().values()])
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in models.storage.classes():
            print("** class doesn't exist **")
        else:
            print([str(instance) for instance in models.storage.all().values()
                   if instance.__class__.__name__ == class_name])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
