# Organisation Universelle des Livrables sur le Poste Apprenant

## 1. Portée Normative & Contexte Multi-Niveaux

Ce document définit la norme officielle et universelle d'organisation, de nommage et de stockage de l'ensemble des livrables sur le poste de travail et le dépôt Git de l'apprenant.  
Il s'applique à tous les agents IA opérant sur le poste apprenant (en particulier l'**`Agent Réalisation de Sprint`**) ainsi qu'à l'apprenant lui-même.

### Généricité N1, N2, N3
Le cadre s'applique aux trois niveaux de formation de l'**EFP (Établissement de Formation Professionnelle)** :
- **Niveau N1 (Découvrir) :**
  - **Projet d'Imitation :** *Blog de l'EFP*.
  - **Code Applicatif (`src/`) :** HTML5, CSS3, JavaScript vanilla, PHP procédural/modulaire, requêtes SQL relationnelles.
- **Niveau N2 (Prototyper) :**
  - **Projet d'Imitation :** *Blog de l'EFP*.
  - **Code Applicatif (`src/`) :** Programmation Orientée Objet (POO PHP), Architecture 3-tiers / MVC (Modèle-Vue-Contrôleur).
- **Niveau N3 (Développer / Réaliser) :**
  - **Projet d'Imitation :** *Blog des Lauréats de l'EFP*.
  - **Code Applicatif (`src/`) :** Framework moderne (**Laravel**), architecture 2 couches / découplée, Blade, Alpine.js, Tailwind CSS, tests automatisés TDD.

---

## 2. Cartographie Globale du Dépôt Apprenant

```text
[racine-projet]/
├── tutoriels/              # Livrables d'apprentissage (fiches techniques, diaporamas, commandes)
│   ├── README.md           # Documentation d'accueil UNIQUE du dossier tutoriels (aucun autre README dans tutoriels/)
│   └── [slug-domaine]/
│       └── [slug-ua]/
│           └── [slug-tuto]/ # Dossier unitaire de tutoriel (AUCUN README.md ici)
├── src/                    # Code source de l'application (incrément du sprint selon stack active)
├── docs/                   # Documentation d'ingénierie logicielle et d'analyse :
│   ├── cadrage/            # Notes de cadrage, matrices de périmètre In-Scope / Out-of-Scope
│   ├── analyse/            # Dossiers d'analyse usagers, Personas, User Stories
│   ├── produit/            # Manifestes de Vision Produit (Product Goal)
│   ├── conception/         # UI Kit, maquettes, User Flow Mermaid, diagrammes (remplace docs/design/)
│   └── architecture/       # Dossiers d'architecture, diagrammes de composants, ADR
├── sprints/                # Gouvernance agile et cérémonies :
│   ├── sprints.md          # Feuille de route globale et historique des sprints
│   ├── sprint-[N].md       # Engagement de sprint (timebox 80h, rôles, découpage des tâches techniques)
│   ├── pv-review-[N].md    # Procès-verbaux contradictoires Go/No-Go et retours PO
│   └── retrospective-[N].md# Bilans réflexifs d'équipe et engagements d'amélioration continue
├── scrum/                  # Product Backlog vivant (product-backlog.md) et artéfacts agiles partagés
├── rapport/                # Chapitres modulaires et script Node.js d'assemblage (concat-chapitres.js)
├── presentations/          # Diaporamas de soutenance de projet et revues au format Marp
├── .agents/                # Configuration locale de l'Agent IA (rules/, references/, skills/)
├── .sync/                  # Traçabilité sémantique inter-agents (fichiers version.yml miroirs)
├── README.md               # Vitrine d'accueil professionnelle du dépôt d'ingénierie logicielle
└── .gitignore              # Fichier d'exclusions standardisées
```

---

## 3. Règles d'Exclusion et de Structuration Formelle

1. **Suppression formelle du dossier `issues/` :**  
   Les tâches techniques et le suivi opérationnel sont gérés directement dans le cadre des cérémonies agiles sous `sprints/` (fichier `sprint-[N].md`). Aucun dossier `issues/` distinct n'est utilisé.
2. **Règle Unique du fichier `README.md` dans `tutoriels/` :**  
   Le fichier `README.md` est requis **uniquement à la racine du dossier `tutoriels/`** (`tutoriels/README.md`) pour en présenter la structure.  
   **Interdiction formelle** de créer des fichiers `README.md` dans les sous-dossiers de domaines (`[slug-domaine]/`), d'UAs (`[slug-ua]/`) ou dans les dossiers unitaires de tutoriels (`[slug-tuto]/`). Le document principal d'un tutoriel porte directement son slug : `[slug-tuto].md`.
3. **Interdiction formelle du dossier racine `labs/` :**  
   Tout atelier pratique d'autoformation est obligatoirement déposé sous `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`.
4. **Interdiction absolue des captures d'écran comme livrables :**  
   Un livrable est exclusivement constitué de fichiers texte, code source ou Markdown versionnés sous Git.

---

## 4. Spécification du Journal des Commandes CLI (`[slug-tuto].command.md`)

- **Définition :**  
  Le journal des commandes constitue le **rapport de réalisation d'un tutoriel du point de vue ligne de commande**. Il consigne fidèlement les commandes terminal exécutées durant l'apprentissage (PowerShell, Composer, Artisan, Node.js, etc.).
- **Règles d'application selon la typologie du tutoriel :**
  - **Demandé UNIQUEMENT pour les tutoriels d'apprentissage et les labs (`tuto-lab`, `tuto-notion`, `tuto-code`)** dès lors que des commandes CLI sont requises.
  - **Formellement NON demandé pour les tâches opérationnelles (`tuto-tache`) :** Les livrables d'ingénierie de projet aux emplacements racine suffisent.
  - **S'il n'y a aucune commande terminal à exécuter (travail purement rédactionnel ou d'édition), le journal `.command.md` ne doit pas être créé.**
- **Format de rédaction :**  
  Présenté directement sous forme d'un bloc de code bash brut (sans double encapsulation Markdown) :
  ````markdown
  ```bash
  mkdir src/Controllers
  php artisan make:controller ArticleController
  ```
  ````
- **Interdiction formelle des commandes Git :**  
  Le journal ne consigne que les commandes opérationnelles utiles de la tâche. Il est formellement interdit d'y inclure les commandes Git (`git add`, `git commit`, `git push`).

---

## 5. Traçabilité et Versioning Sémantique dans `.sync/`

- **Emplacement exclusif des fichiers `version.yml` :**  
  Les numéros de version sémantique des livrables sont maintenus exclusivement dans l'arborescence miroir du dossier `.sync/` :
  `[racine-projet]/.sync/tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/version.yml`
- **Format minimaliste :**
  ```yaml
  comprendre-scrum.md: "1.0.0"
  presentation-comprendre-scrum.md: "1.0.0"
  ```
- **Interdiction formelle :** Ne jamais créer de fichiers `version.yml` dans `tutoriels/`, `src/`, `docs/` ou `sprints/`.
