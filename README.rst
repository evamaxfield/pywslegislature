===============
pywslegislature
===============


.. image:: https://img.shields.io/pypi/v/pywslegislature.svg
        :target: https://pypi.python.org/pypi/pywslegislature

.. image:: https://img.shields.io/travis/JacksonMaxfield/pywslegislature.svg
        :target: https://travis-ci.org/JacksonMaxfield/pywslegislature

.. image:: https://readthedocs.org/projects/pywslegislature/badge/?version=latest
        :target: https://pywslegislature.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Request wrappers around `Washington State Legislative Web Services API <http://wslwebservices.leg.wa.gov/#Table1>`_


* Free software: MIT license

* Documentation: https://pywslegislature.readthedocs.io.

Quickstart
----------

Specific WSL Web Services Handler::

    from pywslegislature import Biennium, WSLRequest, services
    from pywslegislature.services import CommitteeService

    print(CommitteeService.header)
    # 'CommitteeService.asmx'

    print(CommitteeService.source)
    # 'http://wslwebservices.leg.wa.gov/CommitteeService.asmx'

    request = WSLRequest(CommitteeService.header, CommitteeService.GetCommittees, {"biennium": str(Biennium(2013))})
    print(request)
    # <WSLRequest [http://wslwebservices.leg.wa.gov/CommitteeService.asmx/GetCommittees?biennium=2013-14]>

    results = request.process()
    print(results)
    # <WSLResults [http://wslwebservices.leg.wa.gov/CommitteeService.asmx/GetCommittees?biennium=2013-14]>

    # Results are available as xml.etree.ElementTree or collections.OrderedDict
    print(results.xml)
    # ...
    print(results.json)
    # ...

In progress
-----------
ORM style mappings between Legilature objects:

Get the most up-to-date Washington State Legislature details::

    from pywslegislature import Legislature

    current = Legislature()
    print(current.committees[0])
    # <Committee [17366 Appropriations House APP]>

Get a specific Washington State Legislature details::

    from pywslegislature import Biennium, Legislature

    specific = Legislature(Biennium(2013))
    print(current.committees[0])
    # <Committee [8221 Agriculture & Natural Resources House AGNR]>

Credits
-------

This package was created with Cookiecutter_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
