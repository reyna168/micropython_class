import framebuf

class Symbol:
    _BIGNUM = {
        '.': bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0000\x00\x00\x00\x00\x00\x00\x00'),
        '%': bytearray(b'|\xfe\x82\x82\xfe|\xc0\xf0|\x8e\x82\x80\x80\x00\x00\x00\x00\x00\x00 8\x1e\x07\x01\x1f?  ?\x1f\x00\x00'),
        'c': bytearray(b'\x1c"""\x1c\x00\xe0\xf8\x1c\x0e\x06\x06\x06\x0c\x1c\x18\x00\x00\x00\x00\x00\x00\x03\x0f\x1c\x18000\x18\x1c\x04'),
        '0': bytearray(b'\x00\x00\x00\x00\xf8\xfc\x0e\x06\x06\x0e\xfc\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x1f8008\x1f\x0f\x00\x00\x00\x00'),
        '1': bytearray(b'\x00\x00\x00\x00\x000\x18\x0c\xfe\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00??\x00\x00\x00\x00\x00\x00'),
        '2': bytearray(b'\x00\x00\x00\x00\x18\x1c\x0e\x06\x06\x8e\xfcx\x00\x00\x00\x00\x00\x00\x00\x0008<63100\x00\x00\x00\x00'),
        '3': bytearray(b'\x00\x00\x00\x00\x08\x0c\x06\xc6\xc6\xfc\xbc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x1c0000\x1f\x0f\x00\x00\x00\x00'),
        '4': bytearray(b'\x00\x00\x00\x00\x80\xe0p\x1c\xfe\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x06\x06\x06??\x06\x06\x00\x00\x00\x00'),
        '5': bytearray(b'\x00\x00\x00\x00\xf0\xfeNfff\xc6\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x1c0000\x1f\x0f\x00\x00\x00\x00'),
        '6': bytearray(b'\x00\x00\x00\x00\xf0\xfc\x8e\xc6\xc6\xc6\x8c\x08\x00\x00\x00\x00\x00\x00\x00\x00\x07\x1f9000\x1f\x0f\x00\x00\x00\x00'),
        '7': bytearray(b'\x00\x00\x00\x00\x06\x06\x06\x86\xe6v\x1e\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008?\x07\x00\x00\x00\x00\x00\x00\x00'),
        '8': bytearray(b'\x00\x00\x00\x008\xfc\xc6\xc6\xc6\xc6\xfc8\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x1f0000\x1f\x0f\x00\x00\x00\x00'),
        '9': bytearray(b'\x00\x00\x00\x00x\xfc\x86\x86\x86\xc6\xfc\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x08\x181118\x1f\x07\x00\x00\x00\x00')
    }
    
    _HUMID = bytearray(b'\xff\xff\xdd\xbbw\xff\x03+\xab\xab\xab\xab+\x83\xff\xff\xff\xff\x07\xf7\xd7\xd7\x07WSW\x07\xd7\xd7\xff\xff\xff\xff\xff\xdf\xe7\xfb\xd4\xe1\xf5\xc1\xf6\xe5\xd0\xf5\xe2\xd7\xff\xff\xcf\xf0\xdf\xdd\xd9\xd5\xed\xed\xd5\xd9\xdf\xdf\xff\xff\xff')
    _TEMP = bytearray(b'\xff\xff\xff\xbb\xb7o\xff\x03{[Kc[{\x03\xff\xff\xff\x07\xf7\xd7\xd7\x07WSW\x07\xd7\xd7\xff\xff\xff\xff\xff\xff\xdf\xe7\xfb\xdf\xc1\xdd\xc1\xdd\xdd\xc1\xdd\xc1\xdf\xff\xcf\xf0\xdf\xdd\xd9\xd5\xed\xed\xd5\xd9\xdf\xdf\xff\xff\xff')
    
    def __init__(self, oled):
        self.oled = oled

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def temp(self, x, y):
        fb = framebuf.FrameBuffer(self._TEMP, 32, 16, framebuf.MVLSB)
        self.oled.framebuf.blit(fb, x, y)

    def humid(self, x, y):
        fb = framebuf.FrameBuffer(self._HUMID, 32, 16, framebuf.MVLSB)
        self.oled.framebuf.blit(fb, x, y)

    def text(self, str, x, y):
        for i in str:
            fb = framebuf.FrameBuffer(self._BIGNUM[i], 16, 16, framebuf.MVLSB)
            self.oled.framebuf.blit(fb, x, y)
            x += 16
