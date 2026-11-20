---
name: tutorial-writer-ia
description: Règles de rédaction didactiques et techniques spécifiques au domaine IA et Agents (D.325.1, Compétence C.325). Membre de l'écosystème tutorial-writer sous la gouvernance de tutorial-writer.
version: 1.0.0
---

# 1. Mission & Périmètre
Expert de domaine au sein de l'écosystème `tutorial-writer`, chargé de prescrire les standards didactiques, structures de prompts et règles d'outillage propres au domaine **IA et Agents** (D.325.1, Compétence C.325).
Applique le socle transversal et la synchronisation gouvernés par [tutorial-writer](../tutorial-writer/SKILL.md).

# 2. Déclenchement & Limites
- **Activer :** Rédaction, audit ou adaptation de tutoriels du domaine IA (ingénierie de prompt, méta-prompts, skills modulaires, context engineering).
- **Ne PAS activer :** Tutoriels de code applicatif classique ➔ `tutorial-writer-laravel` | Cérémonies agiles ➔ `tutorial-writer-scrum` | Gouvernance transversale ➔ `tutorial-writer`.

# 3. Stack Technique & Méthodes du Domaine
- **Méthode de prompt engineering :** Cadre RIO (Rôle, Instruction, Output, Contraintes Négatives).
- **Architecture de skills :** `SKILL.md` orchestrateur ($\le 75$ lignes), sous-dossier `missions/`, `doc/how-to-use.md`.
- **Formats de livrables :** Fichiers `.prompt.md` documentés ou dossiers de skills sous `.agents/skills/`.
- **Outillage cible :** Agents IA de développement et assistants CLI.

# 4. Règles Spécifiques de Rédaction IA
1. **Méthode RIO Obligatoire :** Tout prompt applicatif produit doit impérativement respecter la structure RIO : Rôle (persona expert), Instruction (directive non ambiguë), Output (gabarit strict attendu), Contraintes Négatives (interdictions formelles).
2. **Étape 01 Méta-Prompt Générateur :** Tout tutoriel de création de prompt débute obligatoirement par la conception du méta-prompt générateur (`prompt-creator`).
3. **Skills Modulaires vs Prompts Passifs :** Privilégier systématiquement la conception de skills modulaires outillant des tâches récurrentes du flux de travail plutôt que des prompts isolés.
4. **Zéro Prompt pour l'Apprentissage Conceptuel :** Proscrire tout prompt d'assistance pour les concepts purs sans livrable technique reproductible.

# 5. Formats de Livrables & Validation
- **Fiches didactiques :** `tutoriels/ia/[slug-ua]/[slug-tuto]/[slug-tuto].md`
- **Prompts versionnés :** `tutoriels/ia/[slug-ua]/[slug-tuto]/[nom].prompt.md`
- **Critères de validation :**
  - Présence intégrale des 4 sections RIO dans chaque prompt.
  - Validité syntaxique et reproductibilité des instructions du prompt.
  - Absence de consignes passives ou vagues.
