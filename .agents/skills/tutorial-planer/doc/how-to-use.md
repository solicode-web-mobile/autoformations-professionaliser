# Guide Opérationnel : `tutorial-planer`

## 1. Rôle & Déclenchement
Architecte de la progression pédagogique des tutoriels au sein du cursus Solicode (multi-niveaux selon `.agents/rules/`).
Intervient en amont de `tutorial-writer` pour concevoir, auditer et ordonnancer les plans de réalisation par session (`_plan-réalisation-tutos/SX/plan-developpement.md` ou `_tutos/_plan-tuto-*.md`).

## 2. Prompts Types
- *« Conçois la planification de la session S01 en reliant dossier-depart/ au livrable final. »*
- *« Audite ce plan selon les standards pédagogiques, élimine les ruptures cognitives et équilibre les titres. »*
- *« Aligne la liste uas de la fiche session _sessions/S1.md et crée les stubs de tutoriels sous _tutos/. »*

## 3. Déroulement Pas-à-Pas
1. **Cartographie & Sas d'Atterrissage :** Identifier le delta entre `dossier-depart/` et `code-a-apprendre/`. Insérer le sas « Bien Démarrer » (installation + quickstart autonome) en cas de nouvel outil/runtime.
2. **Découpage Continu ($E_{n-1} \to E_n$) :** Ordonner les tutoriels sans saut cognitif.
3. **Titrage Équilibré :** Un seul objectif technique concret en H3 sans entité métier (pas d'Article/Catégorie) + sous-titre logique.
4. **Alignement Référentiel Automatique :** Créer/synchroniser `_sessions/S[X].md`, `_domaines/` et `_uas/` manquantes.
5. **Génération des Stubs (`en_construction: true`) :** Initialiser chaque fichier sous `_tutos/[Domaine]/[UA]/[Code]/[slug].md` avec corps vierge et frontmatter complet.
6. **Validation du Plan :** Renseigner `audite: true` et `statut: "audité et validé"`.

## 4. Livrables & Contrôle Qualité
- [x] Plan de session validé sous `_plan-réalisation-tutos/S[X]/plan-developpement.md`.
- [x] Fiche session `_sessions/S[X].md` synchronisée.
- [x] Domaines et UAs créés/alignés sans entité orpheline.
- [x] Fichiers stubs sous `_tutos/` initialisés avec `en_construction: true`.
- [x] UTF-8 sans BOM et zéro mention de durées aux apprenants.
