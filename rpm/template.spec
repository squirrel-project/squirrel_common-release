Name:           ros-indigo-squirrel-common
Version:        0.0.1
Release:        2%{?dist}
Summary:        ROS squirrel_common package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-squirrel-manipulation-msgs
Requires:       ros-indigo-squirrel-mhand-msgs
Requires:       ros-indigo-squirrel-object-perception-msgs
Requires:       ros-indigo-squirrel-person-tracker-msgs
Requires:       ros-indigo-squirrel-planning-knowledge-msgs
Requires:       ros-indigo-squirrel-prediction-msgs
Requires:       ros-indigo-squirrel-rgbd-mapping-msgs
BuildRequires:  ros-indigo-catkin

%description
Definitions for mesages, services and actions. Startup packages for the robots

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
* Tue Jan 12 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-2
- Autogenerated by Bloom

* Thu Dec 17 2015 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-1
- Autogenerated by Bloom

* Wed Dec 16 2015 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-0
- Autogenerated by Bloom

