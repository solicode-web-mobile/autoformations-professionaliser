# Typologie des Tutoriels et Échelle de Maturité de l'EFP

## 1. Principes Directeurs

Ce document définit les normes fondamentales d'ingénierie pédagogique de l'**EFP (Établissement de Formation Professionnelle)** :
- La dissociation absolue entre l'**Échelle de Maturité** (`maturite:`) et la **Typologie des Tutoriels** (`type:`).
- L'adoption du préfixe canonique **`tuto-*`** pour tous les types de tutoriels (`tuto-atelier`, `tuto-notion`, `tuto-code`, `tuto-tache`).
- La destination physique des livrables (dossier `tutoriels/` vs code applicatif `src/` vs emplacements racine `docs/`, `sprints/`, `scrum/`).
- La politique d'exigence des diaporamas Marp et des rapports de commandes CLI (`.command.md`).
- Le lien normatif avec [.agents/references/maturation-ua-labs.md](maturation-ua-labs.md).

---

## 2. L'Échelle de Maturité de l'EFP

$$\text{veille} \longrightarrow \text{lab} \longrightarrow \text{ua-lab} \longrightarrow \text{tutoriel} \quad (+\; \text{projet})$$

| Slug Maturité | Intitulé Didactique | Définition & Rôle dans le Cursus EFP |
| :--- | :--- | :--- |
| **`veille`** | Veille Technologique | Recherche exploratoire, prospective et état de l'art sans formalisation d'atelier. |
| **`lab`** | Atelier d'Expérimentation Pratique | Atelier actif guidé où l'apprenant mène l'investigation. **On ne donne PAS les notions de base en détail**, mais uniquement le travail à faire, les compétences à acquérir et les pistes de recherche. |
| **`ua-lab`** | Unité d'Atelier Validée & Intégrée | **Lab réalisé, validé sur le terrain et officiellement intégré au référentiel de compétences de l'EFP**. Le plan d'UA-Lab est spécifié et **les notions de base sont données en détail** (« Notions fondamentales » consolidées). |
| **`tutoriel`** | Standardisation Industrielle | Apprentissage guidé pas-à-pas, déterministe ($E_{n-1} \to E_n$) de code applicatif ou de syntaxe isolée. |
| **`projet`** | Ingénierie Opérationnelle | Réalisation de sprint Scrum, cadrage, backlog et cérémonies agiles (**0% théorie**). |

---

## 3. Typologie des Tutoriels (Préfixe Canonique `tuto-*`)

### A. `tuto-atelier` — Atelier Pratique Guidé (Maturité `lab`)
> [!IMPORTANT]
> Un tutoriel d'atelier porte toujours la maturité **`maturite: "lab"`**.  
> La valeur `ua-lab` est **exclusivement une maturité d'Unité d'Apprentissage (`_uas/`)** désignant une UA validée et intégrée dans le cursus de l'EFP. Elle n'est jamais portée par un tutoriel unitaire.

- **Finalité :** Assimilation collective et guidée d'un domaine ou d'une compétence nouvelle (Design Thinking, Scrum méthodologique, Modélisation UML, Architecture, Outillage IA).
- **Cycle de maturation au niveau tutoriel :**
  - Au stade exploratoire : Travail à faire + Ce que l'apprenant doit apprendre, **SANS notions de base en détail**.
  - Après validation terrain : **Notions de base DONNÉES EN DÉTAIL** (« Notions fondamentales » consolidées). L'UA associée est alors promue en `maturite: "ua-lab"`.
- **Livrables attendus (dans `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`) :**
  1. Fiche technique d'atelier : `[slug-tuto].md`.
  2. Diaporama Marp de restitution : `presentation-[slug-tuto].md` (**exclusif au format atelier**).
  3. Journal des commandes CLI : `[slug-tuto].command.md` (si des commandes terminal ont été exécutées).
  4. Fichiers de code ou manifestes d'atelier exploratoire (dans le même dossier unitaire).

### B. `tuto-tache` — Tâche Opérationnelle de Projet (Maturité `projet`)
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

### C. `tuto-notion` — Tutoriel de Notion Hors Projet d'Imitation (Maturité `tutoriel`)
- **Finalité :** Enseignement d'un concept théorique et pratique isolée en bac à sable, sans impact direct sur l'incrément déployable du projet d'imitation (ex : kata d'algorithmique, manipulation d'expressions régulières, découverte de la syntaxe Blade).
- **Livrables attendus (dans `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`) :**
  1. Fiche technique d'apprentissage : `[slug-tuto].md`.
  2. Fichiers de code d'exercices ou tests isolés (dans le même sous-dossier).
  3. Journal des commandes CLI : `[slug-tuto].command.md` (si manipulation CLI).
- **Règle :** **SANS présentation Marp** (ce n'est pas un atelier collectif).

### D. `tuto-code` — Tutoriel de Code sur Projet d'Imitation (Maturité `tutoriel`)
- **Finalité :** Développement incrémental de code contribuant directement à l'incrément déployable du sprint sur le projet d'imitation (*Blog de l'EFP* en N1/N2, *Blog des Lauréats* en N3).
- **Livrables attendus :**
  1. **Code source applicatif :** Déposé directement sous **`src/`** (ou l'arborescence officielle de la stack active : contrôleurs, services, modèles, vues Blade, tests TDD).
  2. **Journal des commandes CLI :** `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].command.md` (consigne les commandes d'environnement, Artisan, Composer, migrations, tests).
- **Règle :** **SANS présentation Marp**.

---

## 4. Matrice de Synthèse & Règles de Restitution

| Type de Tutoriel (`type:`) | Maturité Typique (`maturite:`) | Destination du Livrable | Diaporama Marp ? | Journal CLI (`.command.md`) ? |
| :--- | :--- | :--- | :---: | :---: |
| **`tuto-atelier`** | `lab` | `tutoriels/.../[slug-tuto]/` | **OUI** (`presentation-[slug-tuto].md`) | **OUI** (si CLI exécuté) |
| **`tuto-tache`** | `projet` | Emplacements racine (`docs/`, `sprints/`, `scrum/`, etc.) | **NON** | **NON** (proscrit) |
| **`tuto-notion`** | `tutoriel` | `tutoriels/.../[slug-tuto]/` | **NON** | **OUI** (si CLI exécuté) |
| **`tuto-code`** | `tutoriel` | **`src/`** (arborescence applicative) | **NON** | **OUI** (`tutoriels/.../[slug-tuto].command.md`) |

---

## 5. Règle du Journal des Commandes CLI

> [!IMPORTANT]
> Le journal des commandes CLI (`[slug-tuto].command.md`) représente le **rapport d'exécution technique du tutoriel**.  
> - Il atteste que les commandes requises (création de composants, installation de dépendances, migration, compilation d'assets, exécution de tests) ont été rigoureusement exécutées.  
> - Il est strictement réservé aux tutoriels d'apprentissage et d'atelier (`tuto-atelier`, `tuto-notion`, `tuto-code`).  
> - Il est formellement interdit d'y inclure les commandes de gestion de version Git (`add`, `commit`, `push`).  
> - Il est **proscrit pour les tâches opérationnelles (`tuto-tache`)**.
