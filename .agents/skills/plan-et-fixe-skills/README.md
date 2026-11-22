# Skill `plan-et-fixe-skills`

Orchestre la planification d'implémentation (`/plan`) conjointe aux modifications de projet et à l'adaptation continue des compétences locales (`.agents/skills/`) et règles (`.agents/rules/`) selon les retours du concepteur pédagogique.

## 1. À quoi sert ce Skill ?
- **Planifier avec rigueur :** Produire un artéfact interactif standardisé (`plan-*.md` avec `RequestFeedback: true`) avant toute modification destructive ou structurante sur le projet (sessions, documents, code).
- **Adapter les compétences (« Fixe Skills ») :** Lorsqu'une remarque du concepteur introduit une nouvelle exigence méthodologique ou technique, formaliser simultanément l'évolution requise dans les skills ou les règles concernés.
- **Assurer la cohérence :** Garantir qu'une correction validée sur un document est immédiatement répercutée dans le comportement futur de l'agent.

## 2. Prompts Types d'Invocation
```markdown
@[.agents/skills/plan-et-fixe-skills/SKILL.md] /plan Analyse mes remarques sur la session S1 et adapte les skills associés.
@[.agents/skills/plan-et-fixe-skills/SKILL.md] Propose un plan de modification pour la stack Laravel et fixe les règles et skills d'ingénierie.
@[.agents/skills/plan-et-fixe-skills/SKILL.md] Le concepteur demande de simplifier le rituel de clôture : planifie les changements et ajuste le skill cloture-sprint.
```

## 3. Déroulement Pas-à-Pas

### Phase 1 — Analyse des Retours & Détection d'Impact
1. Extraire les remarques et directives fournies par le concepteur.
2. Identifier les fichiers de contenu ou de code à modifier.
3. Déterminer les compétences (`.agents/skills/`) et règles (`.agents/rules/`) impactées par les nouvelles directives.

### Phase 2 — Rédaction de l'Artéfact de Planification
Générer l'artéfact interactif dans le dossier brain de la conversation :
- Spécifier les arbitrages dans `User Review Required`.
- Lister les questions ouvertes dans `Open Questions`.
- Découper les changements prévus dans `Proposed Changes` (diffs et snippets).
- Détailler les adaptations de skills dans une section dédiée `Adaptation des Skills & Règles`.
- Préciser le plan de vérification (`Verification Plan`).
- Configurer `RequestFeedback: true` et `UserFacing: true`.

### Phase 3 — Validation Concepteur
Attendre l'approbation explicite (clic sur le bouton **Proceed** ou retours complémentaires). Ne modifier aucun fichier de code ou de skill avant cette validation.

### Phase 4 — Exécution Atomique & Fixe des Skills
1. Appliquer les modifications validées sur les fichiers du projet.
2. Créer ou ajuster les fichiers `SKILL.md` (limite $\le 80$ lignes, UTF-8 sans BOM) et `README.md` associés.
3. Mettre à jour les règles transversales dans `.agents/rules/` si applicable.
4. Exécuter le validateur statique : `node .agents/skills/skills-dev/scripts/validate-skills.cjs`.
5. Rédiger l'artéfact `walkthrough.md` pour clore le cycle.

## 4. Vérification Déterministe
Exécuter le script de conformité :
```bash
node .agents/skills/skills-dev/scripts/validate-skills.cjs
```
