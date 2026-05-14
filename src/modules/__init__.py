import importlib
from pathlib import Path
import json

MODULES_DIR = Path(__file__).parent

def load_modules():
    modules = {}

    for module_dir in MODULES_DIR.iterdir():
        if module_dir.is_dir() and (module_dir / "module.py").exists():
            config_file = module_dir / "config.json"
            config = json.load(open(config_file)) if config_file.exists() else {}

            module_name = module_dir.name
            module_path = f"src.modules.{module_name}.module"

            mod = importlib.import_module(module_path)
            modules[module_name] = mod.Module(config)

    return modules
