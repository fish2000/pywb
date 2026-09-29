# -*- coding: utf-8 -*-
#
# utils.py – Project config utilities for pywb
#

root_dir = pathlib.Path(__file__).parent.parent

WABAC_SW_URL = "https://cdn.jsdelivr.net/npm/@webrecorder/wabac@2.27.2/dist/sw.js"

def download_wabac_sw():
    """ Download the WABAC SW JavaScript Source """
    print(f"Downloading {WABAC_SW_URL}")
    with urllib.request.urlopen(WABAC_SW_URL) as response:  # nosec
        with open(root_dir.joinpath("pywb", "static", "wabacSW.js"), "wb") as fh:
            fh.write(response.read())


def get_long_description():
    """ Return the contents of `README.rst` """
    with open(root_dir.joinpath('README.rst'), 'r') as fh:
        long_description = fh.read()
    return long_description


class PyTest(TestCommand):
    user_options = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_suite = ' '

    def run_tests(self):
        from gevent.monkey import patch_all
        patch_all()

        import pytest
        import os
        os.environ.pop('PYWB_CONFIG_FILE', None)
        cmdline = '--cov-config .coveragerc --cov pywb'
        cmdline += ' -v --doctest-modules ./pywb/ tests/'

        errcode = pytest.main(cmdline.split(' '))

        sys.exit(errcode)


def get_git_short_hash():
    import subprocess
    try:
        hash_id = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).rstrip()
        if sys.version_info >= (3, 0):
            hash_id = hash_id.decode('utf-8')
        return hash_id
    except Exception:
        return ''


def generate_git_hash_py(pkg, filename='git_hash.py'):
    try:
        git_hash = get_git_short_hash()
        with open(os.path.join(pkg, filename), 'wt') as fh:
            fh.write('git_hash = "{0}"\n'.format(git_hash))
    except Exception:
        pass


def load_text_as_list(filename):
    with open(filename, 'rt') as fh:
        text_list = fh.read().rstrip().split('\n')
    return text_list


def get_package_data():
    pkgs = ['static/*.*',
            'templates/*',
            '*.yaml']

    for root, dirs, files in os.walk(os.path.join('pywb', 'static')):
        for dir_ in dirs:
            pkgs.append(os.path.relpath(os.path.join(root, dir_, '*'), 'pywb'))

    return pkgs

