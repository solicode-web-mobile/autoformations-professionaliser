# Guide d'Utilisation — Skill `tutorial-writer-ia`

## 1. Rôle & Vocation
Le skill **`tutorial-writer-ia`** prescrit les règles didactiques et normatives pour rédiger les tutoriels du domaine **IA et Agents** (D.325.1, C.325). Il garantit la rigueur de la méthode RIO et l'architecture modulaire des skills IA.

## 2. Déclenchement & Invocations Types
```markdown
@[.agents/skills/tutorial-writer-ia/SKILL.md] Rédige le tutoriel de conception du skill de gestion de dépôt avec la méthode RIO.
```

## 3. Déroulement Pas-à-Pas
1. **Identification du Besoin IA :** Délimiter la tâche récurrente du flux de travail à automatiser/outiller.
2. **Conception du Méta-Prompt (Étape 01) :** Établir le prompt générateur de templates.
3. **Application du Cadre RIO :** Structurer le prompt final (Rôle, Instruction, Output, Contraintes Négatives).
4. **Validation du Livrable :** Sauvegarder sous `tutoriels/ia/[slug-ua]/[slug-tuto]/[slug-tuto].prompt.md`.
