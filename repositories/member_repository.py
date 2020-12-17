from db.run_sql import run_sql
from models.member import Member
from models.activity import Activity

# CRUD: create
def save(member):
    sql = "INSERT INTO members ( name ) VALUES ( %s ) RETURNING id"
    values = [member.name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member


#CRUD: read
def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(result["name"], result["id"])
        members.append(member)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result["name"], result["id"])
    return member



#CRUD: update
def update(member):
    sql = "UPDATE members SET name = %s WHERE id = %s"
    values = [member.name, member.id]
    run_sql(sql, values)
    


#CRUD: delete
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

