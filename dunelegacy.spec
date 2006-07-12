Summary:	Updated clone of Westood Studios' Dune2
Summary(pl):	Zaktualizowany klon gry Dune2
Name:		dunelegacy
Version:	0.94
Release:	0.1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://dl.sourceforge.net/dunelegacy/%{name}-%{version}.tar.gz
# Source0-md5:	f53391b46a18696dcd60ce2e8c610a6f
URL:		http://dunelegacy.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkg-config
BuildRequires:	zziplib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lead one of three interplanetary houses, Atreides, Harkonnen or Ordos,
in an attempt to harvest the largest amount of spice from the sand
dunes. Exchange your spice stockpiles for credits through refinement
and build an army capable of thwarting attempts of the other houses to
stop your harvesting!

Dune Legacy is an effort by a handful of developers to revitalize the
first-ever real-time strategy game. The original game was the basis
for the hugely successful Command and Conquer series, and the gameplay
has been replicated an extended to a wide variety of storylines and
series.

NOTE: Original Dune 2 game files are needed.

%description -l pl
Poprowad¼ jedn± z trzech miêdzyplanetarnych rodzin, Atreidesów,
Harkonnenów lub Ordosów, w wy¶cigu w zebraniu jak najwiêkszej ilo¶ci
przyprawy z pustynnych wydm. Wymieñ zapasy przyprawy na kredyty w
procesie udoskonalania i stwórz armiê zdoln± powstrzymaæ próby innych
rodzin w zmuszeniu Ciê do zaprzestania zbierania przyprawy!

Dune Legacy jest podjet± przez grupê utalentowanych programistów prób±
o¿ywienia pierwszej strategii czasu rzeczywistego. Gra by³a wzorem dla
odnosz±cej olbrzymie sukcesy serii Command and Conquer, a styl gry
zosta³ powielony w du¿ej ilo¶ci innych gier.

UWAGA: Potrzebne sa pliki wchodz±ce w sk³ad Dune 2.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
