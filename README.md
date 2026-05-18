###### README.md >> markdown 
# .gitkeep_action
- Projet basé sur .gitkeep
>Ce projet démontre l'utilisation avancée de `.gitkeep` pour structurer un projet complet, même sans fichier

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
- `.gitkeep` permet de :
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
- Libre d’utilisation

### 🟦 Badges
<img src="https://img.shields.io/badge/Quality-Enterprise-0A66C2?style=for-the-badge&logo=github" />
<img src="https://img.shields.io/badge/Security-Verified-brightgreen?style=for-the-badge&logo=shield" />
<img src="https://img.shields.io/badge/Automation-100%25-blue?style=for-the-badge&logo=githubactions" />
<img src="https://img.shields.io/badge/Compliance-OK-success?style=for-the-badge&logo=checkmarx" />

---
