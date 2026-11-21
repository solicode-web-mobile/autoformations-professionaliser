---
layout: tuto
title: "Valider l'incrément, animer la Sprint Review et la Rétrospective"
sous_titre: "Faire la démonstration de l'incrément en direct, collecter les feedbacks et définir le plan d'actions d'amélioration"
slug: "revue-retrospective"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
permalink: /tutos/revue-retrospective/
tuto_id: "T.351.115"
version: "normal"
ua: "UA.351.11"
maturite: "ua-lab"
type: "tuto-atelier"
nav_order: 5
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
  - chemin: "tutoriels/scrum/initiation-scrum/revue-retrospective/revue-retrospective.md"
    version: "1.0.0"
  - chemin: "tutoriels/scrum/initiation-scrum/revue-retrospective/presentation-revue-retrospective.md"
    version: "1.0.0"
---

## 1. Travail à faire
Clôturer le cycle du Sprint 1 sur votre projet technique individuel selon les règles Scrum : animer la démonstration en direct de l'incrément logiciel opérationnel (*Sprint Review*), collecter les retours d'un évaluateur externe, animer la réunion d'amélioration réflexive (*Sprint Retrospective*) et formaliser 3 actions concrètes pour le Sprint 2.

> [!NOTE]
> **Projet Technique de Référence :** Ce tutoriel est rédigé et illustré à partir du **Portfolio Développeur**, qui sert d'exemple concret de Projet Technique. Vous devez appliquer et transposer cette démarche de clôture et d'amélioration continue à **votre propre projet technique**.

## 2. Notions fondamentales
- **La Revue de Sprint (Sprint Review) :**
  - Consacrée à l'inspection du **produit**.
  - *Règle essentielle :* Démonstration en direct d'un logiciel réellement fonctionnel satisfaisant à 100% à la *Definition of Done* (aucune présentation PowerPoint abstraite).
  - Recueil des retours des parties prenantes (utilisateurs, formateur, pairs) et réajustement immédiat du Product Backlog.
- **La Rétrospective de Sprint (Sprint Retrospective) :**
  - Consacrée à l'inspection du **fonctionnement de l'équipe** (processus, outils, communication, relations humaines).
  - Établie sur un climat de bienveillance et de responsabilité collective autour de 3 axes :
    - *Ce qui a bien fonctionné et qu'il faut conserver.*
    - *Ce qui a été difficile ou source d'inefficacité.*
    - *Quelles actions correctives appliquer dès le sprint suivant.*
- **Le Plan d'Actions d'Amélioration Continue :**
  - Formalise 2 à 3 décisions concrètes, mesurables et immédiatement applicables traitées comme des tâches prioritaires dans le Sprint suivant.

## 3. Application pratique sur le Projet Technique (Exemple Portfolio)
- **Exemple de Démonstration d'Incrément (Sprint Review) :**
  - Validation du Sprint Goal : page web One-Page chargée instantanément, présentation personnelle (US-01), section compétences à 3 catégories (US-03) et vitrine de 2 projets phares avec liens GitHub (US-02).
  - Contrôle DoD : mise en page responsive multi-écrans sans débordement, console d'inspection sans erreur rouge, liens ouverts dans un nouvel onglet sécurisé.
  - Collecte de retours : recueil des remarques formulées par un pair/formateur (ex. rehaussement du contraste et agrandissement des visuels) intégrées dans le backlog pour le Sprint 2.
- **Exemple de Rétrospective du Sprint 1 :**
  - *Points forts :* Précision des estimations des stories statiques (US-01 et US-03), discipline du tableau Kanban, code HTML5 sémantique.
  - *Difficultés :* Temps imprévu pour adapter les dimensions hétérogènes des images de projets (US-02), tests responsive trop tardifs.
  - *3 Actions d'amélioration pour le Sprint 2 :*
    1. Recadrer et normaliser tous les visuels aux dimensions exactes (ex : 800x450 px WebP) avant toute intégration HTML.
    2. Tester le comportement mobile dans les DevTools dès l'achèvement de chaque sous-tâche CSS.
    3. Configurer un formateur automatique de code (Prettier) pour garantir une indentation homogène.
- **Préparation du Sprint 2 :**
  - Charge planifiée : US-04 (Formulaire de contact - 5 pts) + US-05 (Téléchargement CV - 1 pt) + Retouches graphiques (1 pt) = **7 Story Points**.

## 4. Livrables & Critères de validation
- **Livrables attendus :**
  - Fiche technique d'atelier : `tutoriels/scrum/initiation-scrum/revue-retrospective/revue-retrospective.md` sur la branche `sprint1`.
  - Diaporama Marp de restitution : `tutoriels/scrum/initiation-scrum/revue-retrospective/presentation-revue-retrospective.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Les résultats de la démonstration en direct de votre projet technique et la conformité à la DoD sont documentés.
  - [ ] Les retours de l'évaluateur externe sont consignés avec leur répercussion dans le Product Backlog.
  - [ ] La rétrospective analyse sincèrement les points forts et difficultés rencontrées sur votre projet.
  - [ ] 3 actions d'amélioration concrètes, mesurables et réalistes sont contractualisées pour le Sprint 2.
