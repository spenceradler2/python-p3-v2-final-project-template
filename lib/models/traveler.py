from models.__init__ import CONN, CURSOR

class Traveler:
    def __init__(self, name, id =None):
        self.id = id
        self.name = name

    @property
    def name (self):
        return self._name
    @name.setter
    def name (self,name):
        if isinstance(name,str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name of traveler must be a string and be longer than 0 characters!")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS travelers (
            id INTEGER PRIMARY KEY,
            name TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
        INSERT INTO travelers (name) VALUES (?);
        """
        CURSOR.execute(sql,(self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid

    def delete(self):
        self.delete_locations() #Review this not working as nothing gets deleted
        sql = """
        DELETE FROM travelers WHERE id = (?);
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()

    def delete_locations(self): 
        for location in self.locations():
            location.delete()

    @classmethod
    def create(cls,name):
        traveler = Traveler(name=name)
        traveler.save()
        return traveler
    
    @classmethod
    def inst_from_db(cls,row):
        return Traveler(name=row[1], id=row[0])
    
    @classmethod
    def find_by_id(cls,id):
        sql ="""
        SELECT * FROM travelers WHERE id = (?);
        """
        data=CURSOR.execute(sql,(id,)).fetchone()
        if data:
            return Traveler.inst_from_db(data)
        else:
            return None

    @classmethod   
    def all(cls):
        sql = """
        SELECT * FROM travelers;
        """

        data =CURSOR.execute(sql).fetchall()
        return [Traveler.inst_from_db(row) for row in data]
    
    def locations(self):
        from models.location import Location
        sql = """
        SELECT * FROM locations WHERE locations.traveler_id = (?);
        """

        data=CURSOR.execute(sql,(self.id,)).fetchall()
        return [Location.inst_from_db(row) for row in data]

    

