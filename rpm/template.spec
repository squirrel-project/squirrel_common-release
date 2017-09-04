Name:           ros-indigo-robotino-description
Version:        0.0.28
Release:        0%{?dist}
Summary:        ROS robotino_description package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gazebo-plugins
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-gazebo-plugins
BuildRequires:  ros-indigo-xacro

%description
The robotino_description package

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
* Mon Sep 04 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.0.28-0
- Autogenerated by Bloom

* Wed Jun 28 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.0.27-0
- Autogenerated by Bloom

* Tue Jun 27 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.0.26-0
- Autogenerated by Bloom

* Thu Mar 16 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.0.25-0
- Autogenerated by Bloom

* Mon Feb 20 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.0.24-0
- Autogenerated by Bloom

* Mon Feb 13 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.0.23-0
- Autogenerated by Bloom

