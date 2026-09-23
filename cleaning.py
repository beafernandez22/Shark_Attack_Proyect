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