import sys
import ctypes
import unittest
from dynd import nd, ndt

class TestTypeBasics(unittest.TestCase):
    def test_type_repr(self):
        roundtrip = [
          "fixed_string[10, 'utf16']",
          "() -> int32",
          "(int32) -> int32",
          "(int32, float64) -> int32",
          "(..., scale: float64, ...) -> int32",
          "(int32, ..., scale: float64, color: float64, ...) -> int32",
          "(int32, float32, ..., scale: float64, color: float64, ...) -> int32"
        ]

        for s in roundtrip:
            self.assertEqual(repr(ndt.type(s)), "ndt.type(" + repr(s) + ")")


