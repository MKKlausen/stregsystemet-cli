# Stregsystemet-CLI

This repository is the UNOFFICIAL Stregsystemet CLI, to buy things in Stregsystemet, at AAU.
As this is the unofficial Stregsystemet CLI, you use the CLI at your own risk, and there will be provided no support from FIT (#FritFit). Instead contact the developer.

## Requirements

The CLI is a python script that relies on no external dependendencies. The script is tested with python 3.9

## Usage

```bash
$ ./main.py -h
usage: sts [-h] [-u [USER]] [-i [ITEM]] [-c [COUNT]] [-b]

optional arguments:
  -h, --help            show this help message and exit
  -u [USER], --user [USER]
                        Specifies your Stregsystem username
  -i [ITEM], --item [ITEM]
                        Specifies the item you wish to buy
  -c [COUNT], --count [COUNT]
                        Specifies the amount of items you wish to buy
  -b, --balance         Output only stregdollar balance
  ```

If either the user or item arguments or no arguments at all are specified the CLI will enter interactive mode.

The script also keeps track of your balance and what items are available in Stregsystemet.

## Contributions

Contributions are welcome!

Feel free to fork the project and create a pull request. 
To get started with a development environment of Stregsystemet, go to the official [Stregsystemet repository](https://github.com/f-klubben/stregsystemet)
