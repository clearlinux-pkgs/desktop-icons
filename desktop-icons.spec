#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : desktop-icons
Version  : 18.11rc
Release  : 2
URL      : https://gitlab.gnome.org/World/ShellExtensions/desktop-icons/-/archive/18.11rc/desktop-icons-18.11rc.tar.gz
Source0  : https://gitlab.gnome.org/World/ShellExtensions/desktop-icons/-/archive/18.11rc/desktop-icons-18.11rc.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: desktop-icons-data = %{version}-%{release}
Requires: desktop-icons-license = %{version}-%{release}
Requires: desktop-icons-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
Patch1: 0001-Support-proper-packaging-via-system-wide-installatio.patch

%description
# Desktop Icons
## What  is it?
A GNOME Shell extension for providing desktop icons.

%package data
Summary: data components for the desktop-icons package.
Group: Data

%description data
data components for the desktop-icons package.


%package license
Summary: license components for the desktop-icons package.
Group: Default

%description license
license components for the desktop-icons package.


%package locales
Summary: locales components for the desktop-icons package.
Group: Default

%description locales
locales components for the desktop-icons package.


%prep
%setup -q -n desktop-icons-18.11rc
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543328843
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Dwith-system-wide=true  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/desktop-icons
cp LICENSE %{buildroot}/usr/share/package-licenses/desktop-icons/LICENSE
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang desktop-icons

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.desktop-icons.gschema.xml
/usr/share/gnome-shell/extensions/desktop-icons@csoriano/createThumbnail.js
/usr/share/gnome-shell/extensions/desktop-icons@csoriano/dbusUtils.js
/usr/share/gnome-shell/extensions/desktop-icons@csoriano/desktopGrid.js
/usr/share/gnome-shell/extensions/desktop-icons@csoriano/desktopIconsUtil.js
/usr/share/gnome-shell/extensions/desktop-icons@csoriano/desktopManager.js
/usr/share/gnome-shell/extensions/desktop-icons@csoriano/extension.js
/usr/share/gnome-shell/extensions/desktop-icons@csoriano/fileItem.js
/usr/share/gnome-shell/extensions/desktop-icons@csoriano/metadata.json
/usr/share/gnome-shell/extensions/desktop-icons@csoriano/prefs.js
/usr/share/gnome-shell/extensions/desktop-icons@csoriano/stylesheet.css

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/desktop-icons/LICENSE

%files locales -f desktop-icons.lang
%defattr(-,root,root,-)

