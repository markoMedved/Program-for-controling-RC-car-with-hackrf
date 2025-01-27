import numpy as np
from gnuradio import gr
from keyboard import is_pressed


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        if is_pressed("w") and is_pressed("d") == False and is_pressed("s") == False and is_pressed("a") == False:
            output_items[0][:] = input_items[0] 
            return len(output_items[0])
        
        output_items[0][:] = 0
            
        return len(output_items[0])

        
     

        
