"""Hello"""

import click
# Note that neither blessed nor blessings work on Windows and will raise
# and ImportError when trying to import one of their dependencies (as of 
# blessings v1.6 / blessed v1.14.1). The solution to this is probably to 
# check what the OS is and then have two different behaviors depending on
# which OS it is.
import blessed
# import blessings
import cmd2

class myCmd(cmd2.Cmd):
    """This is a subclass of cmd2.Cmd"""
    intro = 'Welcome to the myCmd shell!'
    prompt = '(myCmd)'

    def do_exit(self, arg):
        print('All done now!')
        return True

    def do_ppm(self, arg):
        print('Hello!')

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', default='World', help='Name of the person to greet.')
def hello(count, name):
    """Greet name count times"""
    for x in range(count):
        click.echo('Hello, {}!'.format(name))

@click.command()
@click.option('--arg', default='helloworld', help='A string')
def shell(arg):
    """Start a cmd2 shell"""
    click.echo('{}'.format(arg))
    c = myCmd()
    c.cmdloop()



def main():
    print("It's main()!")

if __name__ == '__main__':
    print("Now it's __name__ == '__main__'!")
