#!/bin/env python

import unittest
import subprocess as sp

class NewUserTestCase(unittest.TestCase):
    def test_can_run_proofread_program(self):
        #  Mary is a new PhD student. She has worked hard during the past
        # months and she wants to publish the results. She is told by her
        # advisor that the article must be written in English. English!
        #  She can write in English, but sometimes she feels unsure concerning
        # prepositions. She knows technical words, but she would like to
        # have more vocabulary. She feels a bit worried.
        #  Fortunately, there is another PhD student that mentions something
        # called "ProofReader". It appears to be a piece of software that can help
        # her with her problems.
        #  After installing this tool, the first thing she does is, of course,
        # try to use it:
        proofread_run_result = sp.run(["proofread"], stderr=sp.PIPE)

        # # Wonderful! It seems to work ...but it returns an error:
        # self.assertNotEqual(0, proofread_run_result.returncode)
        
        # #  Thanksfully, she also gets a hint to use the tool:
        # self.assertIn(
        #     "the following argument is required: query",
        #     proofread_run_result.stderr.decode()
        # )

        #  Mary tries to provide an argument to "proofread". She wants to obtain
        # the synonyms of "compute":
        proofread_run_result = sp.run(["proofread", "#compute"], stdout=sp.PIPE)

        # She gets, as output, a list of words, among them she sees "calculate", 
        # "reckon" and "work out":
        compute_synonyms = ("calculate", "reckon", "work out")
        for synonym in compute_synonyms:
            self.assertIn(synonym, proofread_run_result.stdout.decode())
        # self.fail("finish it!")
        

if __name__ == "__main__":
    unittest.main()
    
