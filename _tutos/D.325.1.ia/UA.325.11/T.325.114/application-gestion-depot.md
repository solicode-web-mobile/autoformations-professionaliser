---
layout: tuto
title: "Application : Outiller l'étape d'initialisation avec le skill gestion-depot"
sous_titre: "Déployer les règles Always-On et concevoir le skill gestion-depot avec ses missions d'initialisation sur le projet d'imitation"
slug: "skill-gestion-depot"
slug_domaine: "ia"
slug_ua: "agent-skills"
permalink: /tutos/skill-gestion-depot/
tuto_id: "T.325.114"
version: "normal"
ua: "UA.325.11"
maturite: "UA-Tâche"
nav_order: 4
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
  - Prompt Engineering directif et méthode RIO (`T.325.111`).
  - Architecture d'un Agent IA, règles Always-On et découvrabilité des skills (`T.325.112`).
  - Pratique de conception d'un skill outillé (`T.325.113`).
  - Connaissance des livrables de l'Étape 1 (dépôt Git, README racine, rapport Node.js, présentations Marp).
- **Prérequis de projet :** Dépôt Git initialisé et publié sur la branche `sprint1` (`UA.351.20`).
- **Branche Git :** `sprint1`

## 2. Travail à Faire
- **Tâche 1 : Règles permanentes Always-On :** Créer le socle des règles projet dans `.agents/rules/` (`contexte-projet.md` et `regles-generales.md`).
- **Tâche 2 : Skill de méta-gouvernance :** Mettre en place `.agents/skills/skills-dev/SKILL.md`.
- **Tâche 3 : Skill opérationnel gestion-depot :** Concevoir `.agents/skills/gestion-depot/SKILL.md` et ses deux missions spécialisées (`missions/init-depot.md` et `missions/init-projet.md`).
- **Tâche 4 : Journalisation des commandes :** Consigner les commandes exécutées dans `tutoriels/ia/agent-skills/skill-gestion-depot/skill-gestion-depot.command.md`.

## 3. Étapes de Réalisation

1. **Étape 1 — Création de l'arborescence agentique du projet :**  
   À la racine du projet `blog-des-laureats`, créez les répertoires dédiés aux règles et aux skills :

```bash
mkdir -p .agents/rules .agents/skills/skills-dev .agents/skills/gestion-depot/missions
```

2. **Étape 2 — Définition du contexte projet Always-On `.agents/rules/contexte-projet.md` :**  
   Créez le fichier `.agents/rules/contexte-projet.md` pour cadrer l'environnement de l'Agent IA :

````markdown
# Contexte du Projet

Ce document définit le cadre spécifique du projet pour l'Agent IA.

---

## 1. Identité du projet

- **Nom du projet** : Projet d'imitation - Niveau 3
- **Établissement** : Solicode Tanger
- **Formateur référent** : ESSARRAJ Fouad

---

## 2. Application à réaliser

- **Nom de l'application** : Blog des lauréats
- **Utilisateurs cibles** :
  - Les lauréats : ajout, modification et publication d'articles.
  - Les apprenants de Solicode : consultation et lecture des articles.
- **Déploiement** : L'application sera accessible en ligne sur Internet.

---

## 3. Stack technique et Architecture de l'application

- **Framework Backend** : Laravel 12 (PHP).
- **Architecture logicielle** : Architecture en 2 couches (Contrôleur mince -> Classe Service).
- **Frontend & Vues** : Gabarits Blade responsives, HTML5, CSS3, JavaScript.
- **Gestion des erreurs** : Traitement explicite de l'erreur 404 (ressources introuvables).
- **Base de données** : MySQL.
- **Gestion de versions & Outils** : Git, GitHub CLI (`gh`).
- **Intelligence Artificielle & Automatisation** : Agent Antigravity.

---

## 4. Démarche d'ingénierie logicielle

L'apprenant et l'Agent IA appliquent les méthodes suivantes :
- **Méthode par imitation** : Progression par étapes avec tutoriels, labs guidés et veilles technologiques.
- **Processus de développement** : 2TUP et Design Thinking.
- **Modélisation** : Diagramme de contexte et cas d'utilisation modélisés en diagrammes Mermaid.
- **Gestion de projet** : Méthodologie Agile/Scrum (sprints, Product Backlog, dossier `issues/`).
````

3. **Étape 3 — Définition des règles générales Always-On `.agents/rules/regles-generales.md` :**  
   Créez le fichier `.agents/rules/regles-generales.md` :

````markdown
# Règles Générales de Rédaction et de Structure

Ces règles s'appliquent de manière générique à tous les fichiers et toutes les interactions de l'Agent IA.

---

## 1. Rédaction et langue

- **Niveau de français A1** :
  - Rédiger des phrases courtes, directes et simples (Sujet + Verbe + Complément).
  - Éviter les phrases longues, passives ou complexes.
- **Vocabulaire technique professionnel** :
  - Conserver les vrais termes techniques des développeurs professionnels.
  - Ne pas remplacer un mot technique précis par un terme vague.

---

## 2. Formatage Markdown

- **Format sans tableau (Facilité d'édition par l'apprenant)** :
  - Interdiction formelle d'utiliser des tableaux Markdown (`| ... | ... |`).
  - Utiliser exclusivement des listes à puces (`- `) à la place des tableaux.

---

## 3. Liens relatifs obligatoires

- **Interdiction formelle des liens absolus** :
  - Ne jamais écrire de chemins locaux (`C:\...`, `D:\...`) ou de liens de type `file:///...`.
  - Toujours utiliser des **liens relatifs** (exemples : `./fichier.md`, `../dossier/fichier.md`).

---

## 4. Structure du dépôt

- **Un fichier `README.md` par dossier** :
  - Tout dossier et sous-dossier du dépôt doit obligatoirement contenir un fichier `README.md`.
  - Ce `README.md` doit expliquer clairement le rôle du dossier et son utilisation.

---

## 5. Gestion des Sprints et branches Git

- **Interdiction formelle de commit et push par l'Agent IA** :
  - L'Agent IA ne doit jamais exécuter les commandes `git commit` ou `git push`.
  - Seul le concepteur (l'apprenant) réalise les commits et les pushs sur le dépôt.
- **Interdiction de travailler directement sur `main`** :
  - Tout travail de développement s'effectue sur la branche active du sprint (`sprint[N]`).
````

4. **Étape 4 — Mise en place du skill méta-gouvernance `.agents/skills/skills-dev/SKILL.md` :**  
   Créez le fichier `.agents/skills/skills-dev/SKILL.md` :

````markdown
---
name: skills-dev
description: >-
  Gouverne, conçoit, crée et raffine les skills, missions et règles du workspace.
  En appel sans consigne, audite les remarques du concepteur non supportées par défaut
  et propose un plan d'évolution sous forme d'artefact.
---

# Skill Méta-Gouvernance : /skills-dev

## 1. Mission
Gouverner, concevoir, créer et auditer les **Skills** (`.agents/skills/`), leurs **Missions** (`<skill>/missions/<nom>.md`) et les **Règles permanentes** (`.agents/rules/`).

## 2. Déclenchement
- **Quand l'activer** :
  - Audit réflexif des remarques du concepteur (sans argument).
  - Création, mise à jour ou refactorisation d'un skill ou d'une mission.
  - Arbitrage entre règle transverse (`.agents/rules/`) et compétence ciblée (`.agents/skills/`).
- **Quand NE PAS l'activer** :
  - Exécution directe d'une tâche de développement applicatif (utiliser le skill métier dédié).
````

5. **Étape 5 — Conception du skill `.agents/skills/gestion-depot/SKILL.md` :**  
   Créez le fichier `.agents/skills/gestion-depot/SKILL.md` :

````markdown
---
name: gestion-depot
description: >-
  Gère les opérations sur le dépôt Git/GitHub et le cycle de vie du projet.
  Sélectionne et exécute la mission appropriée dans son dossier missions/.
---

# Skill Gestion de Dépôt : /gestion-depot

## 1. Mission
Gérer les opérations sur le dépôt Git/GitHub (initialisation locale, gestion des branches de sprint, synchronisation distante et documentation racine).

## 2. Déclenchement
- **Quand l'activer** :
  - Le concepteur demande un travail sur le dépôt (initialiser Git, publier sur GitHub, changer de branche, mettre à jour le README racine, créer l'arborescence de présentations et rapport).
  - Exécution de l'étape 1 du flux de travail (`1. Création et initialisation du projet`).
- **Quand NE PAS l'activer** :
  - Évolution du flux de travail (utiliser `flux-travail`).
  - Création ou modification de skills (utiliser `skills-dev`).

## 3. Missions disponibles
L'agent identifie le travail demandé par le concepteur et exécute la mission correspondante située dans `missions/` :
- `missions/init-depot.md` : Initialiser Git en local, basculer sur la branche active du sprint et publier sur GitHub avec GitHub CLI.
- `missions/init-projet.md` : Structurer le `README.md` racine et initialiser les dossiers de documentation (`presentations/` et `rapport/` avec script Node.js).
````

6. **Étape 6 — Rédaction des missions d'étape dans `.agents/skills/gestion-depot/missions/` :**  
   Créez `missions/init-depot.md` :

````markdown
# Mission : Initialisation du Dépôt (`init-depot.md`)

Initialiser le dépôt Git local, contrôler la branche active du sprint et publier le projet sur GitHub.

## Tâches de la mission
- **Tâche 1 : Détection du sprint et contrôle de branche** : Identifier le sprint actif dans `sprints/sprints.md` (ex: `sprint1`) et s'assurer que le travail est positionné sur la branche de sprint correspondante (`git checkout -b sprint1` ou `git checkout sprint1`).
- **Tâche 2 : Initialisation locale Git** : Vérifier ou exécuter l'initialisation Git locale (`git init`), configurer les exclusions (`.gitignore`) et préparer les fichiers pour le commit initial réalisé par le concepteur.
- **Tâche 3 : Publication sur GitHub** :
  - Publier le dépôt distant via GitHub CLI avec la commande : `gh repo create`.
  - Si GitHub CLI (`gh`) n'est pas connecté : inviter l'apprenant à s'authentifier avec `gh auth login`.
  - Inviter le concepteur à pousser la branche de travail active : `git push -u origin sprint1`.

## Livrables attendus
- Dépôt GitHub distant créé et synchronisé sur la branche de sprint active (`sprint1`).
- Historique Git initialisé proprement avec la branche de travail.
````

   Créez `missions/init-projet.md` :

````markdown
# Mission : Initialisation du Projet (`init-projet.md`)

Structurer le fichier `README.md` racine et initialiser les dossiers documentaires racine (`presentations/` et `rapport/`).

## Tâches de la mission
- **Tâche 1 : Structuration du README.md racine** :
  - Reformuler et structurer le fichier `README.md` racine selon le standard Solicode N3 en intégrant la stack technique du projet (Laravel 12).
- **Tâche 2 : Initialisation des présentations racine (`presentations/`)** :
  - Créer le dossier racine `presentations/` avec son guide `presentations/README.md`.
  - Créer les fichiers diaporamas vides : `presentation-blog.md` et `presentation-sprint1.md` au format Marp.
- **Tâche 3 : Initialisation du rapport modulaire racine (`rapport/`)** :
  - Créer le dossier racine `rapport/` avec son guide `rapport/README.md`.
  - Créer le document consolidé cible : `rapport/rapport-blog.md`.
  - Créer le sous-dossier `rapport/chapitres/` avec son guide `README.md` et les chapitres de base (`01-introduction.md`, `02-conclusion.md`).
  - Mettre en place le script Node.js autonome `rapport/concat-chapitres.js` et le fichier `rapport/package.json` pour la fusion automatique des chapitres.

## Livrables attendus
- Fichier `README.md` racine conforme aux standards Solicode.
- Dossier `presentations/` opérationnel avec ses deux diaporamas (`presentation-blog.md`, `presentation-sprint1.md`).
- Dossier `rapport/` opérationnel avec son sous-dossier `chapitres/` et son script Node.js de fusion.
````

7. **Étape 7 — Journalisation des commandes exécutées :**  
   Créez le sous-dossier et le fichier `tutoriels/ia/agent-skills/skill-gestion-depot/skill-gestion-depot.command.md` :

````markdown
```bash
mkdir -p .agents/rules .agents/skills/skills-dev .agents/skills/gestion-depot/missions
mkdir -p tutoriels/ia/agent-skills/skill-gestion-depot
git add .agents/ tutoriels/ia/agent-skills/skill-gestion-depot/skill-gestion-depot.command.md
git commit -m "feat(ia): outiller l'étape d'initialisation avec les règles Always-On et le skill gestion-depot"
git push origin sprint1
```
````

8. **Étape 8 — Commit et synchronisation sur `sprint1` :**  
   Indexez les nouveaux fichiers agentiques, validez le commit et poussez sur `sprint1` :

```bash
git add .agents/ tutoriels/ia/agent-skills/skill-gestion-depot/skill-gestion-depot.command.md
git commit -m "feat(ia): outiller l'étape d'initialisation avec les règles Always-On et le skill gestion-depot"
git push origin sprint1
```

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Fichiers de règles : `.agents/rules/contexte-projet.md` et `.agents/rules/regles-generales.md`.
  - Skill méta-gouvernance : `.agents/skills/skills-dev/SKILL.md`.
  - Skill gestion de dépôt : `.agents/skills/gestion-depot/SKILL.md` avec `missions/init-depot.md` et `missions/init-projet.md`.
  - Journal des commandes : `tutoriels/ia/agent-skills/skill-gestion-depot/skill-gestion-depot.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Les règles `contexte-projet.md` et `regles-generales.md` sont présentes dans `.agents/rules/`.
  - [ ] Le skill `gestion-depot` référence fidèlement ses deux missions `init-depot.md` et `init-projet.md`.
  - [ ] Les missions décrivent les actions outillées pour reproduire automatiquement l'Étape 1 du flux.
  - [ ] Le journal `skill-gestion-depot.command.md` consigne fidèlement les commandes exécutées.
