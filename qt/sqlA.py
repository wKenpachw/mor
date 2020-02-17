import sqlalchemy

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:451257@localhost:5432/postgres')
conncetion = engine.connect()

"""with conncetion.begin() as chars:
    conncetion.execute("INSERT into public.\"Lafaed\" values (3,'laaf', 60,0) ")"""
"""result = conncetion.execute('SELECT * from public."Laf_enemis" order by "ID_CHAR"')
for row in result:
    print(row)"""

def get_all_chars():
    try:
        result = conncetion.execute('select "ID_CHAR","FIO","init", "curent_HP", "max_HP"  from "Chars" ORDER by "ID_CHAR" ')
    except Exception:
       result = list()
    return result

def get_char_atacks(ind):
    try:
        result = conncetion.execute('SELECT * FROm "Atacks" where "ID_ATACK" = ' + str(ind))
    except Exception:
        result = list()
    return result