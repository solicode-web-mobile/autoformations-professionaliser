# Stratégie GitFlow et Conventions de Commits

## 1. Principes Fondamentaux de Gestion de Version

Ce document définit les règles de gestion de version sous Git appliquées sur le poste de l'apprenant et par l'**`Agent Réalisation de Sprint`** :
- La stratégie des branches par sprint.
- L'interdiction formelle du travail direct sur la branche principale (`main`).
- La souveraineté exclusive de l'apprenant sur les actions de commit et de push.
- Les conventions de nommage des commits atomiques.

---

## 2. Stratégie des Branches par Sprint

1. **Branche Dédiée au Sprint Actif :**
   - L'ensemble des activités d'un sprint (cadrage, tutoriels, code applicatif, documentation) s'effectue sur la branche unique dédiée :
     - Sprint 0 : `sprint0`
     - Sprint 1 : `sprint1`
     - Sprint N : `sprintN`
2. **Interdiction Formelle de Travailler sur `main` :**
   - La branche `main` est protégée. Aucun travail de développement en cours ne doit y être réalisé directement.
   - La fusion vers `main` n'intervient qu'en clôture de sprint, après validation formelle de la Sprint Review et obtention de la décision Go.
3. **Création et Basculement de Branche :**
   - Vérifier la branche courante : `git branch --show-current`
   - Créer et basculer sur la branche du sprint actif : `git checkout -b sprint[N]`

---

## 3. Souveraineté de l'Apprenant & Interdiction IA

> [!CAUTION]
> **Interdiction formelle de commit et push par l'Agent IA :**  
> L'Agent IA ne doit **JAMAIS** exécuter les commandes `git commit` ou `git push`.  
> - Seul l'apprenant (l'humain) est habilité à versionner son travail sur son dépôt GitHub.  
> - L'Agent IA produit les fichiers demandés, vérifie l'état du dépôt (`git status`), contrôle l'encodage (UTF-8 sans BOM) et formule une suggestion de message de commit conventionnel.  
> - L'apprenant inspecte les modifications (`git diff`) et procède lui-même au commit et au push.

---

## 4. Conventions de Commits Atomiques

Chaque commit doit représenter une unité logique de modification cohérente (commit atomique).  
Le message de commit respecte le standard des *Conventional Commits* :

### Structure Canonique
```text
<type>(<scope>): <description courte à l'impératif direct>
```

### Types Autorisés
- **`feat` :** Ajout d'une nouvelle fonctionnalité applicative ou composant (`feat(article): implémenter la route et le contrôleur de consultation`).
- **`docs` :** Ajout ou mise à jour de documentation, tutoriels ou artéfacts de cadrage (`docs(cadrage): formaliser la note de cadrage et le périmètre In/Out`).
- **`test` :** Ajout ou correction de tests automatisés TDD (`test(service): ajouter les tests unitaires pour ArticleService`).
- **`refactor` :** Restructuration du code sans altération fonctionnelle (`refactor(controller): injecter ArticleService via constructeur`).
- **`style` :** Ajustements de mise en page CSS, typographie ou cosmétique (`style(ui): aligner la carte d'article avec les composants Preline UI`).
- **`chore` :** Tâches de maintenance, dépendances ou configuration (`chore(git): initialiser le fichier .gitignore`).

---

## 5. Protocole de Validation Avant Commit

Avant d'inviter l'apprenant à committer :
1. Contrôler l'arborescence des fichiers modifiés et non suivis : `git status`.
2. S'assurer qu'aucun fichier temporaire, binaire ou clé secrète (`.env`) n'est traqué.
3. Vérifier que les fichiers Markdown sont encodés en **UTF-8 sans BOM**.
4. Présenter à l'apprenant la commande exacte suggérée :
   ```bash
   git add .
   git commit -m "docs(scrum): animer la revue 0 et signer le PV Go/No-Go"
   git push origin sprint0
   ```
