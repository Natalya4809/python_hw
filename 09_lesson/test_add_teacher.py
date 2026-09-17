from sqlalchemy import create_engine
from sqlalchemy.sql import text

def test_insert():
    db = create_engine(db.connection_string)
    sql = text("insert into teacher("email")values('marina56@yaa.com')")
    rows = db.execute(sql, 'marina56@yaa.com')