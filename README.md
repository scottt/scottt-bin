Scott Tsai's Collection of Utilities and Scripts
=

C/C++
===

* cc-defines -- dump gcc's builtin macro definitions
* cc-config -- dump gcc's build configuration
* compilefunc -- generate assembler output on STDOUT for specified functions
* gdbdis -- disassmble a function or memory range through GDB
* gdbx -- examine memory through GDB
* function-is-not-used

Software Development
===

* hostlookup-trace -- trace hostname lookup operations through GDB
* lsof-listening -- list programs listening for TCP connections
* lsof-udp -- list programs bound to UDP ports
* http-static-server -- HTTP server that serves static content in CWD

Python
===

* pyindent -- a copy of cpython/Tools/scripts/reindent.py
* pytraceback-to-grep -- convert Python traceback back to file:line format

Command Line / Shell Scripting
===

* clipboard -- print X11 clipboard to STDOUT
* clipboard-primary -- print X11 middle button paste clipboard ('PRIMARY') to STDOUT
* clipboard-open-file-line -- open $EDITOR to filename:line in X11 clipboard
* argv-print -- debug command line argument passing in scripts
* realpath -- like realpath(3), recent GNU coreutils now ships a realpath binary
* crypt -- compute salted hash with crypt(3)
* md5crypt -- compute MD5 salted hash with crypt(3) (glibc extension)
* sha256crypt -- compute SHA256 salted hash with crypt(3) (glibc extension)
* sha512crypt -- compute SHA512 salted hash with crypt(3) (glibc extension)
* lc -- line count
* range -- "range 1 10" prints 1 to 9 (similar to seq(1))
* dict-grep -- grep word in dictionary file
* random-file -- choose N random files in CWD
* size-sum -- add up the size of the files named in STDIN
* zip-dir -- zip up a directory
* slice -- print a subset of lines from STDIN like head(1) or tail(1)
* vim-pager -- use vim as a pager like more(1)

System Administration
===

* iptables-allow-daap -- open port(s) with iptables
* iptables-allow-http
* iptables-allow-mdns
* iptables-allow-nfsv4
* iptables-allow-samba
* iptables-allow-ssh
* ntp-sync -- sync system time through NTP

Text Encoding Conversion
===

* big5 -- convert STDIN from big5 to utf8
* gb2312 -- convert STDIN from gb2312 to utf8
* utf16 -- convert STDIN from utf16 to utf8
* unzip-big5 -- extract a zip file that uses big5 for filenames

Fedora / RHEL Related
===

* rpmbuild-in-dir -- run rpmbuild assuming all source files are in CWD
* rpmspec-in-dir -- run rpmsec assuming all source files are in CWD
* rpmchangelog -- rpm -q --changelog
* rpmlint-pattern -- run rpmlint on files whose name matches pattern
* rpm-name-strip-version
* rpm-review-files-provides-requires -- review RPM content after packaging
* ygin -- yum groupinstall
* yin -- yum install
* yinlocal -- yum localinstall
* ylist -- yum list
* yre -- yum remove
* yupdate -- yum update
* yupdate-review -- review updates in /var/log/yum.log with VIM
* vim_yum_update_review.py -- part of yupdate-review
* yum_update_log.vim  -- part of yupdate-review
* fedora-source-query -- query Fedora build dependencies
* src-install -- install the source for a file that comes with the OS

Video Encoding / Conversion
* ffmpeg-webm-360p -- convert video to the WebM format through ffmpeg
* flv-to-mp3


Miscellaneous
===

* alarm -- play an alarm sound
* bbs -- telnet to a BBS site. Somehow they're still popular in Taiwan
* bbs-atlantis
* bbs-hsnu
* bbs-ptt
* bbs-ptt2
* bbs-wretch
* gnome-recently-used-clear -- clear the recently used files list in GNOME
* pdf-pages -- merge multiple pages from a source PDF into one
* sine-wave-audio -- play a test sound pattern
* vm-start -- manage virtual machines through "virsh"
* xnest -- start a nested Xnest server through startx
