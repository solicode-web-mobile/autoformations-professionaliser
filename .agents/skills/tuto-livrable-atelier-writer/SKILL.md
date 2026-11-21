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
1. **Socle & Gouvernance :** Fait respecter le socle transversal gouverné par [tuto-writer](../tuto-writer/SKILL.md) (encodage UTF-8 sans BOM, Markdown colonne 0, zéro capture d'écran, style A1-A2).
2. **Expertise Technique Métier :** Invoque le skill thématique du domaine concerné :
   - Scrum / Agilité ➔ [tuto-writer-scrum](../tuto-writer-scrum/SKILL.md)
   - UML / Modélisation ➔ [tuto-writer-uml](../tuto-writer-uml/SKILL.md)
   - Architecture logicielle ➔ [tuto-writer-architecture](../tuto-writer-architecture/SKILL.md)
   - Laravel / Back-end ➔ [tuto-writer-laravel](../tuto-writer-laravel/SKILL.md)
   - IA & Agents ➔ [tuto-writer-ia](../tuto-writer-ia/SKILL.md)

---

# 4. Règles Inviolables
1. **Emplacement de Référence sur le Site :** Tout livrable d'atelier d'autoformation réside strictement sous `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/` (le dossier `tutoriels/` étant réservé au poste apprenant).
2. **Format Marp Interactif :** Les diaporamas portent obligatoirement dans leur frontmatter `layout: presentation` et `marp: true` pour être consultables en diaporama plein écran sur le site Jekyll.
3. **Promotion de la Fiche Jekyll :** À l'issue de la réalisation, mettre à jour la fiche `_tutos/...` :
   - Basculer `type: "tuto-atelier-notions"` et `statut_realisation: "realise"`.
   - Mettre à jour `livrables:` avec les chemins `ua-lab/...`.
   - Injecter les **notions fondamentales consolidées** dans le corps du tutoriel.
4. **Zéro Commande Git dans `.command.md` :** Ne consigner que les commandes techniques de l'atelier (jamais `git add`, `commit`, `push`).

---

# 5. Procédure Pas-à-Pas
1. **Étape 1 — Analyse du Sujet :** Lire la fiche `_tutos/.../[slug-tuto].md` rédigée par `tuto-atelier-writer`.
2. **Étape 2 — Génération des Livrables dans `ua-lab/` :** Créer le sous-dossier et rédiger `[slug-tuto].md`, `presentation-[slug-tuto].md` et `[slug-tuto].command.md` avec le skill thématique de domaine.
3. **Étape 3 — Promotion du Tutoriel :** Modifier le tutoriel `_tutos/` en `type: "tuto-atelier-notions"` et enrichir le contenu avec les notions fondamentales.
