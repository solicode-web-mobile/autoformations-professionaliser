---
layout: tuto
title: "Modélisation déclarative de parcours utilisateur (User Flow Mermaid)"
sous_titre: "Cartographier les flux de navigation et décisions utilisateur en syntaxe textuelle Mermaid"
slug: "user-flow"
slug_domaine: "design"
slug_ua: "parcours-utilisateur-prototypage"
permalink: /tutos/user-flow/
tuto_id: "T.311.121"
version: "normal"
ua: "UA.311.12"
type: "tuto-atelier"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
---

## 1. Contexte & Enjeux
Avant de dessiner les écrans d'une interface, il est indispensable de structurer la logique de navigation : comment l'utilisateur entre-t-il sur le site, quelles actions effectue-t-il et quelles décisions orientent son parcours ?

Le **User Flow** modélise cette séquence logique. Grâce à la syntaxe déclarative **Mermaid**, ce diagramme est rédigé sous forme de texte, versionné avec Git et consultable directement dans les fichiers Markdown.

## 2. Ce que vous devez apprendre
- Identifier les étapes logiques d'un parcours utilisateur complet (point d'entrée, actions clés, points de décision, sortie/objectif atteint).
- Maîtriser la syntaxe textuelle déclarative Mermaid `flowchart` :
  - Nœuds d'action rectangulaires (`[Action]`).
  - Nœuds de décision en losange (`{Décision ?}`).
  - Connecteurs orientés avec libellés conditionnels (`-->|Oui|`).
  - Sous-graphes thématiques pour regrouper les zones d'interaction (`subgraph`).
- Garantir la traçabilité et le versionnement du design au même titre que le code applicatif.

## 3. Travail à faire
1. **Étape 1 — Identifier le scénario cible :** Définir le scénario nominal d'un visiteur qui découvre une plateforme Web, recherche un contenu et consulte un élément détaillé.
2. **Étape 2 — Structurer les embranchements :** Identifier au moins deux alternatives ou cas d'erreur (ex : contenu trouvé vs aucun résultat).
3. **Étape 3 — Coder le diagramme Mermaid :** Rédiger le graphe `flowchart TD` en respectant scrupuleusement la syntaxe déclarative.
4. **Étape 4 — Rédiger la fiche et le diaporama :** Formaliser la documentation dans `tutoriels/design/parcours-utilisateur-prototypage/user-flow/user-flow.md` et préparer le diaporama Marp dans `tutoriels/design/parcours-utilisateur-prototypage/user-flow/presentation-user-flow.md`.

## 4. Pistes de recherche active
- Quels sont les avantages d'un diagramme Mermaid textuel par rapport à un schéma réalisé sous un outil graphique propriétaire (Figma, Miro, Photoshop) ?
- Pourquoi un User Flow doit-il toujours commencer par un événement déclencheur et se terminer par un objectif utilisateur accompli ?
- Consultez la documentation officielle de Mermaid JS sur les organigrammes (`flowchart`).

## 5. Livrables attendus & Critères de validation
- **Fiche technique d'atelier :** `tutoriels/design/parcours-utilisateur-prototypage/user-flow/user-flow.md`.
- **Diaporama Marp de restitution :** `tutoriels/design/parcours-utilisateur-prototypage/user-flow/presentation-user-flow.md`.
- **Critère de succès :** Le diagramme Mermaid est syntaxiquement valide, lisible, modélise clairement les choix et actions de l'utilisateur et les livrables sont versionnés sur la branche `sprint0`.
