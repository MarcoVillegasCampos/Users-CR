from flask import render_template, request, redirect
from users_app import app
from users_app import User



@app.route( "/user", methods=['POST'] )
def displayForm():
    return render_template( "user.html" )

@app.route( "/user/new", methods=['GET'] )
def displayHome():
    

        
   
    
        return render_template( "home.html" )

