import logging

log_dir = r"D:\C_Workspaces_Repositories\GitHub_Repositories\Python_Learning\Advanced Topics"
logging.basicConfig(filename=log_dir+'\sample.log', level=logging.NOTSET)

logging.debug('Here you have some information for debugging.')
logging.info('Everything is normal. Relax!')
logging.warning('Something unexpected but not important happend.')
logging.error('Something unexpected and important happened.')
logging.critical('OMG!!! A critical error happend and the code cannot run!')