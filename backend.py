import pickle

# Charger le modèle
def load_model(model_path="Modele\last_modele.pkl"):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

# Mappages pour convertir les valeurs catégoriques en numériques
MAPPINGS = {
    "Parental_Involvement": {"High": 2, "Medium": 1, "Low": 0, "Élevé": 2, "Moyen": 1, "Faible": 0},
    "Access_to_Resources": {"High": 2, "Medium": 1, "Low": 0, "Élevé": 2, "Moyen": 1, "Faible": 0},
    "Motivation_Level": {"High": 2, "Medium": 1, "Low": 0, "Élevé": 2, "Moyen": 1, "Faible": 0},
    "Family_Income": {"High": 2, "Medium": 1, "Low": 0, "Élevé": 2, "Moyen": 1, "Faible": 0},
    "Peer_Influence": {"Positive": 2, "Neutral": 1, "Negative": 0, "Positive": 2, "Neutral": 1, "Négative": 0},
    "Parental_Education_Level": {"Postgraduate": 2, "College": 1, "High School": 0, "Post-universitaire": 2, "Université": 1, "Lycée": 0},
    "Distance_from_Home": {"Near": 1, "Moderate": 1, "Far": 0, "Proche": 1, "Modéré": 1, "Loin": 0},
}

# Appliquer les mappages pour la prediction
def apply_mappings(student_data):
    for column, mapping in MAPPINGS.items():
        student_data[column] = mapping[student_data[column]]
    return student_data

# Préparer les données pour la prédiction
def prepare_data(student_data, feature_order):
    return [[student_data[feature] for feature in feature_order]]

# Prédire les notes
def predict_grade(model, input_data):
    return model.predict(input_data)
