# Communication Inter-Agents : Directives pour l'Agent Réalisation de Sprint

- **Émetteur :** Agent de Rédaction de l'Autoformation (`redacteur-autoformation`)
- **Destinataire :** Agent Réalisation de Sprint (`realisation-sprint`)
- **Date :** 2026-11-21
- **Objet :** Structuration des flux opérationnels (`flux-travail-s[X].md`) et qualification rigoureuse des Unités d'Apprentissage (UA)

---

## 1. Contexte & Constat

Lors de l'analyse du flux de travail opérationnel de la session S0 ([`flux-travail-s0.md`](file:///d:/labs-web/projet-imiation-n3/flux-travail/sessions/flux-travail-s0.md)), deux ajustements structurels majeurs sont requis pour garantir un alignement direct et sans distorsion avec la plateforme d'autoformation Jekyll de l'EFP :

1. **Suppression des conteneurs de « Phases » artificielles :**  
   Le découpage du flux de travail ne doit plus utiliser de « Phases » génériques (ex: *Phase 1 : UA-Lab...*, *Phase 2 : UA-Lab...*). Le plan de session est directement composé de la **séquence ordonnée des Unités d'Apprentissage (UAs)**.
2. **Qualification explicite du type et de la maturité de chaque UA :**  
   Chaque bloc d'apprentissage doit déclarer son type d'UA formel (`UA-Lab` ou `UA-Tâche`) et son niveau de maturité, sans confusion avec les types de tutoriels unitaires (`tuto-*`).

---

## 2. Règle Normative de Typologie : Niveau UA vs Niveau Tutoriel

| Niveau d'Entité | Attribut / Métadonnée | Types Autorisés | Description & Usage |
| :--- | :--- | :--- | :--- |
| **Niveau UA** (`_uas/`) | **Type d'UA** & **`maturite`** | **`UA-Lab`** (`maturite: "lab"` ou `"ua-lab"`) | Atelier d'apprentissage pratique guidé (découverte active d'un paradigme). |
| | | **`UA-Tâche`** (`maturite: "projet"`) | Tâche d'application opérationnelle sur le projet réel (cadrage, backlog, incrément, rituels). 0% théorie. |
| **Niveau Tutoriel** (`_tutos/`) | **`type`** | **`tuto-atelier`** | Fiche d'atelier pratique guidé (composant d'une `UA-Lab`). |
| | | **`tuto-tache`** | Fiche de tâche opérationnelle de sprint (composant d'une `UA-Tâche`). |
| | | **`tuto-notion`** | Fiche de notion théorique/syntaxique isolée hors imitation. |
| | | **`tuto-code`** | Fiche de progression incrémentale de code ($E_{n-1} \to E_n$). |

> [!IMPORTANT]
> `tuto-atelier` et `tuto-tache` sont des **types de tutoriels** (`type:` sous `_tutos/`).  
> Ils ne doivent jamais être employés comme type d'UA. Au niveau UA, les types officiels sont **`UA-Lab`** et **`UA-Tâche`**.

---

## 3. Directives d'Adaptation pour le Flux Opérationnel de S0 (`flux-travail-s0.md`)

Il est demandé à l'Agent Réalisation de Sprint d'actualiser [`flux-travail-s0.md`](file:///d:/labs-web/projet-imiation-n3/flux-travail/sessions/flux-travail-s0.md) selon la structure canonique suivante :

1. **Remplacer les 5 « Phases » par les 5 Unités d'Apprentissage ordonnées :**
   - **UA 1 (UA-Lab) :** *Initiation à la Démarche Agile et Cadre Scrum* (`UA.351.11`) — 5 tutoriels (Étapes 1 à 5) — Statut : **Réalisée** (`maturite: "ua-lab"`).
   - **UA 2 (UA-Lab) :** *Design Thinking : Démarche et Empathie sur l'Application Todo List* (`UA.311.11`) — 3 tutoriels (Étapes 6, 7, 8) — Statut : **À réaliser** (`maturite: "lab"`).
   - **UA 3 (UA-Lab) :** *Design Thinking : Parcours Utilisateur et Prototypage d'Interface* (`UA.311.12`) — 2 tutoriels (Étapes 9, 10) — Statut : **À réaliser** (`maturite: "lab"`).
   - **UA 4 (UA-Tâche) :** *Application Projet : Dépôt, Cadrage, Stack et Backlog Initial* (`UA.351.01`) — 6 tutoriels (Étapes 11 à 16) — Statut : **À réaliser** (`maturite: "projet"`).
   - **UA 5 (UA-Tâche) :** *Incrément Maquette de la Page d'Accueil et Clôture Agile* (`UA.351.02`) — 2 tutoriels (Étapes 17, 18) — Statut : **À réaliser** (`maturite: "projet"`).
2. **Durée de Session :** Confirmer la mention que la durée globale (80h) est fournie à **titre purement indicatif** pour les formateurs et concepteurs pédagogiques.
3. **Incrément Visuel :** Confirmer le ciblage exclusif sur la **Maquette de la Page d'Accueil** du Blog des Lauréats.

---

Merci de prendre en compte cette structure pour les livraisons de flux opérationnels présents et futurs.
