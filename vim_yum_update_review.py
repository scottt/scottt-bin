import sys
import os
import subprocess
import itertools

import vim

DEBUG = 0

def version_start_index(s):
    for (i, c) in enumerate(s):
        if c.isdigit() and i != 0 and s[i-1] == '-':
            return i
    raise ValueError

# Supported input formats:
# 1. /var/log/yum.log
#    Mar 23 05:37:10 Updated: system-config-printer-0.7.82.1-3.fc9.x86_64
# 2. /var/log/dnf.rpm.log
#   Mar 13 18:00:25 INFO Installed: systemd-python3-208-15.fc20.x86_64
# 3. /var/log/dnf.rpm.log
#   2017-07-21T02:31:43Z INFO Upgraded: mesa-libOSMesa-17.1.5-1.fc26.i686
# 4. /var/log/dnf.rpm.log
#   2018-12-23T15:46:33Z SUBDEBUG Upgraded: qemu-guest-agent-2:3.0.0-2.fc29.x86_64
def package_version_arch_from_line(line):
    f = line.split()
    if f[1] == 'INFO' or f[1] == 'SUBDEBUG': # format 3 or 4
        package_field_index = 3
    elif f[3] == 'INFO':
        package_field_index = 5 # format 2
    else:
        package_field_index = 4 # format 1
    t = f[package_field_index]
    d = version_start_index(t)
    # handle Epoch:Package, ex:
    # Mar 23 05:33:30 Updated: 1:openoffice.org-math-2.4.0-12.1.fc9.x86_64
    epoch = ''
    if t[0].isdigit():
        j = t.index(':')
        epoch = t[:j]
        t = t[j+1:]
    d = version_start_index(t)
    i = t.rindex('.')
    (package, version, arch) = (t[:d-1], t[d:i], t[i+1:])
    if 0:
        try:
            i = t.rindex('.')
            (package, version, arch) = (t[:d-1], t[d:i], t[i+1:])
        except ValueError:
            arch = None
            try:
                version = f[package_field_index + 1]
            except IndexError:
                version = None
    if DEBUG:
        sys.stderr.write('%s\n' % ((package, version, arch),))
    return (package, version, arch)

def rpm_query(option_list):
    'rpm_query([...]) -> [ LINES_OF_RPM_OUTPUT, ... ]'
    p = subprocess.Popen(['rpm', '-q'] + option_list, stdout=subprocess.PIPE)
    return ( x.rstrip() for x in p.stdout )

def rpm_package_name(package, version=None, arch=None):
    o = [ package ]
    if version:
        o.append('-%s' % version)
    if arch:
        o.append('.%s' % arch)
    return ''.join(o)

def make_rpm_query(op):
    def q(package, version, arch):
        return rpm_query([ op, rpm_package_name(package, version, arch) ])
    return q

rpm_changelog = make_rpm_query('--changelog')
rpm_info = make_rpm_query('--info')
rpm_list = make_rpm_query('--list')
rpm_docfiles = make_rpm_query('--docfiles')
rpm_configfiles = make_rpm_query('--configfiles')
rpm_provides = make_rpm_query('--provides')
rpm_requires = make_rpm_query('--requires')
rpm_conflicts = make_rpm_query('--conflicts')

def rpm_news(package, version, arch):
    #FIXME: If one SRPM produces several RPMs, often the NEWS files is only in the main package
    change_files = []
    for i in rpm_query(['--docfiles', rpm_package_name(package, version, arch) ]):
        name = os.path.basename(i).lower()
        if 'news' in name:
            change_files.append(i)
        elif 'change' in name:
            change_files.append(i)
    return change_files

def view_func_output(func):
    #FIXME: figure out a way to clear the message area afterwards
    vim.command('echo "<.. please wait ..>"')
    #FIXME: really want named vim windows
    #FIXME: hard coded to display data in the lower window
    if len(vim.windows) < 2:
        # FIXME: should mark this buffer "no need to save" somehow
        vim.command('rightbelow new')
    #move cursor to lower window
    vim.command('wincmd j')
    out = list(func())
    #FIXME: work around vim-enhanced-7.0.224-3.fc7 buffer slice assignment bug
    vim.current.window.buffer[:-1] = out
    vim.current.window.cursor = (1, 0)
    #move cursor back to the upper window
    vim.command('wincmd k')

def make_view(lines_func):
    #FIXME: must get the current line info before anyone moves the cursor
    def f():
        (p, v, a) = package_version_arch_from_line(vim.current.line)
        view_func_output(lambda: lines_func(p, v, a))
    return f

def changelog_view():
    # Handle 'Upgraded: OLD-PACKGE-VERSION-ARCH' log format by not passing 'VERSION'
    # to rpm query. e.g.
    # "2018-12-23T15:46:33Z SUBDEBUG Upgraded: gnome-contacts-3.30.1-1.fc29.x86_64"
    (package, version, arch) = package_version_arch_from_line(vim.current.line)
    view_func_output(lambda: rpm_changelog(package=package, version=None, arch=arch))

#FIXME: automatically create views
changelog_view = changelog_view
info_view = make_view(rpm_info)
list_view = make_view(rpm_list)
docfiles_view = make_view(rpm_docfiles)
configfiles_view = make_view(rpm_configfiles)
provides_view = make_view(rpm_provides)
requires_view = make_view(rpm_requires)
conflicts_view = make_view(rpm_conflicts)
news_view = make_view(rpm_news)
