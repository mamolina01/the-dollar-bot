import requests
import matplotlib.pyplot as plt
from config import *

def getDollar(year_start,year_end):
    url ="https://api.estadisticasbcra.com/usd"
    header =  {"Content-Type":"application/json", "Authorization": f"Bearer {dollar_token}"}
    inicio=252*(year_start-2000)
    final=252*(year_end-1999)
    promedios=[]
    dolar=requests.get(url, headers=header).json()
    for x in range(year_start,year_end):
        promedio_anual=0
        for i in range(inicio,final,84):
            try:
                fecha=dolar[i]["d"]
                valor=dolar[i]["v"]
                print(f"{fecha} - Valor: {valor}")
                promedio_anual+=valor
            except Exception as e:
                print(e)
        promedios.append(promedio_anual/3)
        inicio+=252
        final+=252

    x=range(year_start,year_end)

    fig,ax=plt.subplots()
    ax.bar(x,promedios,color="g")
    plt.xlabel("Año")
    plt.ylabel("Valor")
    plt.savefig("grafico.png")
    plt.show()
  

def getDollarDate(fecha):
    url=f"https://cont1-virtual1.certisend.com/web/container/api/v1/fintech/ar/bcra/dolar_value?token-susc={Token_Susc}&token-api={Token_API}&date={fecha}&internalid={id}" 
    api=requests.get(url,"accept: application/json").json()["data"][0]["bancos"][3]
    promedio_13_venta=api["mostrador_11hs_vende"]
    banco=api["banco"]
    return promedio_13_venta,banco
