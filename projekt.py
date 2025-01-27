#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: marko
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import soapy
import projekt_epy_block_0_0 as epy_block_0_0  # embedded python block
import projekt_epy_block_0_1 as epy_block_0_1  # embedded python block
import projekt_epy_block_0_2 as epy_block_0_2  # embedded python block
import projekt_epy_block_0_2_0 as epy_block_0_2_0  # embedded python block
import projekt_epy_block_0_2_1 as epy_block_0_2_1  # embedded python block
import projekt_epy_block_0_2_2 as epy_block_0_2_2  # embedded python block
import projekt_epy_block_0_2_3 as epy_block_0_2_3  # embedded python block
import projekt_epy_block_0_3 as epy_block_0_3  # embedded python block
import sip



class projekt(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "projekt")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.sym_durration = sym_durration = 305e-6
        self.samp_rate = samp_rate = 3e6

        ##################################################
        # Blocks
        ##################################################

        self.soapy_hackrf_sink_0 = None
        dev = 'driver=hackrf'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_hackrf_sink_0 = soapy.sink(dev, "fc32", 1, 'hackfr',
                                  stream_args, tune_args, settings)
        self.soapy_hackrf_sink_0.set_sample_rate(0, samp_rate)
        self.soapy_hackrf_sink_0.set_bandwidth(0, 0)
        self.soapy_hackrf_sink_0.set_frequency(0, 27e6)
        self.soapy_hackrf_sink_0.set_gain(0, 'AMP', True)
        self.soapy_hackrf_sink_0.set_gain(0, 'VGA', min(max(100, 0.0), 47.0))
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            27e6, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.1)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.epy_block_0_3 = epy_block_0_3.blk(example_param=1.0)
        self.epy_block_0_2_3 = epy_block_0_2_3.blk(example_param=1.0)
        self.epy_block_0_2_2 = epy_block_0_2_2.blk(example_param=1.0)
        self.epy_block_0_2_1 = epy_block_0_2_1.blk(example_param=1.0)
        self.epy_block_0_2_0 = epy_block_0_2_0.blk(example_param=1.0)
        self.epy_block_0_2 = epy_block_0_2.blk(example_param=1.0)
        self.epy_block_0_1 = epy_block_0_1.blk(example_param=1.0)
        self.epy_block_0_0 = epy_block_0_0.blk(example_param=1.0)
        self.blocks_vector_source_x_1_0_0_0_1 = blocks.vector_source_c((1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0), True, 1, ())
        self.blocks_vector_source_x_1_0_0_0_0 = blocks.vector_source_c((1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0), True, 1, ())
        self.blocks_vector_source_x_1_0_0_0 = blocks.vector_source_c((1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0), True, 1, ())
        self.blocks_vector_source_x_1_0_0 = blocks.vector_source_c((1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0), True, 1, ())
        self.blocks_vector_source_x_1_0 = blocks.vector_source_c((1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0), True, 1, ())
        self.blocks_vector_source_x_1 = blocks.vector_source_c((1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0), True, 1, ())
        self.blocks_vector_source_x_0_1 = blocks.vector_source_c((1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0), True, 1, ())
        self.blocks_vector_source_x_0 = blocks.vector_source_c((1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0), True, 1, ())
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_repeat_0_5 = blocks.repeat(gr.sizeof_gr_complex*1, (int(samp_rate*sym_durration)))
        self.blocks_repeat_0_4_0_0_1 = blocks.repeat(gr.sizeof_gr_complex*1, (int(samp_rate*sym_durration)))
        self.blocks_repeat_0_4_0_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, (int(samp_rate*sym_durration)))
        self.blocks_repeat_0_4_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, (int(samp_rate*sym_durration)))
        self.blocks_repeat_0_4_0 = blocks.repeat(gr.sizeof_gr_complex*1, (int(samp_rate*sym_durration)))
        self.blocks_repeat_0_4 = blocks.repeat(gr.sizeof_gr_complex*1, (int(samp_rate*sym_durration)))
        self.blocks_repeat_0_3 = blocks.repeat(gr.sizeof_gr_complex*1, (int(samp_rate*sym_durration)))
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, (int(samp_rate*sym_durration)))
        self.blocks_multiply_xx_0_4_0_0 = blocks.multiply_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 300e3, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_4_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_4_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_4_0_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.epy_block_0_3, 0))
        self.connect((self.blocks_repeat_0_3, 0), (self.epy_block_0_0, 0))
        self.connect((self.blocks_repeat_0_4, 0), (self.epy_block_0_2, 0))
        self.connect((self.blocks_repeat_0_4_0, 0), (self.epy_block_0_2_0, 0))
        self.connect((self.blocks_repeat_0_4_0_0, 0), (self.epy_block_0_2_2, 0))
        self.connect((self.blocks_repeat_0_4_0_0_0, 0), (self.epy_block_0_2_1, 0))
        self.connect((self.blocks_repeat_0_4_0_0_1, 0), (self.epy_block_0_2_3, 0))
        self.connect((self.blocks_repeat_0_5, 0), (self.epy_block_0_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.soapy_hackrf_sink_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_vector_source_x_0_1, 0), (self.blocks_repeat_0_3, 0))
        self.connect((self.blocks_vector_source_x_1, 0), (self.blocks_repeat_0_5, 0))
        self.connect((self.blocks_vector_source_x_1_0, 0), (self.blocks_repeat_0_4, 0))
        self.connect((self.blocks_vector_source_x_1_0_0, 0), (self.blocks_repeat_0_4_0, 0))
        self.connect((self.blocks_vector_source_x_1_0_0_0, 0), (self.blocks_repeat_0_4_0_0, 0))
        self.connect((self.blocks_vector_source_x_1_0_0_0_0, 0), (self.blocks_repeat_0_4_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_1_0_0_0_1, 0), (self.blocks_repeat_0_4_0_0_1, 0))
        self.connect((self.epy_block_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.epy_block_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.epy_block_0_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.epy_block_0_2_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.epy_block_0_2_1, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.epy_block_0_2_2, 0), (self.blocks_add_xx_0, 7))
        self.connect((self.epy_block_0_2_3, 0), (self.blocks_add_xx_0, 6))
        self.connect((self.epy_block_0_3, 0), (self.blocks_add_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "projekt")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sym_durration(self):
        return self.sym_durration

    def set_sym_durration(self, sym_durration):
        self.sym_durration = sym_durration
        self.blocks_repeat_0.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_3.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_4.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_4_0.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_4_0_0.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_4_0_0_0.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_4_0_0_1.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_5.set_interpolation((int(self.samp_rate*self.sym_durration)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_repeat_0.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_3.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_4.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_4_0.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_4_0_0.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_4_0_0_0.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_4_0_0_1.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_repeat_0_5.set_interpolation((int(self.samp_rate*self.sym_durration)))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(27e6, self.samp_rate)
        self.soapy_hackrf_sink_0.set_sample_rate(0, self.samp_rate)




def main(top_block_cls=projekt, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
