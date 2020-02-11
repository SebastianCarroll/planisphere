#!/usr/bin/python3
# planisphere.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model planisphere.
#
# Copyright (C) 2014-2020 Dominic Ford <dcf21-www@dcford.org.uk>
#
# This code is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# You should have received a copy of the GNU General Public License along with
# this file; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA  02110-1301, USA

# ----------------------------------------------------------------------------

"""
This is the top level script for drawing all the parts needed to build planispheres which work at a range of
different latitudes. They are rendered in PDF, SVG and PNG image formats.

Additionally, we use LaTeX to build a summary document for each latitude, which includes all of the parts needed
to build a planisphere for that latitude, and instructions as to how to put them together.
"""


import text

# Render planisphere in all available languages
for language in text.text:
    print(language)