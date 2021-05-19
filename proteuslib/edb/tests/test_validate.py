###############################################################################
# ProteusLib Copyright (c) 2021, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory, Oak Ridge National
# Laboratory, National Renewable Energy Laboratory, and National Energy
# Technology Laboratory (subject to receipt of any required approvals from
# the U.S. Dept. of Energy). All rights reserved.
#
# Please see the files COPYRIGHT.md and LICENSE.md for full copyright and license
# information, respectively. These files are also available online at the URL
# "https://github.com/nawi-hub/proteuslib/"
#
###############################################################################
"""
Tests for validate module
"""
import pytest
from ..validate import validate_reaction, validate_component
from .data import component_data, reaction_data


@pytest.mark.unit
@pytest.mark.parametrize("comp", component_data)
def test_validate_component(comp):
    assert validate_component(comp)


@pytest.mark.unit
@pytest.mark.parametrize("reaction", reaction_data)
def test_validate_reaction(reaction):
    assert validate_reaction(reaction)
