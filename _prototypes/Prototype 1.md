---
title: "Portfolio Développeur — Consultation détaillée d'une réalisation"
layout: prototype
code: "Prototype 1"
session: "S1"

travail_a_faire: >
  Transposer l'ensemble des acquis du Projet d'Imitation au domaine du Portfolio Développeur en autonomie individuelle :
  formalisation du cadre projet sous Scrum, conception fonctionnelle et technique (diagramme de contexte et cas d'utilisation en syntaxe déclarative),
  Product Backlog et Sprint Backlog S1 (User Stories INVEST ordonnancées), et développement sous Laravel de la page de consultation détaillée
  d'une réalisation selon une architecture découplée en deux couches (route dynamique, contrôleur mince IoC, classe Service sur persistance
  tabulaire CSV en mémoire, gabarit Blade responsive sous Tailwind CSS et gestion robuste de l'erreur 404). Clôture par la démonstration en Sprint Review
  et la rétrospective d'équipe.

livrable:
  - "Dépôt GitHub versionné avec commits atomiques et README structuré"
  - "Charte de cadrage projet et charte d'équipe Scrum signée"
  - "Diagramme de contexte système et cas d'utilisation macro (syntaxe déclarative)"
  - "Product Backlog ordonnancé selon MoSCoW et Sprint Backlog S1"
  - "Dossier d'architecture en 2 couches et ADR-01 (persistance transitoire CSV)"
  - "Application Laravel fonctionnelle : route `/realisations/{id}`, contrôleur, `RealisationService`, layout Blade et gestion 404"
  - "Procès-verbal de démonstration en Sprint Review et compte-rendu de rétrospective"
---
