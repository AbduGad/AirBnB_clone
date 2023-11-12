#!/usr/bin/python3
"""_summary_

Returns:
    _type_: _description_
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.place import Place
from models.user import User
from models.state import State


class HBNBCommand(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_

    Returns:
        _type_: _description_
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_

        Returns:
            _type_: _description_
        """
        return True

    def do_EOF(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_

        Returns:
            _type_: _description_
        """
        return True

    def emptyline(self):
        """_summary_
        """
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
        """summary

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

        obj = storage.all()

        args = arg.split()

        if len(args) < 1:
            print(["{}".format(str(ins))
                  for _, ins in obj.items()])
            return
        if args[0] not in models.storage.classes():
            print("** class doesn't exist **")
            return
        else:
            for key, value in obj.items():
                if value.__class__.__name__ == args[0]:
                    # tmpobj = eval(value['__class__'])(**value)
                    print(value)
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
