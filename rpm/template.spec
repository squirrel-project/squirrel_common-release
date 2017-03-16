Name:           ros-indigo-squirrel-navigation-msgs
Version:        0.0.25
Release:        0%{?dist}
Summary:        ROS squirrel_navigation_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
Messages for squirrel_navigation package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Mar 16 2017 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.25-0
- Autogenerated by Bloom

* Mon Feb 20 2017 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.24-0
- Autogenerated by Bloom

* Mon Feb 13 2017 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.23-0
- Autogenerated by Bloom

* Mon Jul 11 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.19-1
- Autogenerated by Bloom

* Mon Jul 11 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.19-0
- Autogenerated by Bloom

* Tue May 10 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.18-0
- Autogenerated by Bloom

* Thu Apr 14 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.17-0
- Autogenerated by Bloom

* Mon Apr 11 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.16-0
- Autogenerated by Bloom

* Sun Apr 10 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.15-0
- Autogenerated by Bloom

* Wed Apr 06 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.14-0
- Autogenerated by Bloom

* Wed Mar 02 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.13-0
- Autogenerated by Bloom

* Wed Feb 24 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.12-0
- Autogenerated by Bloom

* Mon Feb 22 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.11-0
- Autogenerated by Bloom

* Mon Feb 22 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.10-1
- Autogenerated by Bloom

* Mon Feb 22 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.10-0
- Autogenerated by Bloom

* Wed Feb 17 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.9-0
- Autogenerated by Bloom

* Thu Feb 04 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.8-0
- Autogenerated by Bloom

* Tue Feb 02 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.7-0
- Autogenerated by Bloom

* Mon Feb 01 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.6-0
- Autogenerated by Bloom

* Wed Jan 20 2016 Federico Boniardi <boniardi@informatik.uni-freiburg.de> - 0.0.5-0
- Autogenerated by Bloom

