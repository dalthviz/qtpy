import pytest

from qtpy import PYQT5, PYQT6, PYQT_VERSION
from tests.utils import using_conda


@pytest.mark.skipif(
    PYQT6 and using_conda(),
    reason="Not available on PyQt6 with conda",
)
def test_qtsensors():
    """Test the qtpy.QtSensors namespace"""
    QtSensors = pytest.importorskip("qtpy.QtSensors")

    assert QtSensors.QAccelerometer is not None
    assert QtSensors.QAccelerometerFilter is not None
    assert QtSensors.QAccelerometerReading is not None


@pytest.mark.skipif(
    PYQT5 and PYQT_VERSION.startswith("5.9"),
    reason=(
        "A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.* "
        "to work with scoped enum access"
    ),
)
@pytest.mark.skipif(
    PYQT6 and using_conda(),
    reason="Not available on PyQt6 with conda",
)
def test_enum_access():
    """Test scoped and unscoped enum access."""
    QtSensors = pytest.importorskip("qtpy.QtSensors")

    assert (
        QtSensors.QSensor.FixedOrientation
        == QtSensors.QSensor.AxesOrientationMode.FixedOrientation
    )
