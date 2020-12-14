from flask import Flask, render_template, request
from flask import Blueprint
from models.member import Member

members_blueprint = Blueprint("members", __name__)