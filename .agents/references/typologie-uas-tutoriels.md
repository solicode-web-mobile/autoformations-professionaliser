# Typologie des Unités d'Apprentissage et Slugs des Tutoriels

## 1. Principes Directeurs

Ce document définit la classification didactique et technique de l'ensemble des modules d'apprentissage de Solicode :
- La distinction stricte entre les types d'**Unités d'Apprentissage** (`UA-*`) et les slugs de types de **Tutoriels** (`tuto-*`).
- La destination physique des livrables (dossier `tutoriels/` vs emplacements racine vs dossier `src/`).
- La politique d'exigence des supports Marp et des journaux de commandes CLI (`.command.md`).

---

## 2. Typologie des Unités d'Apprentissage (UA)

| Type d'UA | Intitulé Didactique | Nature Pédagogique | Composition Typique |
| :--- | :--- | :--- | :--- |
| **`UA-Lab`** | Unité d'Atelier Pratique & Découverte | Découverte conceptuelle, acquisition de nouveaux domaines, modélisation UML/Mermaid, architecture logicielle | 1 fiche d'atelier guidé (`tuto-lab`) + éventuellement 1 application pratique |
| **`UA-Tâche`** | Unité d'Ingénierie Opérationnelle | 0% théorie. Actions de cadrage, rituels agiles Scrum, organisation de dépôt, clôture de sprint et soutenances | 1 à 4 tâches opérationnelles de projet (`tuto-tache`) |
| **`UA-Tuto`** | Unité d'Apprentissage de Code | Progression incrémentale $E_{n-1} \to E_n$ d'acquisition de compétences de développement | Séquence de tutoriels techniques (`tuto-notion` ou `tuto-code`) |

---

## 3. Typologie et Slugs Normalisés des Tutoriels

### A. `tuto-lab` — Atelier Pratique Guidé
- **Finalité :** Assimilation collective et guidée d'un domaine ou d'une compétence nouvelle (Design Thinking, Scrum théorique, Modélisation UML, Patterns d'architecture, Outillage IA).
- **Livrables attendus (dans `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`) :**
  1. Fiche technique d'atelier : `[slug-tuto].md`.
  2. Diaporama Marp de restitution : `presentation-[slug-tuto].md` (**exclusif au format lab**).
  3. Journal des commandes CLI : `[slug-tuto].command.md` (si des commandes terminal ont été exécutées).
  4. Fichiers de code ou manifestes d'atelier exploratoire (dans le même dossier unitaire).

### B. `tuto-tache` — Tâche Opérationnelle de Projet
- **Finalité :** Production concrète de livrables de projet ou réalisation d'un rituel de sprint (note de cadrage, Product Backlog, UI Kit, User Flow, Sprint Planning, Sprint Review, Rétrospective).
- **Livrables attendus :**
  - Fichiers d'ingénierie opérationnels déposés directement aux **emplacements racine officiels** :
    - `docs/cadrage/note-cadrage.md`, `docs/conception/ui-kit.md`, `docs/conception/maquettes-sprint-1.md`
    - `scrum/product-backlog.md`
    - `sprints/sprint-[N].md`, `sprints/pv-review-[N].md`, `sprints/retrospective-[N].md`
    - `README.md`, `rapport/`, `presentations/`
- **Règles d'allègement strictes :**
  - **Aucun journal des commandes CLI `[slug-tuto].command.md` requis.** Les livrables de projet suffisent.
  - **Aucun diaporama Marp de restitution requis** (sauf si la tâche est explicitement une soutenance).

### C. `tuto-notion` — Tutoriel d'Apprentissage Hors Projet d'Imitation
- **Finalité :** Enseignement d'un concept théorique et pratique isolée en bac à sable, sans impact direct sur l'incrément déployable du projet d'imitation (ex : kata d'algorithmique, manipulation d'expressions régulières, découverte de la syntaxe Blade).
- **Livrables attendus (dans `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`) :**
  1. Fiche technique d'apprentissage : `[slug-tuto].md`.
  2. Fichiers de code d'exercices ou tests isolés (dans le même sous-dossier).
  3. Journal des commandes CLI : `[slug-tuto].command.md` (si manipulation CLI).
- **Règle :** **SANS présentation Marp** (ce n'est pas un lab collectif).

### D. `tuto-code` — Tutoriel d'Apprentissage Sur Projet d'Imitation
- **Finalité :** Développement incrémental de code contribuant directement à l'incrément déployable du sprint sur le projet d'imitation (*Blog de l'EFP* en N1/N2, *Blog des Lauréats* en N3).
- **Livrables attendus :**
  1. **Code source applicatif :** Déposé directement sous **`src/`** (ou l'arborescence officielle de la stack active : contrôleurs, services, modèles, vues Blade, tests TDD).
  2. **Journal des commandes CLI :** `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].command.md` (consigne les commandes d'environnement, Artisan, Composer, migrations, tests).
- **Règle :** **SANS présentation Marp**.

---

## 4. Matrice de Synthèse & Règles de Restitution

| Slug Tutoriel | Domaine / Contexte | Destination du Livrable | Diaporama Marp ? | Journal CLI (`.command.md`) ? |
| :--- | :--- | :--- | :---: | :---: |
| **`tuto-lab`** | Lab & Découverte | `tutoriels/.../[slug-tuto]/` | **OUI** (`presentation-[slug-tuto].md`) | **OUI** (si CLI exécuté) |
| **`tuto-tache`** | Tâche de Projet | Emplacements racine (`docs/`, `sprints/`, `scrum/`, etc.) | **NON** | **NON** (proscrit) |
| **`tuto-notion`** | Apprentissage isolé | `tutoriels/.../[slug-tuto]/` | **NON** | **OUI** (si CLI exécuté) |
| **`tuto-code`** | Code sur Projet | **`src/`** (arborescence applicative) | **NON** | **OUI** (`tutoriels/.../[slug-tuto].command.md`) |

---

## 5. Règle du Journal des Commandes CLI

> [!IMPORTANT]
> Le journal des commandes CLI (`[slug-tuto].command.md`) représente le **rapport d'exécution technique du tutoriel**.  
> - Il atteste que les commandes requises (création de composants, installation de dépendances, migration, compilation d'assets, exécution de tests) ont été rigoureusement exécutées.  
> - Il est strictement réservé aux tutoriels d'apprentissage et de lab (`tuto-lab`, `tuto-notion`, `tuto-code`).  
> - Il est formellement interdit d'y inclure les commandes de gestion de version Git (`add`, `commit`, `push`).  
> - Il est **proscrit pour les tâches opérationnelles (`tuto-tache`)**.
