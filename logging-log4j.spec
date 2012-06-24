# TODO:
# - do something with jms / jmx requirements;
#   http://lists.pld-linux.org/mailman/pipermail/pld-devel-en/2006-May/017648.html
# - jndi (whatever it is) is required for jmx interface
#
# NOTE:
# - javamail is provided by java-gnu-mail
# - jmx by java-sun-jre
#
Summary:	log4j - logging for Java
Summary(pl):	log4j - zapis log�w dla Javy
Name:		logging-log4j
Version:	1.2.14
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/logging/log4j/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7d8d02888b93e6f8d67b8e5f746196ae
URL:		http://logging.apache.org/log4j/
BuildRequires:	ant
BuildRequires:	javamail >= 1.2
BuildRequires:	java-activation
BuildRequires:	jdk >= 1.2
#BuildRequires:	jms
#BuildRequires:	jmx
BuildRequires:	junit >= 3.8
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	javamail >= 1.2
Requires:	jdk >= 1.2
#Requires:	jms
Requires:	junit
Provides:	log4j = %{version}
Obsoletes:	jakarta-log4j
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
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
Obsoletes:	jakarta-log4j-doc

%description doc
Online manual for log4j.

%description doc -l pl
Dokumentacja online do log4j.

%package javadoc
Summary:	API documentation for log4j
Summary(pl):	Dokumentacja API log4j
Group:		Development/Languages/Java
Obsoletes:	jakarta-log4j-doc

%description javadoc
API documentation for log4j.

%description javadoc -l pl
Dokumentacja API log4j.

%prep
%setup -q -n logging-log4j-%{version}

%build
export JAVA_HOME="%{java_home}"
export CLASSPATH="`/usr/bin/build-classpath mailapi activation junit`"
ant jar javadoc
ln -s %{_javadocdir}/%{name}-%{version} api

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}
install dist/lib/log4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s log4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/log4j.jar
cp -R docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/{css,images,lf5,*.html,*.txt,TODO} api

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
