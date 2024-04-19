import pandas as pd

edades = [19, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 34, 21, 21, 22, 28, 29, 19, 20, 19, 25, 28, 21, 22]

def contar_valores(lista):
    diccionario_contadores = {}
    lista.sort()
    for valor in lista:
        if valor in diccionario_contadores:
            diccionario_contadores[valor] += 1
        else:
            diccionario_contadores[valor] = 1
    return diccionario_contadores

def analisis_estadistico(datos):

    # Creo un DataFrame vacío.
    data_frame = pd.DataFrame()
    diccionario_edades = contar_valores(datos)
    # Agrego todas las columnas correspondientes

    #La primera me mostrata las edades existentes sin repetirse
    data_frame["Edades"] = diccionario_edades.keys()
    # fi: Frecuencia absoluta simple
    data_frame["fi"] = diccionario_edades.values()
    # Fi: Frecuencia absoluta acumulada.
    data_frame["Fi"] = data_frame["fi"].cumsum()
    # ri: Frecuencia absoluta relativa
    data_frame["ri"] = (data_frame["fi"] / data_frame["fi"].sum()).round(3)
    # Ri: Frecuencia absoluta relativa acumulada
    data_frame["Ri"] = (data_frame["ri"].cumsum()).round(3)
    # pi: Frecuencia porcentual simple 
    data_frame["pi%"] = (data_frame["ri"] * 100).round(2)
    # Pi: Frecuencia porcentual acumulada
    data_frame["Pi%"] = (data_frame["pi%"].cumsum()).round(2)
    
    return data_frame

print(analisis_estadistico(edades))

