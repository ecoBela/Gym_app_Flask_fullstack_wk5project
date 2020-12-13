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
#Do we need a def select() here?



#CRUD: update
def update(member):
    sql = "UPDATE members SET name = %s WHERE id = %s"
    values = [member.name, member.id]
    run_sql(sql, values)
    


#CRUD: delete
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

