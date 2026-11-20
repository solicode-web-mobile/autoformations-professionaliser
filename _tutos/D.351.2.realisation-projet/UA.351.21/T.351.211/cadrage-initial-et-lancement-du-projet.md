---
layout: tuto
title: "Cadrage du périmètre du projet (Sprint 1)"
sous_titre: "Définir la vision, identifier les acteurs, délimiter le périmètre In/Out du Sprint 1 et contractualiser la feuille de route"
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
sprint: "sprint1"
statut_realisation: "realise"
livrables:
  - chemin: "tutoriels/realisation-projet/cadrage/perimetre-produit/perimetre-produit.command.md"
    version: "1.0.0"
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 4 — Cadrage du périmètre du projet (*Blog des Lauréats*).
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `sprints/sprints.md`, `sprints/README.md`.
- **Objectif :** Poser le cadre fonctionnel du projet d'imitation (*Blog des Lauréats*) : formaliser la vision produit et les deux acteurs cibles, délimiter ce qui est strictement inclus (In-Scope) et exclu (Out-of-Scope) du premier sprint, et contractualiser la gouvernance dans `sprints/sprints.md` sur la branche `sprint1`.
- **Prérequis :** Initiation à la méthode Agile Scrum (`UA.351.11`) et initialisation du projet (`UA.351.20`).

## 2. Déroulement Pas-à-Pas de la Tâche

1. **Étape 1 — Définition de la Vision Produit & des Personas du Blog des Lauréats :**  
   Avant de modéliser les diagrammes UML ou de créer les tâches de développement, vous devez poser les fondations fonctionnelles du projet d'imitation :
   - **Vision du produit :** Le *Blog des Lauréats* est une vitrine web conçue pour valoriser publiquement les réalisations et profils techniques des lauréats de Solicode auprès des recruteurs et des apprenants.
   - **Acteur primaire (Consommateur en S1) :** *L'Apprenant ou le Visiteur/Recruteur*, qui souhaite consulter le catalogue des réalisations et lire en détail chaque article publié.
   - **Acteur secondaire (Contributeur) :** *Le Lauréat*, qui soumettra et administrera ses articles dans un sprint ultérieur.

2. **Étape 2 — Délimitation In-Scope vs Out-of-Scope du Sprint 1 :**  
   Pour garantir la livraison d'un incrément fonctionnel et testable au bout des 80 heures sans dispersion :
   - **In-Scope (Strictement inclus dans le Sprint 1) :**
     - Consultation publique de la fiche détaillée d'un article de blog via sa route dynamique `/articles/{id}`.
     - Architecture logicielle découplée en deux couches : Contrôleur mince HTTP $\to$ Classe Service.
     - Stockage tabulaire transitoire en mémoire à partir d'un fichier CSV (`articles.csv`).
     - Rendu responsive sous gabarit Blade avec layout maître et composants d'interface.
     - Gestion résiliente de l'erreur HTTP 404 en cas d'identifiant d'article inexistant.
   - **Out-of-Scope (Strictement exclu du Sprint 1) :**
     - Zéro module d'authentification ou de connexion utilisateur.
     - Zéro formulaire de rédaction, modification ou suppression d'article.
     - Zéro base de données relationnelle MySQL (reportée aux sprints ultérieurs).

3. **Étape 3 — Initialisation du dossier `sprints/` et du guide `sprints/README.md` :**  
   Créez le dossier racine `sprints/` pour accueillir la gouvernance du projet :

```bash
mkdir sprints
```

   Rédigez le guide méthodologique `sprints/README.md` définissant les règles de fonctionnement pour l'équipe et l'Agent IA :

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

4. **Étape 4 — Formalisation de la feuille de route dans `sprints/sprints.md` :**  
   Créez le document central de suivi `sprints/sprints.md` en déclarant le Sprint 1 en statut Actif :

```markdown
# Planification des Sprints

Ce document enregistre les sprints du projet. Les sprints suivants seront ajoutés ultérieurement, après chaque session de planification. Pour le moment, seul le Sprint 1 est actif avec la description détaillée du sprint actuel ci-dessous.

---

## Sprint 1 : Initialisation, Cadrage & Première Fonctionnalité Laravel
- **Statut** : Actif
- **Branche Git** : `sprint1`
- **Vision du produit** : Le *Blog des Lauréats* est une vitrine web conçue pour valoriser publiquement les réalisations et profils techniques des lauréats de Solicode auprès des recruteurs et des apprenants.
- **Acteurs cibles** :
  - *Acteur primaire (Consommateur en S1)* : L'Apprenant ou le Visiteur/Recruteur, qui souhaite consulter le catalogue des réalisations et lire en détail chaque article publié.
  - *Acteur secondaire (Contributeur)* : Le Lauréat, qui soumettra et administrera ses articles dans un sprint ultérieur.
- **Périmètre du Sprint 1** :
  - *In-Scope (Strictement inclus dans le Sprint 1)* :
    - Consultation publique de la fiche détaillée d'un article de blog via sa route dynamique `/articles/{id}`.
    - Architecture logicielle découplée en deux couches : Contrôleur mince HTTP -> Classe Service.
    - Stockage tabulaire transitoire en mémoire à partir d'un fichier CSV (`articles.csv`).
    - Rendu responsive sous gabarit Blade avec layout maître et composants d'interface.
    - Gestion résiliente de l'erreur HTTP 404 en cas d'identifiant d'article inexistant.
  - *Out-of-Scope (Strictement exclu du Sprint 1)* :
    - Zéro module d'authentification ou de connexion utilisateur.
    - Zéro formulaire de rédaction, modification ou suppression d'article.
    - Zéro base de données relationnelle MySQL (reportée aux sprints ultérieurs).
- **Objectif pédagogique** : Au terme de la session, l'apprenant est capable d'initialiser un dépôt distant avec GitHub CLI, d'outiller l'environnement avec un Agent IA et un catalogue de missions, de formaliser le processus de développement et le flux de travail, de cadrer le projet sous gouvernance Scrum, de modéliser le diagramme de contexte et les cas d'utilisation avec Mermaid, de gérer les tâches via le dossier `issues/`, et de développer sous Laravel une page de consultation détaillée d'un article selon une architecture 2 couches (Contrôleur mince -> Classe Service) avec gabarit Blade responsive et gestion de l'erreur 404.
- **Déroulement (Vue d'ensemble du travail de la session)** :
  - Initialiser le projet et publier sur GitHub.
  - Outiller l'environnement avec un Agent IA et son catalogue de missions.
  - Formaliser le flux de travail d'ingénierie.
  - Cadrer le périmètre sous gouvernance Scrum.
  - Modéliser le contexte et les cas d'utilisation avec Mermaid.
  - Structurer le Product Backlog et les issues dans `issues/`.
  - Concevoir l'architecture en 2 couches (Contrôleur mince -> Classe Service).
  - Implémenter la consultation d'un article sous Laravel (gabarit Blade responsive et gestion 404).
```

5. **Étape 5 — Journalisation des commandes exécutées :**  
   Dans le fichier `tutoriels/realisation-projet/cadrage/perimetre-produit/perimetre-produit.command.md`, consignez la commande de création du dossier :

```bash
mkdir sprints
```

## 3. Livrables & Critères de Réussite
- **Livrables attendus :**
  - Guide méthodologique : `sprints/README.md`.
  - Fichier de cadrage Scrum : `sprints/sprints.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/realisation-projet/cadrage/perimetre-produit/perimetre-produit.command.md`.
- **Critères de validation :**
  - [ ] La vision produit et les deux acteurs cibles (*Lauréat* et *Apprenant/Visiteur*) sont clairement identifiés.
  - [ ] Les frontières In-Scope et Out-of-Scope du Sprint 1 sont clairement distinguées.
  - [ ] Le fichier `sprints/README.md` explicite le rôle de source de vérité unique (SSOT) pour l'Agent IA et l'équipe.
  - [ ] Le document `sprints/sprints.md` déclare le Sprint 1 en statut Actif sur la branche `sprint1`.
  - [ ] Le journal `perimetre-produit.command.md` consigne la commande `mkdir sprints`.
