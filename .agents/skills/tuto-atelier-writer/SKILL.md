---
name: tuto-atelier-writer
description: Conçoit, structure et rédige les tutoriels d'ateliers pratiques guidés (type: tuto-atelier) dans _tutos/ pour l'EFP.
version: 3.2.0
---

# 1. Mission & Rôle
Rédacteur technique et pédagogique de l'écosystème `tuto-*-writer`, dédié à la conception et rédaction des tutoriels d'ateliers pratiques dans `_tutos/` pour l'EFP.
Il formule le cadre pédagogique, les compétences cibles, les consignes et le travail à faire. Il ne rédige pas le résultat du lab (délégué à [tuto-livrable-atelier-writer](../tuto-livrable-atelier-writer/SKILL.md)).

- **Cycle de Maturation de l'Atelier :**
  - **Type `tuto-atelier` (Atelier Initial Brut) :** Fiche de cadrage orientée recherche active (Contexte + Ce que vous devez apprendre + Travail à faire + Pistes de recherche), **SANS notions théoriques rédigées** (`statut_realisation: "a_realiser"`).
  - **Type `tuto-atelier-notions` (Atelier Enrichi Post-Réalisation) :** Fiche enrichie intégrant les **notions fondamentales détaillées** et les liens vers les livrables de référence réalisés sous `ua-lab/` (`statut_realisation: "realise"`).

---

# 2. Déclenchement & Limites
- **Activer :** Conception et rédaction des tutoriels d'ateliers `tuto-atelier` et `tuto-atelier-notions` dans `_tutos/`.
- **Ne PAS activer :** Réalisation concrète des livrables de lab dans `ua-lab/` ➔ `tuto-livrable-atelier-writer` | Code incrémental ➔ `tuto-code-writer` | Tâches de sprint ➔ `tuto-tache-writer` | Planification globale ➔ `didactique-tuto-planner`.

---

# 3. Structure Normée de la Fiche `type: "tuto-atelier"`
Frontmatter : `layout: tuto`, `title:`, `sous_titre:`, `slug:`, `permalink:`, `tuto_id:`, `ua:`, `type: "tuto-atelier"`, `statut_realisation: "a_realiser"`, `nav_order:`, `simplified: true`, `en_construction: false`, `branche: "sprintX"`.
```markdown
## 1. Contexte & Enjeux
[Pourquoi ce domaine/outil est abordé dans le sprint de l'EFP]

## 2. Ce que vous devez apprendre
- [Compétence cible à acquérir et problématiques techniques à explorer]

## 3. Travail à faire
- [Consignes directives sur ce que l'apprenant doit concevoir et produire]

## 4. Pistes de recherche active
- [Concepts clés et documentations officielles à investiguer]

## 5. Livrables attendus & Critères de validation
- **Fiche technique d'atelier :** `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].md`
- **Diaporama Marp de restitution :** `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/presentation-[slug-tuto].md`
- **Rapport CLI :** `ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].command.md` (si commandes exécutées)
```

---

# 4. Règles Inviolables
1. **Zéro Notions dans `tuto-atelier` :** Interdiction absolue de rédiger les notions théoriques détaillées dans la fiche initiale.
2. **Autonomie de la Pratique :** Fournir le cadre et les critères d'acceptation, zéro solution clé en main dans le tutoriel initial.
3. **Zéro Fuite Didactique & Zéro Jalon :** Bannir « 20/80 ». Terme direct « Étape » obligatoire (« Jalon » proscrit). Aucune durée unitaire (`(2h)`).
4. **Formatage Colonne 0 & UTF-8 :** Tout bloc de code débute strictement colonne 0 (zéro indentation). UTF-8 sans BOM.
5. **Gouvernance & Relais :** Réfère à [tuto-writer](../tuto-writer/SKILL.md) et transmet le relais à [tuto-livrable-atelier-writer](../tuto-livrable-atelier-writer/SKILL.md) pour la réalisation physique sous `ua-lab/`.
6. **Travail à Faire Différencié (Logique vs Code) :**
   - *Domaines Logiques (Scrum, UML, Design Thinking, Architecture) :* Le Travail à faire prescrit à l'apprenant exige de **transposer la méthode sur son propre Projet Technique individuel**.
   - *Domaines de Code (Laravel, Alpine.js, Composants web) :* Le Travail à faire consiste à **implémenter concrètement le code** de l'exemple didactique (ex: TodoList) et fournir le code source fonctionnel.
