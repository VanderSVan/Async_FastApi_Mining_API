from pathlib import Path
from loguru import logger

# Paths
dir_path = Path(__file__).parent
debug_path = dir_path.joinpath('debug.log').absolute()
success_path = dir_path.joinpath('success.log').absolute()
info_path = dir_path.joinpath('info.log').absolute()
warning_path = dir_path.joinpath('warning.log').absolute()
error_path = dir_path.joinpath('error.log').absolute()
critical_path = dir_path.joinpath('critical.log').absolute()

# logging settings
format_ = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {file} | {line} | {message}"
rotation_ = "1 days"
compression_ = "zip"

# data to insert into loop
path_list = [debug_path, success_path, info_path, warning_path, error_path, critical_path]
level_list = ['DEBUG', 'SUCCESS', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


for level_name, file_path in zip(level_list, path_list):
    logger.add(file_path,
               format=format_,
               level=level_name,
               rotation=rotation_,
               compression=compression_
               )

if __name__ == '__main__':
    logger.debug("Test debug message")
    logger.success("Test success message")
    logger.info("Test info message")
    logger.warning("Test warning message")
    logger.error("Test error message")
    logger.exception("Test exception message")
    logger.critical("Test critical message")
