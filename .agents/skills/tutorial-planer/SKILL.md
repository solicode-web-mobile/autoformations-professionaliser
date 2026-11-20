---
name: tutorial-planer
description: Conçoit, audite et optimise les plans de réalisation et la progression pédagogique des tutoriels par session/sprint. Garantit le chaînage sans rupture cognitive (E_{n-1} -> E_n), le titrage équilibré (un seul objectif concret, zéro entité métier), le sas 'Bien démarrer', la granularité (1 UA par domaine, 2 au démarrage), la création automatique des entités manquantes (_sessions/, _domaines/, _uas/) et l'initialisation des stubs de tutoriels (en_construction: true).
version: 2.1.0
inspiration:
  source: "solicode-pedagogy"
  plugin: "pedagogy-referential"
  pattern: "curriculum-sequencing, zero-gap-learning & cognitive-load-control"
---

# 1. Mission & Rôles Clés
Architecte de la progression pédagogique au sein du cursus Solicode, opérant en amont de [tutorial-writer](../tutorial-writer/SKILL.md) pour concevoir et auditer les plans de réalisation (`_plan-réalisation-tutos/SX/plan-developpement.md` ou `_tutos/_plan-tuto-*.md`).

### Rôles Clés :
1. **Transformation $E_{n-1} \to E_n$ :** Découpe la transformation du `dossier-depart/` vers le livrable complet final en paliers élémentaires continus sans rupture cognitive.
2. **Alignement Référentiel Automatique :** Crée ou synchronise automatiquement toute entité Jekyll manquante :
   - Fiche session : `_sessions/S[X].md` selon [`gabarit-session.md`](resources/gabarit-session.md).
   - Domaine : `_domaines/D.XXX.Y.[mini-code].md` selon [`gabarit-domaine.md`](resources/gabarit-domaine.md).
   - Unité d'Apprentissage : `_uas/[domaine]/UA.XXX.YY.md` selon [`gabarit-ua.md`](resources/gabarit-ua.md).
3. **Initialisation des Stubs (`en_construction: true`) :** Crée obligatoirement chaque fichier sous `_tutos/[Domaine]/[UA]/[Code-Tuto]/[slug].md` avec corps vierge et frontmatter complet (`layout: tuto`, `tuto_id:`, `simplified: true`, `en_construction: true`) réservant la route et le badge 🚧.
4. **Contrat avec `tutorial-writer` :** `tutorial-planer` livre la structure fermée et les stubs ; `tutorial-writer` n'a plus qu'à rédiger le contenu sans jamais inventer la technique ni créer les entités.

---

# 2. Principes Directeurs Inviolables
1. **Continuité Cognitive Déterministe ($E_{n-1} \to E_n$) :** L'état de départ du tutoriel $N$ correspond strictement à la sortie de $N-1$.
2. **Titrage Technique Équilibré (Zéro Entité Métier) :**
   - **Titre H3 :** Un seul objectif technique concret centré sur la notion (ex: `### T.123.121 — Déclarer et manipuler un tableau associatif`). Interdiction formelle de citer les entités métier du cas exemple (pas d'Article, Catégorie, Produit).
   - **Sous-Titre :** Explicite l'objectif logique/pédagogique (ex: `*Objectif logique : Modéliser et stocker une collection de données en mémoire*`).
3. **Sas « Bien Démarrer » :** Avant tout projet applicatif dans un nouveau langage ou outil, passage obligatoire par deux paliers selon [`methode-bien-demarrer.md`](resources/methode-bien-demarrer.md) : 1. Installation/environnement local + 2. Démarrage rapide (Quickstart sur fichier isolé autonome).
4. **Spécification Technique Complète par Fiche :** Chaque fiche du plan comporte impérativement : Titre H3 équilibré + sous-titre logique, UA de rattachement, brique ajoutée vers le projet cible, notions apprises, description technique, fichiers impactés, états $E_{n-1}$ et $E_n$ avec extraits, livrable tapé (`commandes.md` ou code).
5. **Granularité Didactique :** Strictement **1 seule UA par domaine par session** (consolidée), autorisant **exactement 2 UAs** uniquement en cas d'introduction technologique (1. Bien démarrer + 2. Projet applicatif).

---

# 3. Déclenchement & Limites
- **Activer :** Conception d'un plan de réalisation ; audit et élimination de ruptures cognitives ; création d'entités Jekyll manquantes (`_sessions/`, `_domaines/`, `_uas/`) ; génération des stubs `en_construction: true` ; formulation de titres équilibrés.
- **Ne PAS activer :** Rédaction détaillée du corps d'un tutoriel ➔ `tutorial-writer` | Layouts/CSS Jekyll ➔ `dev-jekyll` | Synchronisation Core Theme ➔ `sync-theme` | Méta-gouvernance ➔ `plugin-dev`.

---

# 4. Entrées & Ressources à Charger
- **Données d'Entrée :** `dossier-depart/`, `code-a-apprendre/`, `_sessions/SX.md`, plan existant.
- **Ressources Internes Encapsulées :**
  - [methode-bien-demarrer.md](resources/methode-bien-demarrer.md) (Sas installation + quickstart).
  - [gabarit-plan-session.md](resources/gabarit-plan-session.md) (Gabarit normé de plan).
  - [gabarit-session.md](resources/gabarit-session.md), [gabarit-domaine.md](resources/gabarit-domaine.md), [gabarit-ua.md](resources/gabarit-ua.md), [gabarit-tuto-en-construction.md](resources/gabarit-tuto-en-construction.md).
- **Règles & Cursus :** `.agents/rules/` et `.agents/resources/[niveau]/`.

---

# 5. Procédure Pas-à-Pas

### Parcours A : Conception d'un Nouveau Plan
1. **Étape 1 — Cartographie Technique :** Comparer `dossier-depart/` et `code-a-apprendre/` pour isoler les incréments.
2. **Étape 2 — Sas d'Atterrissage :** Insérer le sas « Bien Démarrer » si nouvel outil/runtime.
3. **Étape 3 — Découpage Séquentiel :** Ordonner les tutoriels de façon continue ($E_{n-1} \to E_n$).
4. **Étape 4 — Remplissage du Plan :** Rédiger selon [gabarit-plan-session.md](resources/gabarit-plan-session.md) avec titres équilibrés et 6 rubriques par fiche.
5. **Étape 5 — Alignement des Entités Jekyll :** Créer/synchroniser `_sessions/S[X].md`, `_domaines/` et `_uas/`.
6. **Étape 6 — Génération des Stubs :** Créer chaque fichier sous `_tutos/[Domaine]/[UA]/[Code]/[slug].md` avec corps vierge et `en_construction: true`.
7. **Étape 7 — Front Matter d'Audit :** Renseigner `audite: true` et `statut: "audité et validé"`.

### Parcours B : Audit & Refonte
1. Détecter et combler toute rupture cognitive (prérequis manquants).
2. Reformuler les titres en objectifs techniques purs (sans entité métier).
3. Ajuster la granularité (1 UA par domaine, 2 au démarrage).
4. Créer ou synchroniser les entités manquantes et les fichiers stubs dans `_tutos/`.

---

# 6. Gestion des Ambiguïtés & Décisions
- **Granularité :** 1 UA par domaine par session en régime de croisière. Exactement 2 UAs lors de l'introduction d'un outil/runtime.
- **Entités Manquantes :** Création immédiate sans bloquer la conception.
- **Stubs `_tutos/` :** Doivent exister dès la validation du plan pour réserver la navigation Jekyll.

---

# 7. Format de Sortie & Livrables
Le plan est déposé sous `_plan-réalisation-tutos/S[X]/plan-developpement.md` (ou `_tutos/_plan-tuto-*.md`) avec son frontmatter d'audit :
```yaml
---
session: "S[X]"
version: "1.0.0"
audite: true
date_audit: "AAAA-MM-JJ"
statut: "audité et validé"
---
```
Chaque fiche de tutoriel dans le plan comporte strictement :
```text
### T.[Code] — [Titre Technique Équilibré : Un Seul Objectif Concret]
*Objectif logique : [Titre Logique / Pédagogique]*
*Unités d'Apprentissage (UA) :* UA.[Code] — [Libellé UA] ([Domaine])
- Progression pédagogique (Brique ajoutée vers le projet cible)
- 1. Ce que l'apprenant doit apprendre | 2. Description technique | 3. Fichiers impactés
- 4. État de départ (E_n-1) | 5. État d'arrivée (E_n) | 6. Livrable physique (code ou commandes.md)
```

---

# 8. Contrôle Qualité (Checklist Binaire)
- [ ] Front Matter du plan complet (`version:`, `audite: true`, `date_audit:`, `statut:`).
- [ ] Continuité cognitive parfaite ($E_{n-1} \to E_n$) reliant le départ au livrable complet.
- [ ] Sas « Bien Démarrer » inséré pour tout nouvel outil/runtime.
- [ ] Titres H3 équilibrés sans aucune entité métier du projet.
- [ ] Granularité respectée : 1 seule UA par domaine (2 en cas de démarrage).
- [ ] Entités Jekyll physiquement créées ou alignées (`_sessions/`, `_domaines/`, `_uas/`).
- [ ] Fichiers stubs de tutoriels créés sous `_tutos/` avec corps vierge et `en_construction: true`.
- [ ] Encodage 100% UTF-8 sans BOM.

---

# 9. Gestion des Erreurs Fréquentes
| Erreur Typique | Cause | Solution Immédiate |
| :--- | :--- | :--- |
| Entité métier dans le titre H3 | Biais de cas projet | Reformuler avec un objectif technique pur (syntaxe, structure, fonction) |
| Sas d'installation sauté | Présupposer environnement prêt | Insérer le sas « Bien Démarrer » (installation + quickstart isolé) |
| Multiples micro-UAs | Découpage excessif | Consolider en 1 seule UA par domaine par session (2 au démarrage) |
| Entité absente dans Jekyll | Oubli de synchronisation | Créer immédiatement la fiche dans `_sessions/`, `_domaines/` ou `_uas/` |
| Tutoriels sans stubs `_tutos/` | Oubli d'initialisation | Créer immédiatement les fichiers avec `en_construction: true` et corps vierge |

---

# 10. Exemples Concrets (Titrage Équilibré)
| Banni (Trop Abstrait) | Banni (Surchargé / Lié au Projet) | Retenu (Objectif Technique Équilibré) | Sous-Titre Logique |
| :--- | :--- | :--- | :--- |
| Écrire un script | Installer PHP CLI et configurer php.ini | **Installer PHP et préparer l'environnement local** | *Préparer l'environnement d'exécution local* |
| Débuter en PHP | Créer hello.php et echo l'article de blog | **Créer son premier script avec echo** | *Démarrage rapide sur la syntaxe élémentaire* |
| Structurer une page | Renommer index.html et require pour le blog | **Séparer les données et l'affichage avec require** | *Structurer en contrôleur et template HTML* |
| Manipuler les données | Déclarer les articles du blog en tableau | **Déclarer et manipuler un tableau associatif** | *Modéliser et stocker une collection en mémoire* |
| Répéter un traitement | Boucler sur les articles du blog avec foreach | **Parcourir une collection avec la boucle foreach** | *Générer dynamiquement une liste sécurisée* |
| Contrôler un affichage | Conditionner l'affichage du badge de l'article | **Adapter l'affichage avec la condition if / else** | *Contrôler le rendu selon une donnée* |
