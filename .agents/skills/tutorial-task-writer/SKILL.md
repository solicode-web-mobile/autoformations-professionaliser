---
name: tutorial-task-writer
description: Conçoit, structure et rédige les fiches de tutoriels opérationnels de projet et cérémonies de sprint pour les Unités d'Apprentissage à maturité UA-Tâche (Cadrage de périmètre, Sprint Planning, Sprint Review, Rétrospective réflexive, Backlog Refinement, Débriefing, Prompts de cérémonies).
version: 2.0.0
inspiration:
  source: "solicode-pedagogy"
  plugin: "pedagogy-referential"
  pattern: "ua-task-operational, sprint-ceremonies, zero-theory & ceremony-prompts"
---

# 1. Mission
Ce skill est l'**artisan opérationnel et méthodologique** de l'écosystème **`tutorial-*-writer`**, chargé de concevoir et rédiger les fiches de tutoriels associées aux Unités d'Apprentissage de maturité **`UA-Tâche`**.
Il applique le socle des règles transversales et s'appuie sur le protocole de synchronisation physique gouvernés par le Master Skill **[tutorial-writer](../tutorial-writer/SKILL.md)**.

### Distinction Clé de l'Écosystème `tutorial-*-writer`
- **`UA-Tuto` (Apprentissage incrémental) :** Progression pas-à-pas de code pur ($E_{n-1} \to E_n$), pilotée par [tutorial-code-writer](../tutorial-code-writer/SKILL.md).
- **`UA-Lab` (Atelier pratique guidé) :** Assimilation conceptuelle et pratique outillée (UML, architecture, frameworks, outillage IA), pilotée par [tutorial-lab-writer](../tutorial-lab-writer/SKILL.md).
- **`UA-Tâche` (Tâche opérationnelle & Cérémonies de projet) :** Une `UA-Tâche` n'a **aucune vocation théorique**. Elle formalise et guide l'exécution d'une **tâche de cadrage ou d'un rituel agile du sprint** (cadrage de périmètre, Sprint Planning, Sprint Review, Rétrospective, Backlog Refinement, Débriefing individuel) ainsi que les prompts réutilisables instrumentant ces cérémonies.

---

# 2. Déclenchement & Limites

- **Quand l'activer :**
  - Rédaction et maintenance des fiches de tutoriels associées à une Unité d'Apprentissage de maturité **`UA-Tâche`**.
  - Formalisation des guides opérationnels de cérémonies agiles Scrum (Sprint Planning, Sprint Review, Sprint Retrospective, Backlog Grooming, Bilan).
  - Élaboration des protocoles de cadrage de périmètre de projet.
  - Conception des prompts d'ingénierie réutilisables dédiés à l'automatisation des cérémonies agiles.
- **Quand NE PAS l'activer :**
  - Rédaction de tutoriels de code incrémental (`UA-Tuto`) ➔ Utiliser [tutorial-code-writer](../tutorial-code-writer/SKILL.md).
  - Rédaction d'ateliers pratiques guidés avec théorie ou modélisation (`UA-Lab`) ➔ Utiliser [tutorial-lab-writer](../tutorial-lab-writer/SKILL.md).
  - Planification globale et ordonnancement de sessions ➔ Utiliser [tutorial-planer](../tutorial-planer/SKILL.md).
  - Gouvernance globale, règles partagées et synchronisation ➔ Utiliser [tutorial-writer](../tutorial-writer/SKILL.md).

---

# 3. Structure Normée d'une Fiche `UA-Tâche`

Toute fiche de tutoriel rattachée à une Unité d'Apprentissage de type `UA-Tâche` adopte obligatoirement la structure standardisée en **4 sections** :

```markdown
---
layout: tuto
title: "[Titre Opérationnel de la Tâche]"
sous_titre: "[Sous-titre explicite décrivant l'action concrète dans le sprint]"
slug: "[slug-kebab-case]"
slug_domaine: "[slug_domaine]"
slug_ua: "[slug_ua]"
permalink: /tutos/[slug-kebab-case]/
tuto_id: "T.XXX.YYY"
version: "normal"
ua: "UA.XXX.YY"
maturite: "UA-Tâche"
nav_order: [numéro d'ordre : 1, 2, 3...]
simplified: true
en_construction: false
branche: "sprintX"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Prérequis
- **Base théorique et pratique requise :**
  - [Outil / Notions clés 20/80 requises, ex: Installation et utilisation de GitHub CLI (`gh repo create`)]
  - [Conventions / Branches requises, ex: Création et gestion des branches Git (`sprint[N]`)]
- **Prérequis de projet :** [Présentation du projet par le formateur, tâche/étape antérieure validée]
- **Branche Git :** `sprintX`

## 2. Travail à Faire
- [Synthèse des tâches concrètes et directives à accomplir dans ce tutoriel]

## 3. Étapes de Réalisation
1. **Étape 1 — [Nom étape 1] :** [Consigne directe et directive à l'impératif avec commandes exactes]
2. **Étape 2 — [Nom étape 2] :** [Consigne directe et directive à l'impératif avec commandes exactes]
3. **Étape 3 — [Nom étape 3] :** [Consigne directe et directive à l'impératif avec commandes exactes]

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - [Chemin exact du fichier produit sur la branche sprintX hors dossier labs/]
- **Critères de validation :**
  - [ ] [Critère vérifiable et opposable 1]
  - [ ] [Critère vérifiable et opposable 2]
```

---

# 4. Règles Inviolables
1. **Règle Absolue « Zéro Cours Théorique » :** Les tutoriels `UA-Tâche` ne dispensent aucun cours magistral ni explication conceptuelle passive. La section `Prérequis` énumère uniquement les bases théoriques et pratiques nécessaires sous forme de liste à puces. L'apprenant évalue lui-même sa maîtrise et consulte les labs/ressources théoriques si nécessaire.
2. **Structure Universelle en 4 Sections :** Tout tutoriel `UA-Tâche` doit comporter strictement les sections `1. Prérequis`, `2. Travail à Faire`, `3. Étapes de Réalisation`, `4. Livrables & Critères de Validation`. La section « Positionnement » est bannie (prise en charge par le fil d'Ariane du layout).
3. **Périmètre Strict des Livrables :** Ne lister dans les livrables que les artefacts d'ingénierie formellement exigés par le workflow (exclure les fichiers de configuration utilitaires implicites comme `.gitignore`).
4. **Zéro Affichage de Durée aux Apprenants :** Ne jamais insérer de mention de temps unitaire (`(2h)`, `(4h)`) dans le titre ou le corps de la fiche destinée aux apprenants.
5. **Ciblage Exclusif du Projet d'Imitation :** Toutes les tâches opérationnelles s'exécutent sur le Projet d'imitation (*Blog des Lauréats*).
6. **Livrables Concrets Hors `labs/` sur Branche Unique :** Chaque tâche débouche obligatoirement sur un fichier versionné sur la branche du sprint (`sprintX`) dans les répertoires de projet (`README.md`, `missions/`, `flux-travail/`, `issues/`, `sprints/`). Les livrables de type `UA-Tâche` ne vont JAMAIS dans `labs/`.
7. **Encodage Strict UTF-8 sans BOM :** Tous les fichiers générés respectent la règle 1 de `standards-techniques.md`.
8. **Journalisation Standardisée des Commandes & Compatibilité Terminal :** Dès que la réalisation de la tâche implique la saisie de commandes CLI / terminal par l'apprenant, le tutoriel prescrit la création du fichier journal `[slug-tuto].command.md` déposé dans `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` sur la branche de sprint active. Les commandes sont présentées directement en bloc ```` ```bash ```` (sans double encapsulation Markdown). Les commandes prescrites doivent être directement exécutables sous Windows PowerShell tout en adoptant la syntaxe la plus familière et proche possible des standards Linux (conserver `mkdir`, utiliser `echo "" > <fichier>` au lieu de `touch` ou `New-Item`). Le journal ne consigne que les commandes opérationnelles utiles de la tâche, à l'exclusion formelle des commandes Git (`git add`, `git commit`, `git push`). S'il n'y a aucune commande CLI à exécuter dans le tutoriel (travail purement graphique ou rédactionnel), cette partie ne doit pas être citée.
9. **Gouvernance et Synchronisation Physique par le Master Skill `tutorial-writer` :** L'inspection du référentiel physique (`D:\labs-web\projet-imiation-n3`), la validation des livrables de sprint et leur synchronisation miroir avec les fiches de tutoriels sont gouvernées de manière centralisée par le Master Skill **`tutorial-writer`**. `tutorial-task-writer` garantit la stricte concordance entre le déroulement opérationnel et les dossiers de livrables physiques `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`.
10. **Formatage Strict des Blocs de Code (Zéro Espace & Ligne Vide) :** Tout bloc de code (fenced code block ```` ``` ```` ou ```` ```` ````) doit obligatoirement être précédé d'une ligne vide et commencer strictement à la colonne 0 (sans aucun espace d'indentation), y compris à l'intérieur des listes ordonnées. Le contenu textuel ou Markdown encapsulé doit également débuter à la colonne 0 sans indentation artificielle.
11. **Interdiction des Étapes de Commit/Push :** Les apprenants de Niveau N3 maîtrisent déjà le cycle standard de versionnement Git (validé aux niveaux N1 et N2). Il est formellement interdit d'ajouter une étape directive de commit ou de push (`git add`, `git commit`, `git push`) à la fin des tutoriels. L'apprenant gère son propre cycle de commits atomiques sur la branche de sprint active.