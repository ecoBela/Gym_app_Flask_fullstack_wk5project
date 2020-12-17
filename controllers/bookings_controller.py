from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)