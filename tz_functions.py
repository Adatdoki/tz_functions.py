# -*- coding: utf-8 -*-
"""TZ_functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GcwBsBAMRkBOAlhJEG_5IivfNzLa_qmk
"""

print(" ############### ADATDOKI függvényei   ############### ")
print(" ############### TZ_functions.py       ############### ")
print(" ############### version = 2024.10.13. ############### ")

################################################################################################################################################################

# di() = teljes szélességű, nem sortört táblázat új függvénnyel

from IPython.display import display, HTML

def di(pr):
    """
    Kiírja az adott pandas DataFrame-et HTML táblázatként, kattintható linkekkel.

    Parameters:
    - pr: pandas DataFrame
    """
    # HTML táblázat generálása kattintható linkekkel
    display(HTML(pr.to_html(escape=False, render_links=True)))

# Példa használat:
# di(df)  # df-nek helyettesítsd be a valós DataFrame-edet


################################################################################################################################################################

# 240510 li() = struktúrált listázó függvény, bővítve alapértelmezettel, teljes szélességű, nem sortört táblázat, sorszám inputtal.************ ADATDOKI ***************
# módosított kód, amely a bemenet bekérését és kiértékelését kihagyja, ha van beállított alapértelmezett érték.
# az alapértelmezett sor beállítható az"enter" változóval, pl. "enter=4" vagy "del enter"
# első paramétere kötelező a "dataframe", második opcionális (az adott futtatásban kiírandó sorok száma, ha -1 akkor az összes sor)
# Kiírja az adott pandas DataFrame-et HTML táblázatként, kattintható linkekkel.

import pandas as pd
from IPython.display import display, HTML

try:
    del enter
    enter  # Ellenőrizzük, hogy az enter változó létezik-e
except NameError:
    # Az enter változó létrehozása és alapértelmezett értékének beállítása
    print("A li() függvény listázásnál, legyen alapértelmezett a sorok száma?")
    enter_input = input(' 0 = ne legyen, azaz listázáskor rákérdez. Vagy szám = ennyi sort listáz rákérdezés nélkül. ("enter" változó)')
    if enter_input == '0':
        enter = None
    elif enter_input.isdigit():
        enter = int(enter_input)
    else:
        print("Érvénytelen bemenet!")
        enter = None

def li(df, rows=None):
    
	# Az rows paraméter használata, ha meg van adva
    if rows is not None:
        if rows == -1:
            display(HTML(df.to_html(escape=False, render_links=True, index=True)))
            print("használat: li(df)  # Használja az 'enter' változó értékét ha létezik és nagyobb mint 0, különben az összes sort megjeleníti vagy li(df, -1)")
        else:
            try:
                # Próbáljuk meg értelmezni, hogy rows szám-e
                display_rows = int(rows)
                display(HTML(df.head(display_rows).to_html(escape=False, render_links=True, index=True)))
                print("használat: li(df)  # Használja az 'enter' változó értékét ha létezik és nagyobb mint 0, különben az összes sort megjeleníti vagy li(df, -1)")
            except ValueError:
                print("A 'rows' paraméternek '*' vagy egy pozitív egész számnak kell lennie.")
                print("használat: li(df)  # Használja az 'enter' változó értékét ha létezik és nagyobb mint 0, különben az összes sort megjeleníti vagy li(df, -1)")
    elif enter and enter > 0:  # Ellenőrizzük, hogy az enter értéke nagyobb-e mint 0
        display(HTML(df.head(enter).to_html(escape=False, render_links=True, index=True)))
        print("használat: li(df)  # Használja az 'enter' változó értékét ha létezik és nagyobb mint 0, különben az összes sort megjeleníti vagy li(df, -1)")
    else:
        display(HTML(pr.to_html(escape=False, render_links=True, index=True)))  # Alapértelmezett vagy összes sor listázása
        print("használat: li(df)  # Használja az 'enter' változó értékét ha létezik és nagyobb mint 0, különben az összes sort megjeleníti vagy li(df, -1)")

# Példa használat:
# li(dataframe) dataframe-nek helyettesítsd be a valós DataFrame-edet
# df = pd.DataFrame({'A': range(1, 6), 'B': range(6, 11)})
# li(df)  # Használja az "enter" értékét ha létezik és nagyobb mint 0, különben az összes sort megjeleníti
# li(df, 2)  # Csak 2 sort jelenít meg a DataFrame-ből

# 240507 *********TZ*********** kilistázza az egyedi értékeket *************ADATDOKI***************
# mind a szöveges, mind a numerikus oszlopokban megszámolja az egyedi értékeket DI kiírással,
# 5 paraméterrel: df_name, beállítható megjelenítési számmal (list_values=5),
# csak 1 oszlop lehetőséggel is (columns=['name', 'start']),
# csak szöveges vagy numerikus oszlopok (dtype="numeric");(dtype="object");(dtype="all")
# Függvény meghívása ötödik paraméterrel, hogy csak keresett értékkel rendelkező sorok jelenjenek meg
# list_unique_values(df_EFC_CZ_merged, list_values=3, columns=['chng', 'chng_1'], dtype="object", search_value="valami")
# minden egyes oszlop mellett ki lesz írva az oszlop típusa is.

################################################################################################################################################################

import numpy as np

def list_unique_values(dataframe, list_values=10, columns=None, dtype="all", search_value=None):
    if columns is None:
        columns = sorted(dataframe.columns.tolist())  # Az oszlopok rendezése növekvő sorrendben

    for column in columns:
        print('PARAMÉTEREZÉS: luv(dataframe, list_values=10, columns=["column1", "column2", ...], dtype="all/object/int64/float64/datetime64", search_value="valami")  = list_unique_values(dataframe)')
        if dtype == "numeric" and not np.issubdtype(dataframe[column].dtype, np.number):
            continue
        elif dtype == "object" and not np.issubdtype(dataframe[column].dtype, object):
            continue

        column_type = dataframe[column].dtype
        if search_value:
            values = dataframe[dataframe[column] == search_value][column].value_counts()
        else:
            values = dataframe[column].value_counts()

        # Értékek rendezése növekvő sorrendben
        values_sorted = values.sort_index()

        # Átmeneti DataFrame létrehozása sorszámozással
        temp_df = pd.DataFrame(values_sorted).rename(columns={column: 'Egyedi db'})
        temp_df.index.name = 'Értékek'
        temp_df.reset_index(inplace=True)
        print(f"Egyedi értékek a(z) \033[1m'{column}'\033[0m '\033[4moszlopban\033[0m', (melynek típusa: {column_type}) (összesen: {len(values)} db) (sorok száma: {len(dataframe)})")
        di(temp_df.head(list_values))
        #di(temp_df.tail(list_values))
        print(f"Sorok száma: {len(dataframe)}")
        print()

# Függvény meghívása alapértelmezett értékkel
# list_unique_values(df_EFC_CZ_merged)

# Függvény meghívása második és harmadik paraméter megadásával
# list_unique_values(df_EFC_CZ_merged, list_values=5, columns=['name', 'start'])  # Például az utolsó 5 érték megjelenítése a "name" és "start" oszlopokban

# Függvény meghívása negyedik paraméterrel, hogy csak szöveges vagy numerikus oszlopok jelenjenek meg
# list_unique_values(df_EFC_CZ_merged, list_values=5, columns=['chng', 'chng_1'], dtype="numeric")

# Függvény meghívása keresendő értékkel
# list_unique_values(df_EFC_CZ_merged, search_value="valami")

# Függvény meghívása ötödik paraméterrel, hogy csak keresett értékkel rendelkező sorok jelenjenek meg
# list_unique_values(df_EFC_CZ_merged, list_values=15, columns=['chng', 'chng_1', 'chng_2',], dtype="object", search_value="vběhl")
# list_unique_values(df_EFC_CZ_merged, list_values=15, search_value="vběhl")
# list_unique_values(df_EFC_CZ_merged, list_values=15)

def luv(dataframe, list_values=10, columns=None, dtype="all", search_value=None):
    list_unique_values(dataframe, list_values, columns, dtype, search_value)

################################################################################################################################################################

# plot_histograms 240821
"""
Ebben a kódban a plot_histograms függvényt definiáljuk, amely paraméterként várja a DataFrame nevét (dataframe_name).
A függvény megpróbálja betölteni a megadott DataFrame-et, és ha nem találja, hibát kezel.
Az iteráció és hisztogram kirajzolás része ugyanaz maradt. Most példa használatként megadhatod a DataFrame nevét a plot_histograms függvényben.
Ebben a kódban az `x_bin_width` és `y_bin_width` változókat 1%-os értékekre állítottam,
majd ezeket használtam a `bins` paraméterek megfelelő számának kiszámításához mind az X, mind az Y tengelyen.
`bin_width` értéke az adott oszlop MAX-MIN értékeinek megadott %-ától függ
"""

import matplotlib.pyplot as plt
import pandas as pd

def plot_histograms(df):
    try:
        print("Ilyen oszlopaink vannak: (csak a numerikusokról hisztogram)")
        df.info()

        # Iteráció az oszlopokon és hisztogramok kirajzolása
        for column in df.columns:
            if pd.api.types.is_numeric_dtype(df[column]):
                # Szűrjük ki a NaN értékeket
                col_data = df[column].dropna()

                # Ellenőrizzük, hogy van-e legalább két különböző érték
                if col_data.nunique() > 1:
                    bin_width = 0.01 * (col_data.max() - col_data.min())
                    bins = int((col_data.max() - col_data.min()) / bin_width)

                    plt.figure(figsize=(8, 6))
                    plt.hist(col_data, bins=bins, color='blue', edgecolor='black', alpha=0.5)
                    plt.title(f'Histogram of {column}')
                    plt.xlabel(column)
                    plt.ylabel('Frequency')
                    plt.show()

                    # Feltételezve, hogy a Pearson_egy_oszlop_vizsgalata függvény létezik
                    print(Pearson_egy_oszlop_vizsgalata(df, column))
                    print("=============================================================================================================================================================")

                else:
                    print(f"Az '{column}' oszlopban nincs elegendő változatosság a hisztogram készítéséhez.")

    except KeyError:
        print("Hiba: A DataFrame nem található.")

# Példa használat:
# plot_histograms(df)


################################################################################################################################################################

import numpy as np  # NumPy importálása
from scipy import stats  # Scipy importálása a statisztikai műveletekhez

def numeric_column_summary_statistics(df):
    # Az összes oszlop fejlécének kiválasztása
    all_columns = df.columns

    # Csak a számot tartalmazó oszlopok kiválasztása
    numeric_columns = df.select_dtypes(include='number').columns

    # Statisztikák kiszámolása minden oszlopra
    statistics = pd.DataFrame(index=['Min', 'Max', 'Átlag', 'Medián', 'Modusz', 'Variabilitás', 'Alsó Kvantil', 'Felső Kvantil',
                                     'Korreláció', 'Kovariancia', 'Százalékos Változás', 'Konfidencia-intervallumok',
                                     'Lineáris Regresszió Együtthatók'], columns=all_columns)

    for column in all_columns:
        if column in numeric_columns:
            statistics.at['Min', column] = df[column].min()
            statistics.at['Max', column] = df[column].max()
            statistics.at['Átlag', column] = df[column].mean()
            statistics.at['Medián', column] = df[column].median()
            statistics.at['Modusz', column] = df[column].mode().iloc[0]  # Modusz számítása
            statistics.at['Variabilitás', column] = df[column].std()  # Szórás
            statistics.at['Alsó Kvantil', column] = df[column].quantile(0.25)  # Alsó kvantil
            statistics.at['Felső Kvantil', column] = df[column].quantile(0.75)  # Felső kvantil
            # Korreláció és kovariancia kiszámítása a többi oszloppal
            for other_column in numeric_columns:
                if other_column != column:
                    statistics.at['Korreláció', column] = df[column].corr(df[other_column])
                    statistics.at['Kovariancia', column] = df[column].cov(df[other_column])
            # Százalékos változás számítása
            first_value = df[column].iloc[0]
            last_value = df[column].iloc[-1]
            statistics.at['Százalékos Változás', column] = ((last_value - first_value) / first_value) * 100
            # Konfidencia-intervallumok
            confidence_interval = stats.norm.interval(0.95, loc=df[column].mean(), scale=df[column].std())
            statistics.at['Konfidencia-intervallumok', column] = confidence_interval
            # Lineáris regresszió együtthatók
            # Ez csak egy példa, itt valószínűleg több munka és elemzés kellene
            slope, intercept, r_value, p_value, std_err = stats.linregress(df[column], df['start'])
            statistics.at['Lineáris Regresszió Együtthatók', column] = (slope, intercept, r_value, p_value, std_err)
        else:
            # Nem szám típusú oszlopoknak NaN értékeket adunk
            statistics.at['Min', column] = np.nan
            statistics.at['Max', column] = np.nan
            statistics.at['Átlag', column] = np.nan
            statistics.at['Medián', column] = np.nan
            statistics.at['Modusz', column] = np.nan
            statistics.at['Variabilitás', column] = np.nan
            statistics.at['Alsó Kvantil', column] = np.nan
            statistics.at['Felső Kvantil', column] = np.nan
            statistics.at['Korreláció', column] = np.nan
            statistics.at['Kovariancia', column] = np.nan
            statistics.at['Százalékos Változás', column] = np.nan
            statistics.at['Konfidencia-intervallumok', column] = np.nan
            statistics.at['Lineáris Regresszió Együtthatók', column] = np.nan

    # Statisztikák kiíratása
    print("Összefoglaló statisztikák minden oszlopra:")
    display(statistics)

# numeric_column_summary_statistics(df)

################################################################################################################################################################

######### 2024.10.27 22:58:00 ################################## ADATDOKI ######
# A DataFrame oszlopainak tulajdonságait összegző funkció. Egy dataframe adatainak táblázatos statisztikája.
# https://chatgpt.com/g/g-1NfAVvTfO-hu-jup-python-mester/c/670f693a-a67c-8005-9ffd-140995861135
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Kifejezés            | Leírás
---------------------|-----------------------------------------------------
Dtype                | Az oszlop adattípusa.
count                | Az oszlopban lévő nem NaN értékek száma.
unique               | Az oszlopban lévő egyedi értékek száma.
top                  | Az oszlopban leggyakrabban előforduló érték.
freq                 | Az oszlopban leggyakrabban előforduló érték gyakorisága.
mean                 | Az oszlopban lévő értékek átlaga.
std                  | Az oszlopban lévő értékek szórása.
min                  | Az oszlop legkisebb értéke.
25%                  | Az oszlop alsó kvartilise (25%-os percentilis).
50%                  | Az oszlop mediánja (50%-os percentilis).
75%                  | Az oszlop felső kvartilise (75%-os percentilis).
max                  | Az oszlop legnagyobb értéke.
first                | Az oszlopban az első nem NaN érték.
last                 | Az oszlopban az utolsó nem NaN érték.
NaN_count            | Az oszlopban lévő NaN értékek száma.
unique_top           | Az oszlopban lévő egyedi értékek közül a leggyakoribb.
unique_top_count     | Az oszlopban lévő egyedi értékek közül a leggyakoribb érték előfordulásainak száma.

"""

import inspect

# Dekorátor függvény létrehozása
def add_df_name(func):
    def wrapper(df):
        # Az aktuális hívási keretet megvizsgáljuk, hogy lekérjük a változó nevét
        frame = inspect.currentframe().f_back
        df_name = None
        
        # Végigmegyünk a változókon, és megkeressük azt, amelyik a DataFrame-re mutat
        for name, val in frame.f_locals.items():
            if val is df:
                df_name = name
                break
        
        # Ha megtaláltuk a nevet, átadjuk azt a dinfo-nak
        return func(df, df_name)
    
    return wrapper

# A dinfo függvény
@add_df_name  # Ezzel a dekorátorral "díszítjük" a dinfo-t
def dinfo(df, df_name):
    # Ellenőrizzük, hogy a DataFrame nem üres
    if df.empty:
        print(f"A {df_name} DataFrame üres.")
        return

    # Kiírjuk az oszlopok statisztikai jellemzőit és a sorok számát
    print(f"\n({df_name}) DataFrame oszlopainak statisztikái: {len(df)} sorból áll.")
    
    # Külön listák a numerikus és nem numerikus oszlopok számára
    numeric_stats = []
    non_numeric_stats = []

    # Minden oszlopot külön-külön ellenőrzünk
    for col in df.columns:
        try:
            # Próbálunk numerikus statisztikát kiszámítani az oszlopra
            col_stats = df[[col]].describe().T  # Ha sikerül, numerikus
            numeric_stats.append(col_stats)
        except (ValueError, TypeError):
            # Ha nem numerikus, akkor csak alap statisztikákat számolunk
            col_stats = df[[col]].describe(include='all').T
            non_numeric_stats.append(col_stats)

    # Egyesítjük a numerikus és nem numerikus statisztikákat
    if numeric_stats:
        numeric_stats_df = pd.concat(numeric_stats, axis=0)
    else:
        numeric_stats_df = pd.DataFrame()

    if non_numeric_stats:
        non_numeric_stats_df = pd.concat(non_numeric_stats, axis=0)
    else:
        non_numeric_stats_df = pd.DataFrame()

    # Összevonjuk a statisztikai adatokat egy DataFrame-be
    statistics_df = pd.concat([numeric_stats_df, non_numeric_stats_df], axis=0)

    # Ellenőrizzük, hogy minden szükséges oszlop létezik-e, ha nem, akkor hozzáadjuk None értékkel
    required_columns = ['count', 'unique', 'top', 'freq', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
    for col in required_columns:
        if col not in statistics_df.columns:
            statistics_df[col] = None

    # Hozzáadjuk az első és utolsó elemet, ha vannak adatok
    statistics_df['first'] = df.apply(lambda x: x.dropna().iloc[0] if not x.dropna().empty else None)
    statistics_df['last'] = df.apply(lambda x: x.dropna().iloc[-1] if not x.dropna().empty else None)

    # NaN értékek számolása
    statistics_df['NaN_count'] = df.isnull().sum()

    # Leggyakoribb egyedi érték
    unique_top_values = df.apply(lambda x: x.value_counts().index[0] if not x.value_counts().empty else None)
    statistics_df['unique_top'] = unique_top_values

    # Leggyakoribb egyedi érték darabszáma
    unique_top_counts = df.apply(lambda x: x.value_counts().max() if not x.value_counts().empty else None)
    statistics_df['unique_top_count'] = unique_top_counts

    # Oszlopok típusának hozzáadása
    statistics_df.insert(1, 'Dtype', df.dtypes)

    # Oszlopok típusának hozzáadása és új sorrend
    statistics_df.insert(0, '#', range(1, len(statistics_df) + 1))
    statistics_df = statistics_df[['#', 'Dtype', 'count', 'unique', 'top', 'freq', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'first', 'last', 'NaN_count', 'unique_top', 'unique_top_count']]

    # Itt a statisztikák megjelenítése (feltételezem, hogy van egy di() függvényed erre)
    di(statistics_df)

    return

# használat:
# dinfo(df)

################################################################################################################################################################

# 240507 *********TZ*********** datainfo *************ADATDOKI***************
# kilistázza a dataframe tulajdonságait
databases = ["default_dataframe"]  # Alapértelmezett DataFrame
#functions = [".info()", ".describe()", ".head()", "", ".dtypes"]
functions = [".info()", ".describe()", "",]

def datainfo(dataframe=None):
    if dataframe is None:
        dataframe = databases[0]

    for f in functions:
        command = dataframe + f
        print("\n==>", command)
        output = eval(command)
        print(output)

# Használat: datainfo() vagy datainfo("custom_dataframe")

###################################################################################################################################################

import numpy as np  # NumPy importálása
from scipy import stats  # Scipy importálása a statisztikai műveletekhez

def numeric_column_summary_statistics(df):
    # Az összes oszlop fejlécének kiválasztása
    all_columns = df.columns

    # Csak a számot tartalmazó oszlopok kiválasztása
    numeric_columns = df.select_dtypes(include='number').columns

    # Statisztikák kiszámolása minden oszlopra
    statistics = pd.DataFrame(index=['Min', 'Max', 'Átlag', 'Medián', 'Modusz', 'Variabilitás', 'Alsó Kvantil', 'Felső Kvantil',
                                     'Korreláció', 'Kovariancia', 'Százalékos Változás', 'Konfidencia-intervallumok',
                                     'Lineáris Regresszió Együtthatók'], columns=all_columns)

    for column in all_columns:
        if column in numeric_columns:
            statistics.at['Min', column] = df[column].min()
            statistics.at['Max', column] = df[column].max()
            statistics.at['Átlag', column] = df[column].mean()
            statistics.at['Medián', column] = df[column].median()
            statistics.at['Modusz', column] = df[column].mode().iloc[0]  # Modusz számítása
            statistics.at['Variabilitás', column] = df[column].std()  # Szórás
            statistics.at['Alsó Kvantil', column] = df[column].quantile(0.25)  # Alsó kvantil
            statistics.at['Felső Kvantil', column] = df[column].quantile(0.75)  # Felső kvantil
            # Korreláció és kovariancia kiszámítása a többi oszloppal
            for other_column in numeric_columns:
                if other_column != column:
                    statistics.at['Korreláció', column] = df[column].corr(df[other_column])
                    statistics.at['Kovariancia', column] = df[column].cov(df[other_column])
            # Százalékos változás számítása
            first_value = df[column].iloc[0]
            last_value = df[column].iloc[-1]
            statistics.at['Százalékos Változás', column] = ((last_value - first_value) / first_value) * 100
            # Konfidencia-intervallumok
            confidence_interval = stats.norm.interval(0.95, loc=df[column].mean(), scale=df[column].std())
            statistics.at['Konfidencia-intervallumok', column] = confidence_interval
            # Lineáris regresszió együtthatók
            # Ez csak egy példa, itt valószínűleg több munka és elemzés kellene
            slope, intercept, r_value, p_value, std_err = stats.linregress(df[column], df['start'])
            statistics.at['Lineáris Regresszió Együtthatók', column] = (slope, intercept, r_value, p_value, std_err)
        else:
            # Nem szám típusú oszlopoknak NaN értékeket adunk
            statistics.at['Min', column] = np.nan
            statistics.at['Max', column] = np.nan
            statistics.at['Átlag', column] = np.nan
            statistics.at['Medián', column] = np.nan
            statistics.at['Modusz', column] = np.nan
            statistics.at['Variabilitás', column] = np.nan
            statistics.at['Alsó Kvantil', column] = np.nan
            statistics.at['Felső Kvantil', column] = np.nan
            statistics.at['Korreláció', column] = np.nan
            statistics.at['Kovariancia', column] = np.nan
            statistics.at['Százalékos Változás', column] = np.nan
            statistics.at['Konfidencia-intervallumok', column] = np.nan
            statistics.at['Lineáris Regresszió Együtthatók', column] = np.nan

    # Statisztikák kiíratása
    print("Összefoglaló statisztikák minden oszlopra:")
    display(statistics)

# numeric_column_summary_statistics(df)

##############################################################################################################################################

# 240510 Értékek listázása választható oszlopokban
import shutil

def values(dataframe, columns, max_values_per_line=20, sorted=False):
    for column in columns:
        # Számként értelmezhető értékek keresése
        numeric_values = pd.to_numeric(dataframe[column], errors='coerce')

        # Normálalakos számokat keresünk, amelyeket nem tudunk értelmezni
        non_normal_numeric_values = dataframe[column][~numeric_values.notnull()].unique()

        # Statisztikák numerikus értékekről
        if len(numeric_values.dropna()) > 0:
            print(f"Statistics for column '{column}' (numerical values):")
            print(numeric_values.dropna().describe())
            print()

        # Egyedi értékek numerikus értékekről
        unique_numeric_values = numeric_values.dropna().unique()
        if len(unique_numeric_values) > 0:
            if sorted:
                unique_numeric_values.sort()
            print(f"Unique values in column '{column}' (numerical values):")
            terminal_width = shutil.get_terminal_size().columns
            values_per_line = min(max_values_per_line, terminal_width // 7)  # 7 is the average width of a float number
            for i in range(0, len(unique_numeric_values), values_per_line):
                print("\t".join([f"{value:.2f}" for value in unique_numeric_values[i:i+values_per_line]]))
            print()

        # Nem numerikus értékek listázása
        if len(non_normal_numeric_values) > 0:
            print(f"Non-numeric values in column '{column}':")
            if sorted:
                print(", ".join(map(str, non_normal_numeric_values)))
            else:
                print(", ".join(sorted(map(str, non_normal_numeric_values))))
            print()
			
# Függvény meghívása az adott DataFrame és oszlop nevével
# values(df_EFC_CZ_merged, ('sorsz', 'Division', 'when', 'who', 'with_who', 'total_time', 'W/L/T', 'Hurdles', 'name', 'start', '1_dog', 'name_1', 'chng', '2_dog', 'name_2', 'chng_1', '3_dog', 'name_3', 'chng_2', '4_dog', 'event_place', 'when_date', 'when_time', 'track'), max_values_per_line=25, sorted=True)
# values(df_EFC_CZ_merged, ('start', 'chng', 'chng_1', 'chng_2'), sorted=True)

##############################################################################################################################################

#240331 mind a szöveges, mind a numerikus oszlopokban megszámolja az egyedi értékeket DI kiírással, beállítható megjelenítési számmal, csak 1 oszlop lehetőséggel is
def list_unique_values_240331(dataframe, list_values=10, columns=None):
    if columns is None:
        columns = dataframe.columns.tolist()

    for column in columns:
        values = dataframe[column].value_counts()
        # Átmeneti DataFrame létrehozása sorszámozással
        temp_df = pd.DataFrame(values).rename(columns={column: 'Egyedi db'})
        temp_df.index.name = 'Értékek'
        temp_df.reset_index(inplace=True)
        print(f"Egyedi értékek a(z) '{column}' oszlopban (összesen: {len(values)} db):")
        di(temp_df.head(list_values))
        di(temp_df.tail(list_values))
        print()

# Függvény meghívása alapértelmezett értékkel
#list_unique_values(df_EFC_CZ_merged)

# Függvény meghívása második és harmadik paraméter megadásával
# list_unique_values_240331(df_EFC_CZ_merged, list_values=5, columns=['name', 'start'])  # Például az utolsó 5 érték megjelenítése a "name" és "start" oszlopokban
# list_unique_values_240331(df_EFC_CZ_merged, list_values=25, columns=['start', 'chng', 'chng_1', 'chng_2'])

##############################################################################################################################################
# 240821 A DataFrame összes oszlopán végigiterál, és minden oszlopra megvizsgálja, hogy megfelel-e a Pearson-féle korrelációs együttható feltételeinek.
import numpy as np
import pandas as pd
import scipy.stats as stats

def Pearson_egy_oszlop_vizsgalata(df, oszlop, folytonos_kuszob=20, min_kulonbseg_kuszob=0.01):
    """
    Egy adott oszlop vizsgálata a Pearson-féle korrelációs együttható feltételeinek szempontjából.
    
    Paraméterek:
    df : pd.DataFrame
        Az adatokat tartalmazó DataFrame.
    oszlop : str
        A vizsgálandó oszlop neve.
    folytonos_kuszob : int
        Az egyedi értékek számának küszöbe, amely felett folytonosnak tekintjük a változót.
    min_kulonbseg_kuszob : float
        Az értékek közötti minimális különbség küszöbe, amely alatt a változót folytonosnak tekintjük.
    
    Visszatérési érték:
    dict : Az ellenőrzési eredmények szótára.
    """
    eredmenyek = {}
    
    try:
        # 1. Numerikus változók ellenőrzése
        if pd.api.types.is_numeric_dtype(df[oszlop]):
            eredmenyek['numerikus_valtozok'] = True
        else:
            eredmenyek['numerikus_valtozok'] = False

        # 2. Normál eloszlás ellenőrzése (Shapiro-Wilk teszt)
        _, p_x = stats.shapiro(df[oszlop])

        # A Shapiro-Wilk teszt p-értéke alapján döntsünk: ha p > 0.05, akkor normális eloszlású
        eredmenyek['normal_eloszlas_x'] = p_x > 0.05

        # 3. Folytonos változók ellenőrzése

        # 3.1 Egyedi értékek számának vizsgálata
        egyedi_ertekek_x = df[oszlop].nunique()
        eredmenyek['folytonos_valtozo_x_ertekszam'] = egyedi_ertekek_x > folytonos_kuszob

        # 3.2 Értékek közötti különbségek vizsgálata
        kulonbsegek_x = np.diff(np.sort(df[oszlop].unique()))
        min_kulonbseg_x = np.min(kulonbsegek_x)
        eredmenyek['folytonos_valtozo_x_kulonbseg'] = min_kulonbseg_x < min_kulonbseg_kuszob

        # A két kritérium kombinálásával megállapítjuk, hogy folytonos-e a változó
        eredmenyek['folytonos_x'] = (eredmenyek['folytonos_valtozo_x_ertekszam'] and eredmenyek['folytonos_valtozo_x_kulonbseg'])

    except Exception as e:
        # Hibakezelés: Ha valami hiba történik, rögzítjük az üzenetet
        eredmenyek['hiba'] = str(e)

    return eredmenyek

def Pearson_osszes_oszlop_vizsgalata(df):
    """
    A DataFrame összes oszlopán végigiterál, és minden oszlopra megvizsgálja, hogy megfelel-e a Pearson-féle korrelációs együttható feltételeinek.
    
    Paraméter:
    df : pd.DataFrame
        Az elemzendő adatkeret.
    """
    for oszlop in df.columns:
        print(f'\nOszlop név: {oszlop}')
        print('-----------------------')
        eredmeny = Pearson_egy_oszlop_vizsgalata(df, oszlop)
        for kulcs, ertek in eredmeny.items():
            print(f'{kulcs}: {ertek}')

# Példafelhasználás:
# df = pd.read_csv("adatok.csv")
# Pearson_osszes_oszlop_vizsgalata(df)


#############################################################################################################################################

# 240821 ColStat, Column statisztika
import numpy as np
import pandas as pd
import scipy.stats as stats

def egy_oszlop_vizsgalata(df, oszlop, folytonos_kuszob=20, min_kulonbseg_kuszob=0.01):
    """
    Egy adott oszlop vizsgálata a Pearson-féle korrelációs együttható feltételeinek szempontjából.
    
    Paraméterek:
    df : pd.DataFrame
        Az adatokat tartalmazó DataFrame.
    oszlop : str
        A vizsgálandó oszlop neve.
    folytonos_kuszob : int
        Az egyedi értékek számának küszöbe, amely felett folytonosnak tekintjük a változót.
    min_kulonbseg_kuszob : float
        Az értékek közötti minimális különbség küszöbe, amely alatt a változót folytonosnak tekintjük.
    
    Visszatérési érték:
    dict : Az ellenőrzési eredmények szótára.
    """
    eredmenyek = {
        'numerikus_valtozok': False,
        'normal_eloszlas_x': False,
        'folytonos_valtozo_x_ertekszam': False,
        'folytonos_valtozo_x_kulonbseg': False,
        'folytonos_x': False,
        'hiba': np.nan  # Eredetileg nincs hiba
    }
    
    try:
        # 1. Numerikus változók ellenőrzése
        if pd.api.types.is_numeric_dtype(df[oszlop]):
            eredmenyek['numerikus_valtozok'] = True

            # 2. Normál eloszlás ellenőrzése (Shapiro-Wilk teszt)
            _, p_x = stats.shapiro(df[oszlop].dropna())
            eredmenyek['normal_eloszlas_x'] = p_x > 0.05  # Ha p > 0.05, akkor normál eloszlású

            # 3. Folytonos változók ellenőrzése

            # 3.1 Egyedi értékek számának vizsgálata
            egyedi_ertekek_x = df[oszlop].nunique()
            eredmenyek['folytonos_valtozo_x_ertekszam'] = egyedi_ertekek_x > folytonos_kuszob

            # 3.2 Értékek közötti különbségek vizsgálata
            kulonbsegek_x = np.diff(np.sort(df[oszlop].dropna().unique()))
            min_kulonbseg_x = np.min(kulonbsegek_x) if len(kulonbsegek_x) > 0 else np.inf
            eredmenyek['folytonos_valtozo_x_kulonbseg'] = min_kulonbseg_x < min_kulonbseg_kuszob

            # Kombinált kritérium alapján folytonosság ellenőrzése
            eredmenyek['folytonos_x'] = eredmenyek['folytonos_valtozo_x_ertekszam'] and eredmenyek['folytonos_valtozo_x_kulonbseg']

    except Exception as e:
        # Hibakezelés: Ha valami hiba történik, rögzítjük az üzenetet
        eredmenyek['hiba'] = str(e)

    return eredmenyek

def colstat(df):
    """
    A DataFrame összes oszlopán végigiterál, megvizsgálja őket, és egy jelentés formájában kiírja az eredményeket.
    
    Paraméter:
    df : pd.DataFrame
        Az elemzendő adatkeret.
    
    Kimenet:
    pd.DataFrame : A jelentés, amely tartalmazza minden oszlop vizsgálatának eredményeit.
    """
    print("a Dataframe sorainak száma: ", len(df))
    jelentés = []
    
    for oszlop in df.columns:
        eredmeny = egy_oszlop_vizsgalata(df, oszlop)
        sor = {
            'Column': oszlop,
            'Non-Null Count': df[oszlop].count(),
            'NaN Count': df[oszlop].isna().sum(),
            'Zero Count': (df[oszlop] == 0).sum().sum(),
            'Dtype': df[oszlop].dtype,
        }
        sor.update(eredmeny)
        jelentés.append(sor)
    
    jelentés_df = pd.DataFrame(jelentés)
    return jelentés_df

# Példafelhasználás:
# df = pd.read_csv("adatok.csv")
# jelentés = colstat(df)
# print(jelentés)
# di(jelentés) ez struktúráltabb

###########################################################################################################################

# 240821 színezett_korrelácios_mátrix
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def korrelacios_matrix(df):
    """
    Létrehoz egy korrelációs mátrixot a DataFrame oszlopai között.
    
    Paraméter:
    df : pd.DataFrame
        A bemeneti adatkeret.
    
    Visszatérési érték:
    pd.DataFrame : A korrelációs mátrix.
    """
    # Véletlen oszlop generálása
    df['veletlen_oszlop'] = np.random.randn(len(df))
    
    # Korrelációs mátrix számítása
    corr_matrix = df.corr()
    
    return corr_matrix

def szinezett_korrelacios_matrix(df):
    """
    Megjeleníti a korrelációs mátrixot színezett hőtérképként szélesebb cellákkal és 5 tizedesjeggyel.
    
    Paraméter:
    df : pd.DataFrame
        A bemeneti adatkeret.
    """
    # Korrelációs mátrix létrehozása
    corr_matrix = korrelacios_matrix(df)
    
    # Hőtérkép megjelenítése szélesebb cellákkal és 5 tizedesjeggyel
    plt.figure(figsize=(21, 8))  # Növeljük a cellák szélességét a figsize paraméterrel
    sns.heatmap(
        corr_matrix, 
        annot=True, 
        cmap='coolwarm', 
        vmin=-1, 
        vmax=1, 
        center=0, 
        fmt=".5f",  # Formázzuk az annotációkat 5 tizedesjegyre
        annot_kws={"size": 10}  # Beállíthatjuk a betűméretet is, ha szükséges
    )
    plt.title('Korrelációs mátrix hőtérképe')
    plt.show()

# Példafelhasználás:
# df = pd.read_csv("adatok.csv")
# szinezett_korrelacios_matrix(df)

#############################################################################################################################

######### 2024.10.14 09:15:00 ################################## ADATDOKI ######
# A teljes képernyő szélességű kódmegjelenítést biztosít Jupyter NbClassic-ban.
# Jupyter NbClassic-ban működik csak (localhost:8888/nbclassic/notebooks/)
#########1#########2#########3#########4#########5#########6#########7#########8

# Importáljuk a szükséges modulokat az ajánlott IPython.display-ből
from IPython.display import display, HTML

# Teljes képernyős szélességet biztosít a Jupyter Notebookban
display(HTML("<style>.container { width:100% !important; }</style>"))
print('display(HTML("<style>.container { width:100% !important; }</style>"))')
###############################################################################################################################################################
