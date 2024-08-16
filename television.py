class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        self._status = not self._status

    def mute(self):
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = self._prev_volume
            else:
                self._muted = True
                self._prev_volume = self._volume
                self._volume = Television.MIN_VOLUME

    def channel_up(self):
        if self._status:
            self._channel = (self._channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        if self._status:
            self._channel = (self._channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self):
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = self._prev_volume
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1
                self._prev_volume = self._volume

    def volume_down(self):
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = self._prev_volume
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1
                self._prev_volume = self._volume

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"