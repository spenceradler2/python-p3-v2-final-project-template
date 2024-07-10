from models.__init__ import CONN, CURSOR

class Location:
    def __init__(self, name, traveler_id, id = None):
        self.name = name
        self.traveler_id = traveler_id
        self.id = id

    @property
    def name (self):
        return self._name
    @name.setter
    def name (self,name):
        if isinstance(name,str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name of location must be a string and be longer than 0 characters!")
        
    @property
    def traveler_id (self):
        return self._traveler_id
    
    @traveler_id.setter
    def traveler_id (self,traveler_id):
        from models.traveler import Traveler
        if isinstance(traveler_id,int) and traveler_id > 0 and traveler_id < 100:
            traveler=Traveler.find_by_id(traveler_id)
            if traveler:
                self._traveler_id = traveler_id
            else:
                ValueError("Traveler does not exist. Please try to find by a different id.")
        else:
            raise ValueError("Id must be an integer and must be greater than 0. Additionally this table has a maximum number of id's of 100. Make sure your id is less than 100.")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY,
            name TEXT,
            traveler_id INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
        INSERT INTO locations (name, traveler_id) VALUES (?,?);
        """
        CURSOR.execute(sql,(self.name,self.traveler_id,))
        CONN.commit()

        self.id = CURSOR.lastrowid

    def delete(self): #Review this not working as nothing gets deleted
        sql = """
        DELETE FROM locations WHERE id = (?);
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()

    @classmethod
    def create(cls,name,traveler_id):
        location = Location(name=name, traveler_id=traveler_id)
        location.save()
        return location
    
    @classmethod
    def inst_from_db(cls,row):
        return Location(id=row[0], name=row[1], traveler_id=row[2])
    
    @classmethod
    def find_by_id(cls,id):
        sql ="""
        SELECT * FROM locations WHERE id = (?);
        """
        data=CURSOR.execute(sql,(id,)).fetchone()
        if data:
            return Location.inst_from_db(data)
        else:
            return None

    @classmethod   
    def all(cls):
        sql = """
        SELECT * FROM locations;
        """

        data =CURSOR.execute(sql).fetchall()
        return [Location.inst_from_db(row) for row in data]
    
    def traveler(self):
        from models.location import Traveler
        return Traveler.find_by_id(self.travler_id)
