
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "auto_gallery-1\color_mouse.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_auto_gallery-1_color_mouse.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_gallery-1_color_mouse.py:


Author: Abdur-Rahmaan Janhangeer
Github: https://github.com/Abdur-rahmaanJ

.. GENERATED FROM PYTHON SOURCE LINES 5-41

.. code-block:: default


    from hooman import Hooman

    import pygame

    hapi = Hooman(500, 500)


    def handle_events(event):
        if event.type == pygame.QUIT:
            hapi.is_running = False


    hapi.handle_events = handle_events

    while hapi.is_running:
        hapi.background((255, 255, 255))

        hapi.no_stroke()
        mx = (hapi.mouseX() / hapi.WIDTH) * 255

        hapi.fill((0, mx, 0))
        for i in range(50, 200, 60):
            hapi.rect(i, 50, 30, 30)

        hapi.fill((255, 0, 0))
        hapi.ellipse(hapi.mouseX(), hapi.mouseY(), 10, 10)

        hapi.stroke_size(1)
        hapi.stroke((255, 10, 10))
        hapi.line(0, hapi.mouseY(), hapi.mouseX() - 10, hapi.mouseY())

        hapi.flip_display()
        hapi.event_loop()

    pygame.quit()


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.000 seconds)


.. _sphx_glr_download_auto_gallery-1_color_mouse.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example


    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: color_mouse.py <color_mouse.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: color_mouse.ipynb <color_mouse.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
