try:
    from .TrueRandomTrackColors import TrueRandomTrackColors
except ImportError as e:
    # This is needed for unit tests to work through pytest.
    # Otherwise, pytest will attempt and fail to import this __init__.py
    pass

def create_instance(c_instance):
    return TrueRandomTrackColors(c_instance)