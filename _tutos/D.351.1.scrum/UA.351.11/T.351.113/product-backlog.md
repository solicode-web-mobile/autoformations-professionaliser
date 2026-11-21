---
layout: tuto
title: "Créer, estimer et ordonner le Product Backlog"
sous_titre: "Estimer l'effort en Story Points, appliquer la méthode MoSCoW et contractualiser la DoR et la DoD"
slug: "product-backlog"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
permalink: /tutos/product-backlog/
tuto_id: "T.351.113"
version: "normal"
ua: "UA.351.11"
type: "tuto-atelier-notions"
nav_order: 3
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
sprint: "sprint1"
statut_realisation: "realise"
livrables:
  - chemin: "ua-lab/scrum/initiation-scrum/product-backlog/product-backlog.md"
    version: "1.0.0"
  - chemin: "ua-lab/scrum/initiation-scrum/product-backlog/presentation-product-backlog.md"
    version: "1.0.0"
---

## 1. Travail à faire
Structurer, chiffrer et ordonnancer le carnet de produit Scrum pour votre projet technique individuel. Vous devez attribuer des Story Points à chaque User Story, appliquer la priorisation MoSCoW pour isoler le MVP et formaliser la *Definition of Ready* (DoR) et la *Definition of Done* (DoD).

> [!NOTE]
> **Projet Technique de Référence :** Ce tutoriel est rédigé et illustré à partir du **Portfolio Développeur**, qui sert d'exemple concret de Projet Technique. Vous devez appliquer et adapter ces estimations et grilles qualité à **votre propre projet technique**.

## 2. Notions fondamentales
- **Le Product Backlog :**
  - Liste ordonnée et vivante de tout ce qui est nécessaire au produit. Source unique des exigences sous la responsabilité du Product Owner.
  - Ajusté en continu selon les apprentissages techniques et les retours utilisateurs.
- **L'Estimation Relative par les Story Points :**
  - Mesure non pas un temps en heures fermes, mais un effort combinant quantité de travail, complexité technique et incertitude.
  - Échelle standardisée basée sur la suite de Fibonacci simplifiée : **1, 2, 3, 5, 8, 13**.
    - *1 point :* Tâche triviale (mise à jour d'un texte ou d'un lien).
    - *2 à 3 points :* Fonctionnalité simple maîtrisée (section statique).
    - *5 points :* Taille moyenne avec logique (formulaire avec validation).
    - *8 à 13 points :* Fonctionnalité complexe à décomposer.
- **La Priorisation MoSCoW :**
  - **M — Must have (Indispensable) :** Fonctionnalités vitales constituant le cœur du MVP.
  - **S — Should have (Important) :** Forte valeur ajoutée mais non bloquant pour le premier livrable.
  - **C — Could have (Souhaitable) :** Améliorations de confort réalisées s'il reste du temps.
  - **W — Won't have this time (Reporté) :** Exigences écartées pour le sprint en cours.
- **Definition of Ready (DoR) :** Contrat préalable certifiant qu'une story est suffisamment claire, estimée et indépendante pour être prise en compte dans un sprint.
- **Definition of Done (DoD) :** Grille d'exigence qualité non négociable indispensable pour déclarer une fonctionnalité terminée et prête à la démonstration.

## 3. Application pratique sur le Projet Technique (Exemple Portfolio)
- **Exemple de Product Backlog ordonné (Portfolio) :**
  - *US-01 (Présentation personnelle) :* 2 Story Points | Priorité 1 | **Must have**.
  - *US-03 (Section Compétences techniques) :* 3 Story Points | Priorité 2 | **Must have**.
  - *US-02 (Vitrine des réalisations) :* 5 Story Points | Priorité 3 | **Must have**.
  - *US-04 (Formulaire de contact) :* 5 Story Points | Priorité 4 | **Must have**.
  - *US-05 (Téléchargement du CV PDF) :* 1 Story Point | Priorité 5 | **Must have**.
  - *US-06 (Mode sombre / Dark mode) :* 5 Story Points | Priorité 6 | **Could have** (post-MVP).
  - *US-07 (Section Blog / Articles récents) :* 8 Story Points | Priorité 7 | **Won't have this time**.
- **Effort total du MVP :** **16 Story Points** (US-01 à US-05).
- **Definition of Ready (DoR) du projet technique :** Textes réels rédigés (aucun Lorem Ipsum), ressources graphiques prêtes et critères d'acceptation validés.
- **Definition of Done (DoD) du projet technique :** Code HTML5 sémantique et valide W3C, CSS 100% responsive (desktop et smartphone), zéro erreur dans la console DevTools, attributs d'accessibilité (`alt`, contrastes) et code committé sur la branche Git active.

## 4. Livrables & Critères de validation
- **Livrables attendus :**
  - Fiche technique d'atelier : `ua-lab/scrum/initiation-scrum/product-backlog/product-backlog.md` sur la branche `sprint1`.
  - Diaporama Marp de restitution : `ua-lab/scrum/initiation-scrum/product-backlog/presentation-product-backlog.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Les User Stories de votre projet technique sont ordonnées selon la valeur métier et classées selon la grille MoSCoW.
  - [ ] Chaque élément du backlog possède une estimation cohérente en Story Points sur l'échelle de Fibonacci.
  - [ ] Le périmètre Must have (MVP) est clairement totalisé et délimité.
  - [ ] La Definition of Ready et la Definition of Done sont formalisées avec des critères opérationnels stricts.
