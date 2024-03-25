import os
import unittest
import nbformat
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
NOTEBOOK_PATH = f"{CURRENT_DIR}/analysis.ipynb"

FUNCTION_NAMES = ['create_pokedex', 'filter_columns',
                  'rename_columns', 'clean_data', 'correct_columns_types', 'add_agility_column']


def import_notebook_functions(notebook_path, function_names):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = f.read()

    notebook = nbformat.reads(notebook_content, as_version=4)
    for cell in notebook.cells:
        if cell.cell_type != "code":
            continue

        for function in function_names:
            if f"def {function}(" in cell.source:
                exec(cell.source, globals())
                break


class TestPokedexAnalysis(unittest.TestCase):

    columns_to_keep = ["name", "type1", "type2", "attack", "defense", "hp", "speed",
                       "generation", "is_legendary", "weight_kg", "height_m", "capture_rate"]

    def setUp(self):
        self.df = create_pokedex()

    def test_create_pokedex(self):
        self.assertEqual(pd.DataFrame, type(self.df))
        self.assertEqual((806, 41), self.df.shape)

    def test_filter_columns(self):
        filter_columns(self.df)
        self.assertEqual((806, 12), self.df.shape)
        self.assertEqual(set(self.columns_to_keep), set(self.df.columns))

    def test_rename_columns(self):
        columns = self.df.columns
        rename_columns(self.df)
        new_columns = ['Name', 'Primary Type', 'Secondary Type', 'Attack', 'Defense',
                       'HP', 'Speed', 'Generation', 'Legendary', 'Weight', 'Height', 'Capture Rate']
        expected_columns = set(columns) - \
            set(self.columns_to_keep) | set(new_columns)
        self.assertEqual(expected_columns, set(self.df.columns))

    def test_clean_data(self):
        clean_data(self.df)

        actual_shape = self.df.shape
        expected_shape = (339, 41)

        if (actual_shape[0] == 340):
            self.fail("You avez oublié de drop les doublons")

        if (actual_shape[0] == 804):
            self.fail(
                "Vous avez oublié de drop les lignes avec des valeurs manquantes")

        self.assertEqual(expected_shape, self.df.shape)

        self.assertEqual(list(range(expected_shape[0])), self.df.index.tolist(
        ), "Vous avez oublié de reset l'index")

    # Note: Ce test ne fonctionnera que si vous avez bien implémenté les fonctions précédentes,
    # vu que la modification du type des colonnes se base sur les noms des colonnes renommées
    def test_correct_columns_types(self):
        filter_columns(self.df)
        rename_columns(self.df)
        clean_data(self.df)
        correct_columns_types(self.df)
        self.assertEqual(int, self.df['Generation'].dtype)
        self.assertEqual(int, self.df["HP"].dtype)
        self.assertEqual(int, self.df["Speed"].dtype)
        self.assertEqual(int, self.df["Attack"].dtype)
        self.assertEqual(bool, self.df["Legendary"].dtype)

    # Note: Ce test ne fonctionnera que si vous avez bien implémenté les fonctions précédentes,
    # vu que l'ajout de la colonne 'Agility' se base sur les noms des colonnes renommées
    def test_add_agility_column(self):
        filter_columns(self.df)
        rename_columns(self.df)
        clean_data(self.df)
        correct_columns_types(self.df)
        n_cols = len(self.df.columns)
        add_agility_column(self.df)
        self.assertEqual(n_cols + 1, len(self.df.columns))
        self.assertEqual(float, self.df["Agility"].dtype)
        self.assertEqual(1, self.df["Agility"].apply(
            lambda x: len(str(x).split(".")[1])).max(), "Vous avez oublié d'arrondir le résultat à 1 chiffre après la virgule")
        self.assertEqual(14.248, round(self.df["Agility"].mean(
        ), 3), "Le calcul de la colonne 'Agility' est incorrect")


if __name__ == '__main__':
    import_notebook_functions(NOTEBOOK_PATH, FUNCTION_NAMES)
    unittest.main()
