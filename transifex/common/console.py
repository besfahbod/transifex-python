from __future__ import unicode_literals

import click


class Color:
    """Convenience class for adding color to console output."""

    CYAN = '\033[36m'
    WHITE_BOLD = '\033[1m'
    GREEN = '\033[32m'
    PINK = '\033[91m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    END = '\033[0m'

    @staticmethod
    def format(string):
        """Format the given string, adding color support."""
        return (
            # Context
            string.replace('[high]', Color.WHITE_BOLD)
            .replace('[warn]', Color.PINK)
            .replace('[file]', Color.CYAN)
            .replace('[opt]', Color.PINK)
            .replace('[prompt]', Color.YELLOW)
            .replace('[error]', Color.RED)
            .replace('[end]', Color.END)  # closing tag for any color tag

            # Colors
            .replace('[cyan]', Color.CYAN)
            .replace('[green]', Color.GREEN)
            .replace('[red]', Color.RED)
            .replace('[yel]', Color.YELLOW)
        )

    @staticmethod
    def echo(string, new_line=True):
        """Print to the console with color support."""
        if new_line:
            print(Color.format(string))
        else:
            print(Color.format(string)),


def prompt(prompt_msg, description=None, default=None, new_line=False, vtype=None):
    """Prompt the user to enter a reply.

    :param str prompt_msg: the prompt message
    :param basestr description: an optional description to show above the prompt message
    :param basestr default: an optional default value
    :param bool new_line: if True, an empty line will be printed before the prompt
    :param type vtype: the expected type of the input
    :return: the prompt object returned by Click
    :rtype: Any
    """
    if new_line:
        Color.echo('')

    if description:
        Color.echo('[prompt]{description}[end]'.format(
            description=description))

    return click.prompt(prompt_msg, default=default, type=(vtype or str))
