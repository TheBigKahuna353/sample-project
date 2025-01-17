
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "auto_gallery-1\text_box.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_auto_gallery-1_text_box.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_gallery-1_text_box.py:


Author: https://github.com/TheBigKahuna353

.. GENERATED FROM PYTHON SOURCE LINES 4-39

.. code-block:: default


    from hooman import Hooman

    import pygame

    window_width, window_height = 500, 500
    hapi = Hooman(window_width, window_height)

    bg_col = (255, 255, 255)

    text_box_options = {"background_color": hapi.color["light_grey"], "max_lines": 3}

    text_box = hapi.text_box(100, 100, 300, 40, text_box_options)


    def handle_events(event):
        if event.type == pygame.QUIT:
            hapi.is_running = False
        if event.type == pygame.KEYDOWN:
            text_box.key_down(event)
            if event.key == pygame.K_ESCAPE:
                hapi.is_running = False


    hapi.handle_events = handle_events

    while hapi.is_running:
        hapi.background(bg_col)

        text_box.update()

        hapi.flip_display()
        hapi.event_loop()

    pygame.quit()


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.000 seconds)


.. _sphx_glr_download_auto_gallery-1_text_box.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example


    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: text_box.py <text_box.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: text_box.ipynb <text_box.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
