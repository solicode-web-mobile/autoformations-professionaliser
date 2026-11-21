---
name: tutorial-lab-writer
description: Conçoit, structure et rédige les tutoriels d'ateliers pratiques guidés (type: tuto-atelier) pour l'EFP, en gérant le cycle de maturation (maturite: lab sans notions détaillées -> maturite: ua-lab avec notions détaillées après validation).
version: 3.0.0
---

# 1. Mission & Rôle
Rédacteur technique et pédagogique de l'écosystème `tutorial-*-writer`, dédié aux tutoriels de type **`tuto-atelier`** pour l'EFP (assimilation conceptuelle, modélisation UML/schémas, architecture, frameworks, outillage IA).
Applique le socle transversal, l'organisation des livrables et la maturation gouvernés par [tutorial-writer](../tutorial-writer/SKILL.md), [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md), [.agents/references/typologie-uas-tutoriels.md](../../references/typologie-uas-tutoriels.md) et [.agents/references/maturation-ua-labs.md](../../references/maturation-ua-labs.md).

- **Livrables canoniques d'un `tuto-atelier` :**
  1. Fiche didactique : `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].md`
  2. Diaporama Marp : `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/presentation-[slug-tuto].md`
  3. Rapport d'exécution CLI : `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].command.md` (si commandes CLI exécutées).

- **Cycle de Maturation en 2 Phases (`lab` ➔ `ua-lab`) :**
  - **En `maturite: "lab"` (Avant Réalisation) :** Fiche de cadrage orientée recherche active (Travail à faire + Ce que l'apprenant doit apprendre + Pistes de recherche), **SANS donner les notions de base en détail**.
  - **En `maturite: "ua-lab"` (Post-Validation EFP) :** Fiche consolidée intégrant la spécification formelle du plan de l'UA-Lab et les **notions de base DONNÉES EN DÉTAIL** (« Notions fondamentales » vérifiées sur le terrain).

---

# 2. Déclenchement & Limites
- **Activer :** Ateliers `tuto-atelier` en maturité `lab` ou `ua-lab` ; modélisation UML (Mermaid) ; ateliers agiles Scrum ; dossiers d'architecture (ADR) ; prompts directifs RIO.
- **Ne PAS activer :** Code incrémental pas-à-pas ➔ `tutorial-code-writer` (`tuto-code`) | Tâches de projet / cérémonies sans théorie ➔ `tutorial-task-writer` (`tuto-tache`) | Planification globale ➔ `didactique-tutorial-planner` | Gouvernance & synchronisation ➔ `tutorial-writer`.

---

# 3. Structures Normées des Fiches `tuto-atelier`

Frontmatter commun : `layout: tuto`, `title:`, `sous_titre:`, `slug:`, `permalink:`, `tuto_id:`, `ua:`, `maturite: "lab" | "ua-lab"`, `type: "tuto-atelier"`, `nav_order:`, `simplified: true`, `en_construction: false`, `branche: "sprintX"`.

### A. Fiche en Maturité `lab` (Recherche Active Initiale — Sans Notions Détaillées)
```markdown
## 1. Contexte & Enjeux
[Pourquoi ce domaine/outil est abordé dans le sprint de l'EFP]

## 2. Ce que vous devez apprendre
- [Compétence cible à acquérir]
- [Problématiques techniques à explorer]
- [Questions directrices auxquelles répondre]

## 3. Travail à faire
- [Consignes directives sur ce que l'apprenant doit concevoir et produire]

## 4. Pistes de recherche active
- [Concepts clés et documentations officielles à investiguer]

## 5. Livrables attendus & Critères de validation
- **Fiche de restitution :** `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].md`
- **Diaporama Marp :** `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/presentation-[slug-tuto].md`
- **Rapport CLI :** `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].command.md` (si commandes exécutées)
```

### B. Fiche en Maturité `ua-lab` (Post-Validation & Intégration Référentiel EFP)
```markdown
## 1. Contexte & Enjeux
## 2. Plan Spécifié de l'UA-Lab
- [Spécification des tâches validées et ancrage dans la compétence certifiante C.xxx]
## 3. Notions fondamentales (Données en Détail)
- **[Concept 1] :** [Définition discriminante complète, syntaxe et exemples vérifiés]
- **[Concept 2] :** [Explication technique approfondie]
## 4. Travail Réalisé & Synthèse
- [Rappel du cahier des charges et restitution validée]
## 5. Recherches à effectuer (Approfondissements)
- [Pistes d'investigation avancée]
## 6. Livrables Validés
- Emplacements canoniques conformes sous `tutoriels/`.
```

---

# 4. Règles Inviolables
1. **Dissociation Absolue Maturité / Type :** Le tutoriel porte obligatoirement `type: "tuto-atelier"` et `maturite: "lab"` (au départ) ou `maturite: "ua-lab"` (après validation).
2. **Discrétion des Notions en Phase `lab` :** Interdiction absolue de rédiger les notions théoriques détaillées dans une fiche en maturité `lab`. L'apprenant doit chercher par lui-même.
3. **Autonomie de la Pratique (Zéro Solution Clé en Main) :** Fournir spécifications rigoureuses, cahier des charges RIO et étapes directives, mais interdiction formelle de fournir la solution rédigée complète prête à copier-coller.
4. **Zéro Fuite Didactique :** Interdiction des termes « 20/80 », « Règle des 20/80 » ou « Ce que l'apprenant doit produire ». Utiliser « Notions fondamentales » et « Recherches à effectuer ».
5. **Zéro Durée Affichée & Zéro Jalon :** Aucune mention de temps (`(2h)`) aux apprenants. Terme direct « Étape » obligatoire (« Jalon » proscrit).
6. **Formatage Colonne 0 & UTF-8 :** Tout bloc de code débute strictement colonne 0 (zéro indentation), précédé et suivi d'une ligne vide. UTF-8 sans BOM.
7. **Chemins Canoniques & Livrables Complets :** Conforme à [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md) et [.agents/references/typologie-uas-tutoriels.md](../../references/typologie-uas-tutoriels.md). Dossier `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` contenant obligatoirement `[slug-tuto].md`, `presentation-[slug-tuto].md` et `[slug-tuto].command.md` (si CLI). Proscrire les dossiers orphelins (`labs/`), les `README.md` unitaires et les captures d'écran.
8. **Versionnement Git :** Respecter l'autonomie Git du niveau actif selon [.agents/references/gitflow.md](../../references/gitflow.md).
9. **Gouvernance :** Réfère au Master Skill [tutorial-writer](../tutorial-writer/SKILL.md) pour les règles partagées et la synchronisation avec le projet cible via `.sync/rules-sync.md`.
