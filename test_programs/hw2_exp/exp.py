#from class_mod import *        # allows users to call funcs in module w/o class_mod.*
import class_mod        # must call funcs with class_mod.* unless returned a class instance

#dInit(["localhost"], 2500)
#fp = dopen("example.txt")

#fp.dread()


class_mod.dInit(["localhost"], 2500)
fp = class_mod.dopen("example.txt")

fp.dread()
