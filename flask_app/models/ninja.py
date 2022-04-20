from flask_app.config.mysqlconnection import connectToMySQL



class Ninja:
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def save(cls, data):
        query= "INSERT INTO ninjas (first_name, last_name, dojo_id, age, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(dojo_id)s, %(age)s, NOW(), NOW());"
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data) 

        return result


    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM ninjas;"
    #     ninjas = []
    #     results = connectToMySQL('dojos_and_ninjas').query_db(query)
    #     for row in results:
    #         ninjas.append( cls(row) )
    #     return 


