import pandas as pd
import numpy as np
from sqlalchemy import create_engine

cadena_conexion = 'mysql+pymysql://root:root@localhost:3306/pi01'
conexion = create_engine(cadena_conexion)

sql1 = 'SELECT year, count(*) as Cantidad from races group by year order by year desc;'
sql2 = 'SELECT b.driverRef, count(*) as wins from results a left join drivers b on a.driverId = b.driverId where a.positionOrder = "1" group by b.driverRef order by wins desc' 
sql3 = 'select b.circuitRef circuito, count(*) as carreras from races a left join circuits b on a.circuitId = b.circuitId where a.circuitId !="0" group by b.circuitRef order by carreras desc'
sql4 = 'select b.driverRef, sum(a.points) points from results a left join drivers b on a.driverId = b.driverId where b.nationality in ("american","british") group by 1 order by 2 desc'

def respuesta(id):
    if id =='1':
        return pregunta_1()
    elif id =='2':
        return pregunta_2()
    elif id =='3':
        return pregunta_3()
    elif id =='4':
        return pregunta_4()
    else:
        return 'Invalido'

#año con mas carreras
def pregunta_1():
    df1 = pd.read_sql_query(sql1,conexion)
    return {'year': np.array2string(df1['year'][0]), 'carreras': np.array2string(df1['Cantidad'][0])}


#'piloto mayor cantidad posicion #1'
def pregunta_2():
    df2 = pd.read_sql_query(sql2,conexion)
    return {'driver': df2['driverRef'][0], 'wins': np.array2string(df2['wins'][0])}

#circuito con mas carreras
def pregunta_3():
    df3 = pd.read_sql_query(sql3,conexion)
    df3.drop([0], axis=0, inplace=True)
    df3=df3.reset_index()
    return {'circuito': df3['circuito'][0], 'carreras': np.array2string(df3['carreras'][0])}

#'piloto american o british con mayor cantidad de puntos'
def pregunta_4():
    df4 = pd.read_sql_query(sql4,conexion)
    return{'piloto': df4['driverRef'][0],'puntos': np.array2string(df4['points'][0])}

def pilotos():
    sql_drivers = 'select distinct driverRef from drivers'
    pilotos = pd.read_sql_query(sql_drivers,conexion)
    pilotos = pilotos.to_json()
    return pilotos

def circuitos():
    sql_pilotos = 'select * from circuits'
    res = pd.read_sql_query(sql_pilotos, conexion)
    res = res.to_json()
    return res

def constructores():
    sql_const = 'select * from constructors'
    res = pd.read_sql_query(sql_const, conexion)
    res = res.to_json()
    return res

def carreras():
    sql_races = 'select * from races'
    res = pd.read_sql_query(sql_races, conexion)
    res = res.to_json()
    return res

def campeones():
    sql_campeones = 'SELECT c.name, c.year, b.driverRef FROM pi01.results a left join pi01.drivers b on a.driverId = b.driverId left join pi01.races c on a.raceId = c.raceId where a.positionOrder = "1";'
    res = pd.read_sql_query(sql_campeones, conexion)
    res = res.to_json()
    return res

def pilot_wins(nom):
    sql_wins = f'SELECT c.name, c.year, b.driverRef FROM pi01.results a left join pi01.drivers b on a.driverId = b.driverId left join pi01.races c on a.raceId = c.raceId where a.positionOrder = "1" and b.driverRef like "%%{nom}%%";'
    res = pd.read_sql_query(sql_wins, conexion)
    res = res.to_json()
    return res



#sql5 = 'select count(*) from results4'
#df5 = pd.read_sql_query(sql5,conexion)
#print(df5)