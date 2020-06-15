import sqlalchemy

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:451257@localhost:5432/postgres')
conncetion = engine.connect()

def get_tehAll():
    try:
        result = conncetion.execute('Select * FROM "TehProc"."TehVars"')
    except Exception:
       result = list()
    return result

def get_Names():
    try:
        result = conncetion.execute('Select name FROM "TehProc"."TehVars"')
    except Exception:
       result = list()
    return result

def get_tehFromName(name):
    try:
        result = conncetion.execute('SELECT * FROm "TehProc"."TehVars" where "name" = \'' + str(name) + '\'') 
    except Exception:
        result = list()
    return result

def set_obr(name, HourCount, OneCost):
    conncetion.execute('INSERT INTO "TehProc"."TehVars" ("name", "HourCount", "OneCost") VALUES (\'' + str(name) + '\', ' + str(HourCount) + ',' + str(OneCost) + ')')
    
def get_year(name):
    try:
        result = conncetion.execute('Select "years"."YearName", "years"."YearCost" from "TehProc"."YearCost"  as  "years" INNER JOIN "TehProc"."TehVars" as variant ON ("years"."Obr_ID" = "variant"."Var_id") where "variant"."name" = \'' + str(name) + '\'') 
    except Exception:
        result = list()
    return result

def get_obr(name):
    try:
        result = conncetion.execute('Select "obrs"."HourCount", "obrs"."OneCost" from "TehProc"."TehVars"   as  "obrs"  where "obrs"."name" = \'' + str(name) + '\'') 
    except Exception:
        result = list()
    return result

def get_izd(name):
    try:
        result = conncetion.execute('Select "izd"."IzdName", "izd"."IzdCost" from "TehProc"."IzdCost"  as  "izd" INNER JOIN "TehProc"."TehVars" as variant ON ("izd"."Obr_ID" = "variant"."Var_id") where "variant"."name" = \'' + str(name) + '\'') 
    except Exception:
        result = list()
    return result

def get_id(name):
    res = 0
    try:
        result = conncetion.execute('select "Var_id" from "TehProc"."TehVars" where "TehProc"."TehVars"."name" = \'' + name + '\'') 
    except Exception:
        result = list()
    for row in result:
        res = row[0]
    return res

def set_izd(name, cost,id):
    conncetion.execute('INSERT INTO "TehProc"."IzdCost" ("IzdName", "IzdCost", "Obr_ID") VALUES (\'' + str(name) + '\', '  + str(cost) + ',' + str(id) + ')') 
   
def set_year(name, cost,id):
    conncetion.execute('INSERT INTO "TehProc"."YearCost" ("YearName", "YearCost", "Obr_ID") VALUES (\'' + str(name) + '\', '  + str(cost) + ',' + str(id) + ')') 
   


res = get_obr('Токарный станок')
for row in res:
    print (row[0])
