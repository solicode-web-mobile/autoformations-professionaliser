---
name: didactique-tutorial-planner
description: Conçoit, audite et optimise la progression séquentielle des tutoriels par session/sprint pour tous les niveaux (N1, N2, N3) pour l'EFP. Structure selon la typologie canonique (tuto-atelier, tuto-tache, tuto-notion, tuto-code), garantit le chaînage continu sans rupture (E_{n-1} -> E_n), le titrage équilibré, le sas 'Bien démarrer' et génère les stubs (_tutos/).
version: 1.3.0
---

# Tutorial Planner (Micro Didactique Tous Niveaux)

## 1. Rôle et Mission
Expert du niveau **Micro (Tutoriels & Progression)** opérant de façon générique sur les niveaux **N1, N2 et N3** pour l'**EFP (Établissement de Formation Professionnelle)**, ce skill structure le découpage technique fin à partir des UAs validées, en amont de `tutorial-writer` :
1. **Typologie Didactique Canonique :** Qualifier rigoureusement chaque tutoriel selon [.agents/references/typologie-uas-tutoriels.md](../../references/typologie-uas-tutoriels.md) et [.agents/references/maturation-ua-labs.md](../../references/maturation-ua-labs.md) :
   - `type: "tuto-atelier"` (Maturité `lab`) : Atelier pratique guidé en recherche active (**SANS notions de base en détail**, diaporama Marp obligatoire, rapport CLI si commandes exécutées).
   - `type: "tuto-tache"` (Maturité `projet`) : Cadrage et rituels agiles Scrum (0% théorie, livrables racine selon `organisation-livrables.md`, **zéro `.command.md`**, **zéro diaporama Marp**).
   - `type: "tuto-notion"` (Maturité `tutoriel`) : Notion/syntaxe isolée hors imitation (pratique dans `tutoriels/`, pas de Marp, rapport CLI si commandes).
   - `type: "tuto-code"` (Maturité `tutoriel`) : Code incrémental pas-à-pas ($E_{n-1} \to E_n$) sur l'imitation (code dans `src/`, pas de Marp, rapport CLI si commandes).
2. **Découper la transformation $E_{n-1} \to E_n$ :** Transformer le départ vers le livrable final en paliers élémentaires continus sans rupture cognitive.
3. **Titrage technique équilibré :** Formuler des titres H3 purement techniques sans entités métier du cas exemple.
4. **Alignement référentiel Jekyll :** Créer automatiquement les fiches manquantes (`_sessions/`, `_domaines/`, `_uas/`) selon les gabarits dans `resources/`.
5. **Initialisation physique des stubs :** Créer chaque fichier sous `_tutos/[Domaine]/[UA]/[Code]/[slug].md` avec corps vierge, `maturite:`, `type:` et `en_construction: true`.

## 2. Principes Directeurs Inviolables
1. **Continuité Cognitive ($E_{n-1} \to E_n$) :** L'état initial du tutoriel $N$ correspond strictement à l'état final de $N-1$. Zéro présupposé implicite.
2. **Titrage Technique Équilibré (Zéro Entité Métier) :**
   - **Titre H3 :** Un seul objectif technique concret centré sur la notion (syntaxe, structure, fonction). Interdiction formelle de citer les entités métier du cas projet. Ex: `### T.XXX.YY — Déclarer et manipuler un tableau associatif`.
   - **Sous-Titre :** Explicite l'objectif logique/pédagogique. Ex: `*Objectif logique : Modéliser et stocker une collection de données en mémoire*`.
3. **Sas « Bien Démarrer » :** Obligatoire avant tout projet dans un nouvel outil, runtime ou langage (1. Installation locale + 2. Démarrage rapide sur fichier isolé autonome) selon `resources/methode-bien-demarrer.md`.
4. **Granularité Didactique :** Strictement **1 seule UA par domaine par session** (consolidée), autorisant **exactement 2 UAs** uniquement en cas d'introduction technologique (1. Bien démarrer + 2. Projet applicatif).
5. **Spécification Complète par Fiche :** Titre H3 équilibré, sous-titre logique, UA, typologie canonique (`tuto-atelier`, `tuto-tache`, `tuto-notion`, `tuto-code`), maturité (`lab`, `projet`, `tutoriel`), brique ajoutée, notions apprises, description technique, fichiers impactés, états $E_{n-1}$ et $E_n$ avec extraits, livrables attendus (sans `.command.md` ni Marp pour `tuto-tache`).

## 3. Matérialisation Jekyll & Stubs (`en_construction: true`)
1. **Entités Jekyll :** Créer les entités manquantes à partir des templates dans `resources/` :
   - Fiche session : `_sessions/S[X].md` (`gabarit-session.md`).
   - Domaine : `_domaines/D.XXX.Y.[mini-code].md` (`gabarit-domaine.md`).
   - Unité d'Apprentissage : `_uas/[domaine]/UA.XXX.YY.md` (`gabarit-ua.md`).
2. **Fichiers Stubs dans `_tutos/` :** Chaque tutoriel planifié doit être matérialisé immédiatement par un fichier stub réservant la route Jekyll :
   - Emplacement : `_tutos/[Domaine]/[UA]/[Code-Tuto]/[slug].md`.
   - Frontmatter complet : `layout: tuto`, `tuto_id:`, `maturite:`, `type:`, `simplified: true`, `en_construction: true`. Corps vierge.
3. **Contrat avec `tutorial-writer` :** `didactique-tutorial-planner` livre la structure fermée et les stubs ; `tutorial-writer` n'a plus qu'à rédiger le contenu sans jamais créer les entités.

## 4. Procédure Pas-à-Pas
1. **Cartographie :** Comparer dossier de départ et livrable final pour isoler les incréments techniques.
2. **Sas d'Atterrissage :** Insérer le sas « Bien Démarrer » si nouvel outil/runtime/langage.
3. **Découpage Séquentiel & Qualification Typologique :** Ordonner les paliers $E_{n-1} \to E_n$, qualifier selon `typologie-uas-tutoriels.md` et formuler les titres équilibrés.
4. **Rédaction du Plan :** Rédiger selon `resources/gabarit-plan-session.md` avec frontmatter d'audit (`audite: true`, `statut: "audité et validé"`).
5. **Alignement Référentiel & Stubs :** Créer/synchroniser `_sessions/`, `_domaines/`, `_uas/` et générer les stubs sous `_tutos/`.

## 5. Contrôle Qualité (Checklist Binaire)
- [ ] Chaînage déterministe $E_{n-1} \to E_n$ sans rupture cognitive quel que soit le niveau.
- [ ] Typologie qualifiée conforme à `typologie-uas-tutoriels.md` (`tuto-atelier`, `tuto-tache`, `tuto-notion`, `tuto-code`).
- [ ] Titres H3 100% techniques sans entité métier du cas exemple.
- [ ] Sas « Bien Démarrer » inséré pour tout nouvel outil/runtime/langage.
- [ ] Granularité respectée : 1 UA par domaine (2 max à l'introduction).
- [ ] Entités Jekyll (`_sessions/`, `_domaines/`, `_uas/`) créées et alignées.
- [ ] Fichiers stubs créés sous `_tutos/` avec corps vierge, `maturite:`, `type:` et `en_construction: true`.
