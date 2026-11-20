---
layout: tuto
title: "Définir la vision produit et exprimer les besoins en User Stories"
sous_titre: "Formuler la Vision Produit, concevoir les Personas cibles et rédiger les User Stories avec critères d'acceptation"
slug: "vision-besoins"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
permalink: /tutos/vision-besoins/
tuto_id: "T.351.112"
version: "normal"
ua: "UA.351.11"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
sprint: "sprint1"
statut_realisation: "realise"
livrables:
  - chemin: "tutoriels/scrum/initiation-scrum/vision-besoins/vision-besoins.md"
    version: "1.0.0"
  - chemin: "tutoriels/scrum/initiation-scrum/vision-besoins/presentation-vision-besoins.md"
    version: "1.0.0"
---

## 1. Travail à faire
Cadrer le besoin fonctionnel de votre projet technique individuel en formulant la Vision Produit, en identifiant les utilisateurs cibles à l'aide de Personas réalistes et en rédigeant les User Stories majeures avec des critères d'acceptation vérifiables.

> [!NOTE]
> **Projet Technique de Référence :** Ce tutoriel est rédigé et illustré à partir du **Portfolio Développeur**, qui sert d'exemple concret de Projet Technique. Vous devez vous approprier cette démarche pour modéliser les besoins de **votre propre projet technique**.

## 2. Notions fondamentales
- **La Vision Produit (Product Vision) :**
  - Résume en quelques phrases l'ambition, le public cible, le problème résolu et la valeur ajoutée du produit.
  - Sert de boussole à l'équipe et guide les choix d'arbitrage fonctionnel.
- **La Méthode des Personas :**
  - Un Persona est un personnage fictif représentant un groupe d'utilisateurs réels partageant des habitudes, des objectifs et des contraintes similaires.
  - Permet de concevoir des fonctionnalités centrées sur des attentes concrètes plutôt que sur des suppositions abstraites.
- **Le Formalisme de la User Story :**
  - Décrit une fonctionnalité du point de vue de l'utilisateur final en 3 éléments canoniques :
    - *En tant que* [rôle de l'utilisateur] : qui exprime le besoin ?
    - *Je veux* [action ou fonctionnalité souhaitée] : quelle est la tâche à accomplir ?
    - *Afin de* [bénéfice ou valeur métier] : quelle est la finalité ou la valeur apportée ?
- **Les Critères d'Acceptation (Acceptance Criteria) :**
  - Définissent les conditions de succès claires et mesurables pour valider une User Story.
  - Servent de base directe aux scénarios de tests fonctionnels exécutés par les développeurs.
- **Délimitation du Périmètre (Scope / MVP) :**
  - Isoler le Minimum Viable Product (MVP) comprenant le strict nécessaire pour apporter de la valeur et reporter les fonctionnalités secondaires aux itérations futures.

## 3. Application pratique sur le Projet Technique (Exemple Portfolio)
- **Exemple de Vision Produit (Portfolio) :** Offrir une vitrine web moderne, rapide et responsive valorisant mon identité de développeur web, démontrant mes compétences techniques à travers des projets réels, et facilitant un contact direct avec les recruteurs.
- **Exemple de Personas Cibles :**
  - *Sarah (Recruteuse RH Tech) :* Consulte rapidement, veut identifier la stack technique, la localisation et télécharger le CV en un clic.
  - *Karim (Lead Développeur & Évaluateur Technique) :* Examine la qualité du code sur GitHub, teste les démos en direct et contrôle le responsive.
- **Exemple de 5 User Stories Majeures du MVP :**
  - *US-01 (Présentation personnelle) :* En tant que recruteur visitant le portfolio, je veux lire une brève biographie avec ma photo et mon titre professionnel, afin d'identifier immédiatement mon profil de développeur Web.
  - *US-02 (Vitrine des réalisations) :* En tant que lead dev évaluant le candidat, je veux parcourir une galerie de projets avec démos en ligne et liens GitHub sécurisés, afin de juger de la qualité technique du code.
  - *US-03 (Compétences techniques) :* En tant que recruteur tech, je veux visualiser l'ensemble des compétences classées par catégories (Front, Back, Outils), afin de vérifier l'adéquation avec les postes à pourvoir.
  - *US-04 (Formulaire de contact) :* En tant que prospect ou recruteur, je veux envoyer un message via un formulaire validé, afin d'entrer facilement en relation.
  - *US-05 (Téléchargement du CV PDF) :* En tant que recruteur RH, je veux télécharger le CV complet au format PDF en un clic.
- **Délimitation MVP vs Évolutions reportées :**
  - *Inclus dans le MVP :* US-01 à US-05 (One-Page responsive).
  - *Reporté (post-MVP) :* Dark mode, blog intégré, multilingue.

## 4. Livrables & Critères de validation
- **Livrables attendus :**
  - Fiche technique d'atelier : `tutoriels/scrum/initiation-scrum/vision-besoins/vision-besoins.md` sur la branche `sprint1`.
  - Diaporama Marp de restitution : `tutoriels/scrum/initiation-scrum/vision-besoins/presentation-vision-besoins.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] La Vision Produit de votre projet technique est explicitement formulée.
  - [ ] Au moins 2 Personas sont caractérisés avec leurs attentes et contraintes spécifiques.
  - [ ] Les User Stories respectent rigoureusement le gabarit *En tant que... je veux... afin de...*.
  - [ ] Chaque User Story comporte au moins 2 critères d'acceptation concrets et testables.
  - [ ] Le périmètre du MVP de votre projet technique est délimité sans ambiguïté.
