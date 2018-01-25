Name:           ros-indigo-squirrel-safety-msgs
Version:        0.0.30
Release:        0%{?dist}
Summary:        ROS squirrel_safety_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
The squirrel_safety_msgs package

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
* Thu Jan 25 2018 Philipp Zech <philipp.zech@uibk.ac.at> - 0.0.30-0
- Autogenerated by Bloom

* Thu Jan 25 2018 Philipp Zech <philipp.zech@uibk.ac.at> - 0.0.29-1
- Autogenerated by Bloom

* Tue Sep 05 2017 Philipp Zech <philipp.zech@uibk.ac.at> - 0.0.29-0
- Autogenerated by Bloom

* Mon Sep 04 2017 Philipp Zech <philipp.zech@uibk.ac.at> - 0.0.28-0
- Autogenerated by Bloom

* Wed Jun 28 2017 Philipp Zech <philipp.zech@uibk.ac.at> - 0.0.27-0
- Autogenerated by Bloom

* Tue Jun 27 2017 Philipp Zech <philipp.zech@uibk.ac.at> - 0.0.26-0
- Autogenerated by Bloom

