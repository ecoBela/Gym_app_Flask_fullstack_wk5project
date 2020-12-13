from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member

# CRUD
# Create
def save(activity):
    sql = "INSERT INTO activities (name, upcoming) VALUES (%s, %s) RETURNING id"
    values = [activity.name, activity.upcoming]
    results = run_sql(sql, values)
    activity.id = results[0]['id']
    return activity


# Update
def update(activity):
    sql = "UPDATE activities SET (name, upcoming) = ( %s, %s) WHERE id = %s"
    values = [activity.name, activity.upcoming, activity.id]
    run_sql(sql, values)

# def select_all():
#     sql = 

def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)
