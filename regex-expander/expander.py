import exrex
import click


@click.command()
# @click.option('-p', '--pattern', prompt='A valid regex pattern', help='A valid regex pattern to expand')
# @click.option('-f', '--file-name', default='expanded.txt', prompt='Name of file to export expanded regex', help='Name of file where expanded pattern will be written to')
@click.option('-p', '--pattern', required=True, help='A valid regex pattern to expand')
@click.option('-f', '--file-name', default='expanded.txt',  help='Name of file where expanded pattern will be written to. Defaults to expanded.txt')
@click.option('-d', '--delimiter', default='\n', help='Delimiter used to seperate output. Defaults to newline char')
def expander(pattern, file_name, delimiter):
    """Program that expands specified regular expression and writes it to specified file. No failsafe implemented - be careful!"""
    generator = exrex.generate(pattern)
    decodedDelimiter = bytes(delimiter, "utf-8").decode("unicode_escape")
    with open(file_name, 'w') as file:
        for expandedPattern in generator:
            file.write(str(expandedPattern) + decodedDelimiter)


if __name__ == '__main__':
    expander()
