---
layout: tuto
title: "Initialiser le rapport modulaire et le script d'assemblage Node.js"
sous_titre: "Structurer le dossier rapport/ avec ses chapitres indépendants et automatiser la compilation avec Node.js"
slug: "rapport-modulaire"
slug_domaine: "realisation-projet"
slug_ua: "initialisation"
permalink: /tutos/rapport-modulaire/
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
  - Notions de base sur Node.js (exécution de scripts en ligne de commande : `node script.js`).
  - Structuration de documents modulaires en Markdown.
  - Principes de séparation des contenus et compilation de documentation.
- **Prérequis de projet :** Dépôt Git initialisé, README racine et arborescence créés sur `sprint1` (`T.351.202`).
- **Branche Git :** `sprint1`

## 2. Travail à Faire
- **Tâche 1 : Structuration du dossier :** Créer le répertoire `rapport/` et son sous-dossier `rapport/chapitres/`.
- **Tâche 2 : Rédaction des chapitres de cadrage :** Rédiger `rapport/README.md`, `rapport/chapitres/README.md`, `01-introduction.md` et `02-conclusion.md`.
- **Tâche 3 : Script d'assemblage Node.js :** Créer `rapport/concat-chapitres.js` et le fichier de configuration `rapport/package.json`.
- **Tâche 4 : Génération du rapport consolidé :** Exécuter le script Node.js pour produire le document final `rapport/rapport-blog.md`.
- **Tâche 5 : Journalisation des commandes :** Consigner les commandes exécutées dans `tutoriels/realisation-projet/initialisation/rapport-modulaire/rapport-modulaire.command.md`.

## 3. Étapes de Réalisation

1. **Étape 1 — Création de l'arborescence modulaire :**  
   À la racine du projet `blog-des-laureats`, créez le sous-dossier `chapitres/` dans `rapport/` :
   ```bash
   mkdir -p rapport/chapitres
   ```

2. **Étape 2 — Rédaction du guide d'utilisation `rapport/README.md` :**  
   Dans `rapport/`, créez le fichier `README.md` décrivant l'organisation et la commande de compilation :
   ```markdown
   # Dossier du Rapport de Projet (`rapport/`)

   Ce dossier héberge le rapport technique et académique du projet Blog des lauréats.

   ## 1. Organisation modulaire
   Le rapport est découpé en chapitres indépendants dans le sous-dossier `chapitres/` pour faciliter la rédaction progressive :
   - `chapitres/01-introduction.md` : Contexte, objectifs et périmètre.
   - `chapitres/02-conclusion.md` : Bilan des réalisations et perspectives.

   ## 2. Compilation automatique
   Le fichier unique consolidé `rapport-blog.md` est généré automatiquement à partir des chapitres à l'aide d'un script Node.js :
   - Script : `concat-chapitres.js`
   - Commande directe :
     ```bash
     node concat-chapitres.js
     ```
   - Ou via npm :
     ```bash
     npm run build
     ```

   ## 3. Guide de rédaction
   - Rédiger ou modifier les chapitres dans le sous-dossier `chapitres/`.
   - Chaque fichier de chapitre doit commencer par son titre de niveau 1 (`# Chapitre N : ...`).
   - Lancer le script de compilation après chaque modification pour mettre à jour `rapport-blog.md`.
   - Respecter les règles générales : zéro tableau Markdown, liens relatifs et français professionnel.
   ```

3. **Étape 3 — Rédaction du guide interne `rapport/chapitres/README.md` :**  
   Dans `rapport/chapitres/`, créez le fichier `README.md` formalisant les règles de nommage des chapitres :
   ```markdown
   # Sous-dossier des Chapitres (`rapport/chapitres/`)

   Ce sous-dossier contient les chapitres unitaires qui composent le rapport de projet.

   ## 1. Rôle du sous-dossier
   - Découper la rédaction du rapport en modules indépendants et clairs.
   - Permettre à l'apprenant de se concentrer sur un chapitre spécifique à la fois.
   - Faciliter le travail collaboratif et les revues de code/documentation.

   ## 2. Chapitres inclus
   - `01-introduction.md` : Contexte, objectifs et démarche méthodologique.
   - `02-conclusion.md` : Synthèse des acquis, bilan technique et perspectives d'évolution.

   ## 3. Règle de nommage et compilation
   - Nommer les fichiers avec un préfixe numérique ordonné (`01-...`, `02-...`).
   - Chaque fichier commence par un titre Markdown de niveau 1 (`# Chapitre N : ...`).
   - Le script `../concat-chapitres.js` lit automatiquement ces fichiers par ordre alphabétique pour générer le rapport consolidé `rapport-blog.md`.
   ```

4. **Étape 4 — Rédaction des deux premiers chapitres du rapport :**  
   Dans `rapport/chapitres/`, créez `01-introduction.md` :
   ```markdown
   # Chapitre 1 : Introduction Générale

   ## 1. Contexte du projet
   Dans le cadre de la formation au sein de Solicode Tanger (Niveau 3), le projet d'imitation consiste à concevoir et développer une application web complète intitulée **Blog des lauréats**. Cette plateforme a pour mission de valoriser les parcours des anciens lauréats, de partager leurs retours d'expérience et d'inspirer les nouvelles promotions d'apprenants.

   ## 2. Objectifs du projet
   - Développer une application moderne avec le framework Laravel 12 en PHP.
   - Adopter une architecture logicielle robuste en 2 couches (Contrôleur -> Service).
   - Mettre en œuvre la méthodologie Agile/Scrum avec découpage en sprints successifs.
   - Exploiter les outils d'ingénierie modernes : modélisation UML (diagramme de contexte, cas d'utilisation), gestion de version Git/GitHub et agent IA d'automatisation.

   ## 3. Périmètre initial
   Le premier sprint du projet se concentre sur l'initialisation complète de l'environnement, le cadrage méthodologique, l'outillage de l'Agent IA et la réalisation d'une première fonctionnalité métier : la consultation détaillée d'un article de blog avec gabarit Blade responsive et gestion des erreurs 404.
   ```

   Créez également `rapport/chapitres/02-conclusion.md` :
   ```markdown
   # Chapitre 2 : Conclusion et Perspectives

   ## 1. Bilan des réalisations
   Le démarrage du projet a permis de poser des fondations méthodologiques et techniques solides :
   - Initialisation propre du dépôt GitHub et gestion rigoureuse des branches de sprint.
   - Mise en place d'un environnement de travail assisté par l'Agent IA avec règles Always-On et catalogue de skills modulaires.
   - Formalisation complète du processus de développement dans le flux de travail.
   - Structuration modulaire des présentations et des chapitres du rapport technique.

   ## 2. Acquis pédagogiques et techniques
   - Maîtrise des standards d'ingénierie logicielle (Agile/Scrum, 2TUP).
   - Structuration claire d'une architecture backend Laravel en 2 couches.
   - Automatisation de tâches documentaires à l'aide de scripts Node.js.

   ## 3. Perspectives d'évolution
   Les prochains sprints permettront d'étendre les fonctionnalités de la plateforme Blog des lauréats :
   - Ajout de la gestion complète des articles (création, édition, suppression).
   - Gestion des catégories, tags et commentaires.
   - Authentification, rôles utilisateurs et espace d'administration dédié.
   ```

5. **Étape 5 — Mise en place du script d'assemblage Node.js :**  
   Dans `rapport/`, créez `concat-chapitres.js` :
   ```javascript
   /**
    * Script Node.js de concatenation modulaire des chapitres du rapport.
    * Usage : node concat-chapitres.js
    */

   const fs = require('fs');
   const path = require('path');

   const chapitresDir = path.join(__dirname, 'chapitres');
   const outputFile = path.join(__dirname, 'rapport-blog.md');

   console.log('--- Compilation du Rapport de Projet ---');

   if (!fs.existsSync(chapitresDir)) {
     console.error(`Erreur : Le dossier "${chapitresDir}" n'existe pas.`);
     process.exit(1);
   }

   // Lire tous les fichiers .md du dossier chapitres, en ignorant README.md
   const files = fs.readdirSync(chapitresDir)
     .filter(file => file.endsWith('.md') && file.toLowerCase() !== 'readme.md')
     .sort((a, b) => a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' }));

   if (files.length === 0) {
     console.warn('Attention : Aucun chapitre Markdown trouve a compiler.');
     process.exit(0);
   }

   console.log(`Chapitres detectes (${files.length}) :`);
   files.forEach((file, index) => {
     console.log(`  ${index + 1}. ${file}`);
   });

   // En-tête global du rapport
   let content = `# Rapport de Projet : Blog des Lauréats

   > Document consolidé généré automatiquement à partir des chapitres modulaires.
   > Date de génération : ${new Date().toISOString().split('T')[0]}

   ---

   `;

   // Concaténer chaque chapitre
   files.forEach((file, index) => {
     const filePath = path.join(chapitresDir, file);
     const chapterContent = fs.readFileSync(filePath, 'utf-8').trim();
     content += chapterContent + '\n\n';
     if (index < files.length - 1) {
       content += '---\n\n';
     }
   });

   // Écrire le fichier consolidé
   fs.writeFileSync(outputFile, content, 'utf-8');

   console.log(`Succes : Rapport compile avec succes dans "${path.basename(outputFile)}" !`);
   ```

   Créez également `rapport/package.json` :
   ```json
   {
     "name": "rapport-blog-laureats",
     "version": "1.0.0",
     "description": "Compilation modulaire du rapport de projet pour le Blog des laureats",
     "main": "concat-chapitres.js",
     "scripts": {
       "build": "node concat-chapitres.js"
     },
     "keywords": [
       "solicode",
       "rapport",
       "markdown"
     ],
     "author": "Solicode Tanger",
     "license": "ISC"
   }
   ```

6. **Étape 6 — Compilation du rapport consolidé et vérification :**  
   Dans votre terminal, placez-vous dans `rapport/` et lancez la compilation :
   ```bash
   cd rapport
   node concat-chapitres.js
   cd ..
   ```
   *Le fichier `rapport/rapport-blog.md` est généré automatiquement.*

7. **Étape 7 — Journalisation des commandes exécutées :**  
   Créez le sous-dossier et le fichier `tutoriels/realisation-projet/initialisation/rapport-modulaire/rapport-modulaire.command.md` :
````markdown
```bash
mkdir -p rapport/chapitres
cd rapport
node concat-chapitres.js
cd ..
mkdir -p tutoriels/realisation-projet/initialisation/rapport-modulaire
git add rapport/ tutoriels/realisation-projet/initialisation/rapport-modulaire/rapport-modulaire.command.md
git commit -m "docs: initialiser le rapport modulaire et le script d'assemblage Node.js"
git push origin sprint1
```
````

8. **Étape 8 — Commit et synchronisation sur `sprint1` :**  
   Indexez les nouveaux fichiers, validez le commit et poussez sur `sprint1` :
   ```bash
   git add rapport/ tutoriels/realisation-projet/initialisation/rapport-modulaire/rapport-modulaire.command.md
   git commit -m "docs: initialiser le rapport modulaire et le script d'assemblage Node.js"
   git push origin sprint1
   ```

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Dossier `rapport/` avec `README.md`, `concat-chapitres.js`, `package.json` et `rapport-blog.md`.
  - Sous-dossier `rapport/chapitres/` avec `README.md`, `01-introduction.md` et `02-conclusion.md`.
  - Journal des commandes : `tutoriels/realisation-projet/initialisation/rapport-modulaire/rapport-modulaire.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Les chapitres `01-introduction.md` et `02-conclusion.md` sont rédigés dans `rapport/chapitres/`.
  - [ ] Le script `concat-chapitres.js` s'exécute avec succès via `node concat-chapitres.js` sans erreur.
  - [ ] Le fichier `rapport-blog.md` est généré et regroupe les chapitres assemblés.
  - [ ] Le journal `rapport-modulaire.command.md` consigne fidèlement les commandes exécutées.
