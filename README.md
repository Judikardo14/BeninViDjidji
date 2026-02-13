# 🇧🇯 BéninViDjidji - Bot de Promotion du Patrimoine Béninois

Un chatbot intelligent propulsé par Groq AI pour découvrir et promouvoir l'histoire, la géographie, la culture et le patrimoine du Bénin.

![Drapeau du Bénin](https://upload.wikimedia.org/wikipedia/commons/0/0a/Flag_of_Benin.svg)

## ✨ Fonctionnalités

### 💬 Chat Conversationnel
- Interface de chat interactive avec historique
- Réponses alimentées par Groq AI (modèles LLaMA 3.3 70B)
- Base de connaissances riche sur le Bénin
- Conversations contextuelles et engageantes

### 🎯 Quiz Culturel
- Questions sur l'histoire et la culture béninoise
- Système de score et statistiques
- Explications détaillées pour chaque réponse
- Questions aléatoires pour tester vos connaissances

### 📖 Générateur de Récits Historiques
- Création de récits captivants sur des thèmes historiques
- 6 thèmes disponibles : Royaume du Dahomey, Amazones, Traite négrière, Vaudou, etc.
- Styles narratifs multiples : éducatif, narratif, poétique, journalistique
- Longueur personnalisable : court, moyen, long
- Téléchargement des récits générés

### 🎨 Design
- Arrière-plan animé avec particles.js
- Palette de couleurs du drapeau béninois (vert, jaune, rouge)
- Interface moderne et responsive
- Animations fluides et interactives

## 📋 Prérequis

- Python 3.8 ou supérieur
- Une clé API Groq (gratuite)

## 🚀 Installation

1. **Cloner ou télécharger le projet**

2. **Installer les dépendances**

```bash
pip install streamlit groq
```

## 🔑 Obtenir une clé API Groq

1. Visitez [https://console.groq.com](https://console.groq.com)
2. Créez un compte gratuit
3. Allez dans "API Keys"
4. Générez une nouvelle clé API
5. Copiez la clé (format : `gsk_...`)

## 🎯 Utilisation

1. **Lancer l'application**

```bash
streamlit run benin_vidjidji.py
```

2. **Configurer l'API**
   - Dans la barre latérale, entrez votre clé API Groq
   - La clé sera sauvegardée pour la session en cours

3. **Explorer les fonctionnalités**
   - **Chat** : Posez des questions sur le Bénin
   - **Quiz** : Testez vos connaissances
   - **Récits** : Générez des histoires captivantes

## 📚 Contenu Couvert

### Histoire
- Royaume du Dahomey (17e-19e siècle)
- Amazones du Dahomey
- Indépendance (1er août 1960)
- Traite négrière et mémoire
- Personnages historiques

### Géographie
- Capitales : Porto-Novo et Cotonou
- Villes principales
- Relief et climat
- Frontières et voisins

### Culture
- Vaudou : religion traditionnelle
- Musique (Angélique Kidjo)
- Danses traditionnelles
- Artisanat
- Langues nationales

### Patrimoine UNESCO
- Palais royaux d'Abomey
- Sites historiques
- Monuments importants

## ⚙️ Paramètres Avancés

Dans la barre latérale, vous pouvez ajuster :

- **Modèle** : Choisissez entre LLaMA 3.3 70B, LLaMA 3.1 70B ou Mixtral 8x7B
- **Température** : Contrôle la créativité (0.0 = précis, 1.0 = créatif)
- **Tokens max** : Longueur maximale des réponses

## 🎨 Personnalisation

### Couleurs
Les couleurs du drapeau béninois sont intégrées partout :
- 💚 Vert : #008751
- 💛 Jaune : #FCD116
- ❤️ Rouge : #E8112d

### Ajouter votre logo
Pour intégrer votre logo, remplacez cette ligne dans le code :

```python
st.sidebar.image("CHEMIN_VERS_VOTRE_LOGO.png", width=200)
```

## 🌟 Exemples de Questions

- "Quelle est l'histoire des Amazones du Dahomey ?"
- "Parle-moi du Vaudou et de son origine"
- "Qu'est-ce que la Porte du non-retour à Ouidah ?"
- "Qui était le roi Béhanzin ?"
- "Quels sont les sites UNESCO au Bénin ?"

## 🐛 Dépannage

### L'application ne démarre pas
```bash
# Vérifier que Streamlit est installé
streamlit --version

# Réinstaller si nécessaire
pip install --upgrade streamlit
```

### Erreur d'API
- Vérifiez que votre clé API est valide
- Assurez-vous d'avoir des crédits disponibles sur Groq
- Vérifiez votre connexion Internet

### Problème d'affichage
- Effacez le cache du navigateur
- Rechargez la page (Ctrl+R ou Cmd+R)
- Essayez un autre navigateur

## 📝 Structure du Code

```
benin_vidjidji.py
├── Configuration (Streamlit + API)
├── Animation particles.js
├── CSS personnalisé
├── Base de connaissances
├── Questions de quiz
├── Thèmes de récits
├── Interface principale
│   ├── Onglet Chat
│   ├── Onglet Quiz
│   └── Onglet Récits
└── Footer
```

## 🤝 Contribution

Ce projet a été conçu pour promouvoir le patrimoine béninois. N'hésitez pas à :
- Ajouter plus de contenu historique
- Enrichir la base de questions du quiz
- Proposer de nouveaux thèmes de récits
- Améliorer l'interface

## 📄 Licence

Ce projet est créé dans un but éducatif et de promotion culturelle.

## 🙏 Remerciements

- **Groq** pour leur API rapide et puissante
- **Streamlit** pour le framework web
- **Particles.js** pour l'animation d'arrière-plan
- Tous les contributeurs à la connaissance du patrimoine béninois

## 📧 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue.

---

**💚💛❤️ Fait avec passion pour promouvoir le patrimoine du Bénin 🇧🇯**
