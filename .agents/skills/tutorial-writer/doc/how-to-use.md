# Guide d'Utilisation du Skill : tutorial-writer

## 1. Présentation & Rôle
`tutorial-writer` est l'**artisan pédagogique universel** chargé de concevoir et rédiger les guides d'apprentissage techniques pas-à-pas (tutoriels) pour les apprenants Solicode (Niveaux N1, N2, N3 selon les règles locales du dépôt).

Tout tutoriel produit est **directement et nativement simplifié dès sa conception** : sans surcharge cognitive, visuel d'abord, théorie courte (règle des 20/80), et pratique ultra-ciblée. Il applique en permanence le cycle de pédagogie active :
$$\text{Comprendre} \longrightarrow \text{Reproduire} \longrightarrow \text{Expérimenter} \longrightarrow \text{Réaliser} \longrightarrow \text{Réutiliser}$$

---

## 2. Cas d'Usage Principaux
- Rédaction d'une **série progressive de tutoriels** à partir d'un plan de session validé et du code cible.
- Rédaction d'un **tutoriel unitaire autonome** (apprentissage isolé d'une notion avec son micro-livrable).
- Modernisation ou allègement d'un tutoriel existant trop verbeux ou dense pour le niveau visé.
- Application de la **règle Pareto 20/80** pour l'assimilation théorique.
- En N3 : Rédaction ciblée exclusivement sur le **Projet d'imitation** (*Blog des Lauréats*) sur la branche Git `sprintX`.

---

## 3. Prompts Types d'Invocation

```markdown
# Rédaction d'un tutoriel planifié en N3 sur la branche sprint1
@[.agents/skills/tutorial-writer/SKILL.md] Rédige le tutoriel T.321.112 défini dans _tutos/_plan-tuto-D.321.1-laravel.md pour la route d'accueil du Blog des Lauréats sur la branche sprint1.
```

```markdown
# Rédaction d'un tutoriel unitaire simplifié
@[.agents/skills/tutorial-writer/SKILL.md] Rédige un tutoriel unitaire simplifié pour apprendre à manipuler les collections en Laravel.
```

```markdown
# Simplification avec la règle Pareto 20/80
@[_tutos/D.321.1.laravel/UA.321.11/T.321.111/theorie-routage-et-vues.md] @[.agents/skills/tutorial-writer/SKILL.md] Applique la règle Pareto 20/80 : fournis 20% de définitions fondamentales et confie 80% à la recherche active.
```

---

## 4. Prérequis & Données d'Entrée
- **Plan de cadrage :** Fiche technique du tutoriel issue de `_tutos/_plan-tuto-D.XXX.Y-*.md` (N3) ou `plan-developpement.md` (N1/N2).
- **Branche Git :** Branche unique du sprint (ex: `sprint1` en N3).
- **Ciblage Exclusif :** Le corps du tutoriel guide l'apprenant exclusivement sur le Projet d'imitation (*Blog des Lauréats*).
- **Règles applicables :**
  - `.agents/rules/pedagogie-spartel-n3.md` (Pareto 20/80, pas de durée affichée aux apprenants, style direct impératif).
  - `.agents/rules/standards-techniques.md` (Strict UTF-8 sans BOM, livrables de code source et markdown).

---

## 5. Déroulement Pas-à-Pas (Ce que fait l'Agent)
1. **Étape 1 — Cadrage & Chargement du Domaine :** Identifie le domaine technique et prend connaissance des contraintes du niveau N3.
2. **Étape 2 — Structuration du Front Matter :** Renseigne `layout: tuto`, l'UA, le code tuto, le titre canonique (sans mention de durée), la branche du sprint, et configure `en_construction: false` dès validation.
3. **Étape 3 — Rédaction de la Théorie Simplifiée (Pareto 20/80) :** Fournit les 20% de définitions indispensables et formule les 80% de points d'approfondissement confiés à la recherche active de l'apprenant.
4. **Étape 4 — Rédaction de la Pratique Guidée :** Formule des consignes séquentielles à l'impératif direct (*« Ouvrez »*, *« Ajoutez »*, *« Testez »*) sur le Projet d'imitation.
5. **Étape 5 — Clôture & Livrable sur Branche Git :** Précise l'emplacement exact des fichiers impactés dans le projet et les critères de validation `[ ]`.

---

## 6. Livrables Produits & Méthode de Vérification
- **Livrables attendus :**
  - Fichier Markdown normé : `_tutos/[Domaine]/[UA]/[Code-Tuto]/[slug-tuto].md`.
- **Comment vérifier le résultat :**
  - [x] Le tutoriel cible exclusivement le Projet d'imitation.
  - [x] Zéro mention de durée de tâche n'est visible pour l'apprenant.
  - [x] La branche Git du sprint (ex : `sprint1`) est clairement spécifiée.
  - [x] Toutes les consignes sont formulées à l'impératif direct.
  - [x] Le statut est configuré à `en_construction: false` dès que le tutoriel est finalisé.
  - [x] Le fichier est encodé en UTF-8 sans BOM.