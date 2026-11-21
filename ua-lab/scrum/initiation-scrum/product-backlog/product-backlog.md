---
layout: default
title: "Fiche d'Atelier : Créer, estimer et ordonner le Product Backlog"
---
# Tutoriel 3 : Créer, estimer et ordonner le Product Backlog

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-product-backlog.html](./presentation-product-backlog.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Encadrant** : ESSARRAJ Fouad | EFP

---

## 1. Objectifs d'apprentissage

Ce troisième tutoriel permet d'apprendre à structurer, chiffrer et ordonner les fonctionnalités d'un projet web :
- Comprendre la nature vivante et évolutive du Product Backlog.
- Savoir estimer la complexité d'une User Story en utilisant l'estimation relative (Story Points).
- Appliquer la méthode de priorisation MoSCoW pour distinguer l'indispensable du secondaire.
- Définir les critères de la *Definition of Ready* (DoR) pour démarrer le code sereinement.
- Établir une *Definition of Done* (DoD) rigoureuse pour garantir la qualité technique du produit.
- Mettre en pratique ces concepts sur le Product Backlog de votre **Blog des Lauréats**.

---

## 2. Volet Théorique : Backlog, Estimations et Qualité

### 2.1 Qu'est-ce que le Product Backlog ?
- Le Product Backlog est la liste ordonnée et dynamique de tout ce qui pourrait être nécessaire au produit.
- C'est la source unique des besoins pour l'équipe de développement.
- Il n'est jamais figé : le Product Owner l'ajuste en continu selon les retours des utilisateurs et les apprentissages techniques de l'équipe.
- Les éléments les plus prioritaires se trouvent en haut de la liste, décrits avec précision. Les éléments plus lointains restent plus généraux.

### 2.2 L'estimation relative par les Story Points
- En démarche Agile, on n'estime pas en heures fermes, mais en **Story Points** (points d'effort relatif).
- Un Story Point mesure à la fois : la quantité de travail, la complexité technique et le niveau d'incertitude.
- L'équipe utilise généralement une échelle inspirée de la suite de Fibonacci simplifiée : **1, 2, 3, 5, 8, 13**.
  - 1 point : Tâche triviale, rapide et sans risque (ex : modifier un texte ou un lien).
  - 2 à 3 points : Fonctionnalité simple et bien maîtrisée (ex : intégrer une section statique).
  - 5 points : Fonctionnalité de taille moyenne avec de la logique (ex : formulaire avec validation).
  - 8 à 13 points : Fonctionnalité complexe nécessitant souvent d'être découpée en stories plus petites.

### 2.3 La priorisation par la méthode MoSCoW
La méthode MoSCoW classe chaque besoin selon 4 niveaux d'exigence :
- **M — Must have (Indispensable)** : Fonctionnalités vitales sans lesquelles le produit n'a aucune valeur ou ne peut pas être livré (le cœur du MVP).
- **S — Should have (Important)** : Fonctionnalités apportant une forte valeur ajoutée mais non bloquantes pour la première livraison.
- **C — Could have (Souhaitable)** : Fonctionnalités de confort, à réaliser uniquement s'il reste du temps.
- **W — Won't have this time (Reporté)** : Fonctionnalités écartées pour cette itération, conservées pour les versions ultérieures.

### 2.4 La Définition de Prêt (Definition of Ready - DoR)
Une User Story est considérée comme "prête" (Ready) à être prise en compte dans un Sprint lorsque :
- Son énoncé est clair et compréhensible par tous.
- Ses critères d'acceptation sont rédigés et sans ambiguïté.
- Elle a été estimée en Story Points par l'équipe.
- Elle ne dépend pas d'un élément externe non résolu.

### 2.5 La Définition de Fini (Definition of Done - DoD)
La Definition of Done est le contrat qualité partagé par toute l'équipe :
- Elle définit la liste des critères indispensables pour déclarer une fonctionnalité officiellement terminée.
- Si un seul critère de la DoD n'est pas rempli, la story ne peut pas être considérée comme achevée ni présentée en revue.

---

## 3. Application Pratique : Le Product Backlog du Portfolio

### 3.1 Constitution du Product Backlog initial
Voici le Product Backlog de votre projet technique de Portfolio, classé par ordre de priorité avec ses estimations relatives :

- **Élément 1 (Priorité 1) — US-01 : Présentation personnelle et en-tête**
  - Estimation : **2 Story Points**
  - Justification : Balisage HTML sémantique, photo profil, titre et mise en page CSS simple.
  - Classification MoSCoW : **Must have**.

- **Élément 2 (Priorité 2) — US-03 : Section Compétences techniques (Stack)**
  - Estimation : **3 Story Points**
  - Justification : Organisation en cartes (Front-End, Back-End, Outils), style visuel des badges, grille responsive.
  - Classification MoSCoW : **Must have**.

- **Élément 3 (Priorité 3) — US-02 : Vitrine des réalisations (Projets phares)**
  - Estimation : **5 Story Points**
  - Justification : Création de la galerie, cartes de projets interactives, boutons démo et GitHub, intégration d'images optimisées.
  - Classification MoSCoW : **Must have**.

- **Élément 4 (Priorité 4) — US-04 : Formulaire de contact fonctionnel**
  - Estimation : **5 Story Points**
  - Justification : Mise en place des champs, contrôles de saisie (HTML5/JS), message de confirmation visuel.
  - Classification MoSCoW : **Must have**.

- **Élément 5 (Priorité 5) — US-05 : Bouton Téléchargement du CV (PDF)**
  - Estimation : **1 Story Point**
  - Justification : Ajout d'un bouton stylisé déclenchant le téléchargement du fichier PDF placé dans les assets.
  - Classification MoSCoW : **Must have**.

- **Élément 6 (Priorité 6) — US-06 : Bascule du mode sombre (Dark mode)**
  - Estimation : **5 Story Points**
  - Justification : Gestion des variables CSS et mémorisation du choix en localStorage.
  - Classification MoSCoW : **Could have** (hors MVP).

- **Élément 7 (Priorité 7) — US-07 : Section Blog / Articles récents**
  - Estimation : **8 Story Points**
  - Justification : Structure d'articles, pagination, intégration Markdown.
  - Classification MoSCoW : **Won't have this time** (reporté).

### 3.2 Total du périmètre MVP (Must have)
- Somme des points des stories indispensables (US-01 à US-05) : **16 Story Points**.
- Ce total représente l'effort global nécessaire pour livrer la première version complète et professionnelle de votre portfolio.

### 3.3 La Definition of Ready (DoR) pour le Portfolio
Avant de développer une story de votre portfolio, vous vérifiez :
- Les textes et contenus réels sont rédigés (pas de faux texte "Lorem Ipsum").
- Les images ou captures d'écran des projets sont disponibles et compressées au format WebP ou PNG.
- Les critères d'acceptation sont écrits et compris.

### 3.4 La Definition of Done (DoD) pour le Portfolio
Une User Story de votre portfolio est déclarée **Terminée (Done)** uniquement si :
- Le code HTML est sémantique et valide (W3C).
- La mise en page CSS est 100% responsive (testée sur écran ordinateur et écran mobile).
- La console du navigateur n'affiche aucune erreur ni avertissement critique.
- L'accessibilité de base est respectée (attributs `alt` sur les images, contraste des couleurs lisible).
- Le code source est committé sur la branche Git active avec un message explicite.

---

## 4. Auto-évaluation et Validation

Vérifiez les points suivants avant d'entamer le tutoriel suivant :
- Votre Product Backlog est classé par ordre strict de priorité.
- Chaque User Story a reçu une estimation relative cohérente en Story Points.
- Vous avez distingué le MVP (16 points Must have) des fonctionnalités reportées.
- Votre Definition of Done est claire et applicable à chaque incrément.
- Vous êtes prêt à planifier et lancer votre premier Sprint dans le Tutoriel 4.
