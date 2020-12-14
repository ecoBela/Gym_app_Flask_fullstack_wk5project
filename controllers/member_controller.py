from flask import Flask, render_template, request
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository 

members_blueprint = Blueprint("members", __name__)

#routes

#/members: GET, will render index.html page displaying options
@members_blueprint.route("/members")
def members():
    return render_template("members/index.html")

#/members/new: GET, will render new.html page displaying form
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")

#/members: POST, will add member to db but should redirect user to home page afterwards
# @members_blueprint.route("/members" methods=["POST"])
# def create_member():
    

#/members/id: GET, will render the show.html page displaying member
# remember to change the route to members/<id>
@members_blueprint.route("/members/4") 
def show_member():
    return render_template("members/show.html")

#/members/edit: GET, will render edit.html page displaying form
@members_blueprint.route("/members/edit")
def edit_member():
    return render_template("members/edit.html")

#/members/id: PUT will add edits to db but should redirect user to home page afterwards