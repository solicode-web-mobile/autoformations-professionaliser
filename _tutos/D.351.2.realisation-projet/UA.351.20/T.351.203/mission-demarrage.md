---
layout: tuto
title: "Créer la mission de démarrage et son prompt d'ingénierie"
sous_titre: "Formaliser missions/1.init-projet.mission.md et concevoir le prompt d'étape missions/1.init-projet.prompt.md"
slug: "mission-demarrage"
slug_domaine: "realisation-projet"
slug_ua: "initialisation"
permalink: /tutos/mission-demarrage/
tuto_id: "T.351.203"
version: "normal"
ua: "UA.351.20"
maturite: "UA-Tâche"
nav_order: 3
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement & Emplacement du Livrable
- **Domaine :** `D.351.2` (`realisation-projet`)
- **Unité d'Apprentissage :** `UA.351.20` (`initialisation`)
- **Tutoriel :** `T.351.203` (`mission-demarrage`)
- **Type d'UA :** `UA-Tâche` *(Les livrables sont des fichiers de projet opérationnels — ils ne sont PAS placés dans le dossier `labs/`)*.
- **Position dans le flux :** Phase A — Initialisation du Projet, Outillage IA & Méthodologie / Étape 01 — Initialisation et publication du projet.
- **Branche Git :** `sprint1`
- **Emplacement exact des livrables :**
  - `missions/1.init-projet.mission.md` *(Sous-dossier missions/)*
  - `missions/1.init-projet.prompt.md` *(Sous-dossier missions/)*

## 2. Déroulement Pas-à-Pas de la Tâche

1. **Étape 1 — Analyse du contrat d'étape :**  
   Dans la démarche d'ingénierie augmentée par IA, chaque étape clé de réalisation fait l'objet d'une **fiche de mission** (contrat d'exécution pour l'apprenant et l'Agent) et d'un **prompt d'ingénierie** (outil de guidage déterministe au format RIO).

2. **Étape 2 — Rédaction de la fiche de mission `missions/1.init-projet.mission.md` :**  
   Dans le dossier `missions/`, créez le fichier `1.init-projet.mission.md` :

   ```markdown
   # Mission 1 : Initialisation et publication du projet

   ## 1. Objectif de la mission
   Initialiser l'espace de travail local du projet d'imitation *Blog des Lauréats*, créer l'arborescence standardisée, rédiger le `README.md` avec la stack technique N3, et publier le dépôt sur votre compte GitHub personnel sur la branche `sprint1`.

   ## 2. Prérequis
   - Présentation du projet par le formateur.
   - Outils installés : Git et GitHub CLI (`gh`).

   ## 3. Travail à réaliser
   1. Initialiser le dépôt Git local et configurer le `.gitignore`.
   2. Créer la branche de travail `sprint1`.
   3. Créer l'arborescence des 7 dossiers : `.agents/`, `docs/`, `flux-travail/`, `issues/`, `labs/`, `missions/`, `sprints/`.
   4. Rédiger le fichier `README.md` complet intégrant la stack N3.
   5. Publier le dépôt sur votre compte GitHub personnel via `gh repo create`.

   ## 4. Livrables attendus
   - Dépôt GitHub personnel public et accessible.
   - Fichiers `.gitignore`, `commandes.md`, `README.md` à la racine.
   - Fichiers `missions/1.init-projet.mission.md` et `missions/1.init-projet.prompt.md`.

   ## 5. Critères d'acceptation
   - [ ] La branche `sprint1` est active et à jour.
   - [ ] Le `README.md` détaille rigoureusement la stack N3 (Laravel 12, Blade, Tailwind, Alpine, CSV).
   - [ ] L'arborescence des dossiers est respectée.
   ```

3. **Étape 3 — Conception du prompt d'ingénierie `missions/1.init-projet.prompt.md` :**  
   Dans le dossier `missions/`, créez le fichier `1.init-projet.prompt.md` en appliquant la méthode RIO (Rôle, Instructions, Output délimité) avec contraintes négatives bloquantes :

   ```markdown
   # Prompt d'Ingénierie : Audit et Validation de l'Initialisation Projet

   ## Rôle
   Tu es le **Coach Technique Solicode N3** et l'assistant de vérification du projet d'imitation *Blog des Lauréats*.

   ## Contexte
   L'apprenant vient d'exécuter la première étape du Sprint 1 : initialisation du dépôt Git, création de l'arborescence de travail, rédaction du README.md avec la stack technique N3 et publication sur son compte GitHub personnel.

   ## Instructions
   1. Inspecte l'arborescence du projet et vérifie la présence des 7 dossiers obligatoires : `.agents/`, `docs/`, `flux-travail/`, `issues/`, `labs/`, `missions/`, `sprints/`.
   2. Vérifie que le fichier `README.md` contient bien la stack technique N3 (Laravel 12, Blade, Tailwind CSS, Alpine.js, architecture 2 couches).
   3. Vérifie que le fichier `.gitignore` exclut `.env`, `vendor/` et `node_modules/`.
   4. Valide que le travail est positionné sur la branche unique `sprint1`.
   5. Rédige un rapport de conformité concis indiquant si l'étape est validée pour passer à l'étape suivante.

   ## Contraintes Négatives
   - Ne pas accepter de capture d'écran comme preuve.
   - Refuser tout fichier de livrable déposé dans `labs/` pour cette étape (l'UA étant une UA-Tâche).
   - Répondre avec un français professionnel A1-A2 clair et direct.

   ## Format de Sortie
   - Tableau récapitulatif de validation (Élément vérifié, Statut Conforme/Non-conforme, Observation).
   - Décision finale : `[VALIDÉ]` ou `[À CORRIGER]`.
   ```

4. **Étape 4 — Test et validation avec l'Agent IA :**  
   Soumettez le prompt à l'Agent IA Antigravity pour tester sa capacité à auditer votre dépôt sans hallucination et vérifier le retour du tableau de conformité.

5. **Étape 5 — Sauvegarde et publication sur la branche de sprint :**  
   Indexez les fichiers de mission et publiez sur la branche `sprint1` de votre compte personnel :
   ```bash
   git add missions/1.init-projet.mission.md missions/1.init-projet.prompt.md
   git commit -m "docs: formaliser la mission 1.init-projet et son prompt d'ingénierie"
   git push origin sprint1
   ```

## 3. Livrables & Critères de Réussite
- **Livrables attendus :**
  - Fichier `missions/1.init-projet.mission.md` sur la branche `sprint1`.
  - Fichier `missions/1.init-projet.prompt.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] La mission `missions/1.init-projet.mission.md` formalise les objectifs et critères de l'étape 1.
  - [ ] Le prompt `missions/1.init-projet.prompt.md` respecte la méthode RIO avec contraintes négatives strictes.
  - [ ] Les deux fichiers sont situés dans `missions/` et publiés sur `sprint1`.
