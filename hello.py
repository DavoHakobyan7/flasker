from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    my_name = "Ben"
    stuff = "This is Bold text"

    favorite_pizza = ["Pepperoni", "cheese", "altono", 41]
    return render_template("index.html", my_name=my_name, 
                           stuff=stuff, 
                           favorite_pizza=favorite_pizza)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)



#Invalid URL popokhutyun
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500



if __name__ == "__main__":
    app.run(debug=True)