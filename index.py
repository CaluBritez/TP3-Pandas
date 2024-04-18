import pandas as pd

# Obtengo los datos
datos_curso = pd.read_csv("edadesIPF.csv")

def analisis_estadistico(data):

    # Verifico que el parámetro data sea de tipo DataFrame.
    assert isinstance(data, pd.DataFrame), "El DataFrame no es de tipo DataFrame"  
    # Verifico que la columna Edad sea de tipo numérico.
    assert data["Edad"].dtype in ["int64","float64",], f"El tipo de dato de la columna Edad no es numérico"

    # Creo un DataFrame vacío.
    data_frame = pd.DataFrame()

    # Agrego todas las columnas correspondientes

    #La primera me mostrata las edades existentes sin repetirse
    data_frame["Edades"] = data["Edad"].sort_values().unique()
    # fi: Frecuencia absoluta simple
    data_frame["fi"] = data["Edad"].groupby(data["Edad"]).size().values
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

print(analisis_estadistico(datos_curso))

