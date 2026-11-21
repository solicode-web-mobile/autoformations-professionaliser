# Skill : didactique-tuto-planner (Tous Niveaux N1, N2, N3)

## Présentation
Le skill **`didactique-tuto-planner`** est l'expert du niveau **Micro (Tutoriels & Progression)**, opérant de façon **générique sur l'ensemble des 3 niveaux (N1, N2, N3)**. Il intervient une fois la session et ses UAs cadrées par `didactique-session-planner` pour concevoir le découpage pas-à-pas déterministe ($E_{n-1} \to E_n$), formuler les titres techniques équilibrés et générer les stubs Jekyll réservant la navigation sous `_tutos/`.

## Responsabilités Clés
1. **Progression Continue ($E_{n-1} \to E_n$) :** Élimination de tout saut conceptuel reliant le code de départ au code final.
2. **Titrage Équilibré :** Titres H3 purement techniques sans mention des entités métier du cas exemple (Article, Catégorie, etc.) + sous-titres logiques.
3. **Sas « Bien Démarrer » :** Insertion systématique du sas d'installation et de démarrage rapide autonome pour toute nouvelle technologie ou runtime.
4. **Matérialisation Jekyll & Stubs :** Synchronisation des collections Jekyll et création physique des stubs sous `_tutos/` avec `en_construction: true`.

## Gabarits Disponibles (`resources/`)
Le skill encapsule 6 gabarits normés sous son dossier `resources/` :
- `methode-bien-demarrer.md` : Guide du sas d'atterrissage.
- `gabarit-plan-session.md` : Structure type d'un plan de réalisation de tutoriels.
- `gabarit-session.md`, `gabarit-domaine.md`, `gabarit-ua.md` : Modèles d'entités Jekyll.
- `gabarit-tuto-en-construction.md` : Modèle de stub de tutoriel.

## Prompts Types
- **Planifier la progression d'une UA (N1, N2 ou N3) :**
  > « Active didactique-tuto-planner pour concevoir le plan séquentiel des tutoriels de l'UA, formuler des titres équilibrés et initialiser les stubs dans _tutos/. »
- **Auditer un plan de tutoriels existant :**
  > « Utilise didactique-tuto-planner pour auditer le plan de réalisation, supprimer les entités métier des titres H3 et vérifier la continuité E_{n-1} -> E_n. »