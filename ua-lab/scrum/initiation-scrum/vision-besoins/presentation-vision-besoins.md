---
layout: presentation
title: "Présentation : T.351.112 — Vision Produit et User Stories (Cas TodoList)"
marp: true
theme: default
paginate: true
header: "T.351.112 : Vision Produit et User Stories"
footer: "Scrum & Ingénierie Agile"
nav_exclude: true
---

<!-- _class: lead -->
# T.351.112 : Définir la vision produit et exprimer les besoins en User Stories
### Cas d'étude didactique : Application TodoList
**Unité d'Apprentissage : UA.351.11 — Initiation Scrum**

- **Public** : Développeurs Web (Niveau N3)
- **Domaine** : Scrum & Ingénierie Agile (`D.351.1`)
- **Compétence** : `C.351` — Piloter et animer la démarche Scrum

---

## 1. La Vision Produit : La boussole du projet

> *"Pour les étudiants et professionnels submergés par leurs tâches, l'application **TodoList** est un gestionnaire personnel en ligne, fluide et responsive, qui permet de capturer, visualiser et valider ses tâches en un instant, sans inscription ni configuration."*

- **Pourquoi une vision produit ?**
  - Fédère toute l'équipe autour d'une ambition commune.
  - Évite la dispersion et la « dérive des objectifs » (*scope creep*).
  - Sert de critère d'arbitrage pour refuser les fonctionnalités superflues.

---

## 2. Les Personas cibles de la TodoList

- **Yassine (21 ans, Étudiant en déplacement) :**
  - **Usage :** 100% Smartphone en mobilité (entre deux cours, transports).
  - **Objectif :** Noter une tâche en 3 secondes et cocher d'un geste du pouce.
  - **Attente clé :** Boutons tactiles larges, saisie immédiate par la touche Entrée.

- **Nadia (28 ans, Coordinatrice de projet) :**
  - **Usage :** Ordinateur de bureau multi-écrans.
  - **Objectif :** Vue d'ensemble claire, filtrage des tâches terminées et compteur dynamique.
  - **Attente clé :** Interface aérée, aucun rechargement de page.

---

## 3. Le Gabarit d'une User Story & Critères d'Acceptation

### Structure canonique :
- **En tant que** [rôle de l'utilisateur]
- **Je veux** [action ou fonctionnalité souhaitée]
- **Afin de** [bénéfice tangible ou valeur métier]

### Les Critères d'Acceptation :
- Fixent le contrat de succès clair entre le Product Owner et les Développeurs.
- Rédigés sous forme de scénarios testables et vérifiables.
- Servent de guide pour les tests fonctionnels avant la livraison.

---

## 4. Les 5 User Stories du Backlog TodoList

1. **US-01 (Ajout rapide) :** En tant qu'utilisateur, je veux saisir et valider une tâche par bouton ou touche Entrée.
2. **US-02 (Affichage & Compteur) :** En tant qu'utilisateur, je veux visualiser ma liste et le décompte des tâches en cours.
3. **US-03 (Cochage & Achèvement) :** En tant qu'utilisateur, je veux cocher une tâche pour la marquer barrée.
4. **US-04 (Filtrage 3 vues) :** En tant qu'utilisateur, je veux basculer entre Toutes / En cours / Terminées.
5. **US-05 (Suppression & Purge) :** En tant qu'utilisateur, je veux effacer une tâche ou nettoyer la liste.

---

## 5. Périmètre MVP vs Évolutions reportées

- **Cœur du MVP (Sprint 1) :**
  - US-01 (Ajout via formulaire avec focus).
  - US-02 (Affichage dynamique de la liste et compteur).
  - US-03 (Cochage interactif avec style barré).

- **Incrément du Sprint 2 :**
  - US-04 (Boutons de filtre Toutes / En cours / Terminées).
  - US-05 (Bouton de suppression unitaire et purge globale).

- **Reporté post-MVP :** LocalStorage, Dark Mode, rappels horaires.

---

<!-- _class: lead -->
# Conclusion de l'Atelier T.351.112
### Prêt pour l'estimation du Backlog

- La vision et les User Stories définissent avec précision **CE QU'IL FAUT CONSTRUIRE**.
- **Prochaine étape (T.351.113) :** Créer, estimer et ordonner le Product Backlog avec les Story Points et la méthode MoSCoW.
