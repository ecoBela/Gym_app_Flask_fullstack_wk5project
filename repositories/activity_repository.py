from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member
import pdb

# CRUD
# Create
def save(activity):
    sql = "INSERT INTO activities (name, upcoming) VALUES (%s, %s) RETURNING id"
    values = [activity.name, activity.upcoming]
    results = run_sql(sql, values)
    activity.id = results[0]['id']
    return activity


# Read - displays all upcoming
def select_all():
    sql = "SELECT * FROM activities WHERE upcoming = True"
    results = run_sql(sql)
    return results
    
#displays upcoming and past events
def select_all_including_past():
    sql = "SELECT * FROM activities"
    results = run_sql(sql)
    return results

def select(id):
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    return results

# Update
def update(activity):
    sql = "UPDATE activities SET (name, upcoming) = ( %s, %s) WHERE id = %s"
    values = [activity.name, activity.upcoming, activity.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)

def get_members(activity):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.activity_id = %s;"
    values = [activity.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members
