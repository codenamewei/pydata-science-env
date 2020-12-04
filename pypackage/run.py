from database import *
from query import *
from router import *

if __name__ == "__main__":

    print("Start program")

    runSchema()

    insert()

    query()

    router1 = Router1("OWL Router", 123)

    router1.start()

    print("End program")
