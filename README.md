###### README.md >> markdown 
# .gitkeep_action
- Projet basé sur .gitkeep
>Ce projet démontre l'utilisation avancée de `.gitkeep` pour structurer un projet complet, même sans fichier

<p align="center">
  
[![CI](https://github.com/teremuhamblin/.gitkeep_action/actions/workflows/release.yml/badge.svg)](https://github.com/teremuhamblin/.gitkeep_action/actions/workflows/release.yml)

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

### ▶ Démarrer
```make
make run
```

### 🧪 Tester
```make
make test
```

### 🐳 Docker
```docker
docker build -t gitkeep .
docker run gitkeep
```

### 📜 License
>Apache 2.0 : License
- Libre d’utilisation---

<p align="left">

  <!-- Version -->
  <img src="https://img.shields.io/github/v/tag/Teremu/.gitkeep_action?label=Version&color=blueviolet&style=for-the-badge" />

  <!-- CI -->
  <img src="https://img.shields.io/github/actions/workflow/status/Teremu/.gitkeep_action/ci.yml?label=CI&style=for-the-badge&logo=github" />

  <!-- Node -->
  <img src="https://img.shields.io/badge/Node.js-20.x-339933?style=for-the-badge&logo=node.js&logoColor=white" />

  <!-- License -->
  <img src="https://img.shields.io/github/license/Teremu/.gitkeep_action?style=for-the-badge&color=yellow" />

  <!-- Issues -->
  <img src="https://img.shields.io/github/issues/Teremu/.gitkeep_action?style=for-the-badge&color=orange" />

  <!-- PR -->
  <img src="https://img.shields.io/github/issues-pr/Teremu/.gitkeep_action?style=for-the-badge&color=brightgreen" />

  <!-- Commits -->
  <img src="https://img.shields.io/github/commit-activity/m/Teremu/.gitkeep_action?style=for-the-badge&color=blue" />

  <!-- Repo Size -->
  <img src="https://img.shields.io/github/repo-size/Teremu/.gitkeep_action?style=for-the-badge&color=9cf" />

</p>

---


