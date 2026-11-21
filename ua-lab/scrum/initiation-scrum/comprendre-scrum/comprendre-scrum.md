---
layout: default
title: "Fiche d'Atelier : Comprendre l'approche Agile et Scrum (Cas d'étude TodoList)"
---
# Tutoriel 1 : Comprendre l'approche Agile et le cadre Scrum

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-comprendre-scrum.html](./presentation-comprendre-scrum.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Cas d'étude didactique** : Application TodoList (Gestionnaire de tâches)
- **Établissement** : EFP

---

## 1. Objectifs d'apprentissage

Ce premier atelier d'initiation permet d'acquérir les bases de l'Agilité et du cadre Scrum :
- Comprendre la rupture entre le cycle de développement traditionnel (en V ou cascade) et l'approche itérative Agile.
- Identifier les valeurs fondamentales de l'Agilité adaptées aux réalités du développement Web.
- Connaître les 3 rôles centraux de l'équipe Scrum et leurs responsabilités respectives.
- Maîtriser le principe des Sprints et de l'incrément de produit opérationnel.
- Mettre en application ces notions sur un cas d'école concret : l'application **TodoList** (gestionnaire de tâches).

---

## 2. Volet Théorique & Méthodologique

### 2.1 Cycle classique (en V) vs Démarche Agile
- **Le modèle en cascade traditionnel (Cycle en V) :**
  - Fonctionne par grandes étapes séquentielles figées : spécifications exhaustives, conception d'ensemble, développement complet, tests tardifs et livraison finale.
  - Risque majeur : l'**effet tunnel**. Le client et les utilisateurs découvrent le logiciel après plusieurs mois, avec un fort risque d'inadéquation au besoin réel ou d'évolution du contexte métier.
- **La démarche Agile :**
  - Privilégie une progression empirique, itérative et incrémentale.
  - Le produit est construit bloc par bloc à travers des cycles courts appelés **Sprints**.
  - Chaque cycle produit une version opérationnelle, testée et directement utilisable du produit.
  - Elle accepte et intègre le changement comme une opportunité d'amélioration continue.

### 2.2 Les 4 Valeurs du Manifeste Agile (2001)
1. **Les individus et leurs interactions** avant les processus et les outils.
2. **Un logiciel opérationnel** avant une documentation exhaustive.
3. **La collaboration avec les clients** avant la négociation contractuelle stricte.
4. **L'adaptation au changement** avant le suivi rigide d'un plan initial.

### 2.3 Les 3 Piliers du Cadre Scrum
Scrum repose sur le contrôle empirique de processus :
- **Transparence :** Les aspects significatifs du processus sont visibles par tous les membres de l'équipe et les parties prenantes.
- **Inspection :** Les artéfacts et l'avancement sont examinés fréquemment pour détecter les écarts éventuels.
- **Adaptation :** Dès qu'un écart dépasse les limites acceptables, le processus ou le produit est réajusté sans délai.

### 2.4 Les 3 Rôles de l'Équipe Scrum
- **Le Product Owner (PO) :**
  - Porte la vision produit et maximise la valeur métier délivrée par l'équipe.
  - Rédige les fonctionnalités sous forme de User Stories et ordonne les priorités dans le Product Backlog.
  - Valide les fonctionnalités développées à l'issue de chaque démonstration de sprint.
- **Le Scrum Master (SM) :**
  - Coach méthodologique et serviteur-leader de l'équipe.
  - Veille au respect des règles, des valeurs et des événements du cadre Scrum.
  - Élimine les obstacles techniques ou méthodologiques qui freinent les développeurs.
- **L'Équipe de Développement (Développeurs) :**
  - Groupe autonome et pluridisciplinaire responsable de la réalisation technique.
  - Détermine la façon de concevoir, coder et tester les fonctionnalités sélectionnées.
  - S'engage collectivement sur la qualité et la robustesse de l'incrément livré.

### 2.5 Les 5 Événements Fondamentaux
1. **Le Sprint :** La boîte de temps régulière (timebox) contenant tous les autres événements.
2. **Le Sprint Planning :** Réunion initiale définissant l'objectif du sprint (*Sprint Goal*) et les éléments engagés (*Sprint Backlog*).
3. **Le Daily Scrum :** Point synchronisé quotidien de 15 minutes pour évaluer l'avancement et identifier les blocages.
4. **La Sprint Review :** Démonstration interactive de l'incrément logiciel pour collecter les retours des utilisateurs.
5. **La Sprint Retrospective :** Analyse réflexive du fonctionnement de l'équipe pour décider de 2 à 3 actions d'amélioration concrètes.

---

## 3. Application Pratique : Cadrage de l'Application TodoList

Pour appréhender ces concepts sur un cas technique concret et accessible, nous appliquons Scrum au développement d'une application **TodoList** (gestionnaire de tâches réactif).

### 3.1 Pourquoi le cycle en V échoue sur une TodoList ?
- **Scénario classique en cascade :**
  - Rédiger un cahier des charges de 30 pages décrivant la gestion de sous-tâches imbriquées, le tri multi-critères, le partage collaboratif, le stockage cloud et les rappels sonores.
  - Après 3 mois de développement, le logiciel est livré mais se révèle trop complexe : les utilisateurs voulaient simplement une interface épurée sur smartphone pour cocher une tâche en 2 secondes.
- **Scénario itératif Agile :**
  - **Sprint 1 (MVP) :** Livrer immédiatement une page web épurée permettant de saisir une tâche, l'afficher dans une liste et la cocher comme terminée.
  - **Sprint 2 :** Dès les premiers retours des testeurs, ajouter le filtrage des tâches actives et la persistance locale dans le navigateur (*LocalStorage*).

### 3.2 Cartographie des 3 Rôles pour l'Équipe TodoList
- **Product Owner (PO) :**
  - Définit le persona cible (l'étudiant ou le professionnel actif ayant besoin de clarté mentale).
  - Établit la priorité absolue : rapidité de saisie et lisibilité sur petit écran.
  - Décide de repousser les options secondaires (catégories, thèmes graphiques) aux versions ultérieures.
- **Scrum Master (SM) :**
  - Met en place le tableau visuel Kanban (colonnes : *À faire, En cours, En test, Terminé*).
  - Facilite le découpage des tâches techniques et s'assure que le temps de travail reste fluide.
  - Résout immédiatement les blocages d'environnement ou d'intégration Git.
- **Développeurs :**
  - Conçoivent la structure sémantique HTML5 et la mise en page CSS responsive (ordinateur et mobile 375px).
  - Écrivent le code JavaScript modulaire pour gérer la manipulation du DOM et les événements utilisateurs.
  - Contrôlent l'absence totale d'erreurs dans la console navigateur.

### 3.3 Charte d'Engagement Agile de l'Équipe
1. **Transparence intégrale :** Tout le code est versionné quotidiennement sur GitHub sur la branche active du sprint.
2. **Focus sur le Sprint Goal :** L'équipe concentre son énergie sur l'objectif engagé sans disperser ses efforts sur des détails superflus.
3. **Qualité immédiate (Definition of Done) :** Une tâche n'est déclarée terminée que si elle est testée sur mobile et ordinateur, et validée sans warning console.
4. **Amélioration continue :** Chaque fin de sprint donne lieu à un bilan sincère des réussites et des axes de progrès techniques.

---

## 4. Auto-évaluation & Checklist

Vérifiez que vous maîtrisez les éléments de ce premier atelier :
- [ ] Vous savez expliquer pourquoi l'approche itérative réduit le risque d'effet tunnel par rapport au cycle en V.
- [ ] Vous citez les 4 valeurs du Manifeste Agile et les 3 piliers empiriques de Scrum.
- [ ] Vous distinguez avec précision les responsabilités respectives du Product Owner, du Scrum Master et des Développeurs.
- [ ] Vous savez justifier l'organisation d'un MVP et le découpage par Sprints sur le cas de la TodoList.
