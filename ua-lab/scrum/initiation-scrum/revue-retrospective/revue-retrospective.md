---
layout: default
title: "Fiche d'Atelier : Valider l'incrément, animer la Sprint Review et la Rétrospective"
---
# Tutoriel 5 : Valider l'incrément, animer la Sprint Review et la Rétrospective

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-revue-retrospective.html](./presentation-revue-retrospective.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Encadrant** : ESSARRAJ Fouad | EFP

---

## 1. Objectifs d'apprentissage

Ce cinquième et dernier tutoriel permet d'apprendre à clôturer une itération avec rigueur et à s'inscrire dans une démarche d'amélioration continue :
- Comprendre le rôle et l'organisation d'une réunion de Revue de Sprint (*Sprint Review*).
- Savoir faire la démonstration en direct d'un incrément fonctionnel répondant à la *Definition of Done*.
- Recueillir et analyser les retours des utilisateurs et parties prenantes pour réajuster le Product Backlog.
- Animer une réunion de Rétrospective de Sprint (*Sprint Retrospective*) pour analyser ses pratiques.
- Formuler un plan d'actions d'amélioration mesurables et réalistes pour le Sprint suivant.
- Mettre en pratique cette double cérémonie sur votre **Blog des Lauréats**.

---

## 2. Volet Théorique : Revue de Sprint, Rétrospective et Amélioration

### 2.1 La Revue de Sprint (Sprint Review)
La Sprint Review a lieu le dernier jour du Sprint. C'est le moment privilégié d'inspection du produit :
- **Principe fondamental** : On ne présente pas des diapositives théoriques, on fait une démonstration en direct d'un logiciel réellement opérationnel.
- L'équipe présente uniquement les éléments qui satisfont à 100% la *Definition of Done*.
- Les parties prenantes (utilisateurs, clients, formateur) testent les fonctionnalités, donnent leurs avis et proposent des ajustements.
- Le Product Owner met à jour le Product Backlog en fonction des retours obtenus.

### 2.2 La Rétrospective de Sprint (Sprint Retrospective)
Alors que la Revue inspecte le **produit**, la Rétrospective inspecte le **fonctionnement de l'équipe** :
- Elle réunit l'équipe Scrum (PO, SM, Développeurs) pour évaluer comment s'est déroulé le Sprint sur les plans humain, méthodologique, technique et organisationnel.
- Elle repose sur la confiance et la bienveillance : l'objectif n'est pas de chercher des coupables, mais de comprendre les causes profondes des difficultés rencontrées.
- Elle se structure traditionnellement autour de 3 questions :
  - Qu'est-ce qui a bien fonctionné et que nous devons continuer à faire ?
  - Qu'est-ce qui a été difficile, inefficace ou source de blocage ?
  - Quelles actions concrètes décidons-nous d'appliquer dès le prochain Sprint pour progresser ?

### 2.3 Le plan d'actions d'amélioration continue
- Une rétrospective sans plan d'actions ne sert à rien.
- L'équipe choisit 2 à 3 actions concrètes, immédiatement applicables dès le Sprint suivant.
- Ces actions sont traitées comme des tâches prioritaires au même titre que les fonctionnalités techniques.

---

## 3. Application Pratique : Clôture du Sprint 1 du Portfolio

### 3.1 Démonstration de l'Incrément (Sprint Review)
À l'issue des 5 jours de code du Sprint 1, vous procédez à la démonstration de votre site portfolio :
- **Vérification de l'atteinte du Sprint Goal** :
  - La page web One-Page se charge rapidement et affiche correctement l'identité professionnelle et la présentation (US-01).
  - La section compétences présente les 3 catégories avec des badges clairs et lisibles (US-03).
  - Les 2 projets phares s'affichent avec leurs captures d'écran, descriptions et boutons fonctionnels (US-02).
- **Contrôle de la Definition of Done (DoD)** :
  - Test multi-écrans : la page s'adapte parfaitement sur écran large d'ordinateur et sur écran smartphone via l'émulateur DevTools.
  - Absence totale d'erreurs dans la console d'inspection (zéro avertissement rouge).
  - Les liens externes vers GitHub s'ouvrent dans un nouvel onglet avec `target="_blank"` et `rel="noopener noreferrer"`.
  - Le code source final du Sprint 1 est versionné et synchronisé sur Git.
- **Recueil des retours d'un évaluateur externe** :
  - Présentez votre site à un pair apprenant ou à votre formateur référent.
  - Notez les remarques formulées (ex : *"Le contraste de la couleur du sous-titre est un peu faible sur fond clair"*, *"Les images des projets mériteraient d'être agrandies"*).
  - Ces retours sont immédiatement ajoutés au Product Backlog sous forme de petites tâches d'ajustement pour le Sprint 2.

### 3.2 Conduite de la Rétrospective du Sprint 1
En tant que développeur autonome sur votre projet, analysez votre semaine de développement :

- **Ce qui a très bien fonctionné** :
  - Les estimations des stories US-01 (Présentation) et US-03 (Compétences) étaient justes et le découpage technique a été respecté.
  - L'usage du tableau Kanban a permis de maintenir un focus constant et de ne pas s'éparpiller sur des détails secondaires.
  - Le balisage sémantique HTML5 a été appliqué avec rigueur dès la première ligne de code.

- **Ce qui a été difficile ou source de ralentissement** :
  - La mise en page responsive des cartes de projets (US-02) a pris plus de temps que prévu en raison de dimensions d'images non uniformisées au départ.
  - Tendance à tester le responsive uniquement à la fin du Sprint plutôt qu'au fil de l'eau.

- **Les 3 actions d'amélioration concrètes pour le Sprint 2** :
  - **Action 1** : Recadrer et normaliser toutes les images aux dimensions exactes (ex : 800x450 px en format WebP) avant de les intégrer dans le code HTML.
  - **Action 2** : Effectuer la vérification mobile dans les DevTools dès la fin de chaque sous-tâche CSS, sans attendre la fin de la semaine.
  - **Action 3** : Configurer un formatteur de code automatique (Prettier) pour garantir une indentation irréprochable sans perte de temps manuelle.

### 3.3 Préparation du Sprint 2
- Réajustement du Product Backlog : intégration des retours de la revue et des actions de rétrospective.
- Les fonctionnalités prévues pour le Sprint 2 sont prêtes :
  - **US-04** : Formulaire de contact fonctionnel avec contrôles de saisie (5 points).
  - **US-05** : Bouton de téléchargement du CV au format PDF (1 point).
  - **Ajustements Sprint 1** : Amélioration du contraste des sous-titres et recadrage des visuels (1 point).
- Charge prévisionnelle du Sprint 2 : **7 Story Points**, ce qui laisse du temps pour peaufiner l'accessibilité et les tests.

---

## 4. Auto-évaluation et Bilan de l'Unité d'Apprentissage

Félicitations ! En complétant ces 5 tutoriels, vous avez acquis et appliqué l'intégralité du cycle Scrum :
- Vous comprenez l'intérêt des méthodes Agiles face au modèle classique.
- Vous savez formuler une vision et exprimer des exigences en User Stories avec critères d'acceptation.
- Vous maîtrisez la structuration et la priorisation d'un Product Backlog par la valeur.
- Vous savez organiser un Sprint en le découpant en tâches techniques concrètes.
- Vous pratiquez la démonstration d'incrément, le recueil de retours et l'amélioration continue en rétrospective.
- Votre **Blog des Lauréats** dispose d'un premier incrément opérationnel et d'une méthode de gestion solide pour ses évolutions futures.
