
# src\utils\hash\SHRLogCore_getHashCode.py

import hashlib

def get_md5_hash(decy_code : str) ->str:
    md5 = hashlib.md5()
    md5.update(decy_code.encode('utf-8'))
    ecy_code = md5.hexdigest()
    return ecy_code
