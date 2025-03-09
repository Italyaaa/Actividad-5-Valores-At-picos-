#Función para cargar un archivo como dataframe

def cargar_dataset(data):
    import pandas as pd
    import os
    extension = os.path.splitext(data)[1].lower()
    #Cargar el archivo según su extensión
    if extension == '.csv':
        df = pd.read_csv(data)
        return(df)
    elif extension == '.xlsx':
        df = pd.read_excel(data)
        return(df)
    elif extension == '.json':
        df = pd.read_json(data)
        return(df)
    elif extension == '.html':
        df = pd.read_html(data)
        return(df)
    else:
        #Error desde la conzola
            raise ValueError(f'Formato de archivo no soportado: {extension}')   

###################################################################################################################

#Sustitución por ffill cualitativas
def sustitución_cualitativas_ffill(data):
    import pandas as pd
   #Separo columnas cuantitativas del dataframe
    cuantitativas = data.select_dtypes(include=['float', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_sin_nulos = data.select_dtypes(include=["object", "datetime", "category"])
    #Sustituir valores nulos con pormedio o media
    cualitativas = cualitativas_sin_nulos.fillna(method='ffill')
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas,cualitativas], axis=1)

    return(Datos_sin_nulos)


##############################################################################################################################

#Sustitución por ffill cuantitativas
def sustitución_cualitativas_ffill(data):
    import pandas as pd
   #Separo columnas cuantitativas del dataframe
    cuantitativas_sin_nulos = data.select_dtypes(include=['float', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_sin_nulos = data.select_dtypes(include=["object", "datetime", "category"])
    #Sustituir valores nulos con pormedio o media
    cuantitativas = cuantitativas_sin_nulos.fillna(method='ffill')
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas,cualitativas], axis=1)

    return(Datos_sin_nulos)


########################################################################################################################################

#Sustitución por bfill cualitativas
def sustitución_cualitativas_bfill(data):
    import pandas as pd
   #Separo columnas cuantitativas del dataframe
    cuantitativas = data.select_dtypes(include=['float', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_sin_nulos = data.select_dtypes(include=["object", "datetime", "category"])
    #Sustituir valores nulos con pormedio o media
    cualitativas = cualitativas_sin_nulos.fillna(method='bfill')
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas,cualitativas], axis=1)

    return(Datos_sin_nulos)

########################################################################################################################################

#Sustitución cualitativas por string concreto
def sustitución_string_concreto_cualitativas(data):
    import pandas as pd
   #Separo columnas cuantitativas del dataframe
    cuantitativas = data.select_dtypes(include=['float', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_sin_nulos = data.select_dtypes(include=["object", "datetime", "category"])
    #Sustituir valores nulos con pormedio o media
    cualitativas = cualitativas_sin_nulos.fillna('No info')
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas,cualitativas], axis=1)

    return(Datos_sin_nulos)

###################################################################################################################################################

#Sustitución cuantitativas por constante
def sustitución_nconcreto(data):
    import pandas as pd
   #Separo columnas cuantitativas del dataframe
    cuantitativas_sin_nulos = data.select_dtypes(include=['float', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = data.select_dtypes(include=["object", "datetime", "category"])
    #Sustituir valores nulos con pormedio o media
    cualitativas = cuantitativas_sin_nulos.fillna(0)
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas,cualitativas], axis=1)

    return(Datos_sin_nulos)

######################################################################################################################################################

#Sustitución de valores por método pormedio
def sustitución_promedio(data, col):
    Data_Type=data[col].dtype
    if (Data_Type == "int64") | (Data_Type == "float64"):
    #Primer método de sustitución de valores nulos
    #Sustituir valores nulos con promedio o media
        data[col]=data[col].fillna(round(data[col].mean(),1))
        return (data)
    else: 
            raise ValueError(f"La variable no es numerica, es de tipo: {Data_Type}")

######################################################################################################################################################

def sustitucion_prom_completo(data):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas= data.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = data.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas.fillna(round(cuantitativas.mean(), 1))
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    df = pd.concat([cuantitativas, cualitativas], axis=1)
    return(data)

#######################################################################################################################################################
#Sustitución de valores nulos con el método de “mediana"
def sustitución_mediana(data):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas_con_nulos = data.select_dtypes(include=['float', 'int64', 'float', 'int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = data.select_dtypes(include=['object', 'datetime', 'category'])
    #Sustituir valores nulos con pormedio o media
    cuantitativas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.median(),1))
    #Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas,cualitativas], axis=1)

    return(Datos_sin_nulos)

###############################################################################################################################################################

#Identificación de valores nulos por columna y por dataframe”

def cuenta_valores_nulos(data):
    #Valores nulos por columna
    valores_nulos_cols = data.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = data.isnull().sum().sum()

    return ('Valores nulos por columna' , valores_nulos_cols,
            'Valores nnulos por dataframe', valores_nulos_df)