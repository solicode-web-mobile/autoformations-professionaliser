---
layout: default
title: "Fiche d'Atelier : T.351.115 — Sprint Review et Rétrospective (Cas TodoList)"
tuto_id: "T.351.115"
type: "tuto-notion"
ua: "UA.351.11"
slug: "revue-retrospective"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
nav_exclude: true
---
# T.351.115 : Valider l'incrément, animer la Sprint Review et la Rétrospective

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-revue-retrospective.html](./presentation-revue-retrospective.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Cas d'étude didactique** : Application TodoList (Gestionnaire de tâches)

---

## 1. Contexte & Objectif de l'Atelier
Cet atelier traite de la conclusion formelle du Sprint Scrum à travers ses deux cérémonies d'inspection et d'adaptation : la **Sprint Review**, dédiée à la validation de la valeur du produit devant les parties prenantes, et la **Sprint Retrospective**, dédiée à l'analyse critique et constructive du fonctionnement de l'équipe. L'objectif est d'apprendre à animer une démonstration en direct, à intégrer des retours d'utilisateurs et à concevoir un plan d'actions d'amélioration continue pour le cycle suivant sur le cas de l'application TodoList.

## 2. Données de Référence
- **Projet support** : Application TodoList (gestionnaire de tâches responsive).
- **Ressources associées** : Support de présentation Marp (`presentation-revue-retrospective.md`).
- **Périmètre cible** : Clôture du Sprint 1 (Incrément MVP), revue de la Definition of Done et plan d'amélioration pour le Sprint 2.

## 3. Notions Essentielles

### 3.1 La Sprint Review : L'inspection du produit en direct
La **Sprint Review** a lieu au dernier jour du sprint. Elle réunit le Product Owner, l'équipe de développement, le Scrum Master et les parties prenantes (utilisateurs, formateur, clients).

Dans Scrum, la Sprint Review répond à une règle d'or non négociable : **aucune présentation PowerPoint abstraite, mais une démonstration en direct d'un logiciel réellement fonctionnel**.
- L'équipe manipule le produit sous les yeux des utilisateurs.
- On vérifie que chaque fonctionnalité démontrée satisfait à 100% à la **Definition of Done (DoD)**.
- Le Product Owner valide ou refuse formellement chaque User Story présentée.

Ce rituel n'est pas un tribunal ni une évaluation punitive : c'est un atelier collaboratif d'échange où l'on découvre comment les utilisateurs réagissent devant le logiciel pour décider ensemble de la suite.

### 3.2 Le Recueil de Feedbacks et la Réorientation du Backlog
L'intérêt majeur d'une livraison courte réside dans le feedback direct. Face à l'écran, les utilisateurs émettent des remarques spontanées (*« Le texte est un peu petit sur smartphone »*, *« J'aimerais pouvoir cacher les tâches terminées sans les effacer »*).

Le Product Owner recueille ces retours et les traduit immédiatement en ajustements dans le Product Backlog :
- Création de nouvelles User Stories.
- Réordonnancement des priorités pour le sprint suivant.
- Clarification ou durcissement de certains critères d'acceptation.

### 3.3 La Sprint Retrospective : L'inspection du collectif de travail
Juste après la revue du produit, l'équipe se réunit seule avec le Scrum Master pour la **Sprint Retrospective**.

Tandis que la Revue inspecte le **produit**, la Rétrospective inspecte **l'équipe et ses méthodes de travail** : la communication interne, les outils techniques, la fluidité du tableau Kanban et l'ambiance générale.

Pour qu'une rétrospective porte ses fruits, le Scrum Master instaure un climat de **sécurité psychologique** basé sur la Directive Première de la Rétrospective (Norman Kerth) :
> *"Quelles que soient les erreurs commises, nous comprenons et croyons sincèrement que chacun a fait de son mieux, compte tenu de ce qu'il savait, de ses compétences et des ressources disponibles à ce moment-là."*

L'équipe analyse son travail autour de 3 axes fondamentaux :
1. **Ce qui a bien fonctionné :** Les succès, bonnes pratiques et automatismes à préserver.
2. **Ce qui a posé des difficultés :** Les ralentissements, incompréhensions ou bugs techniques rencontrés.
3. **Ce que nous voulons améliorer :** Les actions concrètes à mettre en œuvre dès demain.

### 3.4 Le Plan d'Actions d'Amélioration : Limiter pour réussir
Une erreur courante consiste à lister 15 bonnes résolutions vagues que personne n'appliquera. 

La règle d'or de l'amélioration continue consiste à choisir **2 à 3 actions correctives concrètes et mesurables au maximum**. Ces actions sont alors inscrites directement dans le Sprint Backlog du sprint suivant comme des tâches prioritaires.

---

## 4. Pratique & Réalisation Guidée (Cas d'école TodoList)

Voici le déroulé complet de la clôture du **Sprint 1** de l'application **TodoList** :

| Étape | Action d'ingénierie agile | Décision prise sur la TodoList | Résultat opérationnel |
| :-: | :--- | :--- | :--- |
| 1 | Animer la Sprint Review en direct | Démonstration live de la saisie, de l'affichage et du cochage de 3 tâches réelles | Validation officielle des stories US-01, US-02 et US-03 par le Product Owner |
| 2 | Contrôler la Definition of Done | Contrôle visuel 375px mobile, console d'inspection 0 erreur, code sémantique | 100% des critères DoD validés |
| 3 | Collecter les feedbacks utilisateurs | Remarque d'un utilisateur sur le besoin d'isoler les tâches actives | US-04 (Filtrage) avancée en priorité numéro 1 pour le Sprint 2 |
| 4 | Conduire la Sprint Retrospective | Bilan transparent : réussite du découpage court, mais test responsive trop tardif | Vote de 3 actions concrètes pour le Sprint 2 |

### 4.1 Déroulement de la Démonstration Live (Sprint Review)
1. **Scénario d'usage :** Devant les utilisateurs, le développeur ouvre l'application dans le navigateur et saisit 3 tâches : *« Acheter du pain »*, *« Réviser cours Scrum »*, *« Finaliser CSS responsive »*. Chaque saisie est validée par la touche Entrée. Les éléments s'insèrent immédiatement dans la liste et le compteur affiche *« 3 tâches restantes »*.
2. **Scénario de cochage :** Le développeur clique sur la case de la deuxième tâche (*« Réviser cours Scrum »*). Le texte se barre instantanément, sa couleur s'atténue et le compteur s'ajuste à *« 2 tâches restantes »*.
3. **Contrôle de conformité DoD :**
   - Bascule en mode simulation mobile (375 x 667 px) : la mise en page s'adapte sans ascenseur horizontal.
   - Ouverture des DevTools : l'onglet Console affiche un journal 100% propre (zéro warning, zéro message d'erreur rouge).
   - **Verdict du PO :** Les 3 User Stories sont formellement acceptées. Le Sprint Goal du Sprint 1 est pleinement atteint.

### 4.2 Feedbacks Utilisateurs & Arbitrage Backlog pour le Sprint 2
- **Feedback 1 (Besoin ergonomique) :** L'utilisateur constate que lorsque la liste grandit, les tâches terminées encombrent visuellement l'espace. Il demande de pouvoir masquer les tâches faites.
  - *Décision PO :* La story **US-04 (Filtrage 3 vues)** est immédiatement placée en première position du Sprint 2.
- **Feedback 2 (Accessibilité tactile) :** Sur smartphone, le bouton d'ajout est jugé un peu étroit pour les gros pouces.
  - *Décision PO :* Une micro-tâche d'agrandissement de la zone tactile (taille minimale de 44x44px) est ajoutée à la dette CSS pour le Sprint 2.

### 4.3 Rétrospective d'Équipe du Sprint 1 (Bilan Réflexif)

#### Ce qui a bien fonctionné (À conserver) :
- Le découpage en micro-tâches courtes (1h à 2h30) a permis une visibilité parfaite de l'avancement chaque matin.
- La communication lors du Daily Scrum : le bug de soumission du formulaire a été identifié et débloqué en 10 minutes grâce à l'intervention du Scrum Master.
- La clarté de la Definition of Done a évité les débats subjectifs sur la qualité du code.

#### Ce qui a posé des difficultés (Axes de progrès) :
- Les tests d'adaptation mobile n'ont été exécutés qu'à la fin du sprint sur la tâche T-09, ce qui a imposé des retouches CSS de dernière minute sous pression.
- L'oubli initial du rafraîchissement formulaire (`e.preventDefault()`) aurait pu être anticipé par une réflexion préalable sur le comportement des événements DOM.

#### Les 3 Actions d'Amélioration Concrètes pour le Sprint 2 :
1. **Action 1 [Organisationnelle] :** Vérifier l'affichage responsive (vue mobile 375px) dans les DevTools dès la fin de chaque sous-tâche CSS, sans attendre l'étape finale de test.
2. **Action 2 [Technique] :** Écrire la signature des fonctions d'événements et documenter les interactions DOM avant d'écrire le code fonctionnel.
3. **Action 3 [Priorisation] :** Préparer la persistance LocalStorage (US-06) pour le Sprint 3 afin de garantir la sauvegarde des données entre deux sessions.

---

## 5. Livrables de Référence Produits & Critères

- **Fiche technique d'atelier** : `ua-lab/scrum/initiation-scrum/revue-retrospective/revue-retrospective.md`
- **Diaporama Marp de restitution** : `ua-lab/scrum/initiation-scrum/revue-retrospective/presentation-revue-retrospective.md`
- **Critères de réussite validés** :
  - [x] Démonstration en direct de l'incrément opérationnel avec validation stricte de la DoD.
  - [x] Collecte et traçabilité des feedbacks utilisateurs traduits dans le Product Backlog.
  - [x] Bilan réflexif de la rétrospective conduit avec franchise et bienveillance.
  - [x] 3 actions concrètes et mesurables adoptées pour l'amélioration du Sprint 2.
  - [x] Fichiers en UTF-8 sans BOM et conformes à l'ensemble des règles du projet.

## 6. Glossaire Pédagogique
- **Sprint Review :** Cérémonie d'inspection du produit en direct réunissant l'équipe et les parties prenantes pour valider l'incrément réalisé.
- **Incrément Opérationnel :** Version concrète, testée et immédiatement utilisable du logiciel répondant à la Definition of Done.
- **Feedback :** Retour d'expérience formulé par les utilisateurs permettant d'adapter la trajectoire du produit.
- **Sprint Retrospective :** Cérémonie interne d'inspection de l'équipe dédiée à l'amélioration continue de ses méthodes et de sa communication.
- **Sécurité Psychologique :** Climat de confiance au sein d'une équipe où chacun peut exprimer ses doutes, difficultés et erreurs sans crainte de jugement.
- **Plan d'Actions d'Amélioration :** Sélection restreinte de 2 à 3 mesures correctives concrètes intégrées en priorité dans le prochain sprint.
