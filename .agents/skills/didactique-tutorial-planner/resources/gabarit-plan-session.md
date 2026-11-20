# Gabarit Normé — Plan de Réalisation d'une Session

Modèle de référence pour tout fichier `_plan-réalisation-tutos/S[X]/plan-developpement.md`. Relie le `dossier-depart/` au **livrable complet final** (transformé avec le `code-a-apprendre/`).

```markdown
---
session: "S[X]"
version: "1.0.0"
audite: true
date_audit: "AAAA-MM-JJ"
statut: "audité et validé"
---

# Plan de Réalisation — Progression [Nom du Domaine] (Session S[X])

**Voie :** [Ex: Développement Web Applicatif] | **Session :** S[X] — [Titre clair] | **Niveau :** [N1/N2/N3]

## 1. Contexte & Objectif
- **Objectif central :** [Objectif concret et observable]
- **Stack & Architecture :** [Outils et organisation des flux]
- **Transformation :** `dossier-depart/` enrichi et transformé vers le livrable complet final.

## 2. Articulation Temporelle
- **Acquis Passés :** [Acquis mobilisés des sessions antérieures]
- **UAs du Sprint :** 1 seule UA par domaine (ou 2 au démarrage technologique : 1. Bien démarrer + 2. Projet applicatif).
- **Perspectives :** [Continuité vers S[X+1]]

## 3. Fiches de Conception Détaillées des Tutoriels
<!-- RÈGLES : Titre H3 = 1 seul objectif technique sans entité métier (pas d'Article/Catégorie). Sous-titre = objectif logique. E_n-1 = sortie de N-1. -->

### T.[Code] — [Titre Équilibré : Un Seul Objectif Technique Concret]
*Objectif logique : [Titre logique / conceptuel]*  
*Unités d'Apprentissage (UA) :* UA.[Code] — [Libellé officiel] ([Domaine])

- **Progression pédagogique :** [Brique de code ajoutée ou transformée vers le projet cible]
- **1. Ce que l'apprenant doit apprendre :** [Notions cibles, syntaxe, fonctions, règles de code]
- **2. Description technique :** [Action concrète modifiant les fichiers issus de `dossier-depart/`]
- **3. Fichiers impactés :** `[chemin/nom-fichier]`
- **4. État de départ ($E_{n-1}$) :** [Extrait représentatif avant manipulation]
- **5. État d'arrivée ($E_n$) :** [Extrait représentatif après manipulation]
- **6. Livrable physique tapé :** [Code source ou fichier `commandes.md`. Zéro constat verbal sans code]. Cible : `[chemin/fichier]`.

## 4. Articulation vers les Projets (Triade Active)
1. **Tutoriels :** Comprendre avec le minimum de code sur le projet guidé.
2. **Projet d'Imitation :** Livrable complet de session issu de la transformation de `dossier-depart/`.
3. **Projet Prototype :** Réinvestissement autonome sur un cas similaire sans pas-à-pas.
4. **Projet Fil Rouge :** Transfert et consolidation de la compétence métier.
```
