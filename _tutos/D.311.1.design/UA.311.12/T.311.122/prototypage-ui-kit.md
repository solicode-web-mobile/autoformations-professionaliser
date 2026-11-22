---
layout: tuto
title: "Prototypage d'interface et conception de l'UI Kit (Preline UI)"
sous_titre: "Structurer un système de conception modulaire avec Tailwind CSS et les composants Preline UI"
slug: "prototypage-ui-kit"
slug_domaine: "design"
slug_ua: "parcours-utilisateur-prototypage"
permalink: /tutos/prototypage-ui-kit/
tuto_id: "T.311.122"
version: "normal"
ua: "UA.311.12"
type: "tuto-atelier"
etape: 11
nav_order: 2
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
---

## 1. Contexte & Enjeux
Le prototypage rapide permet de valider l'ergonomie, la hiérarchie visuelle et la pertinence d'une interface avant d'écrire le code fonctionnel backend.

Pour garantir une expérience utilisateur cohérente et professionnelle, les équipes modernes s'appuient sur un **UI Kit** et un système de conception modulaire (*Design System*). Dans cet atelier, nous explorons la bibliothèque **Preline UI**, basée sur les classes utilitaires de **Tailwind CSS**.

## 2. Ce que vous devez apprendre
- Définir les fondements d'un UI Kit : palette de couleurs sémantiques, échelle typographique, espacements harmonisés et grille responsive.
- Explorer le catalogue de composants accessibles et responsive de **Preline UI** adaptés à une page d'accueil de blog :
  - Barre de navigation principale (*Navbar / Header*).
  - Zone d'accroche visuelle (*Hero Section*).
  - Carte d'article standardisée (*Card Article* avec miniature, badge de catégorie, titre, auteur et date).
  - Pied de page structuré (*Footer*).
- Assembler ces composants pour créer un prototype interactif fluide et validable auprès des utilisateurs.

## 3. Travail à faire
Spécifiez et assemblez l'UI Kit de composants d'interface (pour vos exemples et cas pratiques, adaptez l'UI Kit aux besoins de votre **Projet Technique individuel** ; la solution de référence du formateur consultable ci-dessous illustre le cas modèle **TodoList**) :
1. **Étape 1 — Définir la charte graphique de base :** Sélectionner une couleur primaire, une couleur secondaire, les teintes de texte et de fond en classes Tailwind CSS.
2. **Étape 2 — Sélectionner les composants Preline UI :** Choisir les gabarits HTML adaptés pour le Header, le Hero, la grille de cartes d'articles et le Footer.
3. **Étape 3 — Rédiger la spécification de l'UI Kit :** Documenter le rôle de chaque composant, ses classes Tailwind et son comportement adaptatif (desktop / mobile).
4. **Étape 4 — Rédiger la fiche et le diaporama :** Consigner la documentation dans `tutoriels/design/parcours-utilisateur-prototypage/prototypage-ui-kit/prototypage-ui-kit.md` et préparer le diaporama Marp dans `tutoriels/design/parcours-utilisateur-prototypage/prototypage-ui-kit/presentation-prototypage-ui-kit.md`.

## 4. Pistes de recherche active
- Quels sont les principes fondamentaux de l'approche *Atomic Design* (atomes, molécules, organismes, gabarits, pages) ?
- Pourquoi privilégier une bibliothèque de composants basée sur Tailwind CSS (comme Preline UI) plutôt qu'un framework CSS monolithique traditionnel ?
- Consultez la documentation officielle : [Documentation Tailwind CSS](https://tailwindcss.com/docs) et le catalogue de composants [Preline UI](https://preline.co/).

## 5. Livrables attendus & Critères de validation
- **Fiche technique d'atelier :** `tutoriels/design/parcours-utilisateur-prototypage/prototypage-ui-kit/prototypage-ui-kit.md`.
- **Diaporama Marp de restitution :** `tutoriels/design/parcours-utilisateur-prototypage/prototypage-ui-kit/presentation-prototypage-ui-kit.md`.
- **Critère de succès :** L'UI Kit documente clairement les 4 composants majeurs d'accueil avec leurs classes Tailwind CSS, leur disposition adaptative et les livrables sont versionnés sur la branche `sprint0`.
