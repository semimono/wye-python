

# - receive source definition (what is the source code and what are the build vars)
# - set build vars from input (aka, what is the output language, how much optimization should be done, etc.)
# - parse (call out parsing/syntax errors)
# - construct dependency tree
# - construct definition tree
# - 
# - write translated code to source files in target directory
# - output link files (linking line numbers in translated source to original source, etc.)

import sys, getopt

VERSION = '0.0.1'

def show_help(program_name):
  print('''  USAGE: `%s <command> [sub-command] [options]`
    for more info on a command enter: `<command> help`

  COMMANDS:
    help        -Show this output
    version     -Show the version of wqye python compiler
    build       -Build a wye project''' % program_name)
  sys.exit()

def show_version():
  print('Wye python compiler version %s' % VERSION)
  sys.exit()

def unknown_command(program_name, command):
  print('unknown command: %s' % command)
  advise_help(program_name)
  sys.exit(2)

def advise_help(program_name):
  print('for help: `%s help`' % program_name)

def build_project(program_name, args):
  print('TODO: implement compiler')


if __name__ == '__main__':
  program_name = sys.argv[0]
  
  commands = {
    '-h': lambda: show_help(program_name),
    '--help': lambda: show_help(program_name),
    'help': lambda: show_help(program_name),
    'version': show_version,
    'build': lambda: build_project(program_name, sys.argv[2:])
  }

  # check for no command
  if len(sys.argv) < 2:
    advise_help(program_name)
    exit(2)
  
  # delegate to command
  commands.get(sys.argv[1], lambda: unknown_command(program_name, sys.argv[1]))()
