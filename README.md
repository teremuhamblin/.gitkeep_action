# .gitkeep_action
- Projet basé sur .gitkeep
>Ce projet démontre l'utilisation avancée de `.gitkeep` pour structurer un projet complet, même sans fichier

<p align="center">
  
[![CI](https://github.com/teremuhamblin/.gitkeep_action/actions/workflows/release.yml/badge.svg)](https://github.com/teremuhamblin/.gitkeep_action/actions/workflows/release.yml)
[![Security](https://github.com/teremuhamblin/.gitkeep_action/actions/workflows/security.yml/badge.svg)](https://github.com/teremuhamblin/.gitkeep_action/actions/workflows/security.yml)
</p>

### Objectifs
- Versionner des dossiers vides
- Préparer la structure d’un projet avant développement
- Créer des espaces réservés pour modules, logs, data, tests, etc.
- Maintenir une architecture propre dès le début

### Structure `OPTIONNELLE`
[![CI](https://github.com/teremuhamblin/.gitkeep_action/actions/workflows/ci.yml/badge.svg)](https://github.com/teremuhamblin/.gitkeep_action/actions/workflows/ci.yml)
```md
- `src/` — Code source
- `logs/` — Logs runtime
- `data/` — Données
- `cache/` — Cache interne
- `tmp/` — Fichiers temporaires
- `docs/` — Documentation
- `tests/` — Tests unitaires
```
- Chaque dossier contient un fichier `.gitkeep` pour être versionné.

### Pourquoi .gitkeep ?
>Git n’enregistre pas les dossiers vides.  
`.gitkeep` permet de :
```md
- garder la structure du projet
- préparer des modules futurs
- organiser le projet avant d’écrire du code
- faciliter CI/CD et documentation
```

## Licence
Libre d’utilisation.
