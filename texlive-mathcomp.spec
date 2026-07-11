%global tl_name mathcomp
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1f
Release:	%{tl_revision}.1
Summary:	Text symbols in maths mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathcomp
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcomp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcomp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcomp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package which provides access to some interesting characters of the
Text Companion fonts (TS1 encoding) in maths mode.

