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