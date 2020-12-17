from database import *
from query import *
from router import *
from router.subrouter import *

if __name__ == "__main__":

    print("Start program")

    runSchema()

    insert()

    query()

    router1 = Router1("OWL Router", 123)

    router1.start()

    gateway = Gateway()

    gateway.initiate()

    print("End program")
