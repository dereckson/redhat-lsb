%ifarch %{ix86}
%define ldso ld-linux.so.2
%endif

%ifarch %{ia64}
%define ldso ld-linux-ia64.so.2
%endif

%define lsbrelver 1.4

Summary: LSB support for Red Hat Linux
Name: redhat-lsb
Version: 1.1.0
Release: 0.4
URL: http://www.linuxbase.org/
Source0: %{name}-%{version}.tar.bz2
Source1: http://prdownloads.sourceforge.net/lsb/lsb-release-%{lsbrelver}.tar.gz
License: GPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-root
Provides: lsb = %{version}
ExclusiveArch: i386

%ifarch %{ix86}
# archLSB IA32 Base Libraries
Requires: libc.so.6
Requires: libm.so.6
Requires: libpthread.so.0
Requires: libz.so.1
Requires: libutil.so.1
%endif

%ifarch ia64
# archLSB IA64 Base Libraries
Requires: libcrypt.so.1
Requires: libdb.so.3
Requires: libdl.so.2
Requires: libpthread.so.0
%endif

# gLSB Base Libraries
Requires: libdl.so.2
Requires: libcrypt.so.1

# gLSB Utility Libraries
Requires: libz.so.1
Requires: libncurses.so.5

# gLSB Graphics Libraries
Requires: libX11.so.6
Requires: libXext.so.6
Requires: libSM.so.6
Requires: libICE.so.6
Requires: libXt.so.6
Requires: libGL.so.1

# gLSB Command and Utilities
Requires: /bin/awk
Requires: /bin/basename
Requires: /bin/cat
Requires: /bin/chgrp
Requires: /bin/chmod
Requires: /bin/chown
Requires: /bin/cp
Requires: /bin/cpio
Requires: /bin/cut
Requires: /bin/date
Requires: /bin/dd
Requires: /bin/df
Requires: /bin/echo
Requires: /bin/egrep
Requires: /bin/false
Requires: /bin/fgrep
Requires: /bin/grep
Requires: /bin/gunzip
Requires: /bin/gzip
Requires: /bin/hostname
Requires: /bin/kill
Requires: /bin/ln
Requires: /bin/ls
Requires: /bin/mkdir
Requires: /bin/mknod
Requires: /bin/mktemp
Requires: /bin/more
Requires: /bin/mount
Requires: /bin/mv
Requires: /bin/nice
Requires: /bin/ps
Requires: /bin/pwd
Requires: /bin/rm
Requires: /bin/rmdir
Requires: /bin/sed
Requires: /bin/sh
Requires: /bin/sleep
Requires: /bin/sort
Requires: /bin/stty
Requires: /bin/su
Requires: /bin/sync
Requires: /bin/tar
Requires: /bin/touch
Requires: /bin/true
Requires: /bin/umount
Requires: /bin/uname
Requires: /sbin/fuser
Requires: /sbin/pidof
Requires: /usr/bin/ar
Requires: /usr/bin/at
Requires: /usr/bin/batch
Requires: /usr/bin/bc
Requires: /usr/bin/chfn
Requires: /usr/bin/chsh
Requires: /usr/bin/cksum
Requires: /usr/bin/cmp
Requires: /usr/bin/col
Requires: /usr/bin/comm
Requires: /usr/bin/crontab
Requires: /usr/bin/csplit
Requires: /usr/bin/diff
Requires: /usr/bin/dirname
Requires: /usr/bin/du
Requires: /usr/bin/env
Requires: /usr/bin/expand
Requires: /usr/bin/expr
Requires: /usr/bin/file
Requires: /usr/bin/find
Requires: /usr/bin/fold
Requires: /usr/bin/gencat
Requires: /usr/bin/getconf
Requires: /usr/bin/groups
Requires: /usr/bin/head
Requires: /usr/bin/iconv
Requires: /usr/bin/id
Requires: /usr/bin/install
Requires: /usr/bin/ipcrm
Requires: /usr/bin/ipcs
Requires: /usr/bin/join
Requires: /usr/bin/killall
Requires: /usr/bin/locale
Requires: /usr/bin/localedef
Requires: /usr/bin/logname
Requires: /usr/bin/lpr
Requires: /usr/bin/m4
Requires: /usr/bin/make
Requires: /usr/bin/man
Requires: /usr/bin/md5sum
Requires: /usr/bin/mkfifo
Requires: /usr/bin/newgrp
Requires: /usr/bin/nl
Requires: /usr/bin/nohup
Requires: /usr/bin/od
Requires: /usr/bin/passwd
Requires: /usr/bin/paste
Requires: /usr/bin/patch
Requires: /usr/bin/pathchk
Requires: /usr/bin/pr
Requires: /usr/bin/printf
Requires: /usr/bin/renice
Requires: /usr/bin/rsync
Requires: /usr/bin/split
Requires: /usr/bin/strip
Requires: /usr/bin/sum
Requires: /usr/bin/tail
Requires: /usr/bin/tee
Requires: /usr/bin/test
Requires: /usr/bin/time
Requires: /usr/bin/tr
Requires: /usr/bin/tsort
Requires: /usr/bin/tty
Requires: /usr/bin/unexpand
Requires: /usr/bin/uniq
Requires: /usr/bin/wc
Requires: /usr/bin/xargs
Requires: /usr/sbin/groupadd
Requires: /usr/sbin/groupdel
Requires: /usr/sbin/groupmod
Requires: /usr/sbin/sendmail
Requires: /usr/sbin/useradd
Requires: /usr/sbin/userdel
Requires: /usr/sbin/usermod

# gLSB System Initialization
Requires: /lib/lsb/init-functions
Requires: chkconfig >= 1.3.2-1
Requires: initscripts >= 6.56-1

%description
The Linux Standards Base (LSB) is an attempt to develop a set of
standards that will increase compatibility among Linux distributions.
The redhat-lsb package provides utilities needed for LSB Compliant
Applications.  It also contains requirements that will ensure that all
components required by the LSB that are provided by Red Hat Linux are
installed on the system.

%prep
%setup -q -a 1

%build
cd lsb-release-%{lsbrelver}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/%{_mandir} \
         $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_libdir}/lsb
make DESTDIR=$RPM_BUILD_ROOT install
cd lsb-release-%{lsbrelver}
make mandir=$RPM_BUILD_ROOT/%{_mandir} prefix=$RPM_BUILD_ROOT/%{_prefix} install
cd ..
cat > $RPM_BUILD_ROOT/etc/lsb-release <<EOF
LSB_VERSION="1.1.0"
EOF

ln -s %{ldso} $RPM_BUILD_ROOT/lib/ld-lsb.so.1

ln -snf ../../../sbin/chkconfig $RPM_BUILD_ROOT%{_libdir}/lsb/install_initd
ln -snf ../../../sbin/chkconfig $RPM_BUILD_ROOT%{_libdir}/lsb/remove_initd



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/lsb-release
/etc/redhat-lsb
%{_mandir}/*/*
%{_bindir}/*
%{_libdir}/lsb
/lib/lsb
/lib/ld-lsb.so.1

%changelog
* Tue Mar 12 2002 Bill Nottingham <notting@redhat.com>
- add initscripts support

* Thu Jan 24 2002 Matt Wilson <msw@redhat.com>
- Initial build.


