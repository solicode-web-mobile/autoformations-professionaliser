---
layout: tuto
title: "Pratique : Diagramme de cas d'utilisation macro"
sous_titre: "Modéliser les 15 cas d'utilisation macro du Blog des Lauréats avec relations structurelles en Mermaid"
slug: "modelisation-macro"
slug_domaine: "uml"
slug_ua: "cas-utilisation"
permalink: /tutos/modelisation-macro/
tuto_id: "T.311.221"
version: "normal"
ua: "UA.311.22"
maturite: "UA-Lab"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Cartographier l'ensemble des cas d'utilisation macro du *Blog des Lauréats* sous forme de diagramme UML en syntaxe déclarative Mermaid.js, puis isoler et spécifier le cas d'usage central retenu pour le premier sprint : **« Consulter un article de blog »**.

Vous devez concevoir :
1. Le fichier source Mermaid des cas d'utilisation : `use-cases-macro.mmd`.
2. La fiche technique d'analyse fonctionnelle : `modelisation-macro.md`.
3. Le diaporama Marp de restitution technique : `presentation-modelisation-macro.md`.

## 2. Consignes & Spécifications de Réalisation

1. **Jalon 1 — Cartographie des 15 Cas d'Utilisation Macro :**  
   Identifiez les fonctionnalités visibles du système sans sur-segmentation technique :
   - *Espace Public (Visiteur / Apprenant) :* Consulter l'accueil, lister les articles, consulter un article en détail, filtrer par catégorie, rechercher un lauréat.
   - *Espace Lauréat (Auteur) :* Rédiger un article, modifier son brouillon, publier un article, gérer son profil public.
   - *Espace Modération :* Valider une publication, suspendre un article, gérer les signalements.

2. **Jalon 2 — Modélisation des Relations Structurelles :**  
   Reliez chaque acteur à ses fonctionnalités respectives et appliquez rigoureusement les stéréotypes UML :
   - Relation d'inclusion obligatoire `<<include>>` (ex : *Consulter un article* inclut obligatoirement *Afficher les détails de l'auteur*).
   - Relation d'extension optionnelle ou conditionnelle `<<extend>>` (ex : *Partager sur les réseaux* étend conditionnellement *Consulter un article*).

3. **Jalon 3 — Isolation du Cas d'Usage Central du Sprint 1 :**  
   Isolez formellement le cas d'usage cible du premier incrément logiciel : **« Consulter un article de blog »** avec ses critères d'acceptation nominaux (affichage des métadonnées, titre, contenu) et d'exception (interception d'une ressource absente). Cette spécification servira d'entrée directe à la séance de Sprint Planning (`UA.351.22`).

4. **Jalon 4 — Restitution Marp :**  
   Concevez `presentation-modelisation-macro.md` au format Marp Markdown pour présenter la cartographie fonctionnelle de l'application et la justification du cas prioritaire du Sprint 1.

## 3. Livrables & Critères de validation
- **Livrables attendus :**
  - Diagramme Mermaid : `tutoriels/uml/cas-utilisation/modelisation-macro/use-cases-macro.mmd` sur la branche `sprint1`.
  - Fiche technique : `tutoriels/uml/cas-utilisation/modelisation-macro/modelisation-macro.md` sur la branche `sprint1`.
  - Diaporama Marp : `tutoriels/uml/cas-utilisation/modelisation-macro/presentation-modelisation-macro.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le fichier `use-cases-macro.mmd` compile sans erreur en orientation `graph TD`.
  - [ ] Les 15 cas d'utilisation macro couvrent l'ensemble des besoins du blog sans micro-actions techniques.
  - [ ] Les relations structurelles `<<include>>` et `<<extend>>` sont correctement orientées.
  - [ ] Le cas d'usage central *Consulter un article de blog* est isolé avec clarté.
  - [ ] Le diaporama Marp respecte les règles de lisibilité (zéro tableau Markdown).
