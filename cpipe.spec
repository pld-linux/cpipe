Summary:	Counting pipe
Summary(pl.UTF-8):	Potok ze zliczaniem
Name:		cpipe
Version:	3.0.1
Release:	3
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

%description -l pl.UTF-8
Czy kiedykolwiek zastanawiałeś się jak szybki jest Twój tar, lub ile
danych już zapisał? A co myślisz o kopiowaniu plików przy użyciu
socketa lub nc, z kompresją lub bez, po szybkiej sieci - jak będzie
szybciej?

Jeśli chcesz znać odpowiedź, użyj cpipe jako całkowicie nienaukowego
podejścia do pomiaru przepustowości. Cpipe kopiuje standardowe wejście
na wyjście jednocześnie mierząc czas jaki zajmuje czytanie i
zapisywanie danych. Statystyki średniej przepustowości i całkowitej
ilości skopiowanych bajtów są wypisywane na standardowe wyjście
błędów.

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
%doc CHANGES 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
