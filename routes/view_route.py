from flask import render_template,request,jsonify,Blueprint


view_route = Blueprint("view",__name__)

@view_route.route("/")
def home():
    return render_template("index.html")


@view_route.route("/ic")
def id_class():
    return render_template("id-class.html")

@view_route.route("/login")
def login():
    return render_template("login.html")


@view_route.route("/layout")
def layout():
    return render_template("layout.html")

@view_route.route("/front")
def front():
    return render_template("front.html")

@view_route.route("/js")
def js_basic():
    return render_template("js-basic.html")

@view_route.route("/td")
def todo():
    todo_id = request.args.get("todo-id")

    
    return render_template("todo.html",todo_id=todo_id)


@view_route.route("/save")
def save():
    return render_template("save-user.html")


@view_route.route("/house")
def house_pre():
    return render_template("house_pre.html")


@view_route.route("/cat-dog")
def cat_dog():
    return render_template("cat-dog.html")


@view_route.route("/covid")
def covid():
    return render_template("covid-19.html")
