# Architecture du projet

## 1. Structure
- src/ : code source
- modules/ : modules dynamiques
- logs/ : journaux
- data/ : données persistantes
- cache/ : cache
- tmp/ : fichiers temporaires

## 2. Pipeline
Main → Config → Logger → Loader → Modules
