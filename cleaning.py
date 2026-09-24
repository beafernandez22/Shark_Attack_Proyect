import pandas as pd

# Limpia y estandariza la columna Country
def clean_country(df):
    df["Country"] = (
        df["Country"]
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.upper()
        .fillna("UNKNOWN")
    )
    return df


# Limpia y estandariza la columna State
def clean_state(df):
    df["State"] = (
        df["State"]
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.title()
        .fillna("Unknown")
    )
    return df


# Ejecuta la limpieza de las columnas geográficas
def clean_geographic_data(df):
    df = clean_country(df)
    df = clean_state(df)
    return df


# Limpia y formatea la columna Year
def clean_year(df):
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Year"] = df["Year"].astype("Int64")
    return df

# Limpia la columna Activity
def clean_activity(df):
    df["Activity"] = (
        df["Activity"]
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.lower()
        .replace("", pd.NA)
        .fillna("unknown")
    )
    return df

# Limpia y estandariza la columna de fatalidad
def clean_fatal(df):
    df["Fatal Y/N"] = (
        df["Fatal Y/N"]
        .astype("string")
        .str.strip()
        .str.upper()
    )

    df.loc[~df["Fatal Y/N"].isin(["Y", "N"]), "Fatal Y/N"] = "UNKNOWN"

    return df


# Ejecuta la limpieza completa de las cinco variables
def clean_data(df):
    df = clean_country(df)
    df = clean_state(df)
    df = clean_year(df)
    df = clean_activity(df)
    df = clean_fatal(df)

    return df



# Calcula el número de ataques por periodo
def ataques_por_periodo(df):
    conteo = (
        df["Periodo"]
        .value_counts()
        .sort_index()
        .to_frame("Ataques")
    )

    duracion = {
        "hasta 1800": None,
        "1801-1900": 100,
        "1901-1910": 10,
        "1911-1920": 10,
        "1921-1930": 10,
        "1931-1940": 10,
        "1941-1950": 10,
        "1951-1960": 10,
        "1961-1970": 10,
        "1971-1980": 10,
        "1981-1990": 10,
        "1991-2000": 10,
        "2001-2010": 10,
        "2011-2020": 10,
        "2021-2026": 6,
    }

    conteo["Años"] = conteo.index.map(duracion)

    conteo["Ataques_por_año"] = (
        conteo["Ataques"] / conteo["Años"]
    ).round(1)

    return conteo[
        ["Ataques", "Años", "Ataques_por_año"]
    ]


# Guarda la columna de años en etiquedas por periodo
def ataques_por_periodo(df):
    conteo = df["Periodo"].value_counts().sort_index().to_frame("Ataques")

    duracion = {
        "hasta 1800": None,
        "1801-1900": 100,
        "1901-1910": 10, "1911-1920": 10, "1921-1930": 10,
        "1931-1940": 10, "1941-1950": 10, "1951-1960": 10,
        "1961-1970": 10, "1971-1980": 10, "1981-1990": 10,
        "1991-2000": 10, "2001-2010": 10, "2011-2020": 10,
        "2021-2026": 6,
    }

    conteo["Años"] = conteo.index.map(duracion)
    conteo["Ataques_por_año"] = (conteo["Ataques"] / conteo["Años"]).round(1)
    return conteo[["Ataques", "Años", "Ataques_por_año"]]




