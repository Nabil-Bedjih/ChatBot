
# Nom du Projet
ChatBot

## Description

Ce projet utilise **Rasa** pour développer un chatbot capable de gérer les réservations, les annulations, et les interactions de confirmation avec les utilisateurs. Il inclut également des fonctionnalités avancées de reconnaissance d'intention et de suivi de conversation.

## Fonctionnalités

- **Gestion des Réservations** : Permet de réserver un service en suivant les étapes nécessaires (nom, numéro de téléphone, nombre de personnes, etc.).
- **Annulation de Réservation** : Prend en charge l'annulation des réservations existantes en confirmant avec le code de réservation fourni.
- **Confirmation** : Inclut des étapes de confirmation pour éviter les erreurs lors de la réservation ou l'annulation.
- **Reconnaissance d'Intention** : Utilisation de la reconnaissance d'intentions avec le modèle **DIETClassifier** de Rasa pour mieux comprendre les demandes des utilisateurs.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

- [Python](https://www.python.org/downloads/) (version 3.7 ou plus récente)
- [Rasa](https://rasa.com/docs/rasa/installation) (version 2.0 ou plus récente)
- Clé d'API pour les services de stockage des réservations (si nécessaire)

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-projet.git
   cd votre-projet
   ```


2. **Configurer vos identifiants et le token d'accès** :

   Mettez à jour le fichier `credentials.yml` avec votre **token** et votre **identifiant de channel** pour permettre la connexion avec lvotre serveur Discord. Assurez-vous également que les informations sont correctement référencées dans le fichier `start.py`.

3. **Entraîner le modèle Rasa** :
   ```bash
   rasa train
   ```

4. **Lancer le chatbot** :
   - Démarrez Rasa en mode interactif :
     ```bash
     rasa shell
     ```
   - Ou lancez Rasa en mode serveur HTTP :
     ```bash
     rasa run -m models --enable-api --cors "*"
     ```

5. **Démarrer le fichier `start.py`** :  
   Une fois Rasa démarré, lancez le fichier `start.py` pour initialiser les paramètres du bot :
   ```bash
   python start.py
   ```

## Utilisation

- **Conversation** : Démarrez une conversation avec le chatbot pour réserver, annuler, ou confirmer une réservation.
- **Debugging** : Utilisez `rasa interactive` pour tester les dialogues et ajuster les réponses.
- **conversation avec Discord** : Démarrez une conversation avec le chatbot directement depuis votre serveur Discord.

## Structure du Projet

- `actions/` : Contient les actions personnalisées que le bot peut exécuter.
- `data/` : Inclut les exemples de conversations pour entraîner le modèle.
- `models/` : Dossier contenant les modèles entraînés.

## Contributions

Les contributions sont les bienvenues ! Merci de suivre ces étapes :

1. Forkez ce dépôt
2. Créez votre branche (`git checkout -b feature/nom-feature`)
3. Commitez vos modifications (`git commit -am 'Ajouter une nouvelle fonctionnalité'`)
4. Pushez la branche (`git push origin feature/nom-feature`)
5. Créez une Pull Request
