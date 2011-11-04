# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mathcomp
# catalog-date 2007-01-09 18:22:13 +0100
# catalog-license lppl
# catalog-version 0.1f
Name:		texlive-mathcomp
Version:	0.1f
Release:	1
Summary:	Text symbols in maths mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathcomp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcomp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcomp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcomp.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package which provides access to some interesting characters
of the Text Companion fonts (TS1 encoding) in maths mode.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mathcomp/mathcomp.sty
%doc %{_texmfdistdir}/doc/latex/mathcomp/mathcomp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mathcomp/mathcomp.dtx
%doc %{_texmfdistdir}/source/latex/mathcomp/mathcomp.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
