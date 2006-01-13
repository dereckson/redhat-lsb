# Define this to link to which library version
%define lsbsover 3

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

%define lsbrelver 2.0
%define srcrelease 1

Summary: LSB support for Red Hat Linux
Name: redhat-lsb
Version: 3.0
Release: 9
URL: http://www.linuxbase.org/
Source0: %{name}-%{version}-%{srcrelease}.tar.bz2
Source1: http://prdownloads.sourceforge.net/lsb/lsb-release-%{lsbrelver}.tar.gz
Patch0: lsb-release-2.0-disable-etc-lsb-release.patch
License: GPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-root
# dependency for primary LSB application for v1.3
Provides: lsb = %{version}
# dependency for primary LSB application for v2.0 and v3.0
%ifarch %{ix86}
%define archname ia32
%endif
%ifarch ia64
%define archname ia64
%endif
%ifarch ppc
%define archname ppc32
%endif
%ifarch ppc64
%define archname ppc64
%endif
%ifarch s390
%define archname s390
%endif
%ifarch s390x
%define archname s390x
%endif
%ifarch x86_64
%define archname amd64
%endif
Provides: lsb-core-%{archname} = %{version}
Provides: lsb-graphics-%{archname} = %{version}
Provides: lsb-core-noarch = %{version}
Provides: lsb-graphics-noarch = %{version}

ExclusiveArch: i386 ia64 x86_64 ppc ppc64 s390 s390x

%ifarch %{ix86}
# archLSB IA32 Base Libraries
Requires: libcrypt.so.1
Requires: libc.so.6
Requires: libdl.so.2
Requires: libgcc_s.so.1
Requires: libm.so.6
Requires: libpthread.so.0
%endif

%ifarch ia64
# archLSB IA64 Base Libraries
Requires: libcrypt.so.1()(64bit)
Requires: libc.so.6.1()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libgcc_s.so.1()(64bit)
Requires: libm.so.6.1()(64bit)
Requires: libpthread.so.0()(64bit)
%endif

%ifarch ppc
# archLSB PPC32 Base Libraries
Requires: libcrypt.so.1
Requires: libc.so.6
Requires: libdl.so.2
Requires: libgcc_s.so.1
Requires: libm.so.6
Requires: libpthread.so.0
%endif

%ifarch ppc64
# archLSB PPC64 Base Libraries
Requires: libcrypt.so.1()(64bit)
Requires: libc.so.6()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libgcc_s.so.1()(64bit)
Requires: libm.so.6()(64bit)
Requires: libpthread.so.0()(64bit)
%endif

%ifarch s390
# archLSB S390 Base Libraries
Requires: libcrypt.so.1
Requires: libc.so.6
Requires: libdl.so.2
Requires: libgcc_s.so.1
Requires: libm.so.6
Requires: libpthread.so.0
%endif

%ifarch s390x
# archLSB S390X Base Libraries
Requires: libcrypt.so.1()(64bit)
Requires: libc.so.6()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libgcc_s.so.1()(64bit)
Requires: libm.so.6()(64bit)
Requires: libpthread.so.0()(64bit)
%endif

%ifarch x86_64
# archLSB AMD64 Base Libraries
Requires: libcrypt.so.1()(64bit)
Requires: libc.so.6()(64bit)
Requires: libdl.so.2()(64bit)
Requires: libgcc_s.so.1()(64bit)
Requires: libm.so.6()(64bit)
Requires: libpthread.so.0()(64bit)
%endif

# gLSB Base Libraries
Requires: libpthread.so.0%{qual}
Requires: libgcc_s.so.1%{qual}
Requires: libdl.so.2%{qual}
Requires: librt.so.1%{qual}
Requires: libcrypt.so.1%{qual}
Requires: libpam.so.0%{qual}

# LSB Base C++
Requires: libstdc++.so.6%{qual}

# gLSB Utility Libraries
Requires: libz.so.1%{qual}
Requires: libncurses.so.5%{qual}
Requires: libutil.so.1%{qual}

# gLSB Graphics Libraries
Requires: libX11.so.6%{qual}
Requires: libSM.so.6%{qual}
Requires: libICE.so.6%{qual}
Requires: libXt.so.6%{qual}
Requires: libXext.so.6%{qual}
Requires: libXi.so.6%{qual}
Requires: libGL.so.1%{qual}

# gLSB Command and Utilities
Requires: /bin/basename
Requires: /bin/cat
Requires: /bin/chgrp
Requires: /bin/chmod
Requires: /bin/chown
Requires: /bin/cp
Requires: /bin/cpio
Requires: /bin/date
Requires: /bin/dd
Requires: /bin/df
Requires: /bin/dmesg
Requires: /bin/echo
Requires: /bin/ed
Requires: /bin/egrep
Requires: /bin/false
Requires: /bin/fgrep
Requires: /bin/grep
Requires: /bin/hostname
Requires: /bin/ln
Requires: /bin/ls
#Requires: /bin/mailx
Requires: mailx
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
Requires: /usr/bin/awk
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
Requires: /usr/bin/cut
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
Requires: /usr/bin/gettext
Requires: /usr/bin/groups
Requires: /usr/bin/gunzip
Requires: /usr/bin/gzip
Requires: /usr/bin/head
Requires: /usr/bin/iconv
Requires: /usr/bin/id
Requires: /usr/bin/install
Requires: /usr/bin/ipcrm
Requires: /usr/bin/ipcs
Requires: /usr/bin/join
Requires: /usr/bin/kill
Requires: /usr/bin/killall
Requires: /usr/bin/locale
Requires: /usr/bin/localedef
Requires: /usr/bin/logger
Requires: /usr/bin/logname
Requires: /usr/bin/lp
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
Requires: /usr/bin/pax
Requires: /usr/bin/pr
Requires: /usr/bin/printf
Requires: /usr/bin/renice
Requires: /usr/bin/split
Requires: /usr/bin/strip
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
%patch0 -p 0 

%build
cd lsb-release-%{lsbrelver}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/%{_lib} $RPM_BUILD_ROOT/%{_mandir} \
         $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/usr/lib/lsb \
         $RPM_BUILD_ROOT/etc/lsb-release.d/ $RPM_BUILD_ROOT/usr/sbin/
make DESTDIR=$RPM_BUILD_ROOT install
cd lsb-release-%{lsbrelver}
make mandir=$RPM_BUILD_ROOT/%{_mandir} prefix=$RPM_BUILD_ROOT/%{_prefix} install
cd ..
touch $RPM_BUILD_ROOT/etc/lsb-release.d/core-3.0-%{archname}
touch $RPM_BUILD_ROOT/etc/lsb-release.d/core-3.0-noarch
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-3.0-%{archname}
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-3.0-noarch 

for LSBVER in %{lsbsover}; do
  ln -s %{ldso} $RPM_BUILD_ROOT/%{_lib}/%{lsbldso}.$LSBVER
done

mkdir -p $RPM_BUILD_ROOT/bin

ln -snf ../../../sbin/chkconfig $RPM_BUILD_ROOT/usr/lib/lsb/install_initd
ln -snf ../../../sbin/chkconfig $RPM_BUILD_ROOT/usr/lib/lsb/remove_initd
ln -snf mail $RPM_BUILD_ROOT/bin/mailx

gcc -Os -static -o redhat_lsb_trigger{.%{_target_cpu},.c} -DLSBSOVER='"%{lsbsover}"' \
  -DLDSO='"%{ldso}"' -DLSBLDSO='"/%{_lib}/%{lsbldso}"' -D_GNU_SOURCE
install -m 700 redhat_lsb_trigger.%{_target_cpu} \
  $RPM_BUILD_ROOT/usr/sbin/redhat_lsb_trigger.%{_target_cpu}


%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- glibc
if [ -x /usr/sbin/redhat_lsb_trigger.%{_target_cpu} ]; then
  /usr/sbin/redhat_lsb_trigger.%{_target_cpu}
fi

%ifarch %{ix86}
%post
# make this softlink again for /emul
  if [ -f /emul/ia32-linux/lib/%{ldso} ]; then
    for LSBVER in %{lsbsover}; do
      /sbin/sln /emul/ia32-linux/lib/%{ldso} /%{_lib}/%{lsbldso}.$LSBVER || :
    done
  fi
%endif

%files
%defattr(-,root,root)
/etc/redhat-lsb
%dir /etc/lsb-release.d
/etc/lsb-release.d/*
%{_mandir}/*/*
%{_bindir}/*
/bin/mailx
/usr/lib/lsb
/lib/lsb
/%{_lib}/*
/usr/sbin/redhat_lsb_trigger.%{_target_cpu}

%changelog
* Fri Jan 13 2006 Leon Ho <llch@redhat.com> 3.0-9
- Migrated back to rawhide

* Wed Aug  3 2005 Leon Ho <llch@redhat.com> 3.0-8.EL
- Added libstdc++.so.6/libGL.so.1 requirement (RH#154605)

* Wed Aug  3 2005 Leon Ho <llch@redhat.com> 3.0-7.EL
- Fixed multilib problem on lsb_release not to read /etc/lsb-release and solely 
  depends on /etc/lsb-release.d/ (Advised by LSB committee)
- Removed /etc/lsb-release (Advised by LSB committee)

* Mon Aug  1 2005 Leon Ho <llch@redhat.com> 3.0-6.EL
- Made the /etc/lsb-release useful (RH#154605)
- Added redhat_lsb_trigger to fix RH#160585 (Jakub Jelinek)
- Fixed AMD64 base libraries requirement parsing (RH#154605) 

* Fri Jul 29 2005 Leon Ho <llch@redhat.com> 3.0-5.EL
- Fixed redhat-lsb's mkredhat-lsb on fetching lib and cmd requirements (RH#154605)
- Changed explicit mailx command requirement to package requirements (RH#164124)
- Added mailx symlink to /bin/mail (RH#164124)
- Added lsb-core-noarch and lsb-graphics-noarch and lsb-graphics-{arch} requirements (RH#164468)
- Added requirements from lsb_release command on lsb-release.d and deps. (RH#164468)

* Mon Jul 18 2005 Leon Ho <llch@redhat.com> 3.0-4.EL
- Rebuilt

* Tue Jul 05 2005 Leon Ho <llch@redhat.com> 3.0-3.EL
- Disabled support for LSB 1.3 and 2.0

* Mon Jun 20 2005 Leon Ho <llch@redhat.com> 3.0-2.EL
- Upgraded to lsb-release 2.0

* Thu Jun 09 2005 Leon Ho <llch@redhat.com> 3.0-1.EL
- Moved to LSB 3.0

* Wed Apr 13 2005 Leon Ho <llch@redhat.com> 1.3-10
- Fixed ix86 package with ia32 emul support 

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

