"""
BéninViDjidji - Bot de promotion du patrimoine béninois
Version élégante et minimaliste
"""

import streamlit as st
import streamlit.components.v1 as components
from groq import Groq
import random

# Configuration de la page
st.set_page_config(
    page_title="BéninViDjidji",
    page_icon="🇧🇯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS élégant et minimaliste
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Montserrat:wght@300;400;500;600&display=swap');
    
    /* Animation de fond subtile */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    /* Fond principal */
    .stApp {
        background: linear-gradient(-45deg, #f8f9fa, #ffffff, #f5f5f5, #fafafa);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    /* Barre latérale élégante - FOND BLANC */
    section[data-testid="stSidebar"] {
        background: white !important;
        border-right: 1px solid rgba(0, 135, 81, 0.1);
    }
    
    section[data-testid="stSidebar"] > div {
        background: white !important;
    }
    
    /* Accent de couleur sur le côté */
    section[data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(180deg, #008751 0%, #FCD116 50%, #E8112d 100%);
    }
    
    
    /* Titres élégants */
    h1, h2, h3 {
        font-family: 'Cormorant Garamond', serif;
        font-weight: 600;
        color: #1a1a1a;
        letter-spacing: 0.5px;
        animation: fadeIn 0.8s ease-out;
    }
    
    h1 {
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #008751, #FCD116, #E8112d);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Texte du corps */
    p, div, span, label {
        font-family: 'Montserrat', sans-serif;
        color: #2c2c2c;
        line-height: 1.7;
    }
    
    /* Messages du chat */
    .stChatMessage {
        background: white;
        border: 1px solid rgba(0, 135, 81, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        animation: slideIn 0.4s ease-out;
        transition: all 0.3s ease;
    }
    
    .stChatMessage:hover {
        box-shadow: 0 4px 16px rgba(0, 135, 81, 0.08);
        transform: translateY(-2px);
    }
    
    /* Message de l'assistant avec accent */
    .stChatMessage[data-testid="chat-message-assistant"] {
        border-left: 3px solid #008751;
        background: linear-gradient(to right, rgba(0, 135, 81, 0.02), white);
    }
    
    /* Message de l'utilisateur */
    .stChatMessage[data-testid="chat-message-user"] {
        border-left: 3px solid #FCD116;
        background: linear-gradient(to right, rgba(252, 209, 22, 0.02), white);
    }
    
    /* Boutons élégants */
    .stButton > button {
        background: white;
        color: #008751;
        border: 2px solid #008751;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-family: 'Montserrat', sans-serif;
        font-weight: 500;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        letter-spacing: 0.3px;
    }
    
    .stButton > button:hover {
        background: #008751;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 135, 81, 0.3);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Bouton primaire */
    button[kind="primary"] {
        background: linear-gradient(135deg, #008751, #006838) !important;
        color: white !important;
        border: none !important;
    }
    
    button[kind="primary"]:hover {
        background: linear-gradient(135deg, #006838, #008751) !important;
        box-shadow: 0 6px 16px rgba(0, 135, 81, 0.4) !important;
    }
    
    /* Input de chat */
    .stChatInputContainer {
        background: white;
        border: 2px solid rgba(0, 135, 81, 0.15);
        border-radius: 12px;
        padding: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .stChatInputContainer:focus-within {
        border-color: #008751;
        box-shadow: 0 0 0 3px rgba(0, 135, 81, 0.1);
    }
    
    /* Onglets */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: white;
        border-radius: 12px;
        padding: 0.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: #666;
        font-family: 'Montserrat', sans-serif;
        font-weight: 500;
        border-radius: 8px;
        padding: 0.8rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(0, 135, 81, 0.05);
        color: #008751;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0, 135, 81, 0.1), rgba(252, 209, 22, 0.1));
        color: #008751;
        font-weight: 600;
    }
    
    /* Champs de saisie */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        background: white;
        border: 2px solid rgba(0, 135, 81, 0.15);
        border-radius: 8px;
        font-family: 'Montserrat', sans-serif;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #008751;
        box-shadow: 0 0 0 3px rgba(0, 135, 81, 0.1);
    }
    
    /* Radio buttons */
    .stRadio > div {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid rgba(0, 135, 81, 0.1);
    }
    
    .stRadio > div > label {
        padding: 0.5rem;
        border-radius: 6px;
        transition: all 0.2s ease;
    }
    
    .stRadio > div > label:hover {
        background: rgba(0, 135, 81, 0.05);
    }
    
    /* Métriques */
    [data-testid="stMetricValue"] {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        color: #008751;
        font-weight: 600;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background: white;
        border: 1px solid rgba(0, 135, 81, 0.1);
        border-radius: 8px;
        color: #1a1a1a;
        font-family: 'Montserrat', sans-serif;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(0, 135, 81, 0.03);
        border-color: #008751;
    }
    
    /* Messages d'état */
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 8px;
        border-left-width: 4px;
        font-family: 'Montserrat', sans-serif;
        animation: slideIn 0.4s ease-out;
    }
    
    .stSuccess {
        background: rgba(0, 135, 81, 0.05);
        border-left-color: #008751;
    }
    
    /* Sliders */
    .stSlider > div > div > div {
        background: linear-gradient(to right, #008751, #FCD116);
    }
    
    /* Spinner personnalisé */
    .stSpinner > div {
        border-top-color: #008751 !important;
    }
    
    /* Scrollbar personnalisée */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 135, 81, 0.05);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #008751, #FCD116);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #006838, #E8A900);
    }
    
    /* Carte élégante */
    .elegant-card {
        background: white;
        border: 1px solid rgba(0, 135, 81, 0.1);
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        transition: all 0.3s ease;
        animation: fadeIn 0.6s ease-out;
    }
    
    .elegant-card:hover {
        box-shadow: 0 8px 24px rgba(0, 135, 81, 0.1);
        transform: translateY(-4px);
    }
    
    /* Badge de couleur */
    .color-badge {
        display: inline-block;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        margin: 0 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        animation: fadeIn 0.6s ease-out;
    }
    
    /* Séparateur élégant */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, 
            transparent, 
            rgba(0, 135, 81, 0.3), 
            rgba(252, 209, 22, 0.3), 
            rgba(232, 17, 45, 0.3), 
            transparent);
        margin: 2rem 0;
    }
    
    /* Animation de chargement */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .loading {
        animation: pulse 1.5s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)

# Initialisation des variables de session
if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = ""
    
if "messages" not in st.session_state:
    welcome_messages = [
        "Bienvenue. Je suis BéninViDjidji, votre guide spécialisé dans le patrimoine béninois. Comment puis-je vous assister ?",
        "Bonjour. BéninViDjidji à votre service pour explorer l'histoire et la culture du Bénin.",
        "Bienvenue sur BéninViDjidji. Discutons de l'héritage culturel et historique du Bénin.",
    ]
    st.session_state.messages = [
        {"role": "assistant", "content": random.choice(welcome_messages)}
    ]

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
    
if "quiz_questions_answered" not in st.session_state:
    st.session_state.quiz_questions_answered = 0

# Base de connaissances sur le Bénin
BENIN_KNOWLEDGE = """
Le Bénin est un pays d'Afrique de l'Ouest, anciennement appelé Dahomey. Voici des informations essentielles :

HISTOIRE :
- Ancien royaume du Dahomey (17e-19e siècle)
- Royaume puissant avec les Amazones du Dahomey
- Indépendance le 1er août 1960
- Berceau du Vaudou
- Ouidah : porte du non-retour et mémoire de la traite négrière

GÉOGRAPHIE :
- Capitale : Porto-Novo (capitale constitutionnelle), Cotonou (capitale économique)
- Superficie : 114 763 km²
- Frontières : Togo, Nigeria, Niger, Burkina Faso
- Côte atlantique : 121 km
- Climat : tropical au sud, semi-aride au nord

CULTURE :
- Vaudou : religion traditionnelle originaire du Bénin
- Festival international du Vaudou
- Musique : Angélique Kidjo (Grammy Awards)
- Danses traditionnelles : Zangbeto, Guèlèdè
- Artisanat : tissus, bronze, sculptures

PATRIMOINE UNESCO :
- Palais royaux d'Abomey (1985)
- Paysage culturel de Koutammakou (partagé avec le Togo)

SITES HISTORIQUES :
- Musée historique d'Abomey
- Route des esclaves à Ouidah
- Temple des Pythons
- Forêt sacrée de Kpassè
- Palais de Honmè

LANGUES :
- Officielle : Français
- Nationales : Fon, Yoruba, Bariba, Dendi, etc.

ÉCONOMIE :
- Agriculture : coton, palmier à huile, anacarde
- Port autonome de Cotonou
- Tourisme culturel en développement

PERSONNALITÉS :
- Angélique Kidjo : chanteuse
- Béhanzin : dernier roi du Dahomey
- Stanislas Adotevi : philosophe
- Djimon Hounsou : acteur
"""

# Questions de quiz
QUIZ_QUESTIONS = [
    {
        "question": "Quelle est la capitale constitutionnelle du Bénin ?",
        "options": ["Cotonou", "Porto-Novo", "Abomey", "Parakou"],
        "answer": "Porto-Novo",
        "explanation": "Porto-Novo est la capitale constitutionnelle, tandis que Cotonou est la capitale économique."
    },
    {
        "question": "En quelle année le Bénin a-t-il obtenu son indépendance ?",
        "options": ["1958", "1960", "1962", "1965"],
        "answer": "1960",
        "explanation": "Le Bénin a obtenu son indépendance de la France le 1er août 1960."
    },
    {
        "question": "Quel était l'ancien nom du Bénin ?",
        "options": ["Dahomey", "Guinée", "Soudan", "Haute-Volta"],
        "answer": "Dahomey",
        "explanation": "Le pays s'appelait Dahomey jusqu'en 1975, date à laquelle il a été rebaptisé Bénin."
    },
    {
        "question": "Quelle religion traditionnelle est originaire du Bénin ?",
        "options": ["Santeria", "Candomblé", "Vaudou", "Umbanda"],
        "answer": "Vaudou",
        "explanation": "Le Vaudou est une religion traditionnelle originaire du Bénin, plus précisément de la région d'Abomey."
    },
    {
        "question": "Qui sont les Amazones du Dahomey ?",
        "options": ["Des déesses mythologiques", "Des guerrières d'élite", "Des reines", "Des prêtresses"],
        "answer": "Des guerrières d'élite",
        "explanation": "Les Amazones du Dahomey étaient un régiment de guerrières d'élite du royaume du Dahomey, célèbres pour leur courage."
    },
    {
        "question": "Quel site béninois est inscrit au patrimoine mondial de l'UNESCO ?",
        "options": ["Temple des Pythons", "Route des esclaves", "Palais royaux d'Abomey", "Port de Cotonou"],
        "answer": "Palais royaux d'Abomey",
        "explanation": "Les Palais royaux d'Abomey sont inscrits au patrimoine mondial de l'UNESCO depuis 1985."
    },
    {
        "question": "Quelle chanteuse béninoise a remporté plusieurs Grammy Awards ?",
        "options": ["Zeynab", "Angélique Kidjo", "Gnonnas Pedro", "Bella Bellow"],
        "answer": "Angélique Kidjo",
        "explanation": "Angélique Kidjo est une chanteuse béninoise mondialement reconnue, lauréate de plusieurs Grammy Awards."
    },
    {
        "question": "Quelle ville béninoise est connue comme la porte du non-retour ?",
        "options": ["Abomey", "Ouidah", "Cotonou", "Grand-Popo"],
        "answer": "Ouidah",
        "explanation": "Ouidah abrite la Porte du non-retour, monument commémorant les victimes de la traite négrière."
    }
]

# Thèmes pour les récits historiques
STORY_THEMES = {
    "Royaume du Dahomey": "Raconte l'histoire du puissant royaume du Dahomey, ses rois, ses conquêtes et son système politique sophistiqué.",
    "Amazones du Dahomey": "Décris les légendaires Amazones du Dahomey, leur entraînement, leurs batailles et leur rôle dans la société.",
    "Traite négrière": "Explique le rôle tragique de Ouidah dans la traite négrière, la route des esclaves et la mémoire collective.",
    "Vaudou": "Présente les origines et les pratiques du Vaudou, religion traditionnelle béninoise et son influence mondiale.",
    "Palais d'Abomey": "Décris les palais royaux d'Abomey, leur architecture, leurs bas-reliefs et leur importance historique.",
    "Indépendance": "Raconte la lutte pour l'indépendance du Bénin et les premiers pas du pays en tant que nation souveraine."
}

# Sidebar
with st.sidebar:

    import base64
    # Dans la sidebar, remplacez votre section logo par :
    try:
        logo_base64 = base64.b64encode(open("logo.png", "rb").read()).decode()
        st.markdown(f"""
        <div style='text-align: center; padding: 2rem 0;'>
            <div style='
                display: flex;
                align-items: center;
                justify-content: center;
                background: white;
                width: 140px;
                height: 140px;
                border-radius: 50%;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                margin: 0 auto 1rem auto;
                padding: 1rem;
            '>
                <img src='data:image/png;base64,{logo_base64}' style='width: 100px; height: auto; display: block;' alt='Logo BéninViDjidji'>
            </div>
            <h2 style='font-family: "Cormorant Garamond", serif; margin: 0;'>BéninViDjidji</h2>
            <div style='margin-top: 0.5rem;'>
                <span class='color-badge' style='background: #008751;'></span>
                <span class='color-badge' style='background: #FCD116;'></span>
                <span class='color-badge' style='background: #E8112d;'></span>
            </div>
            <p style='font-size: 0.9rem; color: #666; margin-top: 0.5rem;'>Patrimoine Béninois</p>
        </div>
        """, unsafe_allow_html=True)
    except FileNotFoundError:
        st.markdown("""
        <div style='text-align: center; padding: 2rem 0;'>
            <h2 style='font-family: "Cormorant Garamond", serif; margin: 0;'>BéninViDjidji</h2>
            <div style='margin-top: 0.5rem;'>
                <span class='color-badge' style='background: #008751;'></span>
                <span class='color-badge' style='background: #FCD116;'></span>
                <span class='color-badge' style='background: #E8112d;'></span>
            </div>
            <p style='font-size: 0.9rem; color: #666; margin-top: 0.5rem;'>Patrimoine Béninois</p>
        </div>
        """, unsafe_allow_html=True)

    # Récupérer automatiquement la clé API depuis les secrets Streamlit
    try:
        st.session_state.groq_api_key = st.secrets["GROQ_API_KEY"]
    except:
        st.error("⚠️ Configuration API manquante. Contactez l'administrateur.")
        st.session_state.groq_api_key = ""
        
    # Paramètres du modèle
    with st.expander("Paramètres avancés"):
        model = st.selectbox(
            "Modèle",
            ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"],
            help="Choisissez le modèle Groq à utiliser"
        )
        
        temperature = st.slider(
            "Température",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Contrôle la créativité des réponses"
        )
        
        max_tokens = st.slider(
            "Tokens maximum",
            min_value=256,
            max_value=4096,
            value=1024,
            step=128,
            help="Longueur maximale des réponses"
        )
    
    st.markdown("---")
    
    # Statistiques du quiz
    if st.session_state.quiz_questions_answered > 0:
        st.subheader("Statistiques Quiz")
        accuracy = (st.session_state.quiz_score / st.session_state.quiz_questions_answered) * 100
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Score", f"{st.session_state.quiz_score}/{st.session_state.quiz_questions_answered}")
        with col2:
            st.metric("Précision", f"{accuracy:.0f}%")
    
    st.markdown("---")
    
    # Bouton de réinitialisation
    if st.button("Réinitialiser"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Bienvenue. Je suis BéninViDjidji, votre guide spécialisé dans le patrimoine béninois."}
        ]
        st.rerun()
    
    st.markdown("---")
    st.caption("Développé pour promouvoir le patrimoine béninois")

# Interface principale avec onglets
tab1, tab2, tab3 = st.tabs(["Conversation", "Quiz", "Récits Historiques"])

# Onglet Chat
with tab1:
    st.title("Discussion")
    st.markdown("Explorez l'histoire, la géographie et la culture du Bénin à travers une conversation guidée.")
    
    # Afficher l'historique des messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input utilisateur
    if prompt := st.chat_input("Votre question sur le Bénin..."):
        if not st.session_state.groq_api_key:
            st.error("Veuillez configurer votre clé API Groq dans la barre latérale.")
        else:
            # Ajouter le message de l'utilisateur
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Générer la réponse
            with st.chat_message("assistant"):
                try:
                    client = Groq(api_key=st.session_state.groq_api_key)
                    
                    # Préparer les messages avec le contexte
                    messages = [
                        {
                            "role": "system",
                            "content": f"""Tu es BéninViDjidji, un assistant expert sur le Bénin. Tu es professionnel, précis et 
                            éducatif. Tu ne dois JAMAIS utiliser d'émojis dans tes réponses. Ton ton est sérieux et académique, 
                            mais accessible. Utilise les informations suivantes comme base de connaissances :
                            
                            {BENIN_KNOWLEDGE}
                            
                            Réponds de manière claire, structurée et informative. Si on te pose une question hors sujet, 
                            rappelle poliment ta spécialisation."""
                        }
                    ]
                    
                    # Ajouter l'historique des conversations
                    for msg in st.session_state.messages[-6:]:
                        messages.append({"role": msg["role"], "content": msg["content"]})
                    
                    # Appel à l'API Groq
                    with st.spinner("Réflexion en cours..."):
                        completion = client.chat.completions.create(
                            model=model,
                            messages=messages,
                            temperature=temperature,
                            max_tokens=max_tokens,
                            stream=True
                        )
                        
                        response = ""
                        response_placeholder = st.empty()
                        
                        for chunk in completion:
                            if chunk.choices[0].delta.content:
                                response += chunk.choices[0].delta.content
                                response_placeholder.markdown(response + "▌")
                        
                        response_placeholder.markdown(response)
                    
                    # Ajouter la réponse à l'historique
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    
                except Exception as e:
                    st.error(f"Erreur : {str(e)}")
                    st.info("Vérifiez que votre clé API Groq est valide.")

# Onglet Quiz
with tab2:
    st.title("Quiz Culturel")
    st.markdown("Évaluez vos connaissances sur le patrimoine béninois.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if st.button("Nouvelle question", type="primary"):
            st.session_state.current_quiz = random.choice(QUIZ_QUESTIONS)
            st.session_state.quiz_answered = False
            st.rerun()
        
        if "current_quiz" in st.session_state:
            quiz = st.session_state.current_quiz
            
            st.markdown(f"### {quiz['question']}")
            
            if not st.session_state.get("quiz_answered", False):
                user_answer = st.radio(
                    "Choisissez votre réponse :",
                    quiz["options"],
                    key="quiz_radio"
                )
                
                if st.button("Valider", type="secondary"):
                    st.session_state.quiz_answered = True
                    st.session_state.quiz_user_answer = user_answer
                    st.session_state.quiz_questions_answered += 1
                    
                    if user_answer == quiz["answer"]:
                        st.session_state.quiz_score += 1
                    
                    st.rerun()
            else:
                user_answer = st.session_state.quiz_user_answer
                
                if user_answer == quiz["answer"]:
                    st.success(f"Correct. La bonne réponse est **{quiz['answer']}**")
                else:
                    st.error(f"Incorrect. La bonne réponse était **{quiz['answer']}**")
                
                st.info(f"**Explication :** {quiz['explanation']}")
    
    with col2:
        st.markdown("### Votre Score")
        if st.session_state.quiz_questions_answered > 0:
            accuracy = (st.session_state.quiz_score / st.session_state.quiz_questions_answered) * 100
            
            st.metric("Questions", st.session_state.quiz_questions_answered)
            st.metric("Bonnes réponses", st.session_state.quiz_score)
            st.metric("Taux de réussite", f"{accuracy:.0f}%")
            
            if st.button("Réinitialiser le score"):
                st.session_state.quiz_score = 0
                st.session_state.quiz_questions_answered = 0
                st.rerun()
        else:
            st.info("Commencez le quiz pour voir vos statistiques")

# Onglet Récits Historiques
with tab3:
    st.title("Récits Historiques")
    st.markdown("Générez des récits détaillés sur l'histoire et le patrimoine du Bénin.")
    
    # Sélection du thème
    theme = st.selectbox(
        "Thème historique :",
        list(STORY_THEMES.keys()),
        help="Sélectionnez le thème qui vous intéresse"
    )
    
    # Style du récit
    col1, col2 = st.columns(2)
    
    with col1:
        story_length = st.select_slider(
            "Longueur",
            options=["Court", "Moyen", "Long"],
            value="Moyen"
        )
    
    with col2:
        story_style = st.selectbox(
            "Style narratif",
            ["Éducatif", "Narratif", "Académique", "Journalistique"]
        )
    
    # Bouton de génération
    if st.button("Générer le récit", type="primary"):
        if not st.session_state.groq_api_key:
            st.error("Veuillez configurer votre clé API Groq dans la barre latérale.")
        else:
            try:
                client = Groq(api_key=st.session_state.groq_api_key)
                
                # Déterminer les tokens en fonction de la longueur
                length_tokens = {
                    "Court": 512,
                    "Moyen": 1024,
                    "Long": 2048
                }
                
                # Construire le prompt
                story_prompt = f"""En tant qu'historien spécialisé dans le patrimoine béninois, rédigez un récit {story_style.lower()} 
                sur le thème : {theme}.
                
                Contexte : {STORY_THEMES[theme]}
                
                Le récit doit être :
                - De longueur {story_length.lower()}
                - Dans un style {story_style.lower()}
                - Professionnel et informatif
                - Basé sur des faits historiques précis
                - Sans émojis
                
                Incluez des dates, des noms de personnages historiques et des détails culturels pertinents.
                """
                
                with st.spinner("Génération du récit..."):
                    completion = client.chat.completions.create(
                        model=model,
                        messages=[
                            {
                                "role": "system",
                                "content": f"Tu es un historien expert du Bénin. Tu ne dois JAMAIS utiliser d'émojis. {BENIN_KNOWLEDGE}"
                            },
                            {
                                "role": "user",
                                "content": story_prompt
                            }
                        ],
                        temperature=0.8,
                        max_tokens=length_tokens[story_length],
                        stream=True
                    )
                    
                    story = ""
                    story_placeholder = st.empty()
                    
                    for chunk in completion:
                        if chunk.choices[0].delta.content:
                            story += chunk.choices[0].delta.content
                            story_placeholder.markdown(story + "▌")
                    
                    story_placeholder.markdown(story)
                
                # Bouton de téléchargement
                st.download_button(
                    label="Télécharger le récit",
                    data=story,
                    file_name=f"recit_{theme.lower().replace(' ', '_')}.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Erreur lors de la génération : {str(e)}")
                st.info("Vérifiez que votre clé API Groq est valide.")

# Footer élégant
st.markdown("---")
st.markdown("""
<div class='elegant-card' style='text-align: center;'>
    <h3 style='margin-bottom: 1rem;'>BéninViDjidji</h3>
    <p style='margin-bottom: 0.5rem;'><strong>Promotion du Patrimoine Béninois</strong></p>
    <div style='margin: 1rem 0;'>
        <span class='color-badge' style='background: #008751;'></span>
        <span class='color-badge' style='background: #FCD116;'></span>
        <span class='color-badge' style='background: #E8112d;'></span>
    </div>
    <p style='font-size: 0.9rem; color: #666;'>
        Découvrez l'histoire, la culture et le patrimoine du Bénin
    </p>
</div>
""", unsafe_allow_html=True)
