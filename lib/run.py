from models.__init__ import CONN, CURSOR
from models.traveler import Traveler
from models.location import Location

from cli import Cli

Traveler.create_table()
Location.create_table()


Cli().start()