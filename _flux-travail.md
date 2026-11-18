# Flux de travail du projet

Ce document formalise les étapes de réalisation du Projet d'imitation Niveau 3. Il sert de référentiel méthodologique pour guider l'apprenant et l'Agent IA dans la production des livrables.

Les projets suivent les démarches d'ingénierie logicielle : 2TUP, Design Thinking, modélisation UML et méthodologie Agile/Scrum.

---

<!-- Sprint 1 -->

## 1. Création et initialisation du projet

### Base théorique et pratique
- `lab-github` : Installation et utilisation de GitHub CLI (`gh repo create`).
- `lab-git-branches` : Création et gestion des branches Git.

### Prérequis
- Présentation du projet d'imitation par le formateur.
- Notions de base sur Git et GitHub.

### Travail à faire
- **Tâche 1 : Initialisation locale** : Créer le projet, initialiser Git (`git init`) et réaliser le premier commit.
- **Tâche 2 : Publication sur GitHub** : Publier le dépôt via GitHub CLI avec la commande : `gh repo create`.
- **Tâche 3 : Rédaction du README.md** : Nettoyer et structurer le fichier `README.md` racine selon le template standard.

### Livrables
- Dépôt GitHub distant publié et accessible.
- Fichier `README.md` propre et conforme.
- Mission d'étape : `missions/1.init-projet.mission.md`.

---

## 2. Initialisation de l'Agent IA

### Base théorique et pratique
- `lab-prompt-engineering` : Formulation de consignes, rôles et règles IA.
- `lab-agent-ia` : Architecture d'un agent outillé (règles et skills).

### Prérequis
- Dépôt Git initialisé et publié sur GitHub (Étape 1).

### Travail à faire
- Définir le socle commun des règles et contexte du projet : `missions/init-ia.mission.md`.
- Définir le protocole de fonctionnement de l'Agent IA : `missions/init-agent.mission.md`.
- Créer la mission de génération de missions : `missions/missions-creator.mission.md`.
- Mettre en place le catalogue des missions : `missions/missions-index.yml`.
- Rédiger le guide d'utilisation du dossier : `missions/README.md`.

### Livrables
- `missions/init-ia.mission.md`
- `missions/init-agent.mission.md`
- `missions/missions-creator.mission.md`
- `missions/missions-index.yml`
- `missions/README.md`

---

## 3. Documentation du Flux de Travail

### Base théorique et pratique
- `lab-flux-travail` : Démarche 2TUP, ingénierie logicielle et formalisation des étapes.

### Prérequis
- Initialisation de l'Agent IA terminée (Étape 2).

### Travail à faire
- Initialiser le document de suivi du flux de travail : `flux-travail/flux-travail.md`.
- Formaliser la structure standardisée des étapes (`Base théorique et pratique`, `Prérequis`, `Travail à faire`, `Livrables`).
- Créer la mission de gestion du flux : `missions/flux-travail.mission.md`.
- Rédiger le guide du dossier : `flux-travail/README.md`.

### Livrables
- Fichier `flux-travail/flux-travail.md`.
- Mission d'étape : `missions/flux-travail.mission.md`.
- Guide pédagogique : `flux-travail/README.md`.

---

## 4. Création et Planification des issues

### Base théorique et pratique
- `lab-scrum-planning` : Méthodologie Agile/Scrum, découpage en user stories et planification de sprint.

### Prérequis
- Documentation du flux de travail initialisée (Étape 3).

### Travail à faire
- Créer l'espace de suivi des tâches du projet : dossier `issues/`.
- Recenser les tâches hors LMS ou demandées par le chef de projet.
- Organiser les issues par statut (`open`, `à-valider`, `closes`).
- Soumettre les issues à la validation du formateur avant dépôt sur GitHub.

### Livrables
- Guide pédagogique : `issues/README.md`.
- Fichiers de suivi des tâches : `issues/issues-open.md`, `issues/issues-à-valider.md`, `issues/issues-closes.md`.
