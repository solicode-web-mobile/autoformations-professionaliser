---
layout: tuto
title: "Modéliser le User Flow de la page d'accueil du Blog des Lauréats"
sous_titre: "Cartographier les parcours d'accès aux articles et de navigation en syntaxe déclarative Mermaid"
slug: "user-flow-page-accueil-blog"
slug_domaine: "design"
slug_ua: "parcours-utilisateur-prototypage"
permalink: /tutos/user-flow-page-accueil-blog/
tuto_id: "T.311.123"
version: "normal"
ua: "UA.311.12"
type: "tuto-tache"
etape: 12
nav_order: 3
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
livrables:
  - chemin: "docs/conception/user-flow.md"
    version: "0.1.0"
---

## 1. Travail à faire
À partir des fiches Personas du Blog des Lauréats, modélisez le parcours utilisateur d'accueil en syntaxe déclarative Mermaid :
- Modéliser le flux principal : Arrivée sur la page d'accueil $\to$ Découverte du Hero Banner $\to$ Consultation des derniers articles mis en avant $\to$ Filtrage par catégorie $\to$ Sélection d'un article.
- Intégrer les décisions d'interaction et points de bifurcation (ex : recherche vide, catégorie sans article).
- Rédiger le schéma Mermaid et la note explicative dans `docs/conception/user-flow.md`.

## 2. Étapes de Réalisation

1. **Étape 1 — Initialiser le document de conception :**

```powershell
mkdir docs/conception
echo "" > docs/conception/user-flow.md
```

2. **Étape 2 — Rédiger le diagramme Mermaid :**
   Insérez un bloc de code `mermaid` (`flowchart TD`) illustrant le parcours de découverte et de sélection d'articles.

## 3. Livrables attendus & Critères de validation
- **Fichier produit :** `docs/conception/user-flow.md`
- **Critères :** Diagramme Mermaid syntaxiquement valide couvrant au moins 2 parcours types des personas.
