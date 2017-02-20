^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package squirrel_object_perception_msgs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.23 (2017-02-13)
-------------------
* added message for 2d recognizer
* Contributors: Edith Langer

0.0.22 (2016-09-28)
-------------------

0.0.21 (2016-09-15)
-------------------

0.0.20 (2016-09-07)
-------------------

0.0.19 (2016-07-11)
-------------------
* Move service definitions to correct module
  These services handle movement of the pan and tilt unit, which does not really fit into squirrel_object_perception.
* Changed names of variables in service after testing in Vienna.
* Contributors: Markus Bajones, Tim Patten Desktop

0.0.18 (2016-05-10)
-------------------

0.0.17 (2016-04-14)
-------------------
* Merge pull request `#113 <https://github.com/squirrel-project/squirrel_common/issues/113>`_ from bajo/indigo_dev
  Add service for pan/tilt in angles instead of pixel coordinate
* actually enable the service to be build
* Add service for pan/tilt in angles instead of pixel coordinate
* Contributors: Markus Bajones, Nadia Hammoudeh García

0.0.16 (2016-04-11)
-------------------
* added id to lump tracker service
* added to arrays as result (added/updated objects)
* Contributors: Edith Langer

0.0.15 (2016-04-10)
-------------------
* Merge pull request `#106 <https://github.com/squirrel-project/squirrel_common/issues/106>`_ from tpatten/indigo_dev
  Active exploration as ros service
* Merge remote-tracking branch 'upstream/indigo_dev' into indigo_dev
* Added new field to specify if occlusions are considered or not in planning.
* added another fixate service
* Added variance as a field in the ros service request
* Modified service to include robot details.
* Added new service for active exploration.
* manual merge resolution
* whatever...untracked files appeared
* 0.0.4
* update
* 0.0.3
* updated version
* add CHANGELOG.rst
* Contributors: Nadia Hammoudeh García, Philipp Zech, Tim Patten Desktop, buildbot-squirrel, mzillich

0.0.14 (2016-04-06)
-------------------
* Add new action for haf_grasping integration
* added comments for clarification
* Contributors: Markus Bajones, mzillich

0.0.13 (2016-03-02)
-------------------
* Revert "Revert "added more tracking services""
* Revert "added more tracking services"
* added more tracking services
* updated FindDynamicObjects service: using SceneObject now and returns three lists
* Contributors: Edith Langer, Nadia Hammoudeh García, mzillich

0.0.12 (2016-02-24)
-------------------

0.0.11 (2016-02-22)
-------------------

0.0.10 (2016-02-22)
-------------------

0.0.9 (2016-02-17)
------------------

0.0.8 (2016-02-04)
------------------
* forgot the CMakelists file
* added scene object
* Contributors: mzillich

0.0.7 (2016-02-02)
------------------
* fixed recognition
* Contributors: mzillich

0.0.6 (2016-02-01)
------------------

0.0.4 (2016-01-13)
------------------
* small change in CMakeLists
* added srv and msgs for finding dynamic objects
* include folder not found
* Contributors: ipa-nhg

0.0.3 (2016-01-13)
------------------

0.0.2 (2016-01-13)
------------------
* cleanup of CMakeLists.txt and package.xml. Make sure dependencies are in there as well.
* Contributors: Markus Bajones

0.0.1 (2015-12-16)
------------------
* Moved message and service definitions from squirrel_perception/squirrel_active_exploration to squirrel_common/squirrel_object_perception_msgs. Modified CMakeLists and package.xml to correctly generate the header files.
* Add response in *ObjectTracking.srv
* added attention services
* fixed comments
* Added extra field (pose) to Classification.msg in object_perception_msgs. Needed for active_exploration module.
* demo review 2015
* added object tracking
* now uses pose stammped .. again!
* added service to create objects from segmented clusters
  removed obsolete ObjectRecognizer service (now Recognize
* add services for object DB handling
* Update LookForObject action for planning
* Update LookForObject action
* Add missing srv for object recognizer
* Added missing build dependecy
* srv file changes to return array of array
* added explanations to services
* changed service messages
* added new service message for visualization
* added new service messages
* added new service
* Merge branch 'hydro_dev' of https://github.com/epotapova/common into hydro_dev
  Conflicts:
  squirrel_object_perception_msgs/CMakeLists.txt
  squirrel_object_perception_msgs/package.xml
* added new dependencies
* Fixed naming of services. Added missing dependcies
* Merge pull request `#5 <https://github.com/squirrel-project/squirrel_common/issues/5>`_ from epotapova/hydro_dev
  renamed service
* added new srv
* remove unused srv
* changed compilation
* Merge branch 'hydro_dev' of github.com:mzillich/common into hydro_dev
  Conflicts:
  squirrel_object_perception_msgs/CMakeLists.txt
* added missing action lib dependeny
* added get_saliency.srv compilation
* fix typo in message name
* fix merge conflicts
* first consistent version of interfaces
* first set of messages, services
* Add recognition srv definitions.
* Update CMakeLists.txt
  Use new Action name during catkin_make
* Update and rename Look.action to LookForObject.action
  Old name was too generic.
* enforce squirrel naming convention.
* Contributors: Markus Bajones, Michael Zillich, Tim Patten Desktop, epotapova, ipa-jsf, ipa-robotino, mzillich
