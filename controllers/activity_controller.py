from flask import Flask, render_template, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activties", __name__)

# INDEX
@activities_blueprint.route("/activities")
def activities():
    return render_template("activities/index.html")

# @members_blueprint.route("/members")
# def members():
#     members = member_repository.select_all()
#     return render_template("members/index.html", members = members)
# NEW
# CREATE, 
# EDIT
# UPDATE
# SHOW