---
title: "Initialisation de l'Agent IA & Architecture des Skills"
layout: ua
code: "UA.325.11"
slug: "agent-skills"
maturite: "UA-Lab"
ordre: 2
competence: "C.325"
domaine: "D.325.1"
duree: 6
objectif: >
  Maîtriser les principes du Prompt Engineering structuré (méthode RIO), comprendre l'architecture logicielle d'un Agent IA outillé (règles Always-On vs compétences modulaires), concevoir en atelier pratique un premier skill modulaire avec sa mission Marp (skill-presentation), et appliquer ces compétences pour outiller le Blog des Lauréats avec les règles Always-On et le skill gestion-depot.
description: >
  Guidé par le skill mentor domaine-ia, l'apprenant assimile le dialogue déterministe avec les LLMs (méthode RIO, patterns fondamentaux, context engineering), explore l'architecture d'un Agent IA outillé et de ses règles permanentes, conçoit dans un atelier pratique le skill modulaire skill-presentation (avec missions/marp-slides.md et diaporama Marp), puis déploie sur le projet d'imitation le socle de règles (.agents/rules/contexte-projet.md, regles-generales.md) et les skills de démarrage (skills-dev, gestion-depot avec ses missions init-depot et init-projet).
notions:
  - "Méthode directrice RIO (Rôle persona d'expert, Instruction avec contraintes négatives, Output au format strict sans tableau)"
  - "Patterns fondamentaux de prompt (Persona, Template, Constraint, Step-by-Step, Reflective)"
  - "Architecture de l'Agent IA : distinction règles Always-On (.agents/rules/) vs compétences modulaires (.agents/skills/)"
  - "Découvrabilité native d'un skill (frontmatter YAML, plafond <= 75 lignes, missions spécialisées)"
  - "Conception pratique d'un skill outillé (skill-presentation avec missions/marp-slides.md)"
  - "Outillage opérationnel de gestion de dépôt (.agents/skills/gestion-depot/ avec init-depot.md et init-projet.md)"
livrable: >
  Livrables d'apprentissage sous tutoriels/ia/agent-skills/ (dossiers prompt-engineering/, agent-ia/, skill-presentation/ combinant fiches techniques [slug].md, diaporamas Marp presentation-[slug].md et journal skill-gestion-depot.command.md sans README unitaires), et livrables d'outillage sur le Blog des Lauréats (.agents/rules/contexte-projet.md, regles-generales.md, et skills skills-dev/, gestion-depot/).
travail_a_faire: >
  Assimiler le Prompt Engineering et la méthode RIO, explorer l'architecture d'un Agent IA et les règles permanentes, concevoir en atelier le skill d'exemple skill-presentation avec sa mission Marp, puis outiller le projet d'imitation avec les règles Always-On et le skill de démarrage gestion-depot.
---
