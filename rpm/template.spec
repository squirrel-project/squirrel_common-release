Name:           ros-indigo-squirrel-common
Version:        0.0.27
Release:        0%{?dist}
Summary:        ROS squirrel_common package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-robotino-description
Requires:       ros-indigo-robotino-msgs
Requires:       ros-indigo-softhand-description
Requires:       ros-indigo-squirrel-3d-localizer-msgs
Requires:       ros-indigo-squirrel-3d-mapping-msgs
Requires:       ros-indigo-squirrel-dynamic-filter-msgs
Requires:       ros-indigo-squirrel-footprint-observer-msgs
Requires:       ros-indigo-squirrel-hri-msgs
Requires:       ros-indigo-squirrel-kclhand-msgs
Requires:       ros-indigo-squirrel-localizer-msgs
Requires:       ros-indigo-squirrel-manipulation-msgs
Requires:       ros-indigo-squirrel-mhand-msgs
Requires:       ros-indigo-squirrel-navigation-msgs
Requires:       ros-indigo-squirrel-object-perception-msgs
Requires:       ros-indigo-squirrel-person-tracker-msgs
Requires:       ros-indigo-squirrel-planning-knowledge-msgs
Requires:       ros-indigo-squirrel-prediction-msgs
Requires:       ros-indigo-squirrel-rgbd-mapping-msgs
Requires:       ros-indigo-squirrel-sketch-interface-msgs
Requires:       ros-indigo-squirrel-speech-msgs
Requires:       ros-indigo-squirrel-vad-msgs
Requires:       ros-indigo-squirrel-view-controller-msgs
Requires:       ros-indigo-squirrel-waypoint-msgs
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
* Wed Jun 28 2017 Nadia Hammoudeh Garcia <nadia.hammoudeh.garcia@ipa.fraunhofer.de> - 0.0.27-0
- Autogenerated by Bloom

* Tue Jun 27 2017 Nadia Hammoudeh Garcia <nadia.hammoudeh.garcia@ipa.fraunhofer.de> - 0.0.26-0
- Autogenerated by Bloom

* Thu Mar 16 2017 Nadia Hammoudeh Garcia <nadia.hammoudeh.garcia@ipa.fraunhofer.de> - 0.0.25-0
- Autogenerated by Bloom

* Mon Feb 20 2017 Nadia Hammoudeh Garcia <nadia.hammoudeh.garcia@ipa.fraunhofer.de> - 0.0.24-0
- Autogenerated by Bloom

* Mon Feb 13 2017 Nadia Hammoudeh Garcia <nadia.hammoudeh.garcia@ipa.fraunhofer.de> - 0.0.23-0
- Autogenerated by Bloom

* Mon Jul 11 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.19-1
- Autogenerated by Bloom

* Mon Jul 11 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.19-0
- Autogenerated by Bloom

* Tue May 10 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.18-0
- Autogenerated by Bloom

* Thu Apr 14 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.17-0
- Autogenerated by Bloom

* Mon Apr 11 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.16-0
- Autogenerated by Bloom

* Sun Apr 10 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.15-0
- Autogenerated by Bloom

* Wed Apr 06 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.14-0
- Autogenerated by Bloom

* Wed Mar 02 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.13-0
- Autogenerated by Bloom

* Wed Feb 24 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.12-0
- Autogenerated by Bloom

* Mon Feb 22 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.11-0
- Autogenerated by Bloom

* Mon Feb 22 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.10-1
- Autogenerated by Bloom

* Mon Feb 22 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.10-0
- Autogenerated by Bloom

* Wed Feb 17 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.9-0
- Autogenerated by Bloom

* Thu Feb 04 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.8-0
- Autogenerated by Bloom

* Tue Feb 02 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.7-0
- Autogenerated by Bloom

* Mon Feb 01 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.6-0
- Autogenerated by Bloom

* Wed Jan 20 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.5-0
- Autogenerated by Bloom

* Wed Jan 13 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.4-0
- Autogenerated by Bloom

* Wed Jan 13 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.3-1
- Autogenerated by Bloom

* Wed Jan 13 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.3-0
- Autogenerated by Bloom

* Wed Jan 13 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.2-0
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-7
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-6
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-5
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-4
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-3
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-2
- Autogenerated by Bloom

* Thu Dec 17 2015 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-1
- Autogenerated by Bloom

* Wed Dec 16 2015 michael <michael.cashmore@kcl.ac.uk> - 0.0.1-0
- Autogenerated by Bloom

