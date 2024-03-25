#1.0:
import pandas as pd
import plotly.express as graph
import matplotlib.pyplot as plt
def create_pokedex(file_path):
    df=pd.read_csv(file_path)
    return df
de=create_pokedex("pokemon.csv")
print(de.head(5))

#1.1

def filtrer(pokedex_df):

    garder = ["name", "type1", "type2", "attack", "defense", "hp", "speed", "generation", "height_m",
                       "weight_kg", "capture_rate", "is_legendary"]


    pokedex_df.drop(columns=[col for col in pokedex_df.columns if col not in garder], inplace=True)


    return pokedex_df



filtredf = filtrer(de)


print(filtredf.head(5))

#1.2
filtredf = filtredf.rename(columns={
    "name": "Name",
    "type1": "Primary Type",
    "type2": "Secondary Type",
    "attack": "Attack",
    "defense": "Defense",
    "hp": "HP",
    "speed": "Speed",
    "generation": "Generation",
    "height_m": "Height",
    "weight_kg": "Weight",
    "capture_rate": "Capture Rate",
    "is_legendary": "Legendary"
})
print(filtredf.head(5))

#1.3
filtredf = filtredf.drop_duplicates()
gardercolonne = filtredf.columns[filtredf.columns != 'Secondary Type']
filtredf = filtredf.dropna(subset=gardercolonne)
print(filtredf.head(5))

#1.4

filtredf['Attack'] = filtredf['Attack'].astype(int)
filtredf['Generation'] = filtredf['Generation'].astype(int)
filtredf['HP'] = filtredf['HP'].astype(int)
filtredf['Speed'] = filtredf['Speed'].astype(int)

# Convertir la colonne "Legendary" en type booléen
filtredf['Legendary'] = filtredf['Legendary'].astype(bool)
print(filtredf.head(5))

#1.5
filtredf['Agility'] = filtredf['Speed']/filtredf["Weight"]
filtredf['Agility'] = filtredf['Agility'].round(1)
print(filtredf.head(5))

#1.6
primaire = filtredf['Primary Type'].value_counts()
graphique= graph.pie(names=primaire.index, values=primaire.values, title='distribution des types primaires de pokemom',  labels={'names': 'Primary Type', 'values': 'Count'}, hole=0, hover_name=primaire.index)
graphique.show()
#1.7
Pokemons_legendaires = filtredf[filtredf["Legendary"] == True]["Generation"]
Pokemons_non_legendaires = filtredf[filtredf["Legendary"] == False]["Generation"]

unique_generations = sorted(filtredf["Generation"].unique())

plt.hist(Pokemons_legendaires, bins=7, alpha=1, color="blue", label="Légendaires")
plt.hist(Pokemons_non_legendaires, bins=7, alpha=0.75, color="green", label="Non Légendaires")

plt.xlabel("Génération")
plt.ylabel("Nombre de Pokémon")
plt.title("Distribution par Génération")
plt.legend(loc="upper right", prop={'size': 8})
plt.show()

#1.8
import plotly.graph_objs as graph


moyattack = filtredf.groupby("Generation")["Attack"].mean()
moyspeed = filtredf.groupby("Generation")["Speed"].mean()
moygen = filtredf.groupby("Generation")["HP"].mean()
moydef = filtredf.groupby("Generation")["Defense"].mean()


trace_attack = graph.Scatter(x=moyattack.index, y=moyattack.values, name='Attack', line=dict(color='blue'))
trace_speed = graph.Scatter(x=moyspeed.index, y=moyspeed.values, name='Speed', line=dict(color='purple'))
trace_hp = graph.Scatter(x=moygen.index, y=moygen.values, name='HP', line=dict(color='green'))
trace_defense = graph.Scatter(x=moydef.index, y=moydef.values, name='Defense', line=dict(color='red'))
fig = graph.Figure()

fig.add_trace(trace_attack)
fig.add_trace(trace_speed)
fig.add_trace(trace_hp)
fig.add_trace(trace_defense)


fig.update_layout(title='Moyenne des attributs par génération',xaxis_title='Génération',yaxis_title='Moyenne' ,   width=1200, height=600)
fig.show()


