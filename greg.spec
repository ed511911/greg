Name: greg
Version: 1.0
Release: 1%{?dist}
Summary: Alias for grep
License: MIT

%description
This package provides an alias 'greg' for the 'grep' command.

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
echo -e '#!/bin/bash\nexec grep "$@"' > $RPM_BUILD_ROOT/usr/bin/greg
chmod +x $RPM_BUILD_ROOT/usr/bin/greg

%files
/usr/bin/greg

%post
alternatives --install /usr/bin/greg greg /usr/bin/greg 10
