---
layout: tuto
title: "Cadrage du pÃ©rimÃ¨tre du projet (Sprint 1)"
sous_titre: "DÃ©finir la vision, identifier les acteurs, dÃ©limiter le pÃ©rimÃ¨tre In/Out du Sprint 1 et contractualiser la feuille de route"
slug: "perimetre-produit"
slug_domaine: "realisation-projet"
slug_ua: "cadrage"
permalink: /tutos/perimetre-produit/
tuto_id: "T.351.231"
version: "normal"
ua: "UA.351.23"
maturite: "projet"
type: "tuto-tache"
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

## 1. Objectif OpÃ©rationnel & PrÃ©requis
- **Position dans le flux :** Phase A â€” Outillage IA, Gouvernance & Cadrage / Ã‰tape 4 â€” Cadrage du pÃ©rimÃ¨tre du projet (*Blog des LaurÃ©ats*).
- **Branche Git :** `sprint1`
- **Fichiers modifiÃ©s ou crÃ©Ã©s :** `sprints/sprints.md`, `sprints/README.md`.
- **Objectif :** Poser le cadre fonctionnel du projet d'imitation (*Blog des LaurÃ©ats*) : formaliser la vision produit et les deux acteurs cibles, dÃ©limiter ce qui est strictement inclus (In-Scope) et exclu (Out-of-Scope) du premier sprint, et contractualiser la gouvernance dans `sprints/sprints.md` sur la branche `sprint1`.
- **PrÃ©requis :** Initiation Ã  la mÃ©thode Agile Scrum (`UA.351.11`) et initialisation du projet (`UA.351.20`).

## 2. DÃ©roulement Pas-Ã -Pas de la TÃ¢che

1. **Ã‰tape 1 â€” DÃ©finition de la Vision Produit & des Personas du Blog des LaurÃ©ats :**  
   Avant de modÃ©liser les diagrammes UML ou de crÃ©er les tÃ¢ches de dÃ©veloppement, vous devez poser les fondations fonctionnelles du projet d'imitation :
   - **Vision du produit :** Le *Blog des LaurÃ©ats* est une vitrine web conÃ§ue pour valoriser publiquement les rÃ©alisations et profils techniques des laurÃ©ats de Solicode auprÃ¨s des recruteurs et des apprenants.
   - **Acteur primaire (Consommateur en S1) :** *L'Apprenant ou le Visiteur/Recruteur*, qui souhaite consulter le catalogue des rÃ©alisations et lire en dÃ©tail chaque article publiÃ©.
   - **Acteur secondaire (Contributeur) :** *Le LaurÃ©at*, qui soumettra et administrera ses articles dans un sprint ultÃ©rieur.

2. **Ã‰tape 2 â€” DÃ©limitation In-Scope vs Out-of-Scope du Sprint 1 :**  
   Pour garantir la livraison d'un incrÃ©ment fonctionnel et testable au bout des 80 heures sans dispersion :
   - **In-Scope (Strictement inclus dans le Sprint 1) :**
     - Consultation publique de la fiche dÃ©taillÃ©e d'un article de blog via sa route dynamique `/articles/{id}`.
     - Architecture logicielle dÃ©couplÃ©e en deux couches : ContrÃ´leur mince HTTP $\to$ Classe Service.
     - Stockage tabulaire transitoire en mÃ©moire Ã  partir d'un fichier CSV (`articles.csv`).
     - Rendu responsive sous gabarit Blade avec layout maÃ®tre et composants d'interface.
     - Gestion rÃ©siliente de l'erreur HTTP 404 en cas d'identifiant d'article inexistant.
   - **Out-of-Scope (Strictement exclu du Sprint 1) :**
     - ZÃ©ro module d'authentification ou de connexion utilisateur.
     - ZÃ©ro formulaire de rÃ©daction, modification ou suppression d'article.
     - ZÃ©ro base de donnÃ©es relationnelle MySQL (reportÃ©e aux sprints ultÃ©rieurs).

3. **Ã‰tape 3 â€” Initialisation du dossier `sprints/` et du guide `sprints/README.md` :**  
   CrÃ©ez le dossier racine `sprints/` pour accueillir la gouvernance du projet :

```bash
mkdir sprints
```

   RÃ©digez le guide mÃ©thodologique `sprints/README.md` dÃ©finissant les rÃ¨gles de fonctionnement pour l'Ã©quipe et l'Agent IA :

```markdown
# Dossier des Sprints (`sprints/`)

Ce dossier centralise la planification et le suivi des Sprints selon la mÃ©thodologie Agile/Scrum.

---

## 1. RÃ´le du dossier

- Il contient le calendrier et les objectifs de chaque sprint du projet.
- Il sert de source de vÃ©ritÃ© unique (SSOT) pour identifier le sprint actif et sa branche Git associÃ©e.
- L'Agent IA consulte ce dossier pour vÃ©rifier sur quelle branche de travail il doit opÃ©rer.

---

## 2. RÃ¨gle de gouvernance des Sprints

- Seul le concepteur (ou chef de projet) ajoute de nouveaux sprints dans la planification.
- L'Agent IA ne doit jamais inventer de futurs sprints non validÃ©s.
- Chaque sprint actif doit possÃ©der sa branche Git dÃ©diÃ©e au format `sprint[N]`.

---

## 3. Contenu du dossier

- [sprints.md](./sprints.md) : Fichier de suivi de la planification des sprints.
```

4. **Ã‰tape 4 â€” Formalisation de la feuille de route dans `sprints/sprints.md` :**  
   CrÃ©ez le document central de suivi `sprints/sprints.md` en dÃ©clarant le Sprint 1 en statut Actif :

```markdown
# Planification des Sprints

Ce document enregistre les sprints du projet. Les sprints suivants seront ajoutÃ©s ultÃ©rieurement, aprÃ¨s chaque session de planification. Pour le moment, seul le Sprint 1 est actif avec la description dÃ©taillÃ©e du sprint actuel ci-dessous.

---

## Sprint 1 : Initialisation, Cadrage & PremiÃ¨re FonctionnalitÃ© Laravel
- **Statut** : Actif
- **Branche Git** : `sprint1`
- **Vision du produit** : Le *Blog des LaurÃ©ats* est une vitrine web conÃ§ue pour valoriser publiquement les rÃ©alisations et profils techniques des laurÃ©ats de Solicode auprÃ¨s des recruteurs et des apprenants.
- **Acteurs cibles** :
  - *Acteur primaire (Consommateur en S1)* : L'Apprenant ou le Visiteur/Recruteur, qui souhaite consulter le catalogue des rÃ©alisations et lire en dÃ©tail chaque article publiÃ©.
  - *Acteur secondaire (Contributeur)* : Le LaurÃ©at, qui soumettra et administrera ses articles dans un sprint ultÃ©rieur.
- **PÃ©rimÃ¨tre du Sprint 1** :
  - *In-Scope (Strictement inclus dans le Sprint 1)* :
    - Consultation publique de la fiche dÃ©taillÃ©e d'un article de blog via sa route dynamique `/articles/{id}`.
    - Architecture logicielle dÃ©couplÃ©e en deux couches : ContrÃ´leur mince HTTP -> Classe Service.
    - Stockage tabulaire transitoire en mÃ©moire Ã  partir d'un fichier CSV (`articles.csv`).
    - Rendu responsive sous gabarit Blade avec layout maÃ®tre et composants d'interface.
    - Gestion rÃ©siliente de l'erreur HTTP 404 en cas d'identifiant d'article inexistant.
  - *Out-of-Scope (Strictement exclu du Sprint 1)* :
    - ZÃ©ro module d'authentification ou de connexion utilisateur.
    - ZÃ©ro formulaire de rÃ©daction, modification ou suppression d'article.
    - ZÃ©ro base de donnÃ©es relationnelle MySQL (reportÃ©e aux sprints ultÃ©rieurs).
- **Objectif pÃ©dagogique** : Au terme de la session, l'apprenant est capable d'initialiser un dÃ©pÃ´t distant avec GitHub CLI, d'outiller l'environnement avec un Agent IA et un catalogue de missions, de formaliser le processus de dÃ©veloppement et le flux de travail, de cadrer le projet sous gouvernance Scrum, de modÃ©liser le diagramme de contexte et les cas d'utilisation avec Mermaid, de gÃ©rer les tÃ¢ches via le dossier `issues/`, et de dÃ©velopper sous Laravel une page de consultation dÃ©taillÃ©e d'un article selon une architecture 2 couches (ContrÃ´leur mince -> Classe Service) avec gabarit Blade responsive et gestion de l'erreur 404.
- **DÃ©roulement (Vue d'ensemble du travail de la session)** :
  - Initialiser le projet et publier sur GitHub.
  - Outiller l'environnement avec un Agent IA et son catalogue de missions.
  - Formaliser le flux de travail d'ingÃ©nierie.
  - Cadrer le pÃ©rimÃ¨tre sous gouvernance Scrum.
  - ModÃ©liser le contexte et les cas d'utilisation avec Mermaid.
  - Structurer le Product Backlog et les issues dans `issues/`.
  - Concevoir l'architecture en 2 couches (ContrÃ´leur mince -> Classe Service).
  - ImplÃ©menter la consultation d'un article sous Laravel (gabarit Blade responsive et gestion 404).
```

5. **Ã‰tape 5 â€” Journalisation des commandes exÃ©cutÃ©es :**  
   Dans le fichier `tutoriels/realisation-projet/cadrage/perimetre-produit/perimetre-produit.command.md`, consignez la commande de crÃ©ation du dossier :

```bash
mkdir sprints
```

## 3. Livrables & CritÃ¨res de RÃ©ussite
- **Livrables attendus :**
  - Guide mÃ©thodologique : `sprints/README.md`.
  - Fichier de cadrage Scrum : `sprints/sprints.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/realisation-projet/cadrage/perimetre-produit/perimetre-produit.command.md`.
- **CritÃ¨res de validation :**
  - [ ] La vision produit et les deux acteurs cibles (*LaurÃ©at* et *Apprenant/Visiteur*) sont clairement identifiÃ©s.
  - [ ] Les frontiÃ¨res In-Scope et Out-of-Scope du Sprint 1 sont clairement distinguÃ©es.
  - [ ] Le fichier `sprints/README.md` explicite le rÃ´le de source de vÃ©ritÃ© unique (SSOT) pour l'Agent IA et l'Ã©quipe.
  - [ ] Le document `sprints/sprints.md` dÃ©clare le Sprint 1 en statut Actif sur la branche `sprint1`.
  - [ ] Le journal `perimetre-produit.command.md` consigne la commande `mkdir sprints`.
