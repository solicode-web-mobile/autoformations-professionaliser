---
layout: tuto
title: "Cadrage du projet sous gouvernance Scrum"
sous_titre: "Formaliser la planification des sprints dans sprints/sprints.md et activer le Sprint 1 pour le Blog des Lauréats"
slug: "perimetre-produit"
slug_domaine: "realisation-projet"
slug_ua: "cadrage"
permalink: /tutos/perimetre-produit/
tuto_id: "T.351.211"
version: "normal"
ua: "UA.351.21"
maturite: "UA-Tâche"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 4 — Cadrage du projet sous gouvernance Scrum.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `sprints/sprints.md`, `sprints/README.md`.
- **Objectif :** Contractualiser la gouvernance agile du projet d'imitation (*Blog des Lauréats*) en formalisant la planification dans `sprints/sprints.md`, en activant le Sprint 1 sur sa branche de travail dédiée et en rédigeant le guide méthodologique du dossier.
- **Prérequis :** Initiation à la méthode Agile Scrum (`UA.351.11`) et initialisation du projet (`UA.351.20`).

## 2. Déroulement Pas-à-Pas de la Tâche

1. **Étape 1 — Création du dossier et du guide méthodologique `sprints/README.md` :**  
   Initialisez le dossier racine `sprints/` et créez le fichier de guide méthodologique :

```bash
mkdir -p sprints
```

Rédigez le fichier `sprints/README.md` :

```markdown
# Dossier des Sprints (`sprints/`)

Ce dossier centralise la planification et le suivi des Sprints selon la méthodologie Agile/Scrum.

---

## 1. Rôle du dossier

- Il contient le calendrier et les objectifs de chaque sprint du projet.
- Il sert de source de vérité unique (SSOT) pour identifier le sprint actif et sa branche Git associée.
- L'Agent IA consulte ce dossier pour vérifier sur quelle branche de travail il doit opérer.

---

## 2. Règle de gouvernance des Sprints

- Seul le concepteur (ou chef de projet) ajoute de nouveaux sprints dans la planification.
- L'Agent IA ne doit jamais inventer de futurs sprints non validés.
- Chaque sprint actif doit posséder sa branche Git dédiée au format `sprint[N]`.

---

## 3. Contenu du dossier

- [sprints.md](./sprints.md) : Fichier de suivi de la planification des sprints.
```

2. **Étape 2 — Formalisation du fichier de cadrage `sprints/sprints.md` :**  
   Créez le document central de suivi `sprints/sprints.md` en déclarant le premier sprint actif :

```markdown
# Planification des Sprints

Ce document enregistre les sprints du projet. Les sprints suivants seront ajoutés ultérieurement, après chaque session de planification. Pour le moment, seul le Sprint 1 est actif avec la description détaillée du sprint actuel ci-dessous.

---

## Sprint 1 : Initialisation, Cadrage & Première Fonctionnalité Laravel 12
- **Statut** : Actif
- **Branche Git** : `sprint1`
- **Objectif pédagogique** : Au terme de la session, l'apprenant est capable d'initialiser un dépôt distant avec GitHub CLI, d'outiller l'environnement avec un Agent IA et un catalogue de missions, de formaliser le processus de développement et le flux de travail, de cadrer le projet sous gouvernance Scrum, de modéliser le diagramme de contexte et les cas d'utilisation avec Mermaid, de gérer les tâches via le dossier `issues/`, et de développer sous Laravel 12 une page de consultation détaillée d'un article selon une architecture 2 couches (Contrôleur mince -> Classe Service) avec gabarit Blade responsive et gestion de l'erreur 404.
- **Déroulement (Vue d'ensemble du travail de la session)** :
  - Initialiser le projet et publier sur GitHub.
  - Outiller l'environnement avec un Agent IA et son catalogue de missions.
  - Formaliser le flux de travail d'ingénierie.
  - Cadrer le périmètre sous gouvernance Scrum.
  - Modéliser le contexte et les cas d'utilisation avec Mermaid.
  - Structurer le Product Backlog et les issues dans `issues/`.
  - Concevoir l'architecture en 2 couches (Contrôleur mince -> Classe Service).
  - Implémenter la consultation d'un article sous Laravel 12 (gabarit Blade responsive et gestion 404).
```

3. **Étape 3 — Journalisation des commandes exécutées :**  
   Dans le fichier `tutoriels/realisation-projet/cadrage/perimetre-produit/perimetre-produit.command.md`, consignez la commande exécutée :

```bash
mkdir -p sprints
```

## 3. Livrables & Critères de Réussite
- **Livrables attendus :**
  - Guide méthodologique : `sprints/README.md`.
  - Fichier de cadrage Scrum : `sprints/sprints.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/realisation-projet/cadrage/perimetre-produit/perimetre-produit.command.md`.
- **Critères de validation :**
  - [ ] Le fichier `sprints/README.md` explicite le rôle de source de vérité unique (SSOT) pour l'Agent IA et l'équipe.
  - [ ] Le document `sprints/sprints.md` déclare le Sprint 1 en statut Actif sur la branche `sprint1`.
  - [ ] Les objectifs pédagogiques et les 8 étapes clés du Sprint 1 y sont explicitement répertoriés.
  - [ ] Le journal `perimetre-produit.command.md` consigne fidèlement les commandes exécutées.
