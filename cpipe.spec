Summary:	Counting pipe
Summary(pl):	Potok ze zliczaniem
Name:		cpipe
Version:	3.0.1
Release:	2
License:	GPL
Group:		Applications/Archiving
Source0:	http://download.berlios.de/cpipe/%{name}-%{version}.tar.gz
# Source0-md5:	1eaa5b28ef7ef96f1c54d5607ec828b3
Patch0:		%{name}-make_fix.patch
URL:		http://developer.berlios.de/projects/cpipe/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Did you ever want to know how fast your tar is or how much data it has
transferred already. How about using socket or nc to copy files either
with or without compression over a fast network connection, which one
is faster?

If you want to know the answer, use cpipe as a totally unscientific
approach to measure throughput. Cpipe copies its standard input to its
standard output while measuring the time it takes to read an input
buffer and write an output buffer. Statistics of average throughput
and the total amount of bytes copied are printed to the standard error
output.

%description -l pl
Czy kiedykolwiek zastanawia³e¶ siê jak szybki jest Twój tar, lub ile
danych ju¿ zapisa³? A co my¶lisz o kopiowaniu plików przy u¿yciu
socketa lub nc, z kompresj± lub bez, po szybkiej sieci - jak bêdzie
szybciej?

Je¶li chcesz znaæ odpowied¼, u¿yj cpipe jako ca³kowicie nienaukowego
podej¶cia do pomiaru przepustowo¶ci. Cpipe kopiuje standardowe wej¶cie
na wyj¶cie jednocze¶nie mierz±c czas jaki zajmuje czytanie i
zapisywanie danych. Statystyki ¶redniej przepustowo¶ci i ca³kowitej
ilo¶ci skopiowanych bajtów s± wypisywane na standardowe wyj¶cie
b³êdów.

%prep
%setup -q
%patch0

%build
# workaround not to use clig
touch cmdline.c cmdline.h cpipe.1

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}

install cpipe $RPM_BUILD_ROOT%{_bindir}
install cpipe.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
