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
        if not arg:
            print("** class name missing **")
            return

        cls_Name = arg.strip()
        if cls_Name not in storage.classes():
            print("** class doesn't exist **")
        else:
            ins = storage.classes()[cls_Name]
            ins.save()
            print(ins.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
