---
name: tuto-livrable-atelier-writer
description: Réalise concrètement le travail prescrit par les tutoriels d'ateliers (tuto-atelier) en produisant les livrables d'ateliers sous ua-lab/ et en promouvant la fiche Jekyll en tuto-atelier-notions.
version: 1.0.0
---

# 1. Mission & Rôle
Opérateur technique de réalisation d'ateliers pour l'Agent Rédacteur d'Autoformation.
Prend en charge l'exécution concrète du travail à faire formulé par [tuto-atelier-writer](../tuto-atelier-writer/SKILL.md) et produit l'ensemble des livrables de référence sous `ua-lab/`.

- **Livrables produits sous `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/` :**
  1. Fiche de restitution réalisée : `[slug-tuto].md` (synthèse, schémas Mermaid, analyse, cas d'usage résolu).
  2. Diaporama Marp interactif : `presentation-[slug-tuto].md` (format 16:9 avec frontmatter `layout: presentation`).
  3. Journal d'exécution CLI : `[slug-tuto].command.md` (si des manipulations terminal font partie de l'atelier).
  4. Fichiers de ressources ou code d'exercice du lab (si nécessaire).

---

# 2. Déclenchement & Limites
- **Activer :** Réalisation concrète d'une UA-Lab ou d'un tutoriel d'atelier `tuto-atelier` ; production de livrables d'ateliers dans `ua-lab/` ; promotion d'une fiche `_tutos/` en `tuto-atelier-notions`.
- **Ne PAS activer :** Rédaction de l'énoncé/sujet du tutoriel d'atelier ➔ `tuto-atelier-writer` | Rédaction de tâches de sprint ➔ `tuto-tache-writer` | Code incrémental de projet ➔ `tuto-code-writer` | Cadrage macro de session ➔ `didactique-session-planner`.

---

# 3. Mobilisation des Skills Spécifiques & Orchestration
Pour chaque atelier à réaliser, `tuto-livrable-atelier-writer` coordonne l'écosystème :
1. **Délégation de Rédaction à `tuto-notion-writer` :** La rédaction de la fiche technique d'atelier `[slug-tuto].md` est obligatoirement déléguée à [tuto-notion-writer](../tuto-notion-writer/SKILL.md). La fiche porte `type: "tuto-notion"` et `layout: default`.
2. **Socle & Gouvernance :** Fait respecter le socle transversal gouverné par [tuto-writer](../tuto-writer/SKILL.md) (encodage UTF-8 sans BOM, Markdown colonne 0, zéro capture d'écran, style A1-A2).
3. **Expertise Technique Métier :** Invoque le skill thématique du domaine concerné :
   - Scrum / Agilité ➔ [tuto-writer-scrum](../tuto-writer-scrum/SKILL.md)
   - UML / Modélisation ➔ [tuto-writer-uml](../tuto-writer-uml/SKILL.md)
   - Architecture logicielle ➔ [tuto-writer-architecture](../tuto-writer-architecture/SKILL.md)
   - Laravel / Back-end ➔ [tuto-writer-laravel](../tuto-writer-laravel/SKILL.md)
   - IA & Agents ➔ [tuto-writer-ia](../tuto-writer-ia/SKILL.md)

---

# 4. Règles Inviolables
1. **Emplacement de Référence sur le Site :** Tout livrable d'atelier d'autoformation réside strictement sous `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/` (le dossier `tutoriels/` étant réservé au poste apprenant).
2. **Format Marp & Exclusion de Navigation :** Les diaporamas portent obligatoirement dans leur frontmatter `layout: presentation`, `marp: true` et `nav_exclude: true` pour être consultables en plein écran sans polluer la navbar. La fiche de restitution `[slug-tuto].md` porte également `nav_exclude: true`. Zéro mention d'encadrant ni d'établissement.
3. **Règles de Rédaction & Niveau de Détail Approfondi :** La fiche `[slug-tuto].md` applique un haut niveau de détail pédagogique adapté aux débutants : explications narratives complètes (zéro liste sèche) selon le plan : 1. Contexte & Objectif, 2. Données de départ, 3. Notions Essentielles (développées), 4. Pratique & Réalisation Guidée (tableau pas-à-pas), 5. Livrables & Critères, 6. Glossaire.
4. **Promotion de la Fiche Jekyll :** À l'issue de la réalisation, promouvoir la fiche `_tutos/...` en `type: "tuto-atelier-notions"` (`statut_realisation: "realise"`) avec déclaration du bloc `livrables:`.
5. **Zéro Commande Git dans `.command.md` :** Ne consigner que les commandes techniques de l'atelier (jamais `git add`, `commit`, `push`).
6. **Manifeste `version.yml` Obligatoire :** Créer obligatoirement un fichier `version.yml` à la racine du dossier de livrables (`ua-lab/.../version.yml`) recensant chaque livrable produit et sa version.

---

# 5. Procédure Pas-à-Pas
1. **Étape 1 — Analyse du Sujet :** Lire la fiche `_tutos/.../[slug-tuto].md` rédigée par `tuto-atelier-writer`.
2. **Étape 2 — Génération des Livrables dans `ua-lab/` :** Créer le sous-dossier, rédiger les livrables (`.md`, `presentation-*.md`, `.command.md`) et générer `version.yml` avec les versions sémantiques.
3. **Étape 3 — Promotion du Tutoriel :** Modifier le tutoriel `_tutos/` en `type: "tuto-atelier-notions"`, ajouter le bloc `livrables:` validé et enrichir le contenu avec les notions fondamentales.
