---
layout: tuto
title: "Concevoir l'UI Kit et prototyper la Maquette de la Page d'Accueil"
sous_titre: "Spécifier l'UI Kit Preline UI et assembler la maquette ergonomique responsive du Blog des Lauréats"
slug: "maquette-page-accueil"
slug_domaine: "design"
slug_ua: "UA.311.12"
permalink: "/tutos/maquette-page-accueil/"
tuto_id: "T.311.124"
version: "normal"
ua: "UA.311.12"
type: "tuto-tache"
etape: 13
nav_order: 4
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
livrables:
  - chemin: "docs/conception/ui-kit.md"
    version: "0.1.0"
  - chemin: "docs/conception/maquettes-sprint-1.md"
    version: "0.1.0"
---

## 1. Travail à faire
Concevez l'incrément visuel et ergonomique majeur du Sprint 0 sur le *Blog des Lauréats* :
1. **Étape 1 — Spécifier l'UI Kit du projet :** Documentez dans `docs/conception/ui-kit.md` la charte graphique officielle : couleurs primaires/secondaires Tailwind CSS, typographie système, espacements et catalogue de composants Preline UI retenus pour le projet.
2. **Étape 2 — Modéliser le User Flow de la page d'accueil :** Rédigez le diagramme Mermaid `flowchart TD` illustrant le parcours d'un lecteur découvrant la page d'accueil, parcourant la liste des articles et sélectionnant une catégorie.
3. **Étape 3 — Concevoir la maquette ergonomique interactive :** Assemblez la maquette complète de la page d'accueil avec les composants Preline UI :
   - *Header / Navbar avec logo de l'EFP, liens de navigation et bouton de connexion.*
   - *Hero Section mettant en avant le dernier témoignage marquant d'un lauréat.*
   - *Barre de filtre interactif par catégories techniques (Laravel, Scrum, Design, IA).*
   - *Grille responsive de cartes d'articles récents (Card Article).*
   - *Footer institutionnel avec mentions légales et liens utiles.*
4. **Étape 4 — Rédiger la documentation de conception :** Déposez la maquette ergonomique détaillée et son code HTML d'illustration dans `docs/conception/maquettes-sprint-1.md`.

## 2. Consignes de Réalisation
- Créez le dossier et les fichiers de conception :
  ```powershell
  mkdir docs/conception
  echo "" > docs/conception/ui-kit.md
  echo "" > docs/conception/maquettes-sprint-1.md
  ```
- Renseignez `docs/conception/ui-kit.md` avec la grille Tailwind et les composants Preline UI prêts à l'intégration.
- Intégrez dans `docs/conception/maquettes-sprint-1.md` :
  - Le diagramme Mermaid du User Flow de la page d'accueil.
  - La description ergonomique de chaque zone de l'écran.
  - Le prototype de structure HTML utilisant les classes Tailwind CSS et composants Preline UI.

## 3. Livrables attendus
- **Fichiers de projet :** `docs/conception/ui-kit.md` et `docs/conception/maquettes-sprint-1.md`.
- **Critère de conformité :** L'UI Kit est formalisé et la maquette de la page d'accueil est fidèle aux attentes des Personas et prête pour la démonstration.
