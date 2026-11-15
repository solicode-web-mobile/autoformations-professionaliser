# Plan des Tutoriels : D.311.2 — Modélisation Logicielle UML

> **Domaine :** `D.311.2` | **Compétence :** `C.311` — Analyser et modéliser les besoins logiciels | **Session :** S01  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)  
> **Branche Git de Travail :** `sprint1`  
> **Projet Référence :** Projet d'imitation (*Blog des Lauréats*)  
> **Référentiels Liés :** [`../../3.sprints/flux-travail-n3.md`](../../3.sprints/flux-travail-n3.md) | [`../../3.sprints/stack-technique-n3.md`](../../3.sprints/stack-technique-n3.md)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.311.21 — Modélisation de diagramme de contexte

- **Code :** `UA.311.21`
- **Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 04
- **Positionnement Flux de Travail :** Phase B — Analyse, Conception & Planification / Étape 2.1 — Frontières Système & Contexte
- **Briques Stack Technique :** Mermaid.js, Syntaxe déclarative Markdown, Diagramme de contexte système
- **Compétence :** `C.311` — Analyser et modéliser les besoins logiciels
- **Domaine :** `D.311.2` — Modélisation logicielle UML
- **Durée estimée :** 4 heures
- **Objectif :** Délimiter les frontières fonctionnelles du système logiciel et cartographier les interactions avec les acteurs externes en syntaxe déclarative Mermaid.js, puis créer le prompt réutilisable associé.
- **Description :** Modéliser les flux et frontières du système cible. Les concepts théoriques fondamentaux étant déjà acquis en N2, l'apprenant entre directement dans la pratique en produisant le diagramme de contexte en syntaxe déclarative versionnable, puis conçoit le prompt `prompt-diagramme-contexte`.
- **Notions Clés Utilisées dans le Sprint :**
  - Frontière système et concept de boîte noire : délimitation stricte entre le système cible et son environnement.
  - Typologie des acteurs : acteurs primaires (Lecteur public, Lauréat), acteurs secondaires (Modérateur, Formateur PO) et systèmes tiers.
  - Flux d'échange nommés sans détail protocolaire.
  - Syntaxe déclarative Mermaid.js : modélisation textuelle `graph LR`.
- **Livrables :** Diagramme de contexte Mermaid (`livrables/uml/diagramme-contexte.mmd`) et prompt réutilisable (`livrables/ia/prompts/prompt-diagramme-contexte.prompt.md`) sur la branche `sprint1`.
- **Travail à Faire :** Modéliser le diagramme de contexte du Projet d'imitation en Mermaid.js et concevoir le prompt d'automatisation IA.

---

### UA.311.22 — Diagramme de cas d'utilisation macro

- **Code :** `UA.311.22`
- **Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 07
- **Positionnement Flux de Travail :** Phase B — Analyse, Conception & Planification / Étape 2.4 — Cartographie des Cas d'Utilisation Macro
- **Briques Stack Technique :** Mermaid.js, Use Cases UML, Relations structurelles (`<<include>>`, `<<extend>>`)
- **Compétence :** `C.311` — Analyser et modéliser les besoins logiciels
- **Domaine :** `D.311.2` — Modélisation logicielle UML
- **Durée estimée :** 4 heures
- **Objectif :** Cartographier l'ensemble des 15 cas d'utilisation macro du blog en Mermaid.js avec identification des relations d'inclusion et d'extension, puis créer le prompt réutilisable associé.
- **Description :** Représenter les fonctionnalités du système du point de vue des acteurs. Les prérequis théoriques étant validés en N2, l'atelier se concentre sur la pratique immédiate : modélisation des cas d'utilisation macro du Blog des Lauréats, traçabilité avec le Product Backlog et conception du prompt `prompt-use-cases-macro`.
- **Notions Clés Utilisées dans le Sprint :**
  - Cas d'utilisation macro : niveau d'intention observable de l'acteur (15 UCs de l'application).
  - Relations UML structurelles : inclusion obligatoire `<<include>>`, extension conditionnelle `<<extend>>`.
  - Syntaxe Mermaid.js : modélisation `graph TD`.
  - Traçabilité exigences-modèles : alignement biunivoque avec le Product Backlog.
- **Livrables :** Diagramme de cas d'utilisation macro (`livrables/uml/use-cases-macro.mmd`) et prompt réutilisable (`livrables/ia/prompts/prompt-use-cases-macro.prompt.md`) sur la branche `sprint1`.
- **Travail à Faire :** Modéliser les 15 cas d'utilisation en Mermaid.js et concevoir le prompt d'ingénierie réutilisable.

---

## 2. Plan des Tutoriels : UA.311.21

### T.311.211 — Pratique : Diagramme de contexte système

- **Code :** `T.311.211`
- **Maturité :** `UA-Lab` (Pratique guidée sur projet d'imitation)
- **Unité d'Apprentissage parente :** `UA.311.21`
- **Titre Canonique :** Pratique : Diagramme de contexte système
- **Position dans le Flux :** Phase B — Analyse, Conception & Planification / Étape 2.1 — Frontières Système & Contexte.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/uml/diagramme-contexte.mmd`
- **Objectif Opérationnel :** Délimiter les frontières fonctionnelles du système et cartographier les interactions avec les acteurs externes en syntaxe déclarative Mermaid.js.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Identifier les profils d'utilisateurs humains primaires (Lecteur public, Lauréat), secondaires (Modérateur, PO) et systèmes tiers.
  2. *Étape 2 :* Positionner le *Blog des Lauréats* comme boîte noire centrale.
  3. *Étape 3 :* Relier chaque acteur au système central avec des flux orientés et nommés explicitement en syntaxe `graph LR`.
- **Critère de Réussite :** Le fichier `livrables/uml/diagramme-contexte.mmd` est syntaxiquement valide et s'affiche sans erreur de rendu.

---

### T.311.212 — Création du prompt-diagramme-contexte

- **Code :** `T.311.212`
- **Maturité :** `UA-Lab` (Automatisation & Ingénierie IA)
- **Unité d'Apprentissage parente :** `UA.311.21`
- **Titre Canonique :** Création du prompt-diagramme-contexte
- **Position dans le Flux :** Phase B — Analyse, Conception & Planification / Étape 2.1 — Automatisation du Contexte.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-diagramme-contexte.prompt.md`
- **Objectif Opérationnel :** Concevoir le prompt d'ingénierie réutilisable permettant à un agent IA de générer le diagramme de contexte Mermaid pour n'importe quelle application métier.
- **Missions Concrètes Réalisées par le Prompt :**
  1. Analyser la description textuelle d'une application métier et en extraire la liste des acteurs et systèmes tiers.
  2. Déterminer les frontières fonctionnelles et les flux d'échange bidirectionnels.
  3. Générer le code source Mermaid.js (`graph LR`) prêt à être intégré dans un fichier `.mmd`.
- **Cahier des Charges du Prompt (Méthode RIO) :**
  - **Rôle :** Analyste système senior expert en modélisation fonctionnelle et Mermaid.js.
  - **Instruction :** Prendre en entrée la description de l'application métier `[THEME_APPLICATION]` et déduire les acteurs externes, les systèmes tiers et les flux d'échange pour produire le bloc `graph LR`.
  - **Output :** Bloc de code Mermaid pur directement intégrable dans un fichier `.mmd`.
  - **Contraintes Négatives :** Zéro explication textuelle avant ou après le bloc Mermaid.
- **Critère de Réussite :** Le prompt est testé et sauvegardé dans `livrables/ia/prompts/prompt-diagramme-contexte.prompt.md` sur la branche `sprint1`.

---

## 3. Plan des Tutoriels : UA.311.22

### T.311.221 — Pratique : Diagramme de cas d'utilisation macro

- **Code :** `T.311.221`
- **Maturité :** `UA-Lab` (Pratique guidée sur projet d'imitation)
- **Unité d'Apprentissage parente :** `UA.311.22`
- **Titre Canonique :** Pratique : Diagramme de cas d'utilisation macro
- **Position dans le Flux :** Phase B — Analyse, Conception & Planification / Étape 2.4 — Cartographie des Cas d'Utilisation Macro.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/uml/use-cases-macro.mmd`
- **Objectif Opérationnel :** Modéliser les 15 cas d'utilisation macro du système avec relations structurelles en syntaxe déclarative Mermaid.js.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Cartographier les 15 cas d'utilisation couvrant l'espace public (consultation, lecture), l'espace lauréat (rédaction, publication) et la modération.
  2. *Étape 2 :* Relier chaque acteur à ses cas d'utilisation respectifs.
  3. *Étape 3 :* Positionner les dépendances structurelles obligatoires (`<<include>>`) et optionnelles (`<<extend>>`).
- **Critère de Réussite :** Le fichier `livrables/uml/use-cases-macro.mmd` est versionné sur la branche `sprint1` et compile sans avertissement.

---

### T.311.222 — Création du prompt-use-cases-macro

- **Code :** `T.311.222`
- **Maturité :** `UA-Lab` (Automatisation & Ingénierie IA)
- **Unité d'Apprentissage parente :** `UA.311.22`
- **Titre Canonique :** Création du prompt-use-cases-macro
- **Position dans le Flux :** Phase B — Analyse, Conception & Planification / Étape 2.4 — Automatisation des Cas d'Utilisation.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-use-cases-macro.prompt.md`
- **Objectif Opérationnel :** Concevoir le prompt d'ingénierie réutilisable permettant à un agent IA de produire le diagramme de cas d'utilisation macro avec relations structurelles.
- **Missions Concrètes Réalisées par le Prompt :**
  1. Extraire la liste des fonctionnalités et des profils utilisateurs depuis le Product Backlog.
  2. Déduire les cas d'utilisation à granularité macroscopique en éliminant la sur-segmentation technique.
  3. Identifier et relier les relations `<<include>>` et `<<extend>>`.
  4. Produire le code Mermaid.js (`graph TD`) complet.
- **Cahier des Charges du Prompt (Méthode RIO) :**
  - **Rôle :** Analyste fonctionnel senior expert en ingénierie des exigences et diagrammes UML.
  - **Instruction :** Prendre en entrée la liste des acteurs et les fonctionnalités du carnet produit pour déduire l'arborescence des cas d'utilisation avec relations structurelles.
  - **Output :** Bloc de code Mermaid `graph TD` prêt pour un fichier `.mmd`.
  - **Contraintes Négatives :** Pas de diagramme d'activité déguisé en use case, pas de micro-actions techniques.
- **Critère de Réussite :** Le prompt est testé et consigné dans `livrables/ia/prompts/prompt-use-cases-macro.prompt.md` sur la branche `sprint1`.