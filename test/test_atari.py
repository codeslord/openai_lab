import unittest
import pytest
from os import environ
from rl.experiment import run
from . import conftest
import pandas as pd


class AtariTest(unittest.TestCase):

    @classmethod
    def test_breakout_dqn(cls):
        data_df = run('breakout_dqn')
        assert isinstance(data_df, pd.DataFrame)

    @classmethod
    def test_breakout_double_dqn(cls):
        data_df = run('breakout_double_dqn')
        assert isinstance(data_df, pd.DataFrame)
