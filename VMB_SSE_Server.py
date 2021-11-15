import os
from pypbc import *
import hashlib
import time
import binascii
import hmac
from Crypto.Cipher import AES

class SSE_Client:
    def __init__(self,lToken,T,B,Tb,StateW):
        self.tset_dict = dict()
        self.g_keyword =""
        self.g_c = 0
        self.lToken = lToken
        self.T = T
        self.B = b
        self.Tb = Tb

    def xor_encrypt(tips, key):
        ltips = len(tips)
        lkey = len(key)
        secret = []
        num = 0
        for each in tips:
            if num >= lkey:
                num = num % lkey
            tr = each ^ key[num]
            secret.append(str(tr))
            num += 1
        return "".join(secret)
    def xor_decrypt(secret, key):
        tips = secret
        ltips = len(tips)
        lkey = len(key)
        secret = []
        num = 0
        for each in tips:
            if num >= lkey:
                num = num % lkey
            tr = each ^ key[num]
            secret.append(str(tr))
            num += 1
        return "".join(secret)

    def KeyGen(keyLength):
        k1 = os.urandom(keyLength)
        k2 = os.urandom(keyLength)
        k3 = os.urandom(keyLength)
        return [k1,k2,k3]

    def Search(self,lToken,T,B,Tb,StateW):
        lbwi=[]
        for tk in self.lToken:
            vb = self.Tb[tk]
            tk_b = bin(int(tk, 16))[2:]
            bwi = self.xor_decrypt(vb.encode("utf-8"),tk_b.encode("utf-8"))
            lbwi.append(bwi)
        len_q = len(queryKeyword)
        if len_q == 5:
            bw = int(lbwi[0], 2) & int(lbwi[1], 2) & int(lbwi[2], 2)& int(lbwi[3], 2) & int(lbwi[4], 2)
        else:
            bw = int(lbwi[0], 2) & int(lbwi[1], 2) & int(lbwi[2], 2) & int(lbwi[3], 2) & int(lbwi[4], 2) &int(lbwi[5], 2)& int(lbwi[6], 2) & int(lbwi[7], 2) & int(lbwi[8], 2) & int(lbwi[9], 2)
        id_file = 1
        bw_b = bin(int(bw))[2:]
        lstR = []
        for b in bw_b:
            li = hashlib.sha256(str(id_file).encode("utf8")).hexdigest()
            if b=='1':
               lstR.append(self.T[li])
        return

   