Summary:	log4j - logging for Java
Summary(pl):	log4j - zapis log�w dla Javy
Name:		jakarta-log4j
Version:	1.2.9
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/logging/log4j/logging-log4j-%{version}.tar.gz
# Source0-md5:	8c2074c42bf2fb1da72e920689c59ad8
URL:		http://logging.apache.org/log4j/
BuildRequires:	ant
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
%setup -q -n logging-log4j-%{version}

%build
JAVA_HOME="%{_libdir}/java"
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
