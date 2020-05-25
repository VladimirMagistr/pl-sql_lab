import cx_Oracle
import plotly.graph_objects as go
import plotly.offline as py
import chart_studio
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard
import re
#import chart_studio


def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')


#chart_studio.tools.set_credentials_file(username='Vladimir_Magistr', api_key='XXXXXXXXXX')



connectiom = cx_Oracle.connect(user="vova", password="XXXXX")

cursor = connectiom.cursor()

print("connected")
print("Получаем средню длину лепестка. Среднее значение равно:" )
query1 = cursor.execute("""select avg(lengh_cm) from petal
where species_id =1
union
select avg(lengh_cm) from petal
where species_id =2
union
select avg(lengh_cm) from petal
where species_id =3""")

#vo = cursor.fetchall

a =[]
b = []
c = 1
for row in query1:
    print(row[0])
    #if int(row[0]) > 0:
        #pass
    #else:


    a += [row[0]]
    b += [str(c) + '\n' + "Bид ириса"]
    c = c + 1
    #vova = row[0]
    #b = a.append(float(vova))
    #print(b)
    #print(a)
    #try:
        #a = a.append(int(vova))
    #except:
       # pass
#for row in a:
    #print("Средний размер вид " + str(row[0]) )
print(str(a) + 'нашел')
print(str(b) + 'нашел')

data = go.Bar(
   x = b,
   y = a
)

layout = go.Layout(
    title='Виды цветов',
    xaxis=dict(
        title='Виды ирисок',
        titlefont=dict(
            family='Courier New, monospace',
            size=50,
            color=' #ff0000 '
        )
    ),
    yaxis=dict(
        title='Среднии размеры ирисов',
        titlefont=dict(
            family='Courier New, monospace',
            size=50,
            color=' #ff0000 '
        )
    )
)

fig = go.Figure(data=data, layout=layout)
ohyt3 = py.plot(fig, filename='first_diagram')
#fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
#fig.write_html('first_figure.html', auto_open=True)



# вторая часть
cursor.execute("""
select  sepal.lengh_cm,  count(width_cm) from sepal
group by sepal.lengh_cm
order by sepal.lengh_cm
""")
dlinna = []
kolvo = []

for row in cursor:
    print("Длинна ", row[0], " Количество: ", row[1])
    dlinna += [row[0]]
    kolvo += [row[1]]

order_date_prices = go.Scatter(
    x=dlinna,
    y=kolvo,
    mode='markers'
)
data = [order_date_prices]
ohyt2 = py.plot(data)




# Третья часть


cursor.execute("""
Select Count(flower_id)/(select count(*) from sepal), spicies_name from sepal
LEFT join Vid_irisa on sepal.species_id=Vid_irisa.species_id 
group by spicies_name
""")

name = []
count = []

for row in cursor:
    print("Вид ириса ", str(row[1]) + " Количество в выборке: " + str(row[0]) )
    name += [row[1]]
    count += [row[0]]


pie = go.Pie(labels=name, values=count)
ohyt = py.plot([pie])






"...............................Creating DashBoar..........................."

my_dboard = dashboard.Dashboard()

vovin_diagram = fileId_from_url(ohyt3)
voin_kryg = fileId_from_url(ohyt2)
vovini_tochki = fileId_from_url(ohyt)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': vovin_diagram,
    'title': 'Сравнение размеров ирисок'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': voin_kryg,
    'title': 'Исследование количества цветков по их размеру чашелистика'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': vovini_tochki,
    'title': 'Количество видов цветов'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'Lab2_Dashboard_done2')
