from  hashlib import sha256
from typing import List
import math
from app import fernet
class Str:
    @staticmethod
    def hash(code:str):
        return sha256(code.encode()).hexdigest()
        
    
    @staticmethod
    def encrypt(code:str):
        return fernet.encrypt(code.encode()).decode()
    
    @staticmethod
    def decrypt(code:str):
        return fernet.decrypt(code.encode()).decode()
    
    @staticmethod
    def fromList(codes: List[int]):
        return ",".join([str(code) for code in codes])
    @staticmethod
    def toList(code:str):
        return [int(j) for j in code.split(",")]
        
        
class Vect:
    
    @staticmethod
    def euclead_dist(l1: List[int],l2: List[int]):
        return math.dist(l1,l2)