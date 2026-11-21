---
layout: default
title: "Fiche d'Atelier : T.351.113 — Estimation et Product Backlog (Cas TodoList)"
tuto_id: "T.351.113"
type: "tuto-notion"
ua: "UA.351.11"
slug: "product-backlog"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
nav_exclude: true
---
# T.351.113 : Créer, estimer et ordonner le Product Backlog

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-product-backlog.html](./presentation-product-backlog.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Cas d'étude didactique** : Application TodoList (Gestionnaire de tâches)

---

## 1. Contexte & Objectif de l'Atelier
Cet atelier traite de la structuration quantitative et qualitative du carnet de produit (*Product Backlog*). L'objectif est d'assimiler l'estimation relative de l'effort par les Story Points (suite de Fibonacci), de prioriser rationnellement les exigences grâce à la méthode MoSCoW et d'instaurer des garde-fous qualité avec la Definition of Ready (DoR) et la Definition of Done (DoD) sur le cas de l'application TodoList.

## 2. Données de Référence
- **Projet support** : Application TodoList (gestionnaire de tâches responsive).
- **Ressources associées** : Support de présentation Marp (`presentation-product-backlog.md`).
- **Périmètre cible** : Estimation des 5 User Stories initiales + 2 évolutions, sélection MoSCoW et contractualisation DoR/DoD.

## 3. Notions Essentielles

### 3.1 Qu'est-ce que le Product Backlog ?
Le **Product Backlog** est la source unique et vivante de toutes les exigences d'un produit logiciel. Ce n'est pas un document statique figé au début du projet, mais une liste dynamique ordonnée par le Product Owner.

Au fur et à mesure que le projet avance, de nouvelles idées apparaissent, certaines priorités changent suite aux retours utilisateurs et des fonctionnalités superflues sont éliminées. Le haut du backlog regroupe les éléments les plus urgents, les mieux décrits et estimés avec précision, tandis que le bas contient des besoins plus généraux qui seront affinés plus tard.

### 3.2 L'Estimation Relative par Story Points : Pourquoi bannir les heures ?
Les humains sont notoirement médiocres pour estimer une tâche en heures absolues (*« Est-ce que ce formulaire prendra 4h30 ou 6h15 ? »*). En revanche, nous sommes excellents pour comparer deux choses entre elles (*« Ce formulaire est deux fois plus complexe à coder que cette page statique »*).

Le **Story Point** est une unité de mesure abstraite et relative. Il ne mesure pas du temps, mais combine trois dimensions indissociables :
1. **La quantité de travail :** Combien de code, de structure et de styles faut-il produire ?
2. **La complexité technique :** Y a-t-il des algorithmes délicats, des manipulations de DOM imbriquées ou des calculs d'états ?
3. **L'incertitude et le risque :** Maîtrisons-nous la technologie, ou devrons-nous faire des recherches préalables ?

### 3.3 La Suite de Fibonacci et le Planning Poker
Pour éviter les débats stériles (*« Est-ce du 4 ou du 5 ? »*), Scrum utilise l'échelle non linéaire de la suite de Fibonacci adaptée : **1, 2, 3, 5, 8, 13**.
- **1 point :** Tâche triviale, immédiate (modifier un titre, corriger un lien).
- **2 points :** Tâche très simple, répétitive et sans surprise (ajouter un paragraphe, styliser un bouton).
- **3 points :** Tâche standard bien maîtrisée (créer un formulaire basique avec un champ).
- **5 points :** Tâche de complexité moyenne comportant de la logique dynamique (manipulation d'événements, filtrage de tableau).
- **8 points :** Tâche complexe avec plusieurs dépendances techniques.
- **13 points et plus :** Tâche trop volumineuse (un « Epic ») qu'il faut obligatoirement découper en plusieurs stories indépendantes.

La progression exponentielle de Fibonacci reflète une loi naturelle de l'ingénierie : **plus un travail est grand, plus l'incertitude grandit**.

Lors de l'atelier de **Planning Poker**, toute l'équipe de développement vote simultanément avec des cartes pour éviter le biais d'autorité (l'avis du plus bavard ou du plus ancien). En cas d'écart (ex: un vote à 2 et un vote à 8), les extrêmes s'expliquent et l'équipe converge rapidement.

### 3.4 La Méthode de Priorisation MoSCoW
La méthode MoSCoW classe les exigences en 4 catégories rigoureuses :
- **M — Must Have (Indispensable) :** Sans ces fonctionnalités, le produit est inutilisable. C'est le cœur absolu du MVP.
- **S — Should Have (Important) :** Fonctionnalités à forte valeur ajoutée, mais le produit reste exploitable sans elles pour une première livraison.
- **C — Could Have (Souhaitable) :** Améliorations de confort ou de design réalisées s'il reste du temps et de la bande passante.
- **W — Won't Have this time (Reporté) :** Fonctionnalités reconnues comme utiles mais explicitement exclues du sprint en cours.

### 3.5 La Definition of Ready (DoR) : Le filtre d'entrée
La **Definition of Ready** est le contrat garantissant qu'une User Story est suffisamment mûre pour être embarquée dans un sprint de développement. Elle évite aux développeurs de commencer à coder sur des besoins flous. Une story est « Ready » si :
- Son intitulé suit la syntaxe standard (*En tant que...*).
- Ses critères d'acceptation sont clairs et non ambigus.
- Elle a été estimée en Story Points par l'équipe.
- Elle ne dépend d'aucun blocage technique externe non résolu.

### 3.6 La Definition of Done (DoD) : Le filtre de sortie
La **Definition of Done** est la grille d'exigence qualité non négociable indispensable pour déclarer une tâche terminée. Elle empêche de livrer du code bâclé ou instable. Si une story ne respecte pas l'un des critères de la DoD, elle **n'est pas terminée** et ne peut pas être présentée en revue.

---

## 4. Pratique & Réalisation Guidée (Cas d'école TodoList)

Pour donner du sens à ces méthodes, voici le travail d'estimation et d'ordonnancement réalisé sur l'application **TodoList** :

| Étape | Action d'ingénierie agile | Décision prise sur la TodoList | Résultat opérationnel |
| :-: | :--- | :--- | :--- |
| 1 | Estimer l'effort relatif | Utilisation de l'échelle Fibonacci (2, 3, 5 pts) | Chiffrage transparent et consensuel des 5 stories initiales |
| 2 | Appliquer la méthode MoSCoW | Isoler le MVP indispensable pour le Sprint 1 | 3 stories Must Have (8 points au total) engagées |
| 3 | Formaliser la Definition of Ready | Définir 4 conditions d'entrée strictes | Aucune story ambigüe n'entre dans le sprint |
| 4 | Formaliser la Definition of Done | Établir 5 critères d'exigence qualité | Standards stricts : responsive, console 0 erreur, code propre |

### 4.1 Product Backlog Ordonné et Chiffré de la TodoList

| Réf | Fonctionnalité | Rôle & Action | Estimation | Priorité MoSCoW | Cible |
| :-: | :--- | :--- | :-: | :-: | :-: |
| **US-02** | Affichage & Compteur | Visualiser la liste et le nombre de tâches restantes | **2 pts** | **Must Have** | Sprint 1 |
| **US-01** | Ajout de tâche | Saisir et valider une nouvelle tâche via formulaire | **3 pts** | **Must Have** | Sprint 1 |
| **US-03** | Validation & Cochage | Cocher une tâche pour la marquer accomplie | **3 pts** | **Must Have** | Sprint 1 |
| **US-04** | Filtrage 3 vues | Filtrer entre Toutes, En cours et Terminées | **5 pts** | **Should Have** | Sprint 2 |
| **US-05** | Suppression & Purge | Effacer une tâche unitaire ou vider les cochées | **3 pts** | **Should Have** | Sprint 2 |
| **US-06** | Sauvegarde locale | Persister les tâches dans le LocalStorage | **5 pts** | **Could Have** | Sprint 3 |
| **US-07** | Thème sombre | Basculer l'affichage en mode nuit (Dark Mode) | **2 pts** | **Could Have** | Sprint 3 |

> **Bilan de charge engagée pour le Sprint 1 :** 8 Story Points (US-02 + US-01 + US-03). Ce périmètre représente le cœur opérationnel indispensable du produit.

### 4.2 Definition of Ready (DoR) adoptée pour la TodoList
Une User Story ne peut entrer dans le Sprint Planning que si elle remplit 100% des critères suivants :
1. L'énoncé est rédigé selon le gabarit *En tant que... je veux... afin de...*.
2. Au moins 2 critères d'acceptation concrets sont rédigés et validés par le PO.
3. La complexité a été estimée en Story Points par les développeurs (Fibonacci).
4. La maquette ou le gabarit visuel associé est disponible et compris.

### 4.3 Definition of Done (DoD) adoptée pour la TodoList
Une tâche ou User Story n'est déclarée « Terminée » (*Done*) que si elle valide l'ensemble des critères suivants :
1. **Conformité HTML/CSS :** Balisage HTML5 sémantique, structure CSS propre et responsive validée sur écran mobile (largeur 375px) sans débordement horizontal.
2. **Qualité JavaScript :** Aucun message d'erreur ni d'avertissement dans la console du navigateur.
3. **Tests fonctionnels :** Tous les critères d'acceptation de la story ont été testés et validés manuellement.
4. **Lisibilité du code :** Indentation rigoureuse, noms de variables explicites et suppression de tout code mort ou `console.log` de débogage.
5. **Gestion de version :** Code versionné proprement sur la branche active du sprint (`sprint1`) avec message conventionnel clair.

---

## 5. Livrables de Référence Produits & Critères

- **Fiche technique d'atelier** : `ua-lab/scrum/initiation-scrum/product-backlog/product-backlog.md`
- **Diaporama Marp de restitution** : `ua-lab/scrum/initiation-scrum/product-backlog/presentation-product-backlog.md`
- **Critères de réussite validés** :
  - [x] Product Backlog chiffré sur l'échelle de Fibonacci (Story Points relatifs).
  - [x] Priorisation MoSCoW argumentée avec périmètre Sprint 1 calibré à 8 points.
  - [x] Grille DoR formalisée avec critères de maturité d'entrée.
  - [x] Grille DoD formalisée avec critères qualité non négociables.
  - [x] Fichiers UTF-8 sans BOM et conformes aux directives du projet.

## 6. Glossaire Pédagogique
- **Product Backlog :** Carnet d'exigences priorisé et dynamique représentant l'ensemble des fonctionnalités attendues sur le produit.
- **Story Point :** Unité d'estimation relative combinant effort, complexité technique et incertitude.
- **Suite de Fibonacci :** Série mathématique (1, 2, 3, 5, 8...) utilisée en agilité pour modéliser l'incertitude croissante avec la taille des tâches.
- **MoSCoW :** Cadre de priorisation classant les besoins en Must Have, Should Have, Could Have et Won't Have.
- **DoR (Definition of Ready) :** Conditions préalables qu'une story doit remplir pour être sélectionnée en sprint.
- **DoD (Definition of Done) :** Exigences de qualité et de tests indispensables pour déclarer un incrément officiellement terminé.
