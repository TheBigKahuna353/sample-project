
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "auto_gallery-1\button_events.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_auto_gallery-1_button_events.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_gallery-1_button_events.py:


Author: https://github.com/TheBigKahuna353

.. GENERATED FROM PYTHON SOURCE LINES 4-82

.. code-block:: default


    from hooman import Hooman  # imports local not from

    import pygame

    window_width, window_height = 500, 500
    hapi = Hooman(window_width, window_height)

    bg_col = (255, 255, 255)

    # the function that gets called when the button is clicked on


    def button_clicked(this):
        if this.y == 250:
            this.y = 300
        else:
            this.y = 250
        this.background_color = hapi.color["blue"]


    def button_enter(this):
        # hapi.rect(this.x + this.w, 250, 100, 20)
        this.curve = 0.5
        # hapi.background(hapi.color['green'])
        global bg_col
        bg_col = hapi.color["green"]
        this.create_button()


    def button_exit(this):
        # hapi.rect(this.x + this.w, 250, 100, 20)
        this.curve = 0.1
        # hapi.background(hapi.color['green'])
        global bg_col
        bg_col = hapi.color["white"]
        this.create_button()


    grey_style = {
        "background_color": (200, 200, 200),
        "hover_background_color": (220, 220, 220),
        "curve": 1,
        "padding_x": 5,
        "padding_y": 5,
        "font_size": 15,
        "on_click": button_clicked,
        "on_enter": button_enter,
        "on_exit": button_exit,
    }


    button2 = hapi.button(150, 250, 0, 0, "No Click Me", grey_style)


    def handle_events(event):
        if event.type == pygame.QUIT:
            hapi.is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                hapi.is_running = False


    hapi.handle_events = handle_events

    clock = pygame.time.Clock()

    while hapi.is_running:
        hapi.background(bg_col)

        hapi.update_ui()
        hapi.event_loop()

        hapi.flip_display()

        clock.tick(60)

    pygame.quit()


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.000 seconds)


.. _sphx_glr_download_auto_gallery-1_button_events.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example


    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: button_events.py <button_events.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: button_events.ipynb <button_events.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
