# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This module contains dictionaries that can be used to set a matplotlib
plotting style.  It is mostly here to allow a consistent plotting style
in tutorials, but can be used to prepare any matplotlib figure.
"""

from ..utils import minversion
# This returns False if matplotlib cannot be imported
MATPLOTLIB_GE_1_5 = minversion('matplotlib', '1.5')


__all__ = ['astropy_mpl_style_1', 'astropy_mpl_style',
           'astropy_mpl_docs_style']


# Version 1 astropy plotting style for matplotlib
astropy_mpl_style_1 = {
    # Lines
    'lines.linewidth': 1.7,
    'lines.antialiased': True,

    # Patches
    'patch.linewidth': 1.0,
    'patch.facecolor': '#348ABD',
    'patch.edgecolor': '#CCCCCC',
    'patch.antialiased': True,

    # Images
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Font
    'font.size': 12.0,

    # Axes
    'axes.facecolor': '#FFFFFF',
    'axes.edgecolor': '#AAAAAA',
    'axes.linewidth': 1.0,
    'axes.grid': True,
    'axes.titlesize': 'x-large',
    'axes.labelsize': 'large',
    'axes.labelcolor': 'k',
    'axes.axisbelow': True,

    # Ticks
    'xtick.major.size': 0,
    'xtick.minor.size': 0,
    'xtick.major.pad': 6,
    'xtick.minor.pad': 6,
    'xtick.color': '#565656',
    'xtick.direction': 'in',
    'ytick.major.size': 0,
    'ytick.minor.size': 0,
    'ytick.major.pad': 6,
    'ytick.minor.pad': 6,
    'ytick.color': '#565656',
    'ytick.direction': 'in',

    # Legend
    'legend.fancybox': True,
    'legend.loc': 'best',

    # Figure
    'figure.figsize': [8, 6],
    'figure.facecolor': '1.0',
    'figure.edgecolor': '0.50',
    'figure.subplot.hspace': 0.5,

    # Other
    'savefig.dpi': 72,
}
color_cycle = ['#348ABD',   # blue
               '#7A68A6',   # purple
               '#A60628',   # red
               '#467821',   # green
               '#CF4457',   # pink
               '#188487',   # turquoise
               '#E24A33']   # orange

if MATPLOTLIB_GE_1_5:
    # This is a dependency of matplotlib, so should be present.
    from cycler import cycler
    astropy_mpl_style_1['axes.prop_cycle'] = cycler('color', color_cycle)
else:
    astropy_mpl_style_1['axes.color_cycle'] = color_cycle

astropy_mpl_style = astropy_mpl_style_1
"""The most recent version of the astropy plotting style."""

astropy_mpl_docs_style = astropy_mpl_style_1.copy()
"""The plotting style used in the astropy documentation."""

color_cycle_docs = [
    '#E24A33',   # orange
    '#348ABD',   # blue
    '#467821',   # green
    '#A60628',   # red
    '#7A68A6',   # purple
    '#CF4457',   # pink
    '#188487'    # turquoise
]

if MATPLOTLIB_GE_1_5:
    astropy_mpl_docs_style['axes.prop_cycle'] = cycler('color',
                                                       color_cycle_docs)
else:
    astropy_mpl_docs_style['axes.color_cycle'] = color_cycle_docs

astropy_mpl_docs_style['axes.grid'] = False
astropy_mpl_docs_style['figure.figsize'] = (6, 6)
astropy_mpl_docs_style['savefig.facecolor'] = 'none'
astropy_mpl_docs_style['savefig.bbox'] = 'tight'
