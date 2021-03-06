# -*- coding: utf-8 -*-

import os
import unittest

import diff_archiver.resolver

class TestResolver(unittest.TestCase):
	def test_resolveLocal(self):
		r=diff_archiver.resolver.Resolver()
		fname="tests/data/dl.md"
		resolved=r.resolve(fname)
		self.assertEqual(resolved, fname)

	def testHttps(self):
		fname="dl.md"
		remote="https://github.com/actlaboratory/diff_archiver/raw/master/tests/data/dl.md"
		if os.path.exists(fname): os.remove(fname)
		r=diff_archiver.resolver.Resolver()
		resolved=r.resolve(remote)
		self.assertEqual(resolved, fname)
		self.assertTrue(os.path.exists(fname))
		os.remove(fname)
