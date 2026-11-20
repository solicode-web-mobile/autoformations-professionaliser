# Guide d'Utilisation — Skill `tutorial-uml-writer`

## 1. Rôle & Vocation
Le skill **`tutorial-uml-writer`** fournit à l'agent les règles didactiques et contraintes techniques nécessaires pour rédiger les tutoriels du domaine **UML** (D.311.2, C.311). Il opère sous la gouvernance du Master Skill `tutorial-writer`.

## 2. Déclenchement & Invocations Types
Invoquer ce skill lors de la rédaction de fiches de modélisation ou de schémas déclaratifs Mermaid :
```markdown
@[.agents/skills/tutorial-uml-writer/SKILL.md] Rédige le tutoriel de modélisation des cas d'utilisation pour le Blog des Lauréats.
```

## 3. Déroulement Pas-à-Pas
1. **Vérification du Contexte :** S'assurer de la frontière système et des acteurs impliqués.
2. **Rédaction du Diagramme Déclaratif :** Rédiger le code Mermaid (`graph TD`, `sequenceDiagram`, `classDiagram`) calé à la marge gauche (colonne 0).
3. **Traçabilité Backlog :** Lier chaque cas d'usage à sa User Story correspondante.
4. **Validation du Rendu :** Vérifier l'absence d'erreurs de syntaxe Mermaid et l'absence totale de captures d'écran.
