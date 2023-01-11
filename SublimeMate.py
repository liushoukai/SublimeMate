import sys
import sublime
import sublime_plugin
from os.path import dirname
from sublime_plugin import TextCommand
from webbrowser import open_new_tab

sys.path.insert(0, dirname(__file__))


class SublimeMateCommand(TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")


class SublimeMateOpenHelpCommand(TextCommand):
    def run(self, _):
        view_readme()


class SublimeMateOpenBugFile(TextCommand):
    def run(self, _):
        file_bug()


class SublimeMateOpenReleaseNotes(TextCommand):
    def run(self, _):
        view_release_notes()

def file_bug():
    """Opens a new tab in the default browser at this plugin's repo"""
    url = "https://github.com/liushoukai/SublimeMate/issues/new"
    open_new_tab(url)


def view_readme():
    """Opens a new tab in the default browser at this plugin's repo"""
    url = "https://github.com/liushoukai/SublimeMate/blob/master/README.md"
    open_new_tab(url)


def view_release_notes():
    """Opens a new tab in the default browser at this plugin's repo"""
    url = "https://github.com/liushoukai/SublimeMate/releases"
    open_new_tab(url)
