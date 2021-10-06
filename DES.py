import build
import data_controller as dc

def one ():
    dc.check_app_has_data()
    build.show(two, three, "DES1")


def two ():
    dc.check_app_has_data()
    build.show(three, one, "DES2")


def three ():
    dc.check_app_has_data()
    build.show(one, two, "DES3")
    
    