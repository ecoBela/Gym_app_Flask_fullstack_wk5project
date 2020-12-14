from flask import Flask, render_template, request
from flask import Blueprint
from models.member import Member

members_blueprint = Blueprint("members", __name__)

#routes

#/members: GET, will render index.html page displaying options


#/members/new: GET, will render new.html page displaying form

#/members: POST, will add member to db but should redirect user to home page afterwards

#/members/id: GET, will render the show.html page displaying member

#/members/edit: GET, will render edit.html page displaying form

#/members/id: PUT will add edits to db but should redirect user to home page afterwards