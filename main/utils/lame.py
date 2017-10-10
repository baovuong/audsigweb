#coding:utf-8
# from http://z4none.me/post/2014/python-zhong-shi-yong-libmp3lame-jin-xing-mp3-bian-jie-ma

import time
import ctypes

class LameEncoder():
    def __init__(self, sample_rate, channel_count, bit_rate):
        self.dll  = ctypes.CDLL("libmp3lame.dll")
        self.lame = self.dll.lame_init()
        self.dll.lame_set_in_samplerate(self.lame, sample_rate);
        self.dll.lame_set_num_channels(self.lame, channel_count);
        self.dll.lame_set_brate(self.lame, bit_rate);
        self.dll.lame_set_quality(self.lame, 3);
        self.dll.lame_init_params(self.lame);

    def encode(self, pcm_data):
        sample_count    = len(pcm_data) /2
        output_buff_len = int(1.25 * sample_count + 7200)
        output_buff     = ctypes.create_string_buffer(output_buff_len)
        output_size     = self.dll.lame_encode_buffer(self.lame, ctypes.create_string_buffer(pcm_data), 0, sample_count, output_buff, output_buff_len);
        return output_buff.raw[:output_size]

class LameDecoder():
    def __init__(self, sample_rate, channel_count, bit_rate):
        self.dll  = ctypes.CDLL("libmp3lame.dll")
        self.lame = self.dll.lame_init()
        self.hip  = self.dll.hip_decode_init()
        self.dll.lame_set_in_samplerate(self.lame, sample_rate)
        self.dll.lame_set_num_channels(self.lame, channel_count)
        self.dll.lame_set_brate(self.lame, bit_rate)
        self.dll.lame_set_mode(self.lame, 3)
        self.dll.lame_set_quality(self.lame, 3)
        self.dll.lame_init_params(self.lame)
        self.dll.lame_get_framesize(self.lame)

    def decode(self, mp3_data):
        output_buff_len =  self.dll.lame_get_framesize(self.lame) * 2
        output_buff     = ctypes.create_string_buffer(output_buff_len)
        output_size     = self.dll.hip_decode1(self.hip, ctypes.create_string_buffer(mp3_data), len(mp3_data), output_buff, 0);
        return output_buff.raw[:output_size * 2]

    def flush(self):
        output_buff_len =  self.dll.lame_get_framesize(self.lame) * 2
        output_buff     = ctypes.create_string_buffer(output_buff_len)
        output_size     = self.dll.hip_decode1(self.hip, ctypes.create_string_buffer(""), 0, output_buff, 0);
        return output_buff.raw[:output_size * 2]