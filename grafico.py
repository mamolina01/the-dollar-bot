import requests
import matplotlib.pyplot as plt
from config import dollar_token

def getDollar(year_start,year_end):
    url ="https://api.estadisticasbcra.com/usd"
    header =  {"Content-Type":"application/json", "Authorization": f"Bearer {dollar_token}"}
    inicio=252*year_start
    final=252*year_end
    promedios=[]
    dolar=requests.get(url, headers=header).json()
    for x in range(year_start,year_end):
        promedio_anual=0
        for i in range(inicio,final,84):
            fecha=dolar[i]["d"]
            valor=dolar[i]["v"]
            print(f"{fecha} - Valor: {valor}")
            promedio_anual+=valor
        promedios.append(promedio_anual/3)
        inicio+=252
        final+=252
        #print(f"Año: {x} - Valor {promedios[x]}")

    x=range(2000+year_start,2000+year_end)

    fig,ax=plt.subplots()
    ax.bar(x,promedios,color="g")
    plt.xlabel("Año")
    plt.ylabel("Valor")
    plt.savefig("grafico.png")
    plt.show()
  
getDollar(5,20)