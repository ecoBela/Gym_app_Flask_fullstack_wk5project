from db.run_sql import run_sql
from models.member import Member
from models.activity import Activity

#CRUD

## Create

## Read

# Update

## Delete
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)
