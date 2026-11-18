---
layout: tuto
title: "Créer l'Agent et le skill gestion-depot avec la mission init-projet"
sous_titre: "Outiller l'Agent IA avec le skill gestion-depot et formaliser la mission missions/1.init-projet.mission.md"
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

## 1. Prérequis
- **Base théorique et pratique requise :**
  - Architecture d'un Agent IA outillé (règles permanentes et skills outillés).
  - Protocole de pilotage d'ingénierie par fiches de missions (`missions/*.mission.md`).
  - Méthode d'audit et exécution conditionnelle (audit par plan si tâche non précisée, exécution directe si tâche ciblée).
- **Prérequis de projet :** Dépôt publié sur la branche `sprint1` (`T.351.201`) et `README.md` rédigé (`T.351.202`).
- **Branche Git :** `sprint1`

## 2. Travail à Faire
- **Tâche 1 : Mission d'étape (Mode Chatbot) :** Rédiger la fiche de mission `missions/1.init-projet.mission.md` définissant les 3 tâches, les livrables, le protocole d'audit et la structure du `README.md`.
- **Tâche 2 : Skill outillé (Mode Agent) :** Créer le skill `.agents/skills/gestion-depot/SKILL.md` permettant à l'Agent d'auditer et d'exécuter l'initialisation locale, la publication GitHub et la structuration du `README.md`.
- **Tâche 3 : Guide d'utilisation du skill :** Créer le guide d'utilisation opérationnel `.agents/skills/gestion-depot/doc/how-to-use.md`.

## 3. Étapes de Réalisation

1. **Étape 1 — Rédaction de la fiche de mission `missions/1.init-projet.mission.md` :**  
   Dans le dossier `missions/`, créez le fichier `1.init-projet.mission.md` en intégrant le contrat opérationnel :

   ```markdown
   # Mission : Initialisation du Projet (`init-projet.md`)

   Initialiser le projet en local, le publier sur GitHub et structurer son fichier `README.md` racine.

   ## Tâches de la mission
   - **Tâche 1 : Initialisation locale** : Vérifier ou exécuter l'initialisation Git locale (`git init`) et le commit initial.
   - **Tâche 2 : Publication sur GitHub** :
     - Publier le dépôt via GitHub CLI avec la commande : `gh repo create`.
     - Si GitHub CLI (`gh`) n'est pas installé ou non connecté : indiquer à l'apprenant d'installer et de s'authentifier avec GitHub CLI.
   - **Tâche 3 : Rédaction du README.md** : Reformuler et structurer le fichier `README.md` racine selon la structure du livrable ci-dessous en intégrant la stack technique du projet (Laravel 12).

   ## Livrables attendus
   - Dépôt GitHub distant créé et synchronisé sur la branche de sprint active.
   - Fichier `README.md` racine propre et conforme au standard Solicode.

   ## Protocole d'audit et exécution
   - **Si l'apprenant précise une tâche** : Exécuter directement la tâche demandée sans créer d'artefact plan.
   - **Si aucune tâche n'est précisée** : Auditer l'état des livrables (Git local, publication GitHub, contenu du `README.md`) et proposer les actions à réaliser dans un artefact plan pour validation de l'apprenant.

   ## Structure du livrable (README.md)
   - `# [Nom du Projet]`
   - `## 1. Description du projet` (résumé en 2-3 phrases, utilisateurs cibles, déploiement)
   - `## 2. Contexte et Objectifs` (contexte Solicode Tanger, formateur, objectifs techniques et pédagogiques)
   - `## 3. Stack technique` (framework backend Laravel 12, frontend, base de données, Git)
   - `## 4. Organisation des dossiers` (rôle des dossiers : `.agents/`, `docs/`, `flux-travail/`, `issues/`, `labs/`, `sprints/`)
   - `## 5. Méthodologie` (Agile/Scrum, 2TUP, Design Thinking, modélisation UML)
   - `## 6. Démarrage rapide` (prérequis, cloner, lancer)
   ```

2. **Étape 2 — Création du skill outillé `.agents/skills/gestion-depot/SKILL.md` :**  
   Dans votre projet, créez l'arborescence `.agents/skills/gestion-depot/doc/` et rédigez le fichier `SKILL.md` :

   ```markdown
   ---
   name: gestion-depot
   description: Audite l'initialisation Git locale, gère la publication sur GitHub via GitHub CLI (gh) et vérifie la conformité de la structure du README.md racine.
   version: 1.0.0
   ---

   # 1. Mission
   Ce skill outille l'Agent IA pour piloter la mise en place initiale du dépôt de projet et garantir la conformité des livrables de démarrage.

   # 2. Déclenchement & Protocole
   - **Déclenchement :** Exécution de la mission `init-projet` ou demande directe sur Git/GitHub.
   - **Protocole d'exécution :**
     - Si l'apprenant précise une tâche (ex: "publie sur GitHub") : Exécuter directement via `gh repo create` sans créer de plan.
     - Si aucune tâche n'est précisée : Auditer Git, GitHub CLI et `README.md`, puis proposer un plan d'action.

   # 3. Actions Outillées
   - **Initialisation Git :** Exécuter `git init`, configurer `.gitignore`, créer la branche de sprint active (`sprint1`).
   - **Publication GitHub :** Vérifier `gh auth status` et exécuter `gh repo create [nom] --public --source=. --remote=origin --push`.
   - **Contrôle du README :** Vérifier la présence des 6 sections canoniques (Description, Contexte, Stack Laravel 12, Dossiers, Méthodologie, Démarrage).
   ```

3. **Étape 3 — Rédaction du guide d'utilisation `.agents/skills/gestion-depot/doc/how-to-use.md` :**  
   Créez le guide opérationnel du skill :

   ```markdown
   # Guide Opérationnel : Comment Utiliser le Skill `gestion-depot`

   ## 1. Rôle du Skill
   Le skill `gestion-depot` permet à l'Agent IA de vérifier l'état du dépôt Git, d'automatiser sa publication avec GitHub CLI et de contrôler la structure du `README.md`.

   ## 2. Prompts Types
   - *"Vérifie l'état de mon dépôt Git et publie-le sur GitHub."*
   - *"Audite le fichier README.md pour vérifier s'il respecte le standard Solicode N3."*
   - *"Exécute la tâche 2 de la mission init-projet."*
   ```

4. **Étape 4 — Commit et synchronisation sur `sprint1` :**  
   ```bash
   git add missions/1.init-projet.mission.md .agents/skills/gestion-depot/
   git commit -m "feat(ia): ajouter la mission init-projet et le skill gestion-depot"
   git push origin sprint1
   ```

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Mission d'étape (mode chatbot) : `missions/1.init-projet.mission.md`.
  - Skill outillé (mode agent) : `.agents/skills/gestion-depot/SKILL.md`.
  - Guide du skill : `.agents/skills/gestion-depot/doc/how-to-use.md`.
- **Critères de validation :**
  - [ ] La mission `missions/1.init-projet.mission.md` explicite les 3 tâches, le protocole d'audit et la structure attendue du `README.md`.
  - [ ] Le skill `gestion-depot` est créé dans `.agents/skills/gestion-depot/` avec son dossier `doc/`.
  - [ ] L'ensemble est versionné et synchronisé sur la branche `sprint1`.
