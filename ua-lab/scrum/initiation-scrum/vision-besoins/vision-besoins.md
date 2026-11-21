---
layout: default
title: "Fiche d'Atelier : Définir la vision produit et les User Stories"
---
# Tutoriel 2 : Définir la vision produit et exprimer les besoins en User Stories

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-vision-besoins.html](./presentation-vision-besoins.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Encadrant** : ESSARRAJ Fouad | EFP

---

## 1. Objectifs d'apprentissage

Ce deuxième tutoriel permet d'apprendre à cadrer le besoin fonctionnel d'un projet web :
- Savoir formuler une Vision Produit claire pour guider l'ensemble des développements.
- Identifier avec précision les utilisateurs cibles à l'aide de Personas réalistes.
- Maîtriser le formalisme canonique d'une User Story : *En tant que... je veux... afin de...*
- Rédiger des critères d'acceptation concrets et vérifiables pour chaque besoin.
- Délimiter le périmètre initial du produit pour éviter l'éparpillement.
- Appliquer ces principes au cadrage complet de votre **Blog des Lauréats**.

---

## 2. Volet Théorique : Vision, Personas et User Stories

### 2.1 La Vision Produit (Product Vision)
- La Vision Produit est le phare du projet : elle résume en quelques phrases l'ambition, le public cible, le problème résolu et la valeur ajoutée du produit.
- Elle permet à l'équipe de savoir en permanence pourquoi elle développe cette application.
- Elle aide à prendre les bonnes décisions d'arbitrage lors des choix fonctionnels.

### 2.2 Identifier les cibles : La méthode des Personas
- Un Persona est un personnage fictif représentant un groupe d'utilisateurs réels ayant des besoins, des habitudes et des objectifs communs.
- Donner une identité, un contexte et des attentes concrètes à son Persona permet de concevoir des fonctionnalités centrées sur l'utilisateur réel, plutôt que sur des suppositions abstraites.

### 2.3 Le formalisme de la User Story
Une User Story (histoire utilisateur) décrit une fonctionnalité du point de vue de la personne qui l'utilise. Elle suit la structure standard en 3 parties :
- **En tant que** [rôle de l'utilisateur] : qui exprime le besoin ?
- **Je veux** [action ou fonctionnalité souhaitée] : quelle est la tâche à accomplir ?
- **Afin de** [bénéfice ou valeur métier] : quelle est la finalité ou la valeur apportée ?

### 2.4 Les Critères d'Acceptation (Acceptance Criteria)
- Une User Story ne suffit pas à elle seule : elle doit être accompagnée de conditions de succès claires.
- Les critères d'acceptation décrivent exactement ce qui doit fonctionner pour que la fonctionnalité soit validée.
- Ils servent de base aux tests fonctionnels que le développeur effectue avant de clore sa tâche.

### 2.5 Délimiter le périmètre (Scope)
- En début de projet, le piège classique est de vouloir intégrer toutes les idées en même temps.
- L'approche agile préconise de définir un périmètre initial réduit et de qualité (le Minimum Viable Product - MVP), et de reporter les fonctionnalités secondaires aux itérations suivantes.

---

## 3. Application Pratique : Cadrage du Blog des Lauréats

### 3.1 Déclaration de Vision du Portfolio
- **Vision** : *"Offrir une vitrine web moderne, rapide et responsive qui valorise mon identité de développeur web, démontre concrètement mes compétences techniques à travers des projets réels, et permet aux recruteurs de me contacter directement."*
- **Objectif principal** : Obtenir un entretien technique ou une opportunité professionnelle grâce à une démonstration concrète de savoir-faire.

### 3.2 Définition des Personas cibles
- **Persona 1 : Sarah — Recruteuse RH Tech**
  - Profil : Consulte des dizaines de profils par jour sur LinkedIn.
  - Objectif : Vérifier rapidement la disponibilité, la localisation, les technos maîtrisées et télécharger le CV en un clic.
  - Attente clé : Navigation fluide, temps de chargement immédiat, informations de contact visibles dès la première seconde.
- **Persona 2 : Karim — Lead Développeur & Évaluateur Technique**
  - Profil : Développeur senior chargé d'évaluer le niveau technique des candidats.
  - Objectif : Voir les projets réalisés, tester les démos en direct et examiner la propreté du code source sur GitHub.
  - Attente clé : Liens fonctionnels vers les dépôts GitHub, design responsive irréprochable, code HTML sémantique.

### 3.3 Rédaction des 5 User Stories majeures du Portfolio

- **User Story 1 : Présentation personnelle et accroche**
  - *Énoncé* : En tant que recruteur visitant le portfolio, je veux lire une brève biographie professionnelle accompagnée d'une photo et de mon titre, afin d'identifier immédiatement mon profil de développeur Web.
  - *Critères d'acceptation* :
    - Le titre du poste (ex : Développeur Web Full-Stack) est visible sans défilement (above the fold).
    - Un paragraphe de 3 à 5 lignes résume mon parcours, mes motivations et ma spécialité.
    - Une photo professionnelle ou un avatar soigné s'affiche correctement sur tout type d'écran.

- **User Story 2 : Vitrine des réalisations (Projets phares)**
  - *Énoncé* : En tant que lead développeur évaluant le candidat, je veux parcourir une galerie des projets développés, afin de juger de la qualité technique et visuelle de son travail.
  - *Critères d'acceptation* :
    - Chaque projet comprend : un titre, une capture d'écran, une description brève, les technologies utilisées (badges).
    - Deux boutons d'action sont présents pour chaque projet : *Voir la démo en ligne* et *Voir le code sur GitHub*.
    - Les liens externes s'ouvrent dans un nouvel onglet sécurisé (`target="_blank"` avec `rel="noopener noreferrer"`).

- **User Story 3 : Tableau des compétences techniques (Stack)**
  - *Énoncé* : En tant que recruteur technique, je veux visualiser l'ensemble des compétences et outils maîtrisés par catégorie, afin de vérifier leur adéquation avec les postes à pourvoir.
  - *Critères d'acceptation* :
    - Les compétences sont regroupées par catégories claires : Front-End (HTML5, CSS3, JavaScript, Tailwind), Back-End (PHP, Laravel, MySQL) et Outils (Git, GitHub, VS Code).
    - L'affichage reste lisible et s'adapte automatiquement sur écran mobile.

- **User Story 4 : Formulaire de contact fonctionnel**
  - *Énoncé* : En tant que prospect ou recruteur intéressé, je veux envoyer un message via un formulaire en ligne, afin d'entrer facilement en relation avec le développeur.
  - *Critères d'acceptation* :
    - Le formulaire comporte au minimum 3 champs : Nom complet, Adresse email, Message.
    - Les champs obligatoires sont signalés et validés par le navigateur.
    - Un message visuel de confirmation s'affiche après la soumission du formulaire.

- **User Story 5 : Téléchargement du CV au format PDF**
  - *Énoncé* : En tant que recruteur RH, je veux télécharger le CV complet au format PDF en un clic, afin de le conserver dans ma base de candidatures.
  - *Critères d'acceptation* :
    - Un bouton bien visible *Télécharger mon CV* est présent dans l'en-tête ou la barre de navigation.
    - Le clic déclenche le téléchargement d'un fichier PDF propre et à jour.

### 3.4 Délimitation du périmètre initial (MVP)
- **Inclus dans le périmètre du MVP** : Les 5 User Stories ci-dessus (page unique responsive One-Page).
- **Exclu du périmètre initial (reporté à plus tard)** : Blog intégré, bascule en mode sombre (dark mode), version multilingue (français/anglais), animations complexes.

---

## 4. Auto-évaluation et Validation

Vérifiez que vous avez bien validé cette étape :
- Vous avez défini la Vision Produit de votre Blog des Lauréats.
- Vous avez identifié 2 personas cibles aux attentes complémentaires.
- Vos 5 User Stories respectent le format *En tant que... je veux... afin de...* avec des critères d'acceptation concrets.
- Vous avez délimité le périmètre du MVP sans déborder sur des fonctionnalités superflues.
- Vous êtes prêt à prioriser et estimer ce travail dans le Product Backlog lors du Tutoriel 3.
