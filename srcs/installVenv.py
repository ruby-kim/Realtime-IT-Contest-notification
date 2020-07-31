import os, sys
path = "./"

if ".venv" not in os.listdir(path):
	os.system("python3 -m venv .venv")
# os.system("source ../.venv/bin/activate")
# print("Hello world!\n")
