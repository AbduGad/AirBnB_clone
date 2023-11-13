#!/usr/bin/python3
"""CMD Module
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
    """
        command line intrepeter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit
        """
        return True

    def do_EOF(self, arg):
        """EOF
        """
        return True

    def emptyline(self):
        """summary
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
            return

    def do_show(self, arg):
        """_summary_
        Args:
            arg (_type_): _description_
        """
        """storage.reload()"""
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            ins = storage.all()
            if key in ins:
                if isinstance(ins[key], dict):
                    print(eval(storage.all()[key]['__class__'])())
                else:
                    print(storage.all()[key])
                return
            else:
                print("** no instance found **")
                return

    def do_update(self, arg):
        """Update instance of BaseModel
        """
        storage.reload()
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
            return
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
                value = args[3]
                try:
                    value = eval(value)
                except (NameError, SyntaxError):
                    pass
                setattr(obj, attr, value)
                models.storage.save()

    def do_destroy(self, arg):
        """Delete/Destroy instance of BaseModel
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

        storage.reload()
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
