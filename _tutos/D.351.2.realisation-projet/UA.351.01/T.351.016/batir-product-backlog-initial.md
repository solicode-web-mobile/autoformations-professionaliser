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
maturite: "projet"
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

## 1. Prérequis
- **Bases méthodologiques requises :**
  - Maîtrise des principes Scrum et du découpage de besoins en User Stories (`UA.351.11`, `T.351.112`, `T.351.113`).
  - Démarche d'empathie et formalisation de Personas issues du Design Thinking (`UA.311.11`, `T.311.113`).
- **Prérequis de projet :** Note de cadrage (`docs/cadrage/note-cadrage.md`), stack technique Laravel (`docs/cadrage/stack-technique.md`) et Product Goal (`docs/produit/vision-produit.md`) validés sur la branche active.
- **Branche Git :** `sprint0`

## 2. Travail à Faire
Bâtissez le socle fonctionnel et le carnet d'exigences du *Blog des Lauréats* avec l'appui méthodologique du **Groupe 2 (Design)** pour les personas et du **Groupe 1 (Product Owner)** pour le backlog :
- Formaliser les fiches de 3 profils Personas représentatifs dans `docs/analyse/personas.md`.
- Exprimer les besoins fonctionnels sous la forme de User Stories conformes au standard INVEST (*En tant que... je veux... afin de...*).
- Formuler des critères d'acceptation univoques, mesurables et vérifiables pour chaque User Story.
- Estimer l'effort relatif de chaque exigence en Story Points à l'aide de la suite de Fibonacci (1, 2, 3, 5, 8).
- Catégoriser et ordonner le carnet d'exigences selon la matrice MoSCoW (*Must have*, *Should have*, *Could have*, *Won't have*) en concertation avec le Product Owner pour dégager le MVP du premier sprint.
- Rédiger et enregistrer le Product Backlog initial consolidé dans `scrum/product-backlog.md`.

## 3. Étapes de Réalisation

1. **Étape 1 — Créer les répertoires et les fichiers de projet :**  
   Initialisez les espaces dédiés à l'analyse et à la gouvernance Scrum sur votre poste local sous Windows PowerShell :

```powershell
mkdir docs/analyse
mkdir scrum
echo "" > docs/analyse/personas.md
echo "" > scrum/product-backlog.md
```

2. **Étape 2 — Formaliser les fiches Personas du Blog (`docs/analyse/personas.md`) :**  
   À partir des ateliers d'empathie et en coordination avec le Groupe 2 (Design), rédigez les profils détaillés des 3 acteurs clés du *Blog des Lauréats* :
   - **Persona 1 — Amine (22 ans), Apprenant actuel de l'EFP :**
     - *Portrait & Contexte :* En formation active, motivé, en quête de méthodes de travail efficaces et de perspectives d'insertion.
     - *Objectifs :* Consulter des retours d'expérience concrets, découvrir les compétences sollicitées en entreprise et s'inspirer des réussites des anciens.
     - *Freins & Frustrations :* Manque de visibilité sur les attentes réelles des recruteurs, crainte du syndrome de l'imposteur.
     - *Citation type :* « J'ai besoin de lire le témoignage de ceux qui sont passés par l'EFP avant moi pour me projeter avec confiance. »
   - **Persona 2 — Sara (26 ans), Lauréate en poste (Développeuse Web Full Stack) :**
     - *Portrait & Contexte :* Diplômée de l'EFP en poste depuis deux ans dans une ESN, désireuse de transmettre et de redonner à sa communauté.
     - *Objectifs :* Publier des articles techniques, partager ses conseils d'orientation et valoriser son expertise professionnelle.
     - *Freins & Frustrations :* Manque de temps pour rédiger, interface de saisie trop lourde ou complexe.
     - *Citation type :* « Partager mon parcours me permet d'aider les nouveaux apprenants tout en consolidant ma propre visibilité technique. »
   - **Persona 3 — Karim (35 ans), Formateur référent & Modérateur éditorial :**
     - *Portrait & Contexte :* Formateur à l'EFP veillant à la cohérence pédagogique et au rayonnement institutionnel.
     - *Objectifs :* Vérifier la conformité des publications à la charte déontologique et valoriser publiquement les compétences acquises.
     - *Freins & Frustrations :* Risque de dérives éditoriales, charge de modération excessive sans filtres préalables.
     - *Citation type :* « La plateforme doit valoriser le travail des lauréats tout en garantissant une qualité de contenu irréprochable. »

3. **Étape 3 — Rédiger les User Stories au standard INVEST :**  
   Pour chaque fonctionnalité identifiée, rédigez la User Story selon le canevas canonique et vérifiez les 6 critères INVEST :
   - **I**ndependent : Chaque histoire peut être comprise et développée indépendamment des autres.
   - **N**egotiable : La portée et les modalités restent discutables entre l'équipe et le Product Owner.
   - **V**aluable : L'histoire apporte un bénéfice direct et palpable à l'un des Personas cibles.
   - **E**stimable : L'équipe cerne la complexité technique et peut évaluer l'effort nécessaire.
   - **S**mall : L'exigence est suffisamment découpée pour être réalisée au cours d'un sprint de 80h.
   - **T**estable : Des critères d'acceptation univoques permettent de valider sans ambiguïté la livraison.

4. **Étape 4 — Définir les critères d'acceptation et estimer l'effort en Story Points :**  
   Attribuez à chaque User Story des conditions de test concrètes et mesurables. En concertation avec l'équipe de développement, attribuez une estimation relative selon la suite de Fibonacci : 1 (trivial), 2 (simple), 3 (moyen), 5 (complexe), 8 (très complexe).

5. **Étape 5 — Prioriser selon MoSCoW et finaliser le Product Backlog (`scrum/product-backlog.md`) :**  
   Sous l'arbitrage du Product Owner (Groupe 1), classez les User Stories dans les quatre catégories MoSCoW :
   - **Must have :** Indispensables au MVP du Blog (page d'accueil, lecture d'article, authentification auteur).
   - **Should have :** Fortement recommandées mais pouvant être différées sans bloquer la démonstration (filtrage par catégorie, tableau de bord auteur).
   - **Could have :** Fonctionnalités utiles de confort (recherche textuelle avancée).
   - **Won't have :** Fonctionnalités reportées ou explicitement exclues du périmètre initial (messagerie en direct).

   Enregistrez le carnet d'exigences structuré dans `scrum/product-backlog.md` :

| ID | Titre de la User Story | Description Sémantique (INVEST) | Priorité MoSCoW | Estimation (SP) | Critères d'Acceptation |
| :---: | :--- | :--- | :---: | :---: | :--- |
| US01 | Consultation page d'accueil | En tant que visiteur ou apprenant (Amine), je veux visualiser la liste des derniers articles publiés afin de découvrir les retours d'expérience récents. | Must | 5 | Grille responsive, Hero section, tri chronologique descendant des publications. |
| US02 | Consultation article détaillé | En tant que lecteur (Amine), je veux lire le contenu complet d'un article afin d'assimiler les conseils techniques et le retour d'expérience du lauréat. | Must | 5 | Route dynamique `/articles/{id}`, titre, auteur, date, contenu formaté, gestion de l'erreur 404. |
| US03 | Filtrage par catégorie | En tant que lecteur (Amine), je veux filtrer les articles par domaine technique (Laravel, Scrum, Design, IA) afin de cibler directement mes centres d'intérêt. | Should | 3 | Boutons de filtrage actifs, affichage dynamique des articles filtrés. |
| US04 | Authentification auteur | En tant que lauréat (Sara), je veux me connecter avec mes identifiants sécurisés afin d'accéder à mon espace de publication. | Must | 8 | Formulaire de login sécurisé (CSRF, validation), redirection vers le tableau de bord auteur. |
| US05 | Tableau de bord auteur | En tant que lauréat auteur (Sara), je veux visualiser la liste de mes articles et leur statut (brouillon, publié) afin de suivre mes contributions. | Should | 5 | Liste des articles personnels, statuts visibles, actions d'édition et suppression. |
| US06 | Recherche textuelle | En tant que lecteur (Amine), je veux rechercher des articles par mot-clé dans le titre ou le contenu afin de trouver rapidement une solution ciblée. | Could | 3 | Champ de recherche actif, filtrage instantané ou par soumission de formulaire. |
| US07 | Messagerie instantanée | En tant qu'apprenant (Amine), je veux échanger en direct par chat avec un lauréat auteur. | Won't | 13 | Exclu du MVP initial : renvoi vers les profils professionnels externes (LinkedIn / GitHub). |

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Dossier d'analyse usagers : `docs/analyse/personas.md` sur la branche `sprint0`.
  - Carnet d'exigences ordonné : `scrum/product-backlog.md` sur la branche `sprint0`.
- **Critères de validation :**
  - [ ] Les 3 profils Personas (Amine, Sara, Karim) sont documentés avec portrait, objectifs, freins et citation.
  - [ ] Toutes les User Stories sont formulées selon la syntaxe canonique *En tant que... je veux... afin de...*.
  - [ ] Chaque User Story respecte les 6 critères du standard INVEST.
  - [ ] Des critères d'acceptation précis, univoques et testables sont définis pour chaque story.
  - [ ] Les estimations en Story Points (Fibonacci) et la priorisation MoSCoW sont validées avec le Product Owner (Groupe 1).
  - [ ] Les livrables sont enregistrés aux emplacements officiels (`docs/analyse/personas.md` et `scrum/product-backlog.md`) sur la branche `sprint0` en encodage UTF-8 sans BOM.
