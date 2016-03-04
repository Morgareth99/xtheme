About
=====

xtheme - xtremely lightweight Xresources color scheme manager

Screenshot
==========
For a screenshot of xtheme in action, have a look at: http://unix.porn/xtheme.png

License
=======

Copyright (C) 2016 Armin Jenewein <armin@m2m.pm>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2, or (at your option)
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.

Usage
=====

The way xtheme can be used is pretty simple - just call xtheme and
it should tell you about how to generally use it. Here's an example:

Listing installed themes
------------------------

armin@square:~$ xtheme --list
[xtheme]  List of installed themes: 

ashes     eldorado  jason       nudge      tango
astro     embers  london        numix-darkest  tartan
basic     erosion lost        ocean      teva
bespin      fishbone  marrakesh     pretty       tomorrow
bitmute     google  mashup        railscasts     trim
brewer      gotham  mikado        ryd      twilight
city      grayscale mikazuki      seaside      unified
cloud     greybird  monokai       sero       vacu
codeschool  gutterslab  muse        sexy       visi
deaf      iamblack  muzieca01     shapeshifter   visible
default     insi  muzieca-mono  solarized      yousai-bright
dot     isotope navy        specialist     zunjae
eighties    ivory neo       suede
armin@square:~$ 

Getting current theme
---------------------

armin@square:~$ xtheme --get
[xtheme]  Current theme: monokai
armin@square:~$ 

Setting a theme
---------------

armin@square:~$ xtheme --set ivory
[xtheme]  Setting theme: ivory
Creating symbolic link for new theme... done.
xrdb: Loading new Xresources definitions... done.
armin@square:~$ 

Enjoy.


