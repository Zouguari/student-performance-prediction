import streamlit as st
from backend import load_model, apply_mappings, prepare_data, predict_grade

# Charger le modèle
model = load_model()

# Configuration de la page
st.set_page_config(page_title="Application de Prédiction", layout="wide")

# Ajout du CSS pour FontAwesome
st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <style>
    .input-container {
        display: flex;
        align-items: center;
        margin-bottom: -180px;
        margin-top: 15px;
    }
    .input-container i {
        margin-right: 10px;
        color: #007bff;
    }
    .stSidebar .stButton>button {
        width: 100%;
        text-align: left;
        border-radius: 5px;
        padding: 5px 5px;
        margin: 5px 0px;
        border: none;
        background-color: #f4f4f4;
    }
    .stSidebar .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }
    .selected-button {
        background-color: #007bff;
        color: white;
    }
    .unselected-button {
        background-color: #f1f1f1;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Liste des options du menu avec des icônes
menu_options = {
    "Accueil": "🏠",
    "Formulaire": "📝",
    "À propos": "ℹ️",
    "Contact": "📞"
}

# Fonction pour créer un menu vertical dans la sidebar avec des icônes
def render_sidebar():
    selected = st.session_state.get('selected_menu', "Accueil")

    for option, icon in menu_options.items():
        button_class = "selected-button" if option == selected else "unselected-button"
        if st.sidebar.button(f"{icon} {option}", key=option, use_container_width=True):
            st.session_state.selected_menu = option
            selected = option

    return selected

def validate_fields(data):
    for key, value in data.items():
        if value is None or value == "":
            return False, key  # Retourne False et le champ vide
    return True, None

# Menu vertical sur la sidebar
selected = render_sidebar()

# Gestion des pages et modification des titres
if selected == "Accueil":
    st.title("Bienvenue sur l'application de prédiction des notes")
    st.subheader("Prévisions de performance scolaire personnalisées")
    st.write(
        """
        Cette application aide les étudiants à prédire leurs performances scolaires
        en fonction de plusieurs facteurs influençant leur apprentissage.
        """
    )

    st.markdown("### Fonctionnalités principales :")
    st.markdown(
        """
        - Analyse des facteurs comme la motivation, le sommeil, et les activités extrascolaires.
        - Prévisions précises des notes basées sur des algorithmes de Machine Learning.
        - Interface simple et intuitive pour une meilleure expérience utilisateur.
        """
    )

    st.markdown(
        """
        Pour commencer à prédire vos résultats, veuillez remplir le formulaire d'entrée.
        Pour accéder au formulaire, veuillez sélectionner l'option "Formulaire" dans le menu à gauche et entrez vos informations pour obtenir une estimation personnalisée.
        """
    )

elif selected == "Formulaire":
    with st.form(key='formulaire_icones'):
        st.title("Formulaire de Prédiction des Notes")
        st.subheader("Entrez vos informations pour une estimation personnalisée")
        st.markdown("**Veuillez remplir les informations suivantes pour obtenir une prédiction :**")

        st.markdown("### Informations académiques")
        col1, col2 = st.columns(2)

        # Informations académiques
        with col1:
            st.markdown('<div class="input-container"><i class="fas fa-clock"></i><span>Heures d\'étude :</span></div>', unsafe_allow_html=True)
            hours_studied = st.number_input(" ", min_value=0, max_value=168, step=1, key="hours")

            st.markdown('<div class="input-container"><i class="fas fa-percent"></i><span>Présence en classe (%) :</span></div>', unsafe_allow_html=True)
            attendance = st.slider(" ", min_value=0, max_value=100, step=1, key="attendance")

            st.markdown('<div class="input-container"><i class="fas fa-pencil-alt"></i><span>Score précédent :</span></div>', unsafe_allow_html=True)
            previous_scores = st.number_input(" ", min_value=0.0, max_value=20.0, step=0.1, key="previous_scores")

            st.markdown('<div class="input-container"><i class="fas fa-chart-line"></i><span>Niveau de motivation :</span></div>', unsafe_allow_html=True)
            motivation_level = st.selectbox(" ", ["", "Faible", "Moyen", "Élevé"], key="motivation")  # Valeur vide par défaut

        with col2:
            st.markdown('<div class="input-container"><i class="fas fa-book"></i><span>Accès aux ressources :</span></div>', unsafe_allow_html=True)
            access_to_resources = st.selectbox(" ", ["", "Faible", "Moyen", "Élevé"], key="resources")

            st.markdown('<div class="input-container"><i class="fas fa-puzzle-piece"></i><span>Activités extrascolaires :</span></div>', unsafe_allow_html=True)
            extracurricular_activities = st.number_input(" ", min_value=0, max_value=5, step=1, key="extracurricular")

            st.markdown('<div class="input-container"><i class="fas fa-chalkboard-teacher"></i><span>Sessions de tutorat :</span></div>', unsafe_allow_html=True)
            tutoring_sessions = st.number_input(" ", min_value=0, max_value=10, step=1, key="tutoring")

        st.markdown("### Informations personnelles")
        col3, col4 = st.columns(2)

        with col3:
            st.markdown('<div class="input-container"><i class="fas fa-users"></i><span>Implication parentale :</span></div>', unsafe_allow_html=True)
            parental_involvement = st.selectbox(" ", ["", "Faible", "Moyen", "Élevé"], key="parental")

            st.markdown('<div class="input-container"><i class="fas fa-dollar-sign"></i><span>Revenu familial :</span></div>', unsafe_allow_html=True)
            family_income = st.selectbox(" ", ["", "Faible", "Moyen", "Élevé"], key="income")

            st.markdown('<div class="input-container"><i class="fas fa-users"></i><span>Influence des pairs :</span></div>', unsafe_allow_html=True)
            peer_influence = st.selectbox(" ", ["", "Négative", "Neutral", "Positive"], key="peers")

            st.markdown('<div class="input-container"><i class="fas fa-wifi"></i><span>Accès à Internet :</span></div>', unsafe_allow_html=True)
            internet_access = st.radio(" ", ["Oui", "Non"], key="internet")

            st.markdown('<div class="input-container"><i class="fas fa-male"></i><span>Genre :</span></div>', unsafe_allow_html=True)
            gender = st.selectbox(" ", ["", "Homme", "Femme"], key="gender")

        with col4:
            st.markdown('<div class="input-container"><i class="fas fa-graduation-cap"></i><span>Niveau d\'éducation des parents :</span></div>', unsafe_allow_html=True)
            parental_education_level = st.selectbox(" ", ["", "Lycée", "Université", "Post-universitaire"], key="education")

            st.markdown('<div class="input-container"><i class="fas fa-map-marker-alt"></i><span>Distance du domicile :</span></div>', unsafe_allow_html=True)
            distance_from_home = st.selectbox(" ", ["", "Loin", "Modéré", "Proche"], key="distance")

            st.markdown('<div class="input-container"><i class="fas fa-bed"></i><span>Heures de sommeil :</span></div>', unsafe_allow_html=True)
            sleep_hours = st.number_input(" ", min_value=0, max_value=24, step=1, key="sleep")

            st.markdown('<div class="input-container"><i class="fas fa-running"></i><span>Activité physique (heures/semaine) :</span></div>', unsafe_allow_html=True)
            physical_activity = st.number_input(" ", min_value=0, max_value=20, step=1, key="activity")

        submit_button = st.form_submit_button(label="Soumettre les données")

        if submit_button:
            student_data = {
                "Hours_Studied": hours_studied,
                "Attendance": attendance,
                "Previous_Scores": previous_scores,
                "Motivation_Level": motivation_level,
                "Access_to_Resources": access_to_resources,
                "Extracurricular_Activities": extracurricular_activities,
                "Tutoring_Sessions": tutoring_sessions,
                "Parental_Involvement": parental_involvement,
                "Family_Income": family_income,
                "Peer_Influence": peer_influence,
                "Parental_Education_Level": parental_education_level,
                "Distance_from_Home": distance_from_home,
                "Sleep_Hours": sleep_hours,
                "Physical_Activity": physical_activity,
                "Internet_Access": 1 if internet_access == "Oui" else 0,
                "Gender": 1 if gender == "Homme" else 0,
            }

            is_valid, empty_field = validate_fields(student_data)
            if not is_valid:
                st.error(f"Veuillez remplir tous les champs !!")
            else:
                student_data = apply_mappings(student_data)
                feature_order = [
                    "Hours_Studied", "Attendance", "Parental_Involvement", "Access_to_Resources",
                    "Extracurricular_Activities", "Sleep_Hours", "Previous_Scores", "Motivation_Level",
                    "Internet_Access", "Tutoring_Sessions", "Family_Income", "Peer_Influence",
                    "Physical_Activity", "Parental_Education_Level", "Distance_from_Home", "Gender"
                ]

                input_data = prepare_data(student_data, feature_order)
                prediction = predict_grade(model, input_data)

                # Afficher uniquement le résultat de la prédiction
                st.success(f"**Note prédite** : {prediction[0]:.2f}")

elif selected == "À propos":
    st.title("À propos de l'application")
    st.subheader("En savoir plus sur notre mission et les technologies utilisées")
    st.write(
        """
        Cette application a été conçue pour aider les étudiants et les enseignants
        à mieux comprendre les facteurs influençant les performances scolaires.
        """
    )
    st.markdown("**Technologies utilisées :**")
    st.markdown(
        """
        - **Langage :** Python
        - **Framework :** Streamlit
        - **Modèles :** Machine Learning pour la prédiction des notes
        """
    )

elif selected == "Contact":
    st.title("Nous contacter")
    st.subheader("Nous sommes là pour répondre à toutes vos questions")
    st.write("Pour toute question ou suggestion, vous pouvez nous contacter via les adresses email suivantes :")

    # Liste avec une mise en forme plus professionnelle
    st.markdown(
        """
        ### Liste des contacts :
        - 📧 **Chorouk Mouhibi** : [chorouk.mouhibi.56@edu.uiz.ac.ma](mailto:choroukmouhibi08@gmail.com)
        - 📧 **Zineb Arfani** : [zineb.arfani.57@edu.uiz.ac.ma](mailto:zinebarfani.mgsi@gmail.com)
        - 📧 **Yassine Laamarti** : [yassine.laamarti.24@edu.uiz.ac.ma](mailto:yassinelaamarti362@gmail.com)
        - 📧 **Yassine Zouguari** : [yassine.zouguari.58@edu.uiz.ac.ma](mailto:yassine.zouguari.58@edu.uiz.ac.ma)
        """
    )