from users_app.config.MySQLConnection import connectToMySQL

class User:
    def __init__( self, firstname, lastname, email, created_at ):
        self.firstname = firstname
        self.lastname = lastname
        self.email= email
        self.created_at= created_at
        
    
    def printInfo( self ):
        print(f"username: {self.username} password: {self.password} ")

    @classmethod
    def get_all_users( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL( "users" ).query_db( query )

        users = []
        for user in results:
            users.append( User( user['firstname'], user['lastname'], user['email'], user['created_at']) )
        
        return users
    
    @classmethod
    def add_user( cls, newUser ):
        query = f"INSERT INTO users(firstname,lastname,email,created_at) VALUES(%(firstname)s, %(lastname)s,%(email)s,%(NOW()));"
        data = {
            "firstname" : newUser.firstname,
            "lastname" : newUser.lastname,
            "email": newUser.email,
            "created_at": newUser.created_at
        }
        result = connectToMySQL( "todos_db" ).query_db( query, data )
        return result
    
    