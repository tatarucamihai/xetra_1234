
import logging
import logging.config

import yaml

def main():
    """
    Entry point
    
    """
    #Parsing Yaml file
    
    config_path = 'D:/xetra_11/xetra_1234/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test")

if __name__ == '__main__':
    main()