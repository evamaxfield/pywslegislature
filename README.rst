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


Python wrapper around the `Washington State Legislative Web Services API <http://wslwebservices.leg.wa.gov/#Table1>`_ with some extras.


* Free software: MIT license

* Documentation: https://pywslegislature.readthedocs.io.

Quickstart
----------
Get the most up-to-date Washington State Legislature details::

    from pywslegislature import Legislature

    current = Legislature()
    print(current.committees[0])
    # <Committee [17366 Appropriations House APP]>

    print(current.committees[0].as_dict())
    # {'id': 17366, 'name': 'Appropriations', 'long_name': 'House Committee on Appropriations', 'agency': 'House', 'acronym': 'APP', 'phone': 3607867155}

Get a specific Washington State Legislature details::

    from pywslegislature import Biennium, Legislature

    specific = Legislature(Biennium(2013))
    print(current.committees[0])
    # <Committee [8221 Agriculture & Natural Resources House AGNR]>

Specific WSL Web Services Handler::

    from pywslegislature import Biennium, WSLRequest
    from pywslegislature.services import CommitteeService

    request = WSLRequest(CommitteeService, "GetCommittees", {"biennium": str(Biennium(2013))})
    print(request)
    # <WSLRequest [http://wslwebservices.leg.wa.gov/CommitteeService.asmx/GetCommittees?biennium=2013-14]>

    results = request.process()
    print(results)
    # <WSLResults [http://wslwebservices.leg.wa.gov/CommitteeService.asmx/GetCommittees?biennium=2013-14]>

    # Results are available as xml.etree.ElementTree or as collections.OrderedDict
    print(results.xml)
    # ...
    print(results.json)
    # ...

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
