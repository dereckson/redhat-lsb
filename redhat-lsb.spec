# Define this to link to which library version
%define lsbsover 1 2

%ifarch %{ix86}
%define ldso ld-linux.so.2
%define lsbldso ld-lsb.so
%endif

%ifarch ia64
%define ldso ld-linux-ia64.so.2
%define lsbldso ld-lsb-ia64.so
%endif

%ifarch ppc
%define ldso ld.so.1
%define lsbldso ld-lsb-ppc32.so
%endif

%ifarch ppc64
%define ldso ld64.so.1
%define lsbldso ld-lsb-ppc64.so
%endif

%ifarch s390
%define ldso ld.so.1
%define lsbldso ld-lsb-s390.so
%endif

%ifarch s390x
%define ldso ld64.so.1
%define lsbldso ld-lsb-s390x.so
%endif

%ifarch x86_64
%define ldso ld-linux-x86-64.so.2
%define lsbldso ld-lsb-x86-64.so
%endif

%ifarch ia64 ppc64 s390x x86_64
%define qual ()(64bit)
%else
%define qual %{nil}
%endif

%define lsbrelver 1.4

Summary: LSB support for Red Hat Linux
Name: redhat-lsb
Version: 1.3
Release: 8
URL: http://www.linuxbase.org/
Source0: %{name}-%{version}.tar.bz2
Source1: http://prdownloads.sourceforge.net/lsb/lsb-release-%{lsbrelver}.tar.gz
License: GPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-root
# dependency for primary LSB application for v1.3
Provides: lsb = %{version}
# dependency for primary LSB application for v2.0
%ifarch %{ix86}
Provides: lsb-core-ia32 = %{version}
%endif
%ifarch ia64
Provides: lsb-core-ia64 = %{version}
%endif
%ifarch ppc
Provides: lsb-core-ppc32 = %{version}
%endif
%ifarch ppc64
Provides: lsb-core-ppc64 = %{version}
%endif
%ifarch s390
Provides: lsb-core-s390 = %{version}
%endif
%ifarch s390x
Provides: lsb-core-s390x = %{version}
%endif
%ifarch x86_64
Provides: lsb-core-amd64 = %{version}
%endif

%ifarch ia64 ppc64 s390x x86_64
%define qual ()(64bit)
%else
%define qual %{nil}
%endif
ExclusiveArch: i386 ia64 x86_64 ppc ppc64 s390 s390x

%ifarch %{ix86}
# archLSB IA32 Base Libraries
Requires: libcrypt.so.1
Requires: libc.so.6
Requires: libdl.so.2
Requires: libm.so.6
Requires: libpthread.so.0
%endif

%ifarch ia64
# archLSB IA64 Base Libraries
Requires: libcrypt.so.1()(64bit)
Requires: libc.so.6.1()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libm.so.6.1()(64bit)
Requires: libpthread.so.0()(64bit)
%endif

%ifarch ppc
# archLSB PPC32 Base Libraries
Requires: libcrypt.so.1
Requires: libc.so.6
Requires: libdl.so.2
Requires: libm.so.6
Requires: libpthread.so.0
%endif

%ifarch ppc64
# archLSB PPC64 Base Libraries
Requires: libcrypt.so.1()(64bit)
Requires: libc.so.6()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libm.so.6()(64bit)
Requires: libpthread.so.0()(64bit)
%endif

%ifarch s390
# archLSB S390 Base Libraries
Requires: libcrypt.so.1
Requires: libc.so.6
Requires: libdl.so.2
Requires: libm.so.6
Requires: libpthread.so.0
%endif

%ifarch s390x
# archLSB S390X Base Libraries
Requires: libcrypt.so.1()(64bit)
Requires: libc.so.6()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libm.so.6()(64bit)
Requires: libpthread.so.0()(64bit)
%endif

%ifarch x86_64
# archLSB X86-64 Base Libraries
Requires: libcrypt.so.1()(64bit)
Requires: libc.so.6()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libm.so.6()(64bit)
Requires: libpthread.so.0()(64bit)
%endif

# gLSB Base Libraries
Requires: libpthread.so.0%{qual}
Requires: libgcc_s.so.1%{qual}
Requires: libdl.so.2%{qual}
Requires: libcrypt.so.1%{qual}
Requires: libpam.so.0%{qual}

# gLSB Utility Libraries
Requires: libz.so.1%{qual}
Requires: libncurses.so.5%{qual}
Requires: libutil.so.1%{qual}

# gLSB Graphics Libraries
Requires: libX11.so.6%{qual}
Requires: libXext.so.6%{qual}
Requires: libSM.so.6%{qual}
Requires: libICE.so.6%{qual}
Requires: libXt.so.6%{qual}
Requires: libGL.so.1%{qual}

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
Requires: /bin/dmesg
Requires: /bin/echo
Requires: /bin/egrep
Requires: /bin/env
Requires: /bin/false
Requires: /bin/fgrep
Requires: /bin/gettext
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
Requires: /sbin/shutdown
Requires: /usr/bin/[
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
Requires: /usr/bin/msgfmt
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
Requires: /usr/lib/lsb/install_initd
Requires: /usr/lib/lsb/remove_initd
Requires: /usr/sbin/groupadd
Requires: /usr/sbin/groupdel
Requires: /usr/sbin/groupmod
Requires: /usr/sbin/sendmail
Requires: /usr/sbin/useradd
Requires: /usr/sbin/userdel
Requires: /usr/sbin/usermod

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
mkdir -p $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/%{_lib} $RPM_BUILD_ROOT/%{_mandir} \
         $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/usr/lib/lsb
make DESTDIR=$RPM_BUILD_ROOT install
cd lsb-release-%{lsbrelver}
make mandir=$RPM_BUILD_ROOT/%{_mandir} prefix=$RPM_BUILD_ROOT/%{_prefix} install
cd ..
cat > $RPM_BUILD_ROOT/etc/lsb-release <<EOF
LSB_VERSION="1.3"
EOF

for LSBVER in %{lsbsover}; do
  ln -s %{ldso} $RPM_BUILD_ROOT/%{_lib}/%{lsbldso}.$LSBVER
done

ln -snf ../../../sbin/chkconfig $RPM_BUILD_ROOT/usr/lib/lsb/install_initd
ln -snf ../../../sbin/chkconfig $RPM_BUILD_ROOT/usr/lib/lsb/remove_initd

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- glibc
%ifnarch %{ix86}
  /sbin/sln %{ldso} /%{_lib}/%{lsbldso} || :
%else
  if [ -f /emul/ia32-linux/lib/%{ldso} ]; then
    /sbin/sln /emul/ia32-linux/lib/%{ldso} /%{_lib}/%{lsbldso} || :
  else
    /sbin/sln %{ldso} /%{_lib}/%{lsbldso} || :
  fi
%endif

%ifarch %{ix86}
%post
# make this softlink again for /emul
  if [ -f /emul/ia32-linux/lib/%{ldso} ]; then
    /sbin/sln /emul/ia32-linux/lib/%{ldso} /%{_lib}/%{lsbldso} || :
  fi
%endif

%files
%defattr(-,root,root)
%config /etc/lsb-release
/etc/redhat-lsb
%{_mandir}/*/*
%{_bindir}/*
/usr/lib/lsb
/lib/lsb
/%{_lib}/*

%changelog
* Tue Feb 01 2005 Leon Ho <llch@redhat.com> 1.3-9
- Sync what we have changed on the branches
  Wed Nov 24 2004 Harald Hoyer <harald@redhat.com>
  - added post section to recreate the softlink in emul mode (bug 140739)
  Mon Nov 15 2004 Phil Knirsch <pknirsch@redhat.com>
  Tiny correction of bug in new triggers

* Mon Jan 24 2005 Leon Ho <llch@redhat.com> 1.3-8
- Add support provide on lsb-core-* for each arch

* Fri Jan 21 2005 Leon Ho <llch@redhat.com> 1.3-7
- Add to support multiple LSB test suite version
- Add %endif in trigger postun

* Thu Nov 11 2004 Phil Knirsch <pknirsch@redhat.com> 1.3-6
- Fixed invalid sln call for trigger in postun on ia64 (#137647)

* Mon Aug 09 2004 Phil Knirsch <pknirsch@redhat.com> 1.3-4
- Bump release and rebuilt for RHEL4.

* Thu Jul 24 2003 Matt Wilson <msw@redhat.com> 1.3-3
- fix lsb ld.so name for ia64 (#100613)

* Fri May 23 2003 Matt Wilson <msw@redhat.com> 1.3-2
- use /usr/lib/lsb for install_initd, remove_initd

* Fri May 23 2003 Matt Wilson <msw@redhat.com> 1.3-2
- add ia64 x86_64 ppc ppc64 s390 s390x

* Tue Feb 18 2003 Matt Wilson <msw@redhat.com> 1.3-1
- 1.3

* Wed Sep  4 2002 Matt Wilson <msw@redhat.com>
- 1.2.0

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 27 2002 Matt Wilson <msw@redhat.com>
- addeed trigger on glibc to re-establish the ld-lsb.so.1 symlink in the
  forced downgrade case.

* Tue Mar 12 2002 Bill Nottingham <notting@redhat.com>
- add initscripts support

* Thu Jan 24 2002 Matt Wilson <msw@redhat.com>
- Initial build.


