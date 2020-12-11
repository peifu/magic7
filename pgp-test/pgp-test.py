#!/usr/bin/env python3
#coding: utf-8

import pgpy

PGP_PUB_KEY = "./keys/peifu.jiang.asc"
PGP_PRV_KEY = "./keys/peifu.jiang.prv.asc"
TEST_CIPHER_FILE = "./testdata/cipher_message.txt"
TEST_PLAIN_FILE = "./testdata/plain_message.txt"
TEST_DECRYPTED_FILE = "./testdata/decrypted_message.txt"

def read_data(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data

def write_data(path, data):
    f = open(path, "w+")
    f.write(data)
    f.close()

def pgp_encrypt(plain_file):
    key, _ = pgpy.PGPKey.from_file(PGP_PUB_KEY)
    rkey = key.subkeys.values()[0]
    data = read_data(TEST_PLAIN_FILE)
    pmsg = pgpy.PGPMessage.new(data)
    emsg = rkey.encrypt(pmsg).message
    print (emsg)

def pgp_decrypt(cipher_file):
    key, _ = pgpy.PGPKey.from_file(PGP_PRV_KEY)
    emsg = pgpy.PGPMessage.from_file(cipher_file)
    dmsg = key.decrypt(emsg).message
    write_data(TEST_DECRYPTED_FILE, dmsg)

if __name__ == "__main__":
    pgp_decrypt(TEST_CIPHER_FILE)
