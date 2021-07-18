"""
python3 ccp_cli_ex1.py -f <input_file> -e <regex>
"""

from ciscoconfparse import CiscoConfParse as ccp
import click


@click.command()
@click.option('-f', '--filename', 
        help ='Specify configuration file name')
@click.option('-e', '--expression', 
        help ='search expression')

def ccp_find_obj(filename,expression):
    loaded_cfg = ccp(filename)
    filtered_obj = loaded_cfg.find_objects(f"{expression}")
    for item in filtered_obj:
        print(item.text)
        for child in item.children:
            print(child.text)
            
if __name__ == "__main__":
    ccp_find_obj()
