Name:           ros-indigo-squirrel-manipulation-msgs
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS squirrel_manipulation_msgs package

Group:          Development/Libraries
License:        TODO
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
Package defining actions for manipulation

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
* Wed Jan 13 2016 michael <simon.hangl@uibk.ac.at> - 0.0.2-0
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <simon.hangl@uibk.ac.at> - 0.0.1-7
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <simon.hangl@uibk.ac.at> - 0.0.1-6
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <simon.hangl@uibk.ac.at> - 0.0.1-5
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <simon.hangl@uibk.ac.at> - 0.0.1-4
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <simon.hangl@uibk.ac.at> - 0.0.1-3
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <simon.hangl@uibk.ac.at> - 0.0.1-2
- Autogenerated by Bloom

* Thu Dec 17 2015 michael <simon.hangl@uibk.ac.at> - 0.0.1-1
- Autogenerated by Bloom

* Wed Dec 16 2015 michael <simon.hangl@uibk.ac.at> - 0.0.1-0
- Autogenerated by Bloom

