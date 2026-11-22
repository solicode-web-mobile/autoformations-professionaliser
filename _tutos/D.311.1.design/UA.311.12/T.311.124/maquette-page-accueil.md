---
layout: tuto
title: "Concevoir l'UI Kit et prototyper la Maquette de la Page d'Accueil"
sous_titre: "SpÃ©cifier l'UI Kit Preline UI et assembler la maquette ergonomique responsive du Blog des LaurÃ©ats"
slug: "maquette-page-accueil"
slug_domaine: "design"
slug_ua: "UA.311.12"
permalink: /tutos/maquette-page-accueil/
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

## 1. Travail Ã  faire
Concevez l'incrÃ©ment visuel et ergonomique majeur du Sprint 0 sur le *Blog des LaurÃ©ats* :
1. **Ã‰tape 1 â€” SpÃ©cifier l'UI Kit du projet :** Documentez dans `docs/conception/ui-kit.md` la charte graphique officielle : couleurs primaires/secondaires Tailwind CSS, typographie systÃ¨me, espacements et catalogue de composants Preline UI retenus pour le projet.
2. **Ã‰tape 2 â€” ModÃ©liser le User Flow de la page d'accueil :** RÃ©digez le diagramme Mermaid `flowchart TD` illustrant le parcours d'un lecteur dÃ©couvrant la page d'accueil, parcourant la liste des articles et sÃ©lectionnant une catÃ©gorie.
3. **Ã‰tape 3 â€” Concevoir la maquette ergonomique interactive :** Assemblez la maquette complÃ¨te de la page d'accueil avec les composants Preline UI :
   - *Header / Navbar avec logo de l'EFP, liens de navigation et bouton de connexion.*
   - *Hero Section mettant en avant le dernier tÃ©moignage marquant d'un laurÃ©at.*
   - *Barre de filtre interactif par catÃ©gories techniques (Laravel, Scrum, Design, IA).*
   - *Grille responsive de cartes d'articles rÃ©cents (Card Article).*
   - *Footer institutionnel avec mentions lÃ©gales et liens utiles.*
4. **Ã‰tape 4 â€” RÃ©diger la documentation de conception :** DÃ©posez la maquette ergonomique dÃ©taillÃ©e et son code HTML d'illustration dans `docs/conception/maquettes-sprint-1.md`.

## 2. Consignes de RÃ©alisation
- CrÃ©ez le dossier et les fichiers de conception :
  ```powershell
  mkdir docs/conception
  echo "" > docs/conception/ui-kit.md
  echo "" > docs/conception/maquettes-sprint-1.md
  ```
- Renseignez `docs/conception/ui-kit.md` avec la grille Tailwind et les composants Preline UI prÃªts Ã  l'intÃ©gration.
- IntÃ©grez dans `docs/conception/maquettes-sprint-1.md` :
  - Le diagramme Mermaid du User Flow de la page d'accueil.
  - La description ergonomique de chaque zone de l'Ã©cran.
  - Le prototype de structure HTML utilisant les classes Tailwind CSS et composants Preline UI.

## 3. Livrables attendus
- **Fichiers de projet :** `docs/conception/ui-kit.md` et `docs/conception/maquettes-sprint-1.md`.
- **CritÃ¨re de conformitÃ© :** L'UI Kit est formalisÃ© et la maquette de la page d'accueil est fidÃ¨le aux attentes des Personas et prÃªte pour la dÃ©monstration.
