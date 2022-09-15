import pandas as pd
from sqlalchemy import create_engine

cadena_conexion = 'mysql+pymysql://root:root@localhost:3306/pi01'
conexion = create_engine(cadena_conexion)

#año con mas carreras
def pregunta_1():
    sql1 = 'SELECT year, count(*) as Cantidad from races group by year order by year desc;'
    df1 = pd.read_sql_query(sql1,conexion)
    return {'year': df1['year'][0], 'carreras': df1['Cantidad'][0]}


#'piloto mayor cantidad posicion #1'
def pregunta_2():
    sql2 = 'SELECT b.driverRef, count(*) as wins from results a left join drivers b on a.driverId = b.driverId where a.positionOrder = "1" group by b.driverRef order by wins desc' 
    df2 = pd.read_sql_query(sql2,conexion)
    return {'driver': df2['driverRef'][0], 'wins': df2['wins'][0]}

#circuito con mas carreras
def pregunta_3():
    sql3 = 'select b.circuitRef circuito, count(*) as carreras from races a left join circuits b on a.circuitId = b.circuitId where a.circuitId !="0" group by b.circuitRef order by carreras desc'
    df3 = pd.read_sql_query(sql3,conexion)
    df3.drop([0], axis=0, inplace=True)
    df3=df3.reset_index()
    return {'circuito': df3['circuito'][0], 'carreras': df3['carreras'][0]}

#'piloto american o british con mayor cantidad de puntos'
def pregunta_4():
    sql4 = 'select b.driverRef, sum(a.points) points from results a left join drivers b on a.driverId = b.driverId where b.nationality in ("american","british") group by 1 order by 2 desc'
    df4 = pd.read_sql_query(sql4,conexion)
    return{'piloto': df4['driverRef'][0],'puntos': df4['points'][0]}

print(pregunta_1())
print(pregunta_2())
print(pregunta_3())
print(pregunta_4())


