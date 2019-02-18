# -*- coding: utf-8 -*-
# (C) 2019 Muthiah Annamalai

from opentamiltests import *
import unittest
from solthiruthi.tamil99kbd import inv_confusion_matrix as ta_kbd_cm
from solthiruthi.qwertykbd import confusion_matrix as en_kbd_cm
from solthiruthi.typographical import oridam_generate_patterns

DEBUG = False

class SolthiruthiTypographical(unittest.TestCase):
    @staticmethod
    def checkpat(word_in,check_words,kbd_cm,ed):
        """ @word_in - input word
            @check_words - list of adjacent words in keyboard
            @kbd_cm - keyboard confusion matrix
            @ed - edit distance to search at """
        pat = oridam_generate_patterns(word_in,kbd_cm,ed)
        pat = [u"".join(p) for p in pat]
        if DEBUG:
            print "Total = %d"%(len(pat))
            print "Total set = %d"%len( set(pat) )
        return (len(pat),len(set(pat)))
    
    def test_edit_distance_one(self):
        n,_ = SolthiruthiTypographical.checkpat(list('shat'),['what','shag'],en_kbd_cm,1)
        self.assertEqual(n,21)

    def test_edit_distance_two(self):
        n,_ = SolthiruthiTypographical.checkpat(list('arg'),['art','arg'],en_kbd_cm,2)
        self.assertEqual(n,117)

    def test_edit_distance_for_tamil(self):
        n,_ = SolthiruthiTypographical.checkpat(tamil.utf8.get_letters(u'பவளம்'),[u'பவகல்',u'கவளம்'],
                                                ta_kbd_cm,2)
        self.assertEqual(n,234)
    
if __name__ == "__main__":
    unittest.main()
