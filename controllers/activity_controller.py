from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository
import pdb

activities_blueprint = Blueprint("activties", __name__)

# INDEX
@activities_blueprint.route("/activities")
def activities():
    activities = activity_repository.select_all_including_past()
    return render_template("activities/index.html", activities = activities)

# NEW

@activities_blueprint.route("/activities/new")
def new_activity():
    return render_template("activities/new.html")


# CREATE, 
@activities_blueprint.route("/activities", methods=['POST'])
def create_activity():
    activity_name = request.form["name"]
    # upcoming = request.form["upcoming"] except:
    try:
        upcoming = request.form["upcoming"]
    except: 
        upcoming = False
    
    new_activity = Activity(activity_name, upcoming)
    activity_repository.save(new_activity)
    return redirect("/activities")


# SHOW
@activities_blueprint.route("/activities/<id>/show", methods=['GET'])
def show_members(id):
    activity = activity_repository.select(id)
    members = activity_repository.get_members(activity)
    return render_template("/activities/show.html", members=members)

# EDIT

@activities_blueprint.route("/activities/<id>/edit", methods=['GET'])
def edit_activity(id):
    activity = activity_repository.select(id)
    return render_template("activities/edit.html", activity = activity)


# UPDATE

@activities_blueprint.route("/activities/<id>", methods=["POST"])
def update_activity(id):
    name = request.form["name"]
    # upcoming = request.form["upcoming"]
    try:
        upcoming = request.form["upcoming"]
    except: 
        upcoming = False

    activity = Activity(name, upcoming, id)
    activity_repository.update(activity)
    return redirect('/activities')





