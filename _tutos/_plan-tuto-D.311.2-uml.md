# Plan des Tutoriels : D.311.2 — Modélisation Logicielle UML

> **Domaine :** `D.311.2` | **Compétence :** `C.311` — Analyser et modéliser les besoins logiciels | **Session :** S01  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)  
> **Référentiels Liés :** [`../../3.sprints/flux-travail-n3.md`](../../3.sprints/flux-travail-n3.md) | [`../../3.sprints/stack-technique-n3.md`](../../3.sprints/stack-technique-n3.md)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.311.21 — Modélisation de diagramme de contexte

- **Code :** `UA.311.21`
- **Maturité :** `UA-lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 04
- **Positionnement Flux de Travail :** Phase 2 — Analyse des Exigences & Modélisation / Étape 2.1 — Frontières Système & Contexte
- **Briques Stack Technique :** Mermaid.js, Syntaxe déclarative Markdown, Diagramme de contexte système
- **Compétence :** `C.311` — Analyser et modéliser les besoins logiciels
- **Domaine :** `D.311.2` — Modélisation logicielle UML
- **Durée estimée :** 6 heures
- **Objectif :** Délimiter les frontières fonctionnelles du système logiciel et cartographier les interactions avec les acteurs externes en syntaxe déclarative Mermaid.js pour sécuriser le périmètre du projet.
- **Description :** Analyser les flux et les frontières du système logiciel. L'apprenant modélise le diagramme de contexte de l'application en syntaxe déclarative versionnable, identifiant acteurs primaires, secondaires et systèmes tiers.
- **Notions Clés Utilisées dans le Sprint :**
  - Frontière système et concept de boîte noire : délimitation stricte entre le système cible et son environnement.
  - Typologie des acteurs : acteurs primaires humains (Lecteur public, Lauréat), acteurs secondaires (Modérateur, Formateur PO) et système tiers (Service hébergement / GitHub).
  - Flux d'échange nommés : flux orientés représentant les interactions sans détail protocolaire.
  - Syntaxe déclarative Mermaid.js : modélisation textuelle `graph LR` versionnable directement intégrée au Markdown.
- **Livrables :** Diagramme de contexte système Mermaid (`livrables/uml/diagramme-contexte.mmd`) et prompt réutilisable (`livrables/ia/prompts/prompt-diagramme-contexte.prompt.md`).
- **Travail à Faire :** Identifier les acteurs et flux d'échange du système, produire le diagramme Mermaid.js et concevoir le prompt de transposition.

---

### UA.311.22 — Diagramme de cas d'utilisation macro

- **Code :** `UA.311.22`
- **Maturité :** `UA-lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 07
- **Positionnement Flux de Travail :** Phase 2 — Analyse des Exigences & Modélisation / Étape 2.4 — Cartographie des Cas d'Utilisation Macro
- **Briques Stack Technique :** Mermaid.js, Use Cases UML, Relations structurelles
- **Compétence :** `C.311` — Analyser et modéliser les besoins logiciels
- **Domaine :** `D.311.2` — Modélisation logicielle UML
- **Durée estimée :** 8 heures
- **Objectif :** Cartographier l'ensemble des 15 cas d'utilisation macro du blog en Mermaid.js avec identification des relations d'inclusion et d'extension pour isoler et spécifier le cas d'usage central de consultation d'un article.
- **Description :** Représenter l'ensemble des fonctionnalités du système du point de vue des acteurs. L'apprenant modélise les cas d'utilisation macro, structure les dépendances fonctionnelles et garantit la traçabilité avec le Product Backlog.
- **Notions Clés Utilisées dans le Sprint :**
  - Cas d'utilisation macro : granularité fonctionnelle observable sans sur-segmentation technique (15 UCs de l'application).
  - Relations UML structurelles : inclusion obligatoire `<<include>>`, extension conditionnelle `<<extend>>`.
  - Syntaxe Mermaid.js : modélisation `graph TD` reliant acteurs et ovales de cas d'utilisation.
  - Traçabilité exigences-modèles : alignement biunivoque entre chaque PBI du Product Backlog et un cas d'utilisation du diagramme.
- **Livrables :** Diagramme de cas d'utilisation macro (`livrables/uml/use-cases-macro.mmd`) et prompt réutilisable (`livrables/ia/prompts/prompt-use-cases-macro.prompt.md`).
- **Travail à Faire :** Modéliser les 15 cas d'utilisation du système en Mermaid.js, documenter les relations et concevoir le prompt de transposition.

---

## 2. Plan des Tutoriels : UA.311.21

### T.311.211 — Théorie : Diagramme de contexte
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 2 — Analyse des Exigences & Modélisation / Étape 2.1 — Frontières Système & Contexte.
- **Stack mobilisée :** Syntaxe Mermaid.js déclarative, analyse fonctionnelle de niveau 0.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant le rôle du diagramme de contexte dans le cycle de vie logiciel, la distinction entre frontière système et acteurs externes, et les principes de la modélisation textuelle sous Mermaid.js.

#### 3. Notions Clés du Sprint à Ne Pas Oublier
*(L'apprenant doit obligatoirement couvrir ces notions et les enrichir par sa propre recherche) :*
- La notion de boîte noire et d'interface externe.
- La classification des acteurs (primaires, secondaires, systèmes tiers).
- Les conventions de nommage des flux d'échange (verbes d'action ou syntagmes nominaux).
- Les avantages de la syntaxe déclarative versionnable par rapport aux outils graphiques propriétaires.

#### 4. Points de Réflexion & Auto-Évaluation
- *Pourquoi est-il indispensable de figer le diagramme de contexte avant de commencer la rédaction du Product Backlog ?*
- *Quelle est la différence fondamentale entre un acteur humain et un système tiers dans ce diagramme ?*

---

### T.311.212 — Pratique : Modélisation du contexte
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Livrable Attendu
- `livrables/uml/diagramme-contexte.mmd` : Diagramme de contexte complet en syntaxe Mermaid.js.

#### 2. Consignes & Jalons de Réalisation
Bâtir le diagramme de contexte en respectant ces 3 jalons :
1. **Identification des Acteurs :** Recenser au moins 2 profils d'utilisateurs humains primaires (Lecteur public, Lauréat), les acteurs secondaires (Modérateur, PO) et les services tiers (GitHub / Hébergement).
2. **Définition de la Boîte Noire :** Placer le *Blog des Lauréats* au centre du modèle.
3. **Modélisation des Flux :** Relier chaque acteur au système central avec des flux orientés et nommés explicitement.

#### 3. Points de Vigilance
- ⚠️ Aucun flux ne doit relier directement deux acteurs externes entre eux (tous les flux transitent par le système).
- ⚠️ Le diagramme doit rester de niveau macroscopique sans détails de protocoles techniques (ex : pas de mention « TCP/IP »).

#### 4. Critères de Validation
- [ ] Le fichier `livrables/uml/diagramme-contexte.mmd` est présent et s'affiche sans erreur de rendu sous Mermaid.
- [ ] La frontière système est clairement matérialisée.
- [ ] Tous les acteurs du brief projet sont représentés.

---

### T.311.213 — Prompts & Skills : Contexte système Fil Rouge
*(Tâche 3 — Conception Prompts & Skills Projet Fil Rouge)*

#### 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 2.1 (Frontières Système & Contexte) vers le Projet Fil Rouge (ex : Plateforme Cinéma).

#### 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-diagramme-contexte.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de générer le diagramme de contexte Mermaid pour n'importe quelle application métier.

#### 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Analyste système senior expert en modélisation fonctionnelle et Mermaid.js.
- **Instruction :** Prendre en entrée la description de l'application métier `[THEME_APPLICATION]` et déduire les acteurs externes, les systèmes tiers et les flux d'échange pour produire le bloc `graph LR`.
- **Output :** Bloc de code Mermaid pur directement intégrable dans un fichier `.mmd`.
- **Contraintes Négatives :** Zéro explication textuelle avant ou après le bloc Mermaid.

#### 4. Critères de Validation
- [ ] Le prompt est testé avec l'agent IA sur le thème du Projet Fil Rouge.
- [ ] Le code Mermaid généré est syntaxiquement valide et fidèlement aligné sur le domaine métier.

---

## 3. Plan des Tutoriels : UA.311.22

### T.311.221 — Théorie : Cas d'utilisation macro
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 2 — Analyse des Exigences & Modélisation / Étape 2.4 — Cartographie des Cas d'Utilisation Macro.
- **Stack mobilisée :** Modélisation UML, notation Use Cases, Mermaid.js `graph TD`.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches documentaires nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant les concepts fondamentaux du diagramme de cas d'utilisation, la signification rigoureuse des relations structurelles `<<include>>` et `<<extend>>`, et l'articulation avec le Product Backlog.

#### 3. Notions Clés du Sprint à Ne Pas Oublier
*(L'apprenant doit obligatoirement couvrir ces notions et les enrichir par sa propre recherche) :*
- La définition d'un cas d'utilisation comme intention d'un acteur produisant un résultat observable.
- La relation d'inclusion obligatoire (`<<include>>`).
- La relation d'extension conditionnelle (`<<extend>>`).
- La granularité macroscopique (éviter la sur-segmentation en micro-fonctions).

#### 4. Points de Réflexion & Auto-Évaluation
- *Quelle est l'erreur commise lorsqu'un diagramme de cas d'utilisation représente un enchaînement chronologique étape par étape comme un algorithme ?*
- *Comment vérifier qu'aucun besoin utilisateur exprimé dans le Product Backlog n'a été oublié dans le diagramme ?*

---

### T.311.222 — Pratique : Modélisation des cas d'utilisation
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Livrable Attendu
- `livrables/uml/use-cases-macro.mmd` : Diagramme des cas d'utilisation macro de l'application de référence.

#### 2. Consignes & Jalons de Réalisation
Bâtir le diagramme en respectant ces 3 jalons :
1. **Cartographie des 15 UCs :** Identifier les cas d'utilisation couvrant l'espace public (consultation, lecture), l'espace lauréat (rédaction, publication) et l'espace modération.
2. **Association Acteurs-UCs :** Relier chaque acteur à ses cas d'utilisation respectifs.
3. **Formalisation des Relations Structurelles :** Positionner les dépendances obligatoires (`<<include>>`, ex: authentification) et optionnelles (`<<extend>>`).

#### 3. Points de Vigilance
- ⚠️ Ne pas confondre une relation `<<include>>` avec un simple appel de sous-programme.
- ⚠️ Respecter la matrice de traçabilité avec les PBIs du Product Backlog.

#### 4. Critères de Validation
- [ ] Le fichier `livrables/uml/use-cases-macro.mmd` est présent et versionné sous Git.
- [ ] L'ensemble des 15 cas d'utilisation du projet de référence y figurent de manière lisible.
- [ ] La syntaxe Mermaid est propre et sans avertissement de compilation.

---

### T.311.223 — Prompts & Skills : Cas d'utilisation Fil Rouge
*(Tâche 3 — Conception Prompts & Skills Projet Fil Rouge)*

#### 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 2.4 (Cartographie des Cas d'Utilisation Macro) vers le Projet Fil Rouge (ex : Plateforme Cinéma).

#### 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-use-cases-macro.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de produire le diagramme de cas d'utilisation macro pour le Projet Fil Rouge.

#### 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Analyste fonctionnel senior expert en ingénierie des exigences et diagrammes UML.
- **Instruction :** Prendre en entrée la liste des acteurs et les fonctionnalités du carnet produit Fil Rouge pour déduire l'arborescence des cas d'utilisation avec relations `<<include>>` et `<<extend>>`.
- **Output :** Bloc de code Mermaid `graph TD` prêt pour un fichier `.mmd`.
- **Contraintes Négatives :** Pas de diagramme d'activité déguisé en use case, pas de micro-actions techniques.

#### 4. Critères de Validation
- [ ] Le prompt est testé sur le thème de l'application Fil Rouge.
- [ ] Le diagramme généré traduit fidèlement les interactions des utilisateurs avec le système métier.
