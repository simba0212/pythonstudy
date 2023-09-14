from step06_object.objectEx01 import *

if __name__ == '__main__':
    ps = Person()
    print(ps)
    ps.viewPerson()

    ps.setPerson('장길산',14,168.2)
    ps.viewPerson()