Name:           ros-indigo-squirrel-prediction-msgs
Version:        0.0.1
Release:        4%{?dist}
Summary:        ROS squirrel_prediction_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://www.squirrel-project.eu
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
Services for predicting and recommending missing data

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
* Tue Jan 12 2016 michael <senka.krivic@uibk.ac.at> - 0.0.1-4
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <senka.krivic@uibk.ac.at> - 0.0.1-3
- Autogenerated by Bloom

* Tue Jan 12 2016 michael <senka.krivic@uibk.ac.at> - 0.0.1-2
- Autogenerated by Bloom

* Thu Dec 17 2015 michael <senka.krivic@uibk.ac.at> - 0.0.1-1
- Autogenerated by Bloom

* Wed Dec 16 2015 michael <senka.krivic@uibk.ac.at> - 0.0.1-0
- Autogenerated by Bloom

