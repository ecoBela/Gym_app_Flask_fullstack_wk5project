from flask import Flask, render_template, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository

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
# EDIT
# UPDATE
# SHOW