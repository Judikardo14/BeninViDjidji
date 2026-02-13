# Configuration de BéninViDjidji
# Ce fichier peut être utilisé pour personnaliser l'application

# =====================================
# APPARENCE
# =====================================

# Couleurs du drapeau béninois
COLOR_GREEN = "#008751"
COLOR_YELLOW = "#FCD116"
COLOR_RED = "#E8112d"

# Nombre de particules dans l'animation
PARTICLES_COUNT = 150

# Opacité des particules (0.0 à 1.0)
PARTICLES_OPACITY = 1

# Vitesse des particules
PARTICLES_SPEED = 5

# =====================================
# MODÈLE GROQ
# =====================================

# Modèle par défaut
DEFAULT_MODEL = "llama-3.3-70b-versatile"

# Température par défaut (0.0 = précis, 1.0 = créatif)
DEFAULT_TEMPERATURE = 0.7

# Nombre maximum de tokens par défaut
DEFAULT_MAX_TOKENS = 1024

# =====================================
# MESSAGES DE BIENVENUE
# =====================================

WELCOME_MESSAGES = [
    "Akpé ! Je suis BéninViDjidji, votre guide du patrimoine béninois. Comment puis-je vous aider aujourd'hui ?",
    "Bienvenue ! Je suis BéninViDjidji. Découvrez avec moi l'histoire, la culture et le patrimoine du Bénin !",
    "Bonjour ! Je m'appelle BéninViDjidji. Explorons ensemble les richesses culturelles du Bénin !",
    "Akwaba ! Je suis BéninViDjidji, votre assistant pour tout savoir sur le Bénin. Posez-moi vos questions !",
    "Salut ! C'est BéninViDjidji. Prêt à découvrir les merveilles du patrimoine béninois ?",
]

# =====================================
# PERSONNALISATION DU CONTENU
# =====================================

# Activer/désactiver les fonctionnalités
ENABLE_CHAT = True
ENABLE_QUIZ = True
ENABLE_STORIES = True

# Nombre de messages à garder dans l'historique
CHAT_HISTORY_LENGTH = 6

# =====================================
# QUIZ
# =====================================

# Nombre minimum de questions dans le quiz
MIN_QUIZ_QUESTIONS = 8

# Afficher les explications après chaque réponse
SHOW_QUIZ_EXPLANATIONS = True

# =====================================
# RÉCITS HISTORIQUES
# =====================================

# Longueurs des récits (en tokens)
STORY_LENGTH_TOKENS = {
    "Court": 512,
    "Moyen": 1024,
    "Long": 2048
}

# Styles narratifs disponibles
STORY_STYLES = [
    "Éducatif",
    "Narratif", 
    "Poétique",
    "Journalistique"
]

# =====================================
# LOGO
# =====================================

# Chemin vers votre logo (laissez vide pour utiliser le drapeau)
# Exemple : LOGO_PATH = "./assets/logo.png"
LOGO_PATH = "logo.png"

# Si LOGO_PATH est vide, utiliser le drapeau du Bénin
DEFAULT_LOGO = "https://upload.wikimedia.org/wikipedia/commons/0/0a/Flag_of_Benin.svg"

# Largeur du logo en pixels
LOGO_WIDTH = 200

# =====================================
# LIENS ET CONTACT
# =====================================

# Vos liens de contact (optionnels)
CONTACT_LINKS = {
    "email": "",
    "website": "",
    "linkedin": "",
    "twitter": "",
    "github": ""
}

# Message du footer
FOOTER_MESSAGE = "Découvrez l'histoire, la culture et le patrimoine du Bénin à travers l'IA"

# =====================================
# AVANCÉ
# =====================================

# Prompt système pour le chat
SYSTEM_PROMPT_PREFIX = """Tu es BéninViDjidji, un assistant expert sur le Bénin, spécialisé dans l'histoire, 
la géographie, la culture et le patrimoine béninois. Tu es passionné, éducatif et tu utilises des 
anecdotes intéressantes."""

# Température pour la génération de récits
STORY_TEMPERATURE = 0.8

# Activer les animations de particules
ENABLE_PARTICLES = True

# Activer l'effet de neige au démarrage (comme dans le code original)
ENABLE_SNOW_EFFECT = False
