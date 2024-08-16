import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_on():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_power_off():
    tv = Television()
    tv.power()  # Turn TV on
    tv.power()  # Turn TV off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute_on():
    tv = Television()
    tv.power()
    tv.volume_up()  # Increase volume to 1
    tv.mute()  # Mute TV
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_mute_off():
    tv = Television()
    tv.power()
    tv.volume_up()  # Increase volume to 1
    tv.mute()  # Mute TV
    tv.mute()  # Unmute TV
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()  # Increase channel to 1
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_channel_wrap_around_up():
    tv = Television()
    tv.power()
    for _ in range(5):  # Exceed MAX_CHANNEL to wrap around
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()  # Decrease channel to 3 (wrap around from 0)
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_channel_wrap_around_down():
    tv = Television()
    tv.power()
    tv.channel_down()  # Go from channel 0 to MAX_CHANNEL
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()  # Increase volume to 1
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_volume_max():
    tv = Television()
    tv.power()
    for _ in range(5):  # Exceed MAX_VOLUME
        tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()  # Increase volume to 1
    tv.volume_down()  # Decrease volume to 0
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_min():
    tv = Television()
    tv.power()
    tv.volume_down()  # Already at minimum volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_mute_adjustment_up():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_up()  # Should unmute and increase volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_volume_mute_adjustment_down():
    tv = Television()
    tv.power()
    tv.volume_up()  # Increase volume to 1
    tv.mute()
    tv.volume_down()  # Should unmute and decrease volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"