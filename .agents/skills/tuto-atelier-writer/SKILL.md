---
name: tuto-atelier-writer
description: Conçoit, structure et rédige les tutoriels d'ateliers pratiques guidés (type: tuto-atelier initial sans notions -> type: tuto-atelier-notions enrichi après validation terrain) pour l'EFP.
version: 3.1.0
---

# 1. Mission & Rôle
Rédacteur technique et pédagogique de l'écosystème `tuto-*-writer`, dédié aux tutoriels d'ateliers pratiques pour l'EFP (assimilation conceptuelle, modélisation UML/schémas, architecture, frameworks, outillage IA).
Applique le socle transversal, l'organisation des livrables et la maturation gouvernés par [tuto-writer](../tuto-writer/SKILL.md), [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md) et [.agents/references/maturation-et-typologie-ua-tuto.md](../../references/maturation-et-typologie-ua-tuto.md).

- **Livrables canoniques d'un atelier pratique :**
  1. Fiche didactique : `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].md`
  2. Diaporama Marp : `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/presentation-[slug-tuto].md`
  3. Rapport d'exécution CLI : `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].command.md` (si commandes CLI exécutées).

- **Cycle de Maturation en 2 Types d'Ateliers :**
  - **Type `tuto-atelier` (Atelier Initial Brut — Avant Réalisation) :** Fiche de cadrage orientée recherche active (Travail à faire + Ce que l'apprenant doit apprendre + Pistes de recherche), **SANS donner les notions de base en détail** (`statut_realisation: "a_realiser"`).
  - **Type `tuto-atelier-notions` (Atelier Enrichi — Post-Validation Terrain) :** Fiche consolidée intégrant les **notions de base DONNÉES EN DÉTAIL** (« Notions fondamentales » vérifiées sur le terrain) et les liens vers les livrables validés (`statut_realisation: "realise"`).

---

# 2. Déclenchement & Limites
- **Activer :** Ateliers `tuto-atelier` et `tuto-atelier-notions` ; modélisation UML (Mermaid) ; ateliers agiles Scrum ; dossiers d'architecture (ADR) ; prompts directifs RIO.
- **Ne PAS activer :** Code incrémental pas-à-pas ➔ `tuto-code-writer` (`tuto-code`) | Tâches de projet / cérémonies sans théorie ➔ `tuto-tache-writer` (`tuto-tache`) | Planification globale ➔ `didactique-tuto-planner` | Gouvernance & synchronisation ➔ `tuto-writer`.

---

# 3. Structures Normées des Fiches d'Ateliers

Frontmatter commun : `layout: tuto`, `title:`, `sous_titre:`, `slug:`, `permalink:`, `tuto_id:`, `ua:`, `type: "tuto-atelier" | "tuto-atelier-notions"`, `statut_realisation: "a_realiser" | "realise"`, `nav_order:`, `simplified: true`, `en_construction: false`, `branche: "sprintX"`.
*(Rappel : la métadonnée `maturite:` est portée exclusivement par l'UA parente dans `_uas/`).*

### A. Fiche Initiale `type: "tuto-atelier"` (Recherche Active Initiale — Sans Notions Détaillées)
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

### B. Fiche Enrichie `type: "tuto-atelier-notions"` (Post-Validation & Livrables Réalisés)
```markdown
## 1. Contexte & Enjeux
## 2. Notions fondamentales (Données en Détail)
- **[Concept 1] :** [Définition discriminante complète, syntaxe et exemples vérifiés]
- **[Concept 2] :** [Explications consolidées issues de la pratique terrain]
## 3. Travail réalisé & Livrables
- [Synthèse des livrables et liens vers les fichiers de restitution]
```
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
7. **Chemins Canoniques & Livrables Complets :** Conforme à [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md) et [.agents/references/maturation-et-typologie-ua-tuto.md](../../references/maturation-et-typologie-ua-tuto.md). Dossier `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` contenant obligatoirement `[slug-tuto].md`, `presentation-[slug-tuto].md` et `[slug-tuto].command.md` (si CLI). Proscrire les dossiers orphelins (`labs/`), les `README.md` unitaires et les captures d'écran.
8. **Versionnement Git :** Respecter l'autonomie Git du niveau actif selon [.agents/references/gitflow.md](../../references/gitflow.md).
9. **Gouvernance :** Réfère au Master Skill [tuto-writer](../tuto-writer/SKILL.md) pour les règles partagées et la synchronisation avec le projet cible via `.sync/rules-sync.md`.
