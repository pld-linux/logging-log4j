Summary:	log4j - logging for Java
Summary(pl):	log4j - zapis log�w dla Javy
Name:		jakarta-log4j
Version:	1.2.8
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/log4j/%{name}-%{version}.tar.gz
# Source0-md5:	dfc8cd57a4f2b42177b14f147c9dab3d
Patch0:		%{name}-unreachable.patch
Patch1:		%{name}-build.patch
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant
BuildRequires:	javamail >= 1.2
BuildRequires:	jdk >= 1.2
BuildRequires:	jms
BuildRequires:	junit >= 3.8
BuildRequires:	jmx
Requires:	javamail >= 1.2
Requires:	jdk >= 1.2
Requires:	jms
Requires:	junit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With log4j it is possible to enable logging at runtime without
modifying the application binary.

%description -l pl
Przy u�yciu log4j mo�na w��czy� zapis do log�w przy uruchamianiu bez
modyfikowania binarnej aplikacji.

%package doc
Summary:	Online manual for log4j
Summary(pl):	Dokumentacja online do log4j
Group:		Development/Languages/Java

%description doc
Online manual for log4j.

%description doc -l pl
Dokumentacja online do log4j.

%prep
%setup -q
#%patch -p1
%patch1

%build
JAVA_HOME="/usr/lib/java"
CLASSPATH="$CLASSPATH:$JAVA_HOME/jre/lib/rt.jar"
CLASSPATH="$CLASSPATH:%{_javadir}/mail.jar"
CLASSPATH="$CLASSPATH:%{_javadir}/jms.jar"
CLASSPATH="$CLASSPATH:%{_javadir}/activation.jar"
CLASSPATH="$CLASSPATH:%{_javadir}/junit.jar"
CLASSPATH="$CLASSPATH:%{_javadir}/jmxri.jar"
CLASSPATH="$CLASSPATH:%{_javadir}/jmxtools.jar"
export JAVA_HOME CLASSPATH

ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install dist/lib/log4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf log4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/log4j.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*
