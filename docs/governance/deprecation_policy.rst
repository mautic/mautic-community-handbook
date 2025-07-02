Deprecation policy
##################

Why is this policy needed?
**************************

In order for Mautic to continue to be relevant and use up to date technologies, we often need to retire parts of our code or features in the product.

This policy outlines what can be deprecated, the timelines and processes for deprecating, and how we do it both in the code and in communication with Mautic users.

What can be deprecated
**********************

* Methods
* Method parameters
* Constructor parameter additions excluding services
* Constructor parameter removals excluding services
* Return values
* Services
* Code paths & behavior
* Classes
* Plugins
* Unintended behavior
* Internal APIs
* Asset Libraries
* JavaScript
* Mautic core Settings
* Configuration schema
* Themes

What can’t be deprecated
************************

* Do not deprecate test classes. Any test that could be considered deprecated should be removed or modified to be relevant.
* Tests which exercise deprecated code can be annotated with ``@group`` legacy in order to avoid deprecation notices during testing, but a follow-up issue should be filed in order to fix such tests to not exercise deprecated code.

How to deprecate
****************

Notice period
=============

We aim to provide at least one minor release cycle where the deprecation is marked as such and the community has been alerted through communications, before removing it in the next major release.

This generally means that any expected deprecations in a major release should be marked as deprecated from the `x.2` release predating it - for example, being marked as deprecated in ``5.2`` to be removed in ``6.0``.  
  
The above is required by the semantic versioning specification which Mautic follows - read more: [https://semver.org/#how-should-i-handle-deprecating-functionality](https://semver.org/#how-should-i-handle-deprecating-functionality)

If the deprecation is likely to have a wide impact we aim to provide notice at least two minor release cycles in advance - for example being deprecated in the ``x.1`` release and removed in the next major release.

Procedure
=========

A deprecation consists of three parts:

#.  A ``@deprecated`` PHPdoc tag that indicates when the code was deprecated, when it will be removed, and what to use instead, and where appropriate, an ``@see`` link to the ``upgrade.md`` file for the relevant version in which it is being deprecated.  
      
    Here’s an example of how this would look in Mautic:  
      
    [https://github.com/mautic/mautic/pull/11050/files#diff-3f40ece77ee5c3e25a713b6e8a9b8cf04bbcea1eb7270bef3c30ad3290889cccR54](https://github.com/mautic/mautic/pull/11050/files#diff-3f40ece77ee5c3e25a713b6e8a9b8cf04bbcea1eb7270bef3c30ad3290889cccR54)

#.  A ``@trigger\_error(‘...’, E\_USER\_DEPRECATED)`` at runtime to notify developers that deprecated code is being used. The ``@`` suppression should be used in most cases so that we can customize the error handling and avoid flooding logs on production. In some cases, we will omit the ``@`` if it's important to notify developers of a behavior or BC break (e.g. for a critical issue)  
      
    Here’s an example of how this would look in Mautic:  
      
    [https://github.com/mautic/mautic/blob/8a57278758e2c3e1c1ca987aaf9ebd5f05b3c877/app/bundles/CampaignBundle/Executioner/Dispatcher/LegacyEventDispatcher.php#L201](https://github.com/mautic/mautic/blob/8a57278758e2c3e1c1ca987aaf9ebd5f05b3c877/app/bundles/CampaignBundle/Executioner/Dispatcher/LegacyEventDispatcher.php#L201)

#.  In the event of a user-facing deprecation (for example the removal of a feature or function in the front-end) a notice will be displayed when that feature or function is being used, explaining the deprecation and pointing to the user-friendly explanation section of the change record  
      
    Here’s an example of how this would look in Mautic:  
      
    [https://github.com/mautic/mautic/pull/10907](https://github.com/mautic/mautic/pull/10907)

Resources
*********

``@deprecated`` PHPdoc tag format
=================================

.. code-block:: text

   _@deprecated in %deprecation-version% and is removed from %removal-version%. %extra-info%._

   _@see %cr-link%_

``@trigger\_error()`` format
============================

When the ``trigger\_error()`` call is associated with a matching ``@deprecated`` doc tag, the format of the text is the same as the ``@deprecated`` tag:

.. code-block:: text

   _%thing% is deprecated in %deprecation-version% and is removed from %removal-version%. %extra-info%. See %cr-link%_

Where there is no associated ``@deprecated`` doc tag, the format is more relaxed to allow flexibility in wording:

.. code-block:: text

   _%thing% is deprecated in %deprecation-version% <free text describing what will happen> %removal-version%. %extra-info% <optional>. See %cr-link%_

Front-end notice format
=======================

.. code-block:: text

   _%thing% is currently deprecated since %deprecation-version% and will be removed in %removal-version%. %extra-info%(optional). See %cr-link% for more information._

Definitions
***********

%thing%
=======

What is being deprecated - for example, the class name, method name, function name, service name or the use or optional status of a parameter.

%deprecation-version%
=====================

The version string representing when the change occurred.

For Mautic core and other projects that use semantic versioning, the version string is:

.. code-block:: text

   project:major.minor.patch-modifier

%removal-version%
=================

The version string representing when the deprecated code path will be removed.

%extra-info%
============

This is free text. Useful things to include are what version the code will break in, hints on how to correct the code, or what replacement to use, etc.

%cr-link%
=========

The link to the change record - usually the ``upgrade.md`` for the relevant version.

Examples / reference policies which have influenced this one
============================================================

Doctrine

[https://www.doctrine-project.org/policies/deprecation.html](https://www.doctrine-project.org/policies/deprecation.html)

Drupal

[https://www.drupal.org/about/core/policies/core-change-policies/drupal-deprecation-policy](https://www.drupal.org/about/core/policies/core-change-policies/drupal-deprecation-policy)

Pip

[https://pip.pypa.io/en/stable/development/release-process/#deprecation-policy](https://pip.pypa.io/en/stable/development/release-process/#deprecation-policy)
