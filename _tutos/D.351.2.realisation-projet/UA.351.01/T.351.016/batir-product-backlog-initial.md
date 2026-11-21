---
layout: tuto
title: "Bâtir le Product Backlog initial et Personas du Blog"
sous_titre: "Formaliser les Personas cibles du Blog et ordonner les User Stories INVEST selon MoSCoW"
slug: "batir-product-backlog-initial"
slug_domaine: "realisation-projet"
slug_ua: "depot-cadrage-stack-backlog"
permalink: /tutos/batir-product-backlog-initial/
tuto_id: "T.351.016"
version: "normal"
ua: "UA.351.01"
type: "tuto-tache"
nav_order: 6
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
livrables:
  - chemin: "docs/analyse/personas.md"
    version: "0.1.0"
  - chemin: "scrum/product-backlog.md"
    version: "0.1.0"
---

## 1. Travail à faire
Bâtissez le socle fonctionnel du *Blog des Lauréats* avec l'appui méthodologique du **Groupe 2 (Design)** pour les personas et du **Groupe 1 (Product Owner)** pour le backlog :
1. **Étape 1 — Formaliser les Personas du Blog :** À partir des constats d'empathie, créez les fiches de 3 profils types dans `docs/analyse/personas.md` :
   - *Amine (22 ans), apprenant actuel en quête de repères techniques et d'inspiration.*
   - *Sara (26 ans), lauréate en poste souhaitant valoriser son parcours et partager ses conseils.*
   - *Karim (35 ans), formateur/responsable pédagogique veillant à la qualité et modérant les publications.*
2. **Étape 2 — Exprimer les besoins en User Stories :** Rédigez les User Stories initiales selon le format INVEST (*En tant que... je veux... afin de...*).
3. **Étape 3 — Rédiger les critères d'acceptation :** Définissez pour chaque User Story des conditions de test précises et univoques.
4. **Étape 4 — Ordonner selon MoSCoW :** En concertation avec le Product Owner, classez les histoires en *Must have* (indispensables au MVP), *Should have* (importantes mais non bloquantes), *Could have* (confort) et *Won't have* (exclues du MVP).
5. **Étape 5 — Rédiger le carnet d'exigences :** Enregistrez le Product Backlog initial ordonné dans `scrum/product-backlog.md`.

## 2. Consignes de Réalisation
- Créez les répertoires et les fichiers :
  ```powershell
  mkdir docs/analyse, scrum
  echo "" > docs/analyse/personas.md
  echo "" > scrum/product-backlog.md
  ```
- Renseignez `docs/analyse/personas.md` avec les 3 fiches détaillées (portrait, objectifs, freins, citation).
- Renseignez `scrum/product-backlog.md` sous forme de tableau Markdown normalisé :
  | ID | Titre de la User Story | Description Sémantique | Priorité MoSCoW | Estimation (SP) | Critères d'Acceptation |
  | :---: | :--- | :--- | :---: | :---: | :--- |
  | US01 | Consultation page d'accueil | En tant que visiteur, je veux voir les derniers articles publiés... | Must | 5 | Grille responsive, tri chronologique |
  | US02 | Consultation article détaillé | En tant que lecteur, je veux lire le retour d'expérience complet... | Must | 5 | Titre, auteur, date, contenu formaté |
  | US03 | Filtrage par catégorie | En tant que lecteur, je veux filtrer les articles par domaine... | Should | 3 | Boutons catégories actifs |
  | US04 | Authentification auteur | En tant que lauréat, je veux me connecter à mon espace... | Must | 8 | Login sécurisé, redirection tableau de bord |

## 3. Livrables attendus
- **Fichiers de projet :** `docs/analyse/personas.md` et `scrum/product-backlog.md`.
- **Critère de conformité :** Les 3 Personas sont cohérents et le Product Backlog initial est ordonné selon MoSCoW et validé par le Product Owner.
