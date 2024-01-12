import streamlit as st
import pandas as pd
import numpy as np

# create an empty dataframe with column names "Mægler", "Placering", "Kvalitet", "Kategori", "Leje", "Afkast"
tabel = pd.DataFrame(columns=["Mægler", "Placering", "Kvalitet", "Kategori", "Leje", "Afkast"])

# add observations to the dataframe
tabel.loc[0] = ["Colliers", "København", "Primær", np.NaN, 2450, 3.88]
tabel.loc[1] = ["Colliers", "København", "Sekundær", np.NaN, 1850, 4.25]
tabel.loc[2] = ["Nordicals", "København", "Primær", "< 65 m2", 2400, 3.75]
tabel.loc[3] = ["Nordicals", "København", "Sekundær", "< 65 m2", 2000, 3.75]
tabel.loc[4] = ["Nordicals", "København", "Primær", "65-85 m2", 2200, 3.75]
tabel.loc[5] = ["Nordicals", "København", "Sekundær", "65-85 m2", 1900, 4.25]
tabel.loc[6] = ["Nordicals", "København", "Primær", "85-100 m2", 2050, 3.75]
tabel.loc[7] = ["Nordicals", "København", "Sekundær", "85-100 m2", 1750, 4.25]
tabel.loc[8] = ["Nordicals", "København", "Primær", "> 100 m2", 2050, 3.75]
tabel.loc[9] = ["Nordicals", "København", "Sekundær", "> 100 m2", 1600, 4.25]
tabel.loc[10] = ["EDC", "København City", "Primær", "Nyere ejendomme", 2550, 4.00]
tabel.loc[11] = ["EDC", "København City", "Sekundær", "Nyere ejendomme", 2200, 4.25]
tabel.loc[12] = ["EDC", "København City", "Tertiær", "Nyere ejendomme", 2000, 4.50]
tabel.loc[13] = ["EDC", "Østerbro, Frederiksberg og Gentofte", "Primær", "Nyere ejendomme", 2450, 4.00]
tabel.loc[14] = ["EDC", "Østerbro, Frederiksberg og Gentofte", "Sekundær", "Nyere ejendomme", 2100, 4.25]
tabel.loc[15] = ["EDC", "Østerbro, Frederiksberg og Gentofte", "Tertiær", "Nyere ejendomme", 1950, 4.50]
tabel.loc[16] = ["EDC", "København City", "Primær", "Fuldt udviklede ejendomme", 1800, 4.00]
tabel.loc[17] = ["EDC", "København City", "Sekundær", "Fuldt udviklede ejendomme", 1650, 4.25]
tabel.loc[18] = ["EDC", "København City", "Tertiær", "Fuldt udviklede ejendomme", 1500, 4.50]
tabel.loc[19] = ["EDC", "Østerbro, Frederiksberg og Gentofte", "Primær", "Fuldt udviklede ejendomme", 1750, 4.00]
tabel.loc[20] = ["EDC", "Østerbro, Frederiksberg og Gentofte", "Sekundær", "Fuldt udviklede ejendomme", 1650, 4.50]
tabel.loc[21] = ["EDC", "Østerbro, Frederiksberg og Gentofte", "Tertiær", "Fuldt udviklede ejendomme", 1550, 4.75]

# show df
st.title('Leje- og afkastdata for København')
st.dataframe(tabel, width=1400, height=500)  # Adjust width and height as needed

st.title('Beregn månedlig leje per person')

# User inputs
price = st.number_input("Indtast lejlighedens pris (kr):", min_value=3000000)
size = st.number_input("Indtast lejlighedens størrelse (m2):", min_value=50)
people = st.number_input("Indtast antal personer:", min_value=1)

# Allow the user to select rows
selected_indices = st.multiselect('Vælg relevante rækker til udregning', tabel.index)
selected_rows = tabel.loc[selected_indices]

# Display selected rows
st.write('Valgte leje- og afkastniveauer', selected_rows)

# Calculate and display the expected monthly rent per person
if len(selected_rows) > 0 and people > 0:
    st.write("Forventet månedlig leje per person:")
    for method in ['Leje', 'Afkast']:
        if method == 'Leje':
            rent_per_person = selected_rows['Leje'] * size / 12 / people
        else:
            rent_per_person = selected_rows['Afkast'] / 100 * price / 12 / people
        st.write(f"{method}baseret metode:")
        st.write(rent_per_person)






