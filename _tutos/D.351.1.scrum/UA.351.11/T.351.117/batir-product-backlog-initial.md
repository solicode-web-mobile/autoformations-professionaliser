---
layout: tuto
title: "BÃ¢tir le Product Backlog initial du Blog"
sous_titre: "Structurer et ordonner les User Stories INVEST selon la mÃ©thode MoSCoW"
slug: "batir-product-backlog-initial"
slug_domaine: "scrum"
slug_ua: "UA.351.11"
permalink: /tutos/batir-product-backlog-initial/
tuto_id: "T.351.117"
version: "normal"
ua: "UA.351.11"
maturite: "projet"
type: "tuto-tache"
etape: 9
nav_order: 7
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
livrables:
  - chemin: "scrum/product-backlog.md"
    version: "0.1.0"
---

## 1. PrÃ©requis
- **Bases mÃ©thodologiques requises :**
  - MaÃ®trise des principes Scrum et du dÃ©coupage de besoins en User Stories (`UA.351.11`, `T.351.112`, `T.351.113`).
  - DÃ©marche d'empathie et formalisation de Personas issues du Design Thinking (`UA.311.11`, `T.311.113`).
- **PrÃ©requis de projet :** Note de cadrage (`docs/cadrage/note-cadrage.md`), stack technique Laravel (`docs/cadrage/stack-technique.md`) et Product Goal (`docs/produit/vision-produit.md`) validÃ©s sur la branche active.
- **Branche Git :** `sprint0`

## 2. Travail Ã  Faire
BÃ¢tissez le socle fonctionnel et le carnet d'exigences du *Blog des LaurÃ©ats* avec l'appui mÃ©thodologique du **Groupe 2 (Design)** pour les personas et du **Groupe 1 (Product Owner)** pour le backlog :
- Formaliser les fiches de 3 profils Personas reprÃ©sentatifs dans `docs/analyse/personas.md`.
- Exprimer les besoins fonctionnels sous la forme de User Stories conformes au standard INVEST (*En tant que... je veux... afin de...*).
- Formuler des critÃ¨res d'acceptation univoques, mesurables et vÃ©rifiables pour chaque User Story.
- Estimer l'effort relatif de chaque exigence en Story Points Ã  l'aide de la suite de Fibonacci (1, 2, 3, 5, 8).
- CatÃ©goriser et ordonner le carnet d'exigences selon la matrice MoSCoW (*Must have*, *Should have*, *Could have*, *Won't have*) en concertation avec le Product Owner pour dÃ©gager le MVP du premier sprint.
- RÃ©diger et enregistrer le Product Backlog initial consolidÃ© dans `scrum/product-backlog.md`.

## 3. Ã‰tapes de RÃ©alisation

1. **Ã‰tape 1 â€” CrÃ©er les rÃ©pertoires et les fichiers de projet :**  
   Initialisez les espaces dÃ©diÃ©s Ã  l'analyse et Ã  la gouvernance Scrum sur votre poste local sous Windows PowerShell :

```powershell
mkdir docs/analyse
mkdir scrum
echo "" > docs/analyse/personas.md
echo "" > scrum/product-backlog.md
```

2. **Ã‰tape 2 â€” Formaliser les fiches Personas du Blog (`docs/analyse/personas.md`) :**  
   Ã€ partir des ateliers d'empathie et en coordination avec le Groupe 2 (Design), rÃ©digez les profils dÃ©taillÃ©s des 3 acteurs clÃ©s du *Blog des LaurÃ©ats* :
   - **Persona 1 â€” Amine (22 ans), Apprenant actuel de l'EFP :**
     - *Portrait & Contexte :* En formation active, motivÃ©, en quÃªte de mÃ©thodes de travail efficaces et de perspectives d'insertion.
     - *Objectifs :* Consulter des retours d'expÃ©rience concrets, dÃ©couvrir les compÃ©tences sollicitÃ©es en entreprise et s'inspirer des rÃ©ussites des anciens.
     - *Freins & Frustrations :* Manque de visibilitÃ© sur les attentes rÃ©elles des recruteurs, crainte du syndrome de l'imposteur.
     - *Citation type :* Â« J'ai besoin de lire le tÃ©moignage de ceux qui sont passÃ©s par l'EFP avant moi pour me projeter avec confiance. Â»
   - **Persona 2 â€” Sara (26 ans), LaurÃ©ate en poste (DÃ©veloppeuse Web Full Stack) :**
     - *Portrait & Contexte :* DiplÃ´mÃ©e de l'EFP en poste depuis deux ans dans une ESN, dÃ©sireuse de transmettre et de redonner Ã  sa communautÃ©.
     - *Objectifs :* Publier des articles techniques, partager ses conseils d'orientation et valoriser son expertise professionnelle.
     - *Freins & Frustrations :* Manque de temps pour rÃ©diger, interface de saisie trop lourde ou complexe.
     - *Citation type :* Â« Partager mon parcours me permet d'aider les nouveaux apprenants tout en consolidant ma propre visibilitÃ© technique. Â»
   - **Persona 3 â€” Karim (35 ans), Formateur rÃ©fÃ©rent & ModÃ©rateur Ã©ditorial :**
     - *Portrait & Contexte :* Formateur Ã  l'EFP veillant Ã  la cohÃ©rence pÃ©dagogique et au rayonnement institutionnel.
     - *Objectifs :* VÃ©rifier la conformitÃ© des publications Ã  la charte dÃ©ontologique et valoriser publiquement les compÃ©tences acquises.
     - *Freins & Frustrations :* Risque de dÃ©rives Ã©ditoriales, charge de modÃ©ration excessive sans filtres prÃ©alables.
     - *Citation type :* Â« La plateforme doit valoriser le travail des laurÃ©ats tout en garantissant une qualitÃ© de contenu irrÃ©prochable. Â»

3. **Ã‰tape 3 â€” RÃ©diger les User Stories au standard INVEST :**  
   Pour chaque fonctionnalitÃ© identifiÃ©e, rÃ©digez la User Story selon le canevas canonique et vÃ©rifiez les 6 critÃ¨res INVEST :
   - **I**ndependent : Chaque histoire peut Ãªtre comprise et dÃ©veloppÃ©e indÃ©pendamment des autres.
   - **N**egotiable : La portÃ©e et les modalitÃ©s restent discutables entre l'Ã©quipe et le Product Owner.
   - **V**aluable : L'histoire apporte un bÃ©nÃ©fice direct et palpable Ã  l'un des Personas cibles.
   - **E**stimable : L'Ã©quipe cerne la complexitÃ© technique et peut Ã©valuer l'effort nÃ©cessaire.
   - **S**mall : L'exigence est suffisamment dÃ©coupÃ©e pour Ãªtre rÃ©alisÃ©e au cours d'un sprint de 80h.
   - **T**estable : Des critÃ¨res d'acceptation univoques permettent de valider sans ambiguÃ¯tÃ© la livraison.

4. **Ã‰tape 4 â€” DÃ©finir les critÃ¨res d'acceptation et estimer l'effort en Story Points :**  
   Attribuez Ã  chaque User Story des conditions de test concrÃ¨tes et mesurables. En concertation avec l'Ã©quipe de dÃ©veloppement, attribuez une estimation relative selon la suite de Fibonacci : 1 (trivial), 2 (simple), 3 (moyen), 5 (complexe), 8 (trÃ¨s complexe).

5. **Ã‰tape 5 â€” Prioriser selon MoSCoW et finaliser le Product Backlog (`scrum/product-backlog.md`) :**  
   Sous l'arbitrage du Product Owner (Groupe 1), classez les User Stories dans les quatre catÃ©gories MoSCoW :
   - **Must have :** Indispensables au MVP du Blog (page d'accueil, lecture d'article, authentification auteur).
   - **Should have :** Fortement recommandÃ©es mais pouvant Ãªtre diffÃ©rÃ©es sans bloquer la dÃ©monstration (filtrage par catÃ©gorie, tableau de bord auteur).
   - **Could have :** FonctionnalitÃ©s utiles de confort (recherche textuelle avancÃ©e).
   - **Won't have :** FonctionnalitÃ©s reportÃ©es ou explicitement exclues du pÃ©rimÃ¨tre initial (messagerie en direct).

   Enregistrez le carnet d'exigences structurÃ© dans `scrum/product-backlog.md` :

| ID | Titre de la User Story | Description SÃ©mantique (INVEST) | PrioritÃ© MoSCoW | Estimation (SP) | CritÃ¨res d'Acceptation |
| :---: | :--- | :--- | :---: | :---: | :--- |
| US01 | Consultation page d'accueil | En tant que visiteur ou apprenant (Amine), je veux visualiser la liste des derniers articles publiÃ©s afin de dÃ©couvrir les retours d'expÃ©rience rÃ©cents. | Must | 5 | Grille responsive, Hero section, tri chronologique descendant des publications. |
| US02 | Consultation article dÃ©taillÃ© | En tant que lecteur (Amine), je veux lire le contenu complet d'un article afin d'assimiler les conseils techniques et le retour d'expÃ©rience du laurÃ©at. | Must | 5 | Route dynamique `/articles/{id}`, titre, auteur, date, contenu formatÃ©, gestion de l'erreur 404. |
| US03 | Filtrage par catÃ©gorie | En tant que lecteur (Amine), je veux filtrer les articles par domaine technique (Laravel, Scrum, Design, IA) afin de cibler directement mes centres d'intÃ©rÃªt. | Should | 3 | Boutons de filtrage actifs, affichage dynamique des articles filtrÃ©s. |
| US04 | Authentification auteur | En tant que laurÃ©at (Sara), je veux me connecter avec mes identifiants sÃ©curisÃ©s afin d'accÃ©der Ã  mon espace de publication. | Must | 8 | Formulaire de login sÃ©curisÃ© (CSRF, validation), redirection vers le tableau de bord auteur. |
| US05 | Tableau de bord auteur | En tant que laurÃ©at auteur (Sara), je veux visualiser la liste de mes articles et leur statut (brouillon, publiÃ©) afin de suivre mes contributions. | Should | 5 | Liste des articles personnels, statuts visibles, actions d'Ã©dition et suppression. |
| US06 | Recherche textuelle | En tant que lecteur (Amine), je veux rechercher des articles par mot-clÃ© dans le titre ou le contenu afin de trouver rapidement une solution ciblÃ©e. | Could | 3 | Champ de recherche actif, filtrage instantanÃ© ou par soumission de formulaire. |
| US07 | Messagerie instantanÃ©e | En tant qu'apprenant (Amine), je veux Ã©changer en direct par chat avec un laurÃ©at auteur. | Won't | 13 | Exclu du MVP initial : renvoi vers les profils professionnels externes (LinkedIn / GitHub). |

## 4. Livrables & CritÃ¨res de Validation
- **Livrables attendus :**
  - Dossier d'analyse usagers : `docs/analyse/personas.md` sur la branche `sprint0`.
  - Carnet d'exigences ordonnÃ© : `scrum/product-backlog.md` sur la branche `sprint0`.
- **CritÃ¨res de validation :**
  - [ ] Les 3 profils Personas (Amine, Sara, Karim) sont documentÃ©s avec portrait, objectifs, freins et citation.
  - [ ] Toutes les User Stories sont formulÃ©es selon la syntaxe canonique *En tant que... je veux... afin de...*.
  - [ ] Chaque User Story respecte les 6 critÃ¨res du standard INVEST.
  - [ ] Des critÃ¨res d'acceptation prÃ©cis, univoques et testables sont dÃ©finis pour chaque story.
  - [ ] Les estimations en Story Points (Fibonacci) et la priorisation MoSCoW sont validÃ©es avec le Product Owner (Groupe 1).
  - [ ] Les livrables sont enregistrÃ©s aux emplacements officiels (`docs/analyse/personas.md` et `scrum/product-backlog.md`) sur la branche `sprint0` en encodage UTF-8 sans BOM.
