# Skill `skills-dev`

Gouverne, conçoit, audite et affine les compétences locales (`.agents/skills/`) et les règles permanentes (`.agents/rules/`) de l'agent IA.

## 1. À quoi sert ce Skill ?
- **Créer une compétence locale :** Rédiger un fichier `SKILL.md` concis ($\le 80$ lignes) et son `README.md` d'accompagnement sous `.agents/skills/<nom>/`.
- **Raffiner une compétence :** Adapter les contraintes ou la checklist suite à un retour d'expérience.
- **Créer ou modifier une règle :** Formaliser une règle d'or transversale dans `.agents/rules/`.
- **Valider la conformité :** Exécuter le validateur statique déterministe.

## 2. Prompts Types d'Invocation
```markdown
@[.agents/skills/skills-dev/SKILL.md] Crée un nouveau skill local tutorial-writer-api pour le domaine API REST.
@[.agents/skills/skills-dev/SKILL.md] Ajoute une règle dans .agents/rules/ interdisant les requêtes SQL brutes.
@[.agents/skills/skills-dev/SKILL.md] Valide l'ensemble des skills avec le script de conformité.
```

## 3. Structure Canonique d'un Skill
```
.agents/skills/<nom-du-skill>/
├── SKILL.md       # Spécifications techniques et règles d'exécution (<= 80 lignes)
├── README.md      # Documentation utilisateur colocalisée unique et suffisante
└── resources/     # (Optionnel) Gabarits ou ressources dédiées au skill
```

## 4. Vérification Déterministe
Pour vérifier la conformité de l'ensemble des compétences locales :
```powershell
node .agents/skills/skills-dev/scripts/validate-skills.cjs
```
