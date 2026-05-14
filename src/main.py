from src.config import load_config
from src.logger import get_logger
from src.modules import load_modules

def main():
    config = load_config()
    logger = get_logger("Main")

    logger.info("🚀 GitkeepProject started")
    modules = load_modules()

    for name, module in modules.items():
        logger.info(f"▶ Initialisation du module : {name}")
        module.run()

if __name__ == "__main__":
    main()
