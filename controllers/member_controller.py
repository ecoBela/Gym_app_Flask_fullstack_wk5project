from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository 

members_blueprint = Blueprint("members", __name__)






#INDEX
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

# NEW
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")

#CREATE

#/members: POST, will add member to db but should redirect user to home page afterwards
@members_blueprint.route("/members", methods=["POST"])
def create_member():
    name = request.form["name"]
    new_member = Member(name)
    member_repository.save(new_member)
    return redirect ("/")
    



#EDIT

#/members/edit: GET, will render edit.html page displaying form
@members_blueprint.route("/members/<id>/edit")
def edit_member():
    return render_template("members/edit.html")

# UPDATE
# /members/id: PUT will add edits to db but should redirect user to home page afterwards
@members_blueprint.route("/members/<id>", methods=["PUT"])
def update_member(id):
    name = request.form["name"]
    member = Member(name, id)
    member_repository.update(member)
    return redirect("/")


#SHOW
#/members/id: GET, will render the show.html page displaying member
# remember to change the route to members/<id>
@members_blueprint.route("/members/show") 
def show_all_members():
    member_repository.select_all()
    return render_template("members/show.html")

# DELETE