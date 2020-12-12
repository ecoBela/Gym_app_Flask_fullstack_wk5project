from db.run_sql import run_sql
from models.member import Member
from models.activity import Activity

# CRUD: create
def save(member)
    sql = "INSERT INTO members ( name ) VALUES ( %s ) RETURNING id"
    values = [member.name]
    results = run_sql(sql, values)
    member_id = results[0]['id']
    return member


#CRUD: read
#Do we need a def select() here?


#CRUD: update
# def update()

#CRUD: delete
#delete_all()