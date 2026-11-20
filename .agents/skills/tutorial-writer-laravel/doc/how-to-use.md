# Guide d'Utilisation — Skill `tutorial-laravel-writer`

## 1. Rôle & Vocation
Le skill **`tutorial-laravel-writer`** prescrit les règles didactiques et conventions de code pour rédiger les tutoriels du domaine **Laravel** (D.321.1, C.321). Il garantit le respect des conventions du framework, la séparation Back/Front et l'approche Live Coding.

## 2. Déclenchement & Invocations Types
```markdown
@[.agents/skills/tutorial-laravel-writer/SKILL.md] Rédige le tutoriel de création du CRUD des articles avec FormRequest et Blade.
```

## 3. Déroulement Pas-à-Pas
1. **Ciblage Applicatif :** Définir la fonctionnalité ciblée sur le projet Blog des Lauréats.
2. **Scission Back/Front :** Structurer les étapes en isolant le code back-end (modèle, migration, FormRequest, contrôleur) et le code front-end (Blade, Alpine.js).
3. **Journalisation Artisan :** Consigner les commandes Artisan dans `[slug-tuto].command.md` (sans commandes Git).
4. **Vérification de Conformité :** Vérifier l'absence de validation inline et la conformité colonne 0 des blocs de code.
