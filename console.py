#!/usr/bin/python3
"""Describes the console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    cy_brace = re.search(r"\{(.*?)\}", arg)
    bracket = re.search(r"\[(.*?)\]", arg)
    if cy_brace is None:
        if bracket is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:bracket.span()[0]])
            aretl = [i.strip(",") for i in lex]
            aretl.append(bracket.group())
            return aretl
    else:
        lex = split(arg[:cy_brace.span()[0]])
        aretl = [i.strip(",") for i in lex]
        aretl.append(cy_brace.group())
        return aretl


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        watch = re.search(r"\.", arg)
        if watch is not None:
            arg_c = [arg[:watch.span()[0]], arg[watch.span()[1]:]]
            watch = re.search(r"\((.*?)\)", arg_c[1])
            if watch is not None:
                c_cmd = [arg_c[1][:watch.span()[0]], watch.group()[1:-1]]
                if c_cmd[0] in arg_dict.keys():
                    call = "{} {}".format(arg_c[0], c_cmd[1])
                    return arg_dict[c_cmd[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Escape c_cmd to exit the program."""
        return True

    def do_EOF(self, arg):
        """Escape the EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        arg_c = parse(arg)
        if len(arg_c) == 0:
            print("** this class name is missing **")
        elif arg_c[0] not in HBNBCommand.__classes:
            print("** this class doesn't exist **")
        else:
            print(eval(arg_c[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arg_c = parse(arg)
        obj_dict = storage.all()
        if len(arg_c) == 0:
            print("** this class name is missing **")
        elif arg_c[0] not in HBNBCommand.__classes:
            print("** this class doesn't exist **")
        elif len(arg_c) == 1:
            print("** id is missing **")
        elif "{}.{}".format(arg_c[0], arg_c[1]) not in obj_dict:
            print("** instance is not found **")
        else:
            print(obj_dict["{}.{}".format(arg_c[0], arg_c[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        arg_c = parse(arg)
        obj_dict = storage.all()
        if len(arg_c) == 0:
            print("** this class name is missing **")
        elif arg_c[0] not in HBNBCommand.__classes:
            print("** this class doesn't exist **")
        elif len(arg_c) == 1:
            print("** id is missing **")
        elif "{}.{}".format(arg_c[0], arg_c[1]) not in obj_dict.keys():
            print("** instance is not found **")
        else:
            del obj_dict["{}.{}".format(arg_c[0], arg_c[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arg_c = parse(arg)
        if len(arg_c) > 0 and arg_c[0] not in HBNBCommand.__classes:
            print("** this class name doesn't exist **")
        else:
            obj_l = []
            for obj in storage.all().values():
                if len(arg_c) > 0 and arg_c[0] == obj.__class__.__name__:
                    obj_l.append(obj.__str__())
                elif len(arg_c) == 0:
                    obj_l.append(obj.__str__())
            print(obj_l)

    def do_count(self, arg):
        arg_c = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_c[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        arg_c = parse(arg)
        obj_dict = storage.all()

        if len(arg_c) == 0:
            print("** this class is name missing **")
            return False
        if arg_c[0] not in HBNBCommand.__classes:
            print("** this name class doesn't exist **")
            return False
        if len(arg_c) == 1:
            print("** id is missing **")
            return False
        if "{}.{}".format(arg_c[0], arg_c[1]) not in obj_dict.keys():
            print("** instance is not found **")
            return False
        if len(arg_c) == 2:
            print("** attribute name is missing **")
            return False
        if len(arg_c) == 3:
            try:
                type(eval(arg_c[2])) != dict
            except NameError:
                print("** value is missing **")
                return False

        if len(arg_c) == 4:
            obj = obj_dict["{}.{}".format(arg_c[0], arg_c[1])]
            if arg_c[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_c[2]])
                obj.__dict__[arg_c[2]] = valtype(arg_c[3])
            else:
                obj.__dict__[arg_c[2]] = arg_c[3]
        elif type(eval(arg_c[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_c[0], arg_c[1])]
            for x, y in eval(arg_c[2]).items():
                if (x in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[x]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[x])
                    obj.__dict__[x] = valtype(y)
                else:
                    obj.__dict__[x] = y
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
