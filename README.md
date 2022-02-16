Scott Tsai's $HOME/bin
=

C / C++
===

* cc-defines -- dump gcc's builtin macro definitions
* cc-linker-script -- dump gcc's default linker script
* cc-config -- dump gcc's build configuration. Useful when examining vendor cross compiler toolchains.
* cc-compile -- compile program from STDIN and print assembly to STDOUT
* compilefunc -- generate assembler output on STDOUT for specified functions
* gdbdis -- disassemble a function or memory range through GDB
* gdbx -- examine memory through GDB
* gdb-info-scope -- Use gdb to list the variables local to a scope.  Shows DWARF debug info.
* gdb-info-{functions,variables,types,line} -- show functions, variables etc through GDB
* function-is-not-used
* dwarf-analyze-gcc-switches -- analyze which files where compiled with what flags when `-grecord-gcc-switches` is used
* elf-interp-dump -- show `.interp` section content of ELF files

macOS / OSX / iOS
===
* otool-rpath -- print the RPATH from a Mach-O binary
* otool-needed -- print the shared libraries and frameworks required by a Mach-O binary
* otool-install-name -- print the INSTALL NAME of a shared library or framework (similar to a SONAME)
* focus-follows-mouse{,off} -- turn focus-follows-mouse on/off using `yabai`

Software Development
===

* hostlookup-trace -- trace hostname lookup operations through GDB
* lsof-listening -- list programs listening for TCP connections
* lsof-udp -- list programs bound to UDP ports
* http-static-server -- HTTP server that serves static content in CWD
* git-clean -- delete files not tracked by git
* git-config-credential-libsecret -- use libsecret as the Git credentil helper

Python
===

* pyindent -- a copy of cpython/Tools/scripts/reindent.py
* pytraceback-to-grep -- convert Python traceback to a file:line format similar to grep

Django
===
* django-secret-key-gen -- generate random `SECRET_KEY` for `settings.py`

Command Line / Shell Scripting
===

* clipboard-print -- print X11 clipboard to STDOUT
* clipboard-zh-tw-quote -- add Taiwanese style quotation marks to clipboard content
* clipboard-html-escape -- convert '&', '<', '>' to HTML-safe sequences
* clipboard-copy -- copy file content to X11 clipboard
* clipboard-open-file-line -- open $EDITOR to filename:line in X11 clipboard
* argv-print -- debug command line argument passing in scripts
* realpath -- like `realpath(3)`, recent GNU coreutils now ships a realpath binary
* crypt -- compute salted hash with `crypt(3)`
* md5crypt -- compute MD5 salted hash with `crypt(3)` (glibc extension)
* sha256crypt -- compute SHA256 salted hash with `crypt(3)` (glibc extension)
* sha512crypt -- compute SHA512 salted hash with `crypt(3)` (glibc extension)
* lc -- line count
* range -- `range 1 10` prints 1 to 9 (similar to `seq(1)`)
* dict-grep -- grep word in dictionary file
* random-file -- choose N random files in CWD
* random-string -- use `openssl` to generate 32-bytes of random data than base64 encode it
* size-sum -- add up the size of the files named in STDIN
* zip-dir -- zip up a directory
* slice -- print a subset of lines from STDIN like `head(1)` or `tail(1)`
* vim-pager -- use vim as a pager like `more(1)`
* xdg-rename-by-content -- change file extension to match file type detected from content
* terminal-colors-list -- list colors supported by terminal
* prompt-str-gen -- generate a str with terminal underline and color control codes
* treels -- flat, `ls -l` like output with `tree`
* prefix -- print first N characters from STDIN

System Administration / DevOps
===

* utc-timestamp -- Unix timestamp (seconds since Jan 1, 1970) for current time in UTC
* ssh-pubkey-from-pem -- convert SSH public key from PEM to .ssh format
* remote-domain-socket-proxy -- connect to a remote Unix domain socket through a local one.
  e.g. MySQL remote administration.
* iptables-allow-{daap,http,mdns,nfsv4,samba,ssh,soundwire,steam} -- open port(s) with iptables
* iptables-allow-mdns-over-host-nat -- allow mDNS (avahi) over host NAT mostly for libvirt VMs.
* iptables-reject-hinet-youtube-servers -- workaround to get faster YouTube connections in Taiwan
* iptables-reject-slow-akaimai-bloomberg-tv -- workaround for watching bloomberg.com/tv in Taiwan
* iptables-list-INPUT -- list firewall input rules
* iptables-save -- save iptables rules across reboots
* ntp-sync -- sync system time through NTP
* disk-{scan,deactivate} -- useful for eSATA hotplug. Nicer than scsi-rescan in `sg3_utils`.
* git-repo-add-email-notifications -- configures email notification in git repositories.
* vm-start -- manage virtual machines through "virsh" / libvirt
* mdns-discover -- use `avahi-browse` to discover network services
* expressvpn-virtmanager-workaround -- restart virtmanager networks after ExpressVPN disconnect
* generate-random-password -- use `openssl` to generate a random password
* smbclient-browse -- browse available shares on an SMB host using `smbclient`

Certificates
===
* {ca-,}cert-gen -- generate x509 certificate with openssl
* ca-cert-install-on-{fedora,mac} -- install and trust self-signed certificate
* openssl-inspect-{csr,pem} -- inspect Certificate Signing Request and PEM files
* openssl-test-connect -- debug TLS handshake connect
* mac-list-keychains -- list keychains on Mac OS

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
* {ygin,yin,yinlocal,ylist,yre,yupdate} -- yum {group install,install,localinstall,list,remove,update}
* {dgin,din,dinlocal,dlist,dre,dupdate,dbuilddep} -- dnf {group install,install,localinstall,list,remove,update,builddep}
* dnf-wrapper -- implementation of the dnf shorthands
* {d,y}update-review -- review the YUM or DNF log file in VIM. See yum_update_log.vim for key bindings
* vim_yum_update_review.py -- part of yupdate-review
* yum_update_log.vim  -- part of yupdate-review. Key bindings for showing changelog, provides, requires etc
* fedora-source-query -- query Fedora build dependencies
* src-install -- install the source for a file that comes with the OS
* yum-febootstrap -- create chroots from Fedora repositories with yum
* yinchroot -- install package(s) in chroot
* graphics-stack-versions -- list Linux graphics stack component versions on the running system
* airplane-mode-{on,off} -- under Linux, turn bluetooth and WiFi on/off (implemented with `rfkill`)

Audio / Video Encoding and Conversion
===

* sine-wave-audio -- play a sine wave test sound pattern (via GStreamer)
* sine-wave-save -- save a sine wave test sound pattern as a RAW or WAV file
* video-extract-audio -- extract audio streams from video files for (rough, useful for
  music videos from YouTube)
* audio-transcode-for-google-music -- transcode audio files not support by Google Music to a
  suitable format.
* mp4-faststart-optimize -- remux MP4 file into 'faststart' format for streaming using ffmpeg
* qtfaststart-list-moov -- check whether MP4 file is in 'faststart' format
* ffmpeg-h264-mp4-faststart -- convert video to the H264 in MP4 format optimized for streaming
* ffmpeg-h264-mkv -- convert video to H264 in MKV format
* ffmpeg-webm-360p -- convert video to the WebM format through ffmpeg
* flv-to-mp3 -- covnert audio tracks in FLV to an MP3
* pulseaudio-rtp-serve -- broadcast audio from Linux through RTP in PCM or MP3 format
* pulseaudio-simple-serve -- listen for connections and serve PCM audio

Miscellaneous
===

* imgs-to-pdf -- convert bitmap images to a multipage PDF
* pdf-to-jpg -- convert PDF to JPEG
* vector-to-png -- convert SVG to PNG
* pdf-pages -- merge multiple pages from a source PDF into one
* pdf-{add,remove}-password -- remove password from PDF (with qpdf)
* gnome-recently-used-clear -- clear the recently used files list in GNOME
* alarm -- play an alarm sound
* xnest -- start a nested Xnest server through startx
* bbs-{ptt,ptt2} -- telnet to the PTT or PTT2 BBS sites
* bbs -- telnet to a BBS site. Somehow they're still popular in Taiwan
* document-files-in-README -- help maintain this README
