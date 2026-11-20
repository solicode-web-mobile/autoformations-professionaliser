# Guide d'Utilisation — Skill `tutorial-writer-architecture`

## 1. Rôle & Vocation
Le skill **`tutorial-writer-architecture`** prescrit les règles didactiques et techniques pour rédiger les tutoriels du domaine **Architecture logicielle** (D.312.1, C.312). Il gouverne la structuration en couches, la rédaction d'ADR et la séparation des responsabilités.

## 2. Déclenchement & Invocations Types
```markdown
@[.agents/skills/tutorial-writer-architecture/SKILL.md] Rédige le tutoriel d'architecture en couches pour le projet Blog des Lauréats.
```

## 3. Déroulement Pas-à-Pas
1. **Qualification de la Décision :** Identifier le périmètre architectural et formaliser l'ADR correspondant.
2. **Schéma de Séquence :** Tracer le flux de requête à travers les couches applicatives en Mermaid `sequenceDiagram`.
3. **Vérification SOLID :** S'assurer de la séparation stricte des responsabilités (contrôleurs minces, services métier).
4. **Validation des Livrables :** Vérifier que les fiches didactiques et fichiers ADR sont positionnés sous `tutoriels/architecture/[slug-ua]/[slug-tuto]/`.
