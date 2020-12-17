from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)


#INDEX: GET, return index.html, /bookings route
@bookings_blueprint.route("/bookings")
def bookings():
    return render_template('bookings/index.html', bookings=bookings)


#NEW

#CREATE

#SHOW

#EDIT


#UPDATE