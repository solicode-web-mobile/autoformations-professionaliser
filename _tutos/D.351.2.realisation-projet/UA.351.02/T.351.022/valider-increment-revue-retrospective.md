---
layout: tuto
title: "Valider l'Incrément Maquette (Sprint Review 0 Go/No-Go) & Rétrospective 0"
sous_titre: "Animer la démonstration contradictoire, prononcer l'arbitrage Go/No-Go et formaliser la rétrospective"
slug: "valider-increment-revue-retrospective"
slug_domaine: "realisation-projet"
slug_ua: "maquette-accueil-cloture-agile"
permalink: /tutos/valider-increment-revue-retrospective/
tuto_id: "T.351.022"
version: "normal"
ua: "UA.351.02"
type: "tuto-tache"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
livrables:
  - chemin: "sprints/pv-review-0.md"
    version: "0.1.0"
  - chemin: "sprints/retrospective-0.md"
    version: "0.1.0"
---

## 1. Travail à faire
Clôturez officiellement le Sprint 0 en animant les deux cérémonies majeures de fin de sprint :
1. **Étape 1 — Préparer la démonstration contradictoire :** Rassemblez l'ensemble des livrables de cadrage du Sprint 0 (note de cadrage, stack technique, vision produit, personas, backlog initial, UI Kit et maquette de la page d'accueil).
2. **Étape 2 — Animer la Sprint Review 0 :** Présentez la maquette interactive de la page d'accueil et les choix d'ingénierie devant le **Groupe 1** (Product Owner) et les parties prenantes. Recueillez leurs critiques, validations et retours d'ergonomie.
3. **Étape 3 — Prononcer la décision Go/No-Go :** Procédez à l'arbitrage formel :
   - Si les critères de la Definition of Done de cadrage sont respectés ➔ Décision **Go** autorisant le passage au Sprint 1 (Delivery applicatif).
   - En cas d'écart bloquant ➔ Décision **No-Go** avec liste des actions correctives impératives.
4. **Étape 4 — Rédiger le procès-verbal de revue :** Formalisez la décision et les retours dans `sprints/pv-review-0.md`.
5. **Étape 5 — Conduire la Rétrospective du Sprint 0 :** Réunissez l'équipe de développement seule avec le Scrum Master pour analyser le fonctionnement interne du Sprint 0 :
   - *Ce qui a bien fonctionné (forces, bonnes pratiques).*
   - *Ce qui a posé difficulté (frictions, incompréhensions, retards).*
   - *2 engagements fermes d'amélioration continue pour le Sprint 1.*
6. **Étape 6 — Rédiger le compte-rendu de rétrospective :** Formalisez le bilan dans `sprints/retrospective-0.md`.

## 2. Consignes de Réalisation
- Créez les fichiers de clôture de sprint :
  ```powershell
  echo "" > sprints/pv-review-0.md
  echo "" > sprints/retrospective-0.md
  ```
- Renseignez `sprints/pv-review-0.md` :
  - Date, participants, rôle de chacun.
  - Démonstration de la maquette de la page d'accueil et du parcours utilisateur.
  - Contrôle point par point des critères de la Definition of Done de cadrage.
  - Décision collégiale explicite : **Go** ou **No-Go**.
  - Signatures du Scrum Master et du Product Owner (Groupe 1).
- Renseignez `sprints/retrospective-0.md` :
  - Analyse réflexive de l'équipe (méthode Glad/Sad/Mad ou Keep/Drop/Start).
  - Identification des causes racines des difficultés rencontrées.
  - Deux engagements d'équipe actionnables et mesurables pour sécuriser le Sprint 1.

## 3. Livrables attendus
- **Fichiers de projet :** `sprints/pv-review-0.md` et `sprints/retrospective-0.md`.
- **Critère de conformité :** La décision Go/No-Go est formellement actée et les 2 engagements de la rétrospective sont contractualisés.
