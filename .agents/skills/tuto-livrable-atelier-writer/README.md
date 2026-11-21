# Skill : tuto-livrable-atelier-writer

> **Rôle :** Réalisation concrète du travail demandé par les tutoriels d'ateliers et production des livrables de référence sous `ua-lab/`  
> **Écosystème :** `tutorial-*-writer`  
> **Master Skill :** [tuto-writer](../tuto-writer/SKILL.md)  
> **Périmètre :** Plateforme d'autoformation Jekyll (dossier `ua-lab/`)

---

## 1. Description & Cas d'Usage
Ce skill intervient après la conception de la fiche d'atelier par `tuto-atelier-writer` (`_tutos/...` avec `type: "tuto-atelier"`).  
Il délègue la rédaction pédagogique de la fiche technique à **`tuto-notion-writer`** (type `tuto-notion`, explications narratives approfondies adaptées aux débutants, zéro liste sèche) et produit :
1. La fiche technique de restitution rédigée : `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].md` (de type `tuto-notion`).
2. Le diaporama Marp de présentation interactif : `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/presentation-[slug-tuto].md` (doté de `layout: presentation`).
3. Le rapport d'exécution CLI : `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].command.md` (si l'atelier nécessite des commandes terminal).
4. Le manifeste sémantique : `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/version.yml` (recensant chaque livrable créé et sa version, ex: `demarche-design-thinking.md: "1.0.0"`).
5. La promotion de la fiche de tutoriel dans `_tutos/` vers `type: "tuto-atelier-notions"` (`statut_realisation: "realise"`), avec déclaration des `livrables:` réels et injection des notions fondamentales consolidées.

---

## 2. Prompts d'Invocation Types
- *"Réalise les livrables de l'atelier T.351.111 Comprendre Scrum sous ua-lab/"*
- *"Produis les livrables de l'UA-Lab UA.311.11 Design Thinking avec les diaporamas Marp, fiches de restitution et version.yml"*
- *"Passe le tutoriel T.311.111 en tuto-atelier-notions après avoir généré les livrables sous ua-lab/"*

---

## 3. Déroulement Pas-à-Pas
1. **Lecture du Tutoriel Source :** Analyser `_tutos/.../[slug-tuto].md` pour extraire les objectifs et le travail à faire.
2. **Mobilisation du Domaine :** Invoquer le skill technique approprié (`tuto-writer-scrum`, `tuto-writer-uml`, `tuto-writer-architecture`, `tuto-writer-laravel`, `tuto-writer-ia`).
3. **Création sous `ua-lab/` :**
   - Créer le dossier `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/`.
   - Rédiger `[slug-tuto].md` avec `nav_exclude: true`.
   - Rédiger `presentation-[slug-tuto].md` avec `layout: presentation`, `marp: true` et `nav_exclude: true`.
   - Rédiger `[slug-tuto].command.md` si des commandes sont exécutées.
   - Créer le fichier `version.yml` listant les fichiers livrables et leur numéro de version sémantique.
4. **Promotion du Tutoriel Jekyll :**
   - Remplacer `type: "tuto-atelier"` par `type: "tuto-atelier-notions"`.
   - Basculer `statut_realisation: "realise"`.
   - Déclarer le bloc `livrables:` avec les chemins réels existants sous `ua-lab/...`.
   - Injecter les **notions fondamentales consolidées** dans le corps de la fiche.
