
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "auto_gallery-1\fill_arc.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_auto_gallery-1_fill_arc.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_gallery-1_fill_arc.py:


Author: Abdur-Rahmaan Janhangeer
Github: https://github.com/Abdur-rahmaanJ

.. GENERATED FROM PYTHON SOURCE LINES 5-29

.. code-block:: default


    from hooman import Hooman

    import pygame

    window_width, window_height = 500, 500
    hapi = Hooman(window_width, window_height)

    bg_col = (255, 255, 255)

    import hooman

    while hapi.is_running:
        hapi.background(bg_col)

        hapi.fill(hapi.color["red"])

        d = int(hapi.dist((hapi.mouseX(), hapi.mouseY()), (hapi.center_x, hapi.center_y)))
        hapi.fill_arc(hapi.center_x, hapi.center_y, d, 90, 0)

        hapi.event_loop()
        hapi.flip_display()

    pygame.quit()


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.000 seconds)


.. _sphx_glr_download_auto_gallery-1_fill_arc.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example


    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: fill_arc.py <fill_arc.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: fill_arc.ipynb <fill_arc.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
