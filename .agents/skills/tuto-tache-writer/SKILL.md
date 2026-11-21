---
name: tuto-tache-writer
description: Conçoit, structure et rédige les fiches de tutoriels opérationnels de projet et cérémonies de sprint pour l'EFP (maturite: projet, type: tuto-tache, Cadrage, Sprint Planning, Review, Rétrospective, Refinement, Débriefing, Prompts de cérémonies). 0% théorie.
version: 2.3.0
---

# 1. Mission & Rôle
Rédacteur opérationnel de l'écosystème `tutorial-*-writer`, chargé des fiches de type **`tuto-tache`** en maturité **`projet`** pour l'EFP (cadrage, rituels agiles, outillage IA de cérémonies, bilans).
Applique le socle transversal, l'organisation des livrables et la synchronisation gouvernés par [tuto-writer](../tuto-writer/SKILL.md), [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md) et [.agents/references/maturation-et-typologie-ua-tuto.md](../../references/maturation-et-typologie-ua-tuto.md).
- **Distinction :**
  - `tuto-code` / `tuto-notion` = code incrémental pas-à-pas ([tuto-code-writer](../tuto-code-writer/SKILL.md)) ;
  - `tuto-atelier` = atelier guidé avec diaporama Marp ([tuto-atelier-writer](../tuto-atelier-writer/SKILL.md)) ;
  - `tuto-tache` = **0% théorie**, 100% action opérationnelle, livrables aux emplacements racine du projet, **sans `.command.md`** et **sans diaporama Marp**.

---

# 2. Déclenchement & Limites
- **Activer :** Fiches `tuto-tache` en maturité `projet` ; guides de cérémonies agiles (Planning, Review, Rétro, Refinement, Débriefing) ; cadrage de projet ; prompts de cérémonies agiles.
- **Ne PAS activer :** Code incrémental pas-à-pas ➔ `tuto-code-writer` | Ateliers guidés / modélisation / théorie ➔ `tuto-atelier-writer` | Planification de session ➔ `didactique-tuto-planner` | Gouvernance transversale & synchronisation ➔ `tuto-writer`.

---

# 3. Structure Normée en 4 Sections
Toute fiche `tuto-tache` adopte strictement ce gabarit :

```markdown
---
layout: tuto
title: "[Titre Opérationnel de la Tâche]"
sous_titre: "[Action concrète dans le sprint]"
slug: "[slug-kebab-case]"
slug_domaine: "[slug_domaine]"
slug_ua: "[slug_ua]"
permalink: /tutos/[slug-kebab-case]/
tuto_id: "T.XXX.YYY"
version: "normal"
ua: "UA.XXX.YY"
maturite: "projet"
type: "tuto-tache"
nav_order: 1
simplified: true
en_construction: false
branche: "sprintX"
---

## 1. Prérequis
- **Base requise :** [Outils / notions indispensables sous forme de puces sans cours théorique]
- **Prérequis de projet :** [Étape antérieure validée sur la branche Git active]

## 2. Travail à Faire
- [Synthèse directive des actions concrètes à accomplir]

## 3. Étapes de Réalisation
1. **Étape 1 — [Nom] :** [Consigne directe à l'impératif avec commandes exactes]
2. **Étape 2 — [Nom] :** [Consigne directe à l'impératif avec commandes exactes]

## 4. Livrables & Critères de Validation
- **Livrables attendus :** Emplacements racine officiels (`docs/cadrage/`, `docs/conception/`, `docs/produit/`, `sprints/`, `src/`, etc.) conformément à `.agents/references/organisation-livrables.md`. Jamais dans `labs/`.
- **Critères de validation :**
  - [ ] [Critère vérifiable binaire 1]
  - [ ] [Critère vérifiable binaire 2]
```

---

# 4. Règles Inviolables
1. **Zéro Cours Théorique :** Aucun exposé passif. `Prérequis` liste uniquement les bases requises.
2. **4 Sections Strictes :** `1. Prérequis`, `2. Travail à Faire`, `3. Étapes de Réalisation`, `4. Livrables & Critères`. Section « Positionnement » bannie.
3. **Périmètre des Livrables :** Positionnés aux emplacements racine officiels (`docs/`, `sprints/`, `src/`) selon [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md). Zéro capture d'écran.
4. **Zéro Diaporama Marp :** Aucun fichier `presentation-[slug-tuto].md` n'est demandé pour une tâche opérationnelle.
5. **Rapport CLI Non Autorisé (`[slug-tuto].command.md`) :** Pour une tâche `tuto-tache`, le journal des commandes est **formellement non requis et non autorisé**. Les modifications opérationnelles s'appliquent directement sur les fichiers du projet.
6. **Zéro Durée Affichée :** Pas de temps unitaire (`(2h)`) exposé aux apprenants.
7. **Ciblage & Branche :** Exécution sur le projet cible et la branche configurés dans `.agents/rules/`. Hors dossier `labs/`.
8. **Formatage Colonne 0 & UTF-8 :** Tout bloc de code débute à la colonne 0 précédé et suivi d'une ligne vide. UTF-8 sans BOM.
9. **Terminologie & Versionnement :** Terme direct « Étape » obligatoire (terme « Jalon » proscrit). Respect de l'autonomie Git du niveau actif (aucun commit/push imposé si autonomie prescrite selon `.agents/references/gitflow.md`).
10. **Gouvernance :** Réfère au Master Skill [tuto-writer](../tuto-writer/SKILL.md) pour les règles partagées et la synchronisation avec le projet cible via `.sync/rules-sync.md`.
