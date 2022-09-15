"""exports a README and makes it avaliable pulumi dashboard"""
import pulumi

def read_me():
    '''open template readme and read contents into stack output'''
    with open('Pulumi.README.md', encoding="UTF-8") as open_file:
        pulumi.export('readme', open_file.read())
