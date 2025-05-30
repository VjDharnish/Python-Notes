import uuid
import logging

class_name ='Sample_1'

logging.basicConfig(filename='uuid', level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

for i in range(0,10,):
    d = class_name+'_'+str(i)
    uuid_ =uuid.uuid5(namespace= uuid.NAMESPACE_DNS,name =d)
    logging.info(f"{class_name}  record id: {i}  uuid:{uuid_}")


