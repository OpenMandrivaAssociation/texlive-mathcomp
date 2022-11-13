Name:		texlive-mathcomp
Version:	15878
Release:	1
Summary:	Text symbols in maths mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathcomp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcomp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcomp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcomp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package which provides access to some interesting characters
of the Text Companion fonts (TS1 encoding) in maths mode.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mathcomp/mathcomp.sty
%doc %{_texmfdistdir}/doc/latex/mathcomp/mathcomp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mathcomp/mathcomp.dtx
%doc %{_texmfdistdir}/source/latex/mathcomp/mathcomp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
