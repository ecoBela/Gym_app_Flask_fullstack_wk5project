from db.run_sql import run_sql
from models.booking import Booking


#CRUD

## Create - books member into specific class
def save(booking):
    sql = "INSERT INTO bookings ( member_id, activity_id ) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.activity.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking


## Read


# Update

## Delete
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)
