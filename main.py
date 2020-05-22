import cx_Oracle

connectiom = cx_Oracle.connect(user="vovan", password="vovan")

cursor = connectiom.cursor()

print("connected")
print("Получаем средню длину лепестка. Среднее значение равно:" )
query1 = cursor.execute("select avg(lengh_cm) from petal")

#vo = cursor.fetchall



for row in query1:
    print(row[0])

print("Получаем ирисы размер чащелистика которых больше средней" )

query2 = """select Vid_irisa.spicies_name, sepal.flower_id, sepal.width_cm from sepal
LEFT join Vid_irisa on sepal.species_id=Vid_irisa.species_id 
where sepal.width_cm > (select
avg(width_cm)
from
sepal)
order by  width_cm"""
query2 = cursor.execute(query2) # Отличная типипзация



for row in query2:
    print(row)

print("Сколько ирисов с определенной длинной чашелистика" )

query3 = cursor.execute("""select  sepal.lengh_cm,  count(width_cm) from sepal
group by sepal.lengh_cm
order by sepal.lengh_cm""")

for row in query3:
     print(row)


