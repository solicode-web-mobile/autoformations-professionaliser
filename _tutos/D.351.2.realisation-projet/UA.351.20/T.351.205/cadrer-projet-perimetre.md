---
layout: tuto
title: "Cadrer le projet et délimiter le périmètre (In-Scope vs Out-of-Scope)"
sous_titre: "Formaliser les objectifs SMART, la matrice de périmètre stricte et les contraintes du Blog des Lauréats"
slug: "cadrer-projet-perimetre"
slug_domaine: "realisation-projet"
slug_ua: "initialisation"
permalink: /tutos/cadrer-projet-perimetre/
tuto_id: "T.351.205"
version: "normal"
ua: "UA.351.20"
maturite: "UA-Tâche"
nav_order: 5
simplified: true
en_construction: false
branche: "sprint0"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
sprint: "Sprint 0"
statut_realisation: "realise"
livrables:
  - chemin: "docs/cadrage/note-cadrage.md"
    version: "1.0.0"
  - chemin: "tutoriels/realisation-projet/initialisation/cadrer-projet-perimetre/cadrer-projet-perimetre.md"
    version: "1.0.0"
---

## 1. Travail à faire
Poser le cadre méthodologique et technique officiel du *Blog des Lauréats* : formaliser la note de cadrage délimitant les objectifs SMART, identifier les parties prenantes et leurs attentes, construire la matrice de périmètre stricte (ce qui est inclus dans le projet vs ce qui est exclu), identifier les contraintes réglementaires et de délai, et enregistrer le document sous `docs/cadrage/note-cadrage.md`.

## 2. Notions fondamentales
- **La Note de Cadrage :**
  - Document fondateur contractualisant la promesse du projet entre le Product Owner (Groupe 1) et l'équipe de développement.
  - Évite l'effet tunnel et les dérives de périmètre (*scope creep*).
- **Les Objectifs SMART :**
  - Spécifique, Mesurable, Atteignable, Réaliste, Temporellement défini.
- **La Matrice In-Scope vs Out-of-Scope :**
  - Outil d'arbitrage capital déterminant explicitement ce qui fait partie de l'engagement projet et ce qui est formellement exclu ou différé.

## 3. Application pratique sur le Blog des Lauréats
- **Objectifs SMART du projet :**
  - Livrer une vitrine web moderne valorisant les profils et articles des lauréats de Solicode.
  - Développer selon les standards industriels (Laravel, architecture 2 couches, tests TDD, Tailwind CSS / Preline UI).
- **Périmètre In-Scope :**
  - Consultation publique d'un article, catalogue d'articles, gestion des catégories et profils lauréats.
- **Périmètre Out-of-Scope (Sprint 0 / S1) :**
  - Système de paiement en ligne, messagerie instantanée en direct, application mobile native.
- **Arborescence cible :** Enregistrement dans `docs/cadrage/note-cadrage.md`.

## 4. Livrables & Critères de validation
- **Livrables attendus :**
  - Note de cadrage projet officielle : `docs/cadrage/note-cadrage.md sur la branche sprint0`.
  - Fiche de synthèse : `tutoriels/realisation-projet/initialisation/cadrer-projet-perimetre/cadrer-projet-perimetre.md sur la branche sprint0`.
- **Critères de validation :**
  - [ ] Les objectifs du projet respectent les 5 critères SMART.
  - [ ] La matrice In-Scope vs Out-of-Scope délimite clairement les frontières fonctionnelles.
  - [ ] Les contraintes techniques, de délais et de sécurité sont explicitées.
