# Conditional build:
%bcond_without	tests		# build without tests

# disable file duplicate packaging error
%define		_duplicate_files_terminate_build   0
%define		bld_ver	13
%define		bhash	90cf5d8f270a4347a95050320eef3fb7
# class data version seen with file(1) that this jvm is able to load
%define		_classdataversion 55.0
Summary:	Oracle JDK (Java Development Kit) for Linux
Summary(pl.UTF-8):	Oracle JDK - środowisko programistyczne Javy dla Linuksa
Name:		oracle-java11
Version:	11.0.1
Release:	1
License:	restricted, distributable
# http://www.oracle.com/technetwork/java/javase/terms/license/index.html
# See "LICENSE TO DISTRIBUTE SOFTWARE" section, which states you can
# redistribute in unmodified form.
Group:		Development/Languages/Java
# Download URL (requires JavaScript and interactive license agreement):
# http://www.oracle.com/technetwork/java/javase/downloads/index.html
# Use get-source.sh script to download locally.
Source0:	http://download.oracle.com/otn-pub/java/jdk/%{version}+%{bld_ver}/%{bhash}/jdk-%{version}_linux-x64_bin.tar.gz
# NoSource0-md5:	9609ee7a66a7985ce755ced51bc6308f
NoSource:	0
Source1:	Test.java
URL:		http://www.oracle.com/technetwork/java/javase/overview/index.html
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-build >= 4.3-0.20040107.21
BuildRequires:	rpmbuild(macros) >= 1.453
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	%{name}-jdk-base = %{version}-%{release}
Requires:	%{name}-jre = %{version}-%{release}
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	j2sdk = %{version}
Provides:	jdk = %{version}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	java-blackdown
Obsoletes:	jdk
Obsoletes:	kaffe
Conflicts:	netscape4-plugin-java
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		javareldir	java11-%{version}
%define		javadir		%{_jvmdir}/%{javareldir}
%define		jvmjardir	%{_jvmjardir}/java11-%{version}

# rpm doesn't like strange version definitions provided by Sun's libs
%define		_noautoprov	'\\.\\./.*' '/export/.*'
# these with SUNWprivate.* are found as required, but not provided
%define		_noautoreq	'libjava.so(SUNWprivate_1.1)' 'libnet.so(SUNWprivate_1.1)' 'libverify.so(SUNWprivate_1.1)' 'libjava_crw_demo_g\.so.*' 'libmawt.so' 'java(ClassDataVersion)'
# don't depend on other JRE/JDK installed on build host
%define		_noautoreqdep	libjava.so libjvm.so

# binary packages already stripped
%define		_enable_debug_packages 0

# disable stripping which breaks ie jmap -heap <pid>
# Caused by: java.lang.RuntimeException: unknown CollectedHeap type : class sun.jvm.hotspot.gc_interface.CollectedHeap
%define		no_install_post_strip	1

%description
This package symlinks Oracle Java development tools provided by
java11-jdk-base to system-wide directories like /usr/bin, making Oracle
Java the default JDK.

%description -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi programistycznych
uruchomieniowego Javy firmy Oracle, dostarczanych przez pakiet
java11-jdk-base, w standardowych systemowych ścieżkach takich jak
/usr/bin, sprawiając tym samym, że Oracle Java staje się domyślnym JDK
w systemie.

%package jdk-base
Summary:	Oracle JDK (Java Development Kit) for Linux
Summary(pl.UTF-8):	Oracle JDK - środowisko programistyczne Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	jpackage-utils >= 0:1.7.5-8
Provides:	jdk(%{name})

%description jdk-base
Java Development Kit for Linux.

%description jdk-base -l pl.UTF-8
Środowisko programistyczne Javy dla Linuksa.

%package jre
Summary:	Oracle JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	Oracle JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}
Requires:	jpackage-utils >= 0:1.7.5-8
Provides:	java
Provides:	java1.4
Provides:	jre = %{version}
Obsoletes:	java-blackdown-jre
Obsoletes:	jre

%description jre
This package symlinks Oracle Java runtime environment tools provided
by java11-jre-base to system-wide directories like /usr/bin, making
Oracle Java the default JRE.

%description jre -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi środowiska
uruchomieniowego Javy firmy Oracle, dostarczanych przez pakiet
java11-jre-base, w standardowych systemowych ścieżkach takich jak
/usr/bin, sprawiając tym samym, że Oracle Java staje się domyślnym JRE
w systemie.

%package jre-base
Summary:	Oracle JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	Oracle JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	jpackage-utils >= 0:1.7.5-8
Provides:	java(ClassDataVersion) = %{_classdataversion}
Provides:	java(jaas) = %{version}
Provides:	java(jaf) = 1.1.1
Provides:	java(jaxp) = 1.3
Provides:	java(jaxp_parser_impl)
Provides:	java(jce) = %{version}
Provides:	java(jdbc-stdext) = %{version}
Provides:	java(jdbc-stdext) = 3.0
Provides:	java(jmx) = 1.4
Provides:	java(jndi) = %{version}
Provides:	java(jsse) = %{version}
Provides:	jre(%{name})

%description jre-base
Java Runtime Environment for Linux. Does not contain any X11-related
compontents.

%description jre-base -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa. Nie zawiera żadnych
elementów związanych ze środowiskiem X11.

%package jre-base-X11
Summary:	Oracle JRE (Java Runtime Environment) for Linux, X11 related parts
Summary(pl.UTF-8):	Oracle JRE - środowisko uruchomieniowe Javy dla Linuksa, części korzystające z X11
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}

%description jre-base-X11
X11-related part of Java Runtime Environment for Linux.

%description jre-base-X11 -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa, część związana ze
środowiskiem graficznym X11.

%package jre-alsa
Summary:	JRE module for ALSA sound support
Summary(pl.UTF-8):	Moduł JRE do obsługi dźwięku poprzez ALSA
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	%{name}-alsa

%description jre-alsa
JRE module for ALSA sound support.

%description jre-alsa -l pl.UTF-8
Moduł JRE do obsługi dźwięku poprzez ALSA.

%package tools
Summary:	Shared Java tools
Summary(pl.UTF-8):	Współdzielone narzędzia Javy
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	jar
Provides:	java-jre-tools
Obsoletes:	fastjar
Obsoletes:	jar
Obsoletes:	java-jre-tools

%description tools
This package contains tools that are common for every Java(TM)
implementation, such as rmic or jar.

%description tools -l pl.UTF-8
Pakiet ten zawiera narzędzia wspólne dla każdej implementacji
Javy(TM), takie jak rmic czy jar.

%package demos
Summary:	JDK demonstration programs
Summary(pl.UTF-8):	Programy demonstracyjne do JDK
Group:		Development/Languages/Java
Requires:	jre

%description demos
JDK demonstration programs.

%description demos -l pl.UTF-8
Programy demonstracyjne do JDK.

%package sources
Summary:	JRE standard library sources
Summary(pl.UTF-8):	Źródła standardowej biblioteki JRE
Group:		Development/Languages/Java

%description sources
Sources for the standard Java library.

%description sources -l pl.UTF-8
Źródła standardowej bilioteki Java.

%prep
%setup -q -n jdk-%{version}

cp -p %{SOURCE1} Test.java

%build
%if %{with tests}
# Make sure we have /proc mounted,
# javac Test.java fails to get lock otherwise and runs forever:
# Java HotSpot(TM) Client VM warning: Can't detect initial thread stack location - find_vma failed
if [ ! -f /proc/cpuinfo ]; then
	echo >&2 "WARNING: /proc not mounted -- compile test may fail"
fi

# CLASSPATH prevents finding Test.class in .
unset CLASSPATH || :
# $ORIGIN does not work on PLD builders. workaround with LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$(pwd)/lib/jli
./bin/javac Test.java
./bin/java Test

classver=$(cat classver)
if [ "$classver" != %{_classdataversion} ]; then
	echo "Set %%define _classdataversion to $classver and rerun."
	exit 1
fi
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{javadir},%{jvmjardir},%{_javadir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_prefix}/src/%{name}-sources \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_browserpluginsdir}}

cp -a bin conf include lib $RPM_BUILD_ROOT%{javadir}

for i in java jjs keytool \
	rmid rmiregistry pack200 unpack200; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in jaotc jar jarsigner \
	javac javadoc javap jcmd jconsole jdb jdeprscan jdeps jhsdb jimage jinfo jlink \
        jmap jmod jps jrunscript jshell jstack jstat jstatd rmic serialver; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

mv -f $RPM_BUILD_ROOT%{javadir}/lib/src.zip $RPM_BUILD_ROOT%{_prefix}/src/%{name}-sources

ln -s %{javareldir} $RPM_BUILD_ROOT%{_jvmdir}/java
ln -s %{javareldir} $RPM_BUILD_ROOT%{_jvmdir}/java11
ln -s java11-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/java
ln -s java11-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/jre

# modify RPATH so that javac and friends are able to work when /proc is not
# mounted and we can't append to RPATH (for example to keep previous lookup
# path) as RPATH can't be longer than original
#
# for example:
# old javac: RPATH=$ORIGIN/../lib/i386/jli:$ORIGIN/../jre/lib/i386/jli
# new javac: RPATH=%{_prefix}/lib/jvm/java11-1.6.0/jre/lib/i386/jli

# silly rpath: jre/bin/unpack200: RPATH=$ORIGIN
chrpath -d $RPM_BUILD_ROOT%{javadir}/bin/unpack200

fixrpath() {
	execlist=$(find $RPM_BUILD_ROOT%{javadir} -type f -executable | xargs file | awk -F: '/ELF.*executable/{print $1}')
	for f in $execlist; do
		rpath=$(chrpath -l $f | awk '/(R|RUN)PATH=/ { gsub(/.*RPATH=/,""); gsub(/.*RUNPATH=/,""); gsub(/:/," "); print $0 }')
		[ "$rpath" ] || continue

		# file
		file=${f#$RPM_BUILD_ROOT}
		origin=${file%/*}

		new=
		for a in $rpath; do
			t=$(echo $a | sed -e "s,\$ORIGIN,$origin,g")
			# get rid of ../../
			t=$(set -e; t=$RPM_BUILD_ROOT$t; [ -d $t ] || exit 0; cd $t; pwd)
			# skip inexistent paths
			[ "$t" ] || continue

			t=${t#$RPM_BUILD_ROOT}

			if [[ "$new" != *$t* ]]; then
				# append it now
				new=${new}${new:+:}$t
			fi
		done
		# leave old one if new is too long
		if [ ${#new} -gt ${#rpath} ]; then
			echo "WARNING: New ($new) rpath is too long. Leaving old ($rpath) one." >&2
		else
			chrpath -r ${new} $f
		fi
	done
}

fixrpath

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.html legal
%{_jvmdir}/java
%{_jvmjardir}/java
%attr(755,root,root) %{_bindir}/jaotc
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jcmd
%attr(755,root,root) %{_bindir}/jconsole
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/jdeprscan
%attr(755,root,root) %{_bindir}/jdeps
%attr(755,root,root) %{_bindir}/jhsdb
%attr(755,root,root) %{_bindir}/jimage
%attr(755,root,root) %{_bindir}/jinfo
%attr(755,root,root) %{_bindir}/jjs
%attr(755,root,root) %{_bindir}/jlink
%attr(755,root,root) %{_bindir}/jmap
%attr(755,root,root) %{_bindir}/jmod
%attr(755,root,root) %{_bindir}/jps
%attr(755,root,root) %{_bindir}/jrunscript
%attr(755,root,root) %{_bindir}/jshell
%attr(755,root,root) %{_bindir}/jstack
%attr(755,root,root) %{_bindir}/jstat
%attr(755,root,root) %{_bindir}/jstatd
%attr(755,root,root) %{_bindir}/pack200
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{_bindir}/unpack200

%files jdk-base
%defattr(644,root,root,755)
%{_jvmdir}/java11
%attr(755,root,root) %{javadir}/bin/jaotc
%attr(755,root,root) %{javadir}/bin/jarsigner
%attr(755,root,root) %{javadir}/bin/javac
%attr(755,root,root) %{javadir}/bin/javadoc
%attr(755,root,root) %{javadir}/bin/javap
%attr(755,root,root) %{javadir}/bin/jcmd
%attr(755,root,root) %{javadir}/bin/jconsole
%attr(755,root,root) %{javadir}/bin/jdb
%attr(755,root,root) %{javadir}/bin/jdeprscan
%attr(755,root,root) %{javadir}/bin/jdeps
%attr(755,root,root) %{javadir}/bin/jhsdb
%attr(755,root,root) %{javadir}/bin/jimage
%attr(755,root,root) %{javadir}/bin/jinfo
%attr(755,root,root) %{javadir}/bin/jjs
%attr(755,root,root) %{javadir}/bin/jlink
%attr(755,root,root) %{javadir}/bin/jmap
%attr(755,root,root) %{javadir}/bin/jmod
%attr(755,root,root) %{javadir}/bin/jps
%attr(755,root,root) %{javadir}/bin/jrunscript
%attr(755,root,root) %{javadir}/bin/jshell
%attr(755,root,root) %{javadir}/bin/jstack
%attr(755,root,root) %{javadir}/bin/jstat
%attr(755,root,root) %{javadir}/bin/jstatd
%attr(755,root,root) %{javadir}/bin/pack200
%attr(755,root,root) %{javadir}/bin/rmic
%attr(755,root,root) %{javadir}/bin/serialver
%attr(755,root,root) %{javadir}/bin/unpack200
%{javadir}/include
%{javadir}/lib/ct.sym
%{javadir}/lib/*.jar

%files jre
%defattr(644,root,root,755)
%doc lib/server/Xusage*
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/rmid

%files jre-base
%defattr(644,root,root,755)
%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/java
%attr(755,root,root) %{javadir}/bin/jar
%attr(755,root,root) %{javadir}/bin/keytool
%attr(755,root,root) %{javadir}/bin/rmid
%attr(755,root,root) %{javadir}/bin/rmiregistry
%dir %{javadir}/conf
%{javadir}/conf/*.properties
%{javadir}/conf/management
%dir %{javadir}/conf/security
%{javadir}/conf/security/policy
%{javadir}/conf/security/java.policy
%{javadir}/conf/security/java.security
%dir %{javadir}/lib

%{javadir}/lib/jvm.cfg
%{javadir}/lib/modules
%dir %{javadir}/lib/server
%attr(755,root,root) %{javadir}/lib/server/*
%dir %{javadir}/lib/jli
%attr(755,root,root) %{javadir}/lib/jli/libjli.so

%attr(755,root,root) %{javadir}/lib/lib*.so
%exclude %{javadir}/lib/libjsound.so
%exclude %{javadir}/lib/libsplashscreen.so
%exclude %{javadir}/lib/libjawt.so

%attr(755,root,root) %{javadir}/lib/jexec
%dir %{javadir}/lib/security
%{javadir}/lib/security/*.*
%verify(not md5 mtime size) %config(noreplace) %{javadir}/lib/security/cacerts
%{javadir}/lib/*.properties
%{javadir}/lib/tzdb.dat
%lang(ja) %{javadir}/lib/*.properties.ja
%dir %{jvmjardir}
%{javadir}/lib/classlist

%files jre-base-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{javadir}/lib/libsplashscreen.so
%attr(755,root,root) %{javadir}/lib/libjawt.so

%files jre-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{javadir}/lib/libjsound.so

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/rmiregistry

%files sources
%defattr(644,root,root,755)
%dir %{_prefix}/src/%{name}-sources
%{_prefix}/src/%{name}-sources/src.zip
