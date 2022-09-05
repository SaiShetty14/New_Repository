import logging
import os
print("Hello I am Just checking")
file_name=os.path.basename(__file__).split()[0]+".txt"
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler_1=logging.FileHandler(file_name)
formatter1=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s-%(name)s')
file_handler_1.setFormatter(formatter1)
logger.addHandler(file_handler_1)

stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter1)
logger.addHandler(stream_handler)
if __name__=="__main__":
	logger.debug("This is Debugging part")
	logger.info("This is Info part")
	logger.error("This is Error part")
	logger.warning("This is Warning part")
	logger.critical("This is Critical part")

else:
	logger.info(f"This was Imported")