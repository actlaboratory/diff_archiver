# -*- coding: utf-8 -*-
# diff_archiver file path resolver
#Copyright (C) 2020 Yukio Nozawa <personal@nyanchangames.com>

import re
import urllib.request

"""ファイルパスを調べて、ファイルがリモートにある場合にはダウンロードします。"""

class Error(Exception): pass

class Resolver():
	"""resolve メソッドを呼んで使います。"""
	def resolve(self, path):
		"""
			パスが http または https から始まる場合、そのファイルをダウンロードします。層でなければ、そのファイルはローカルに存在すると仮定します。最終的にアクセス可能となったローカル上のファイルパスを返します。

			:param path: 調べるファイルパス
			:rtype: str
		"""
		if re.match(r"https*:\/\/", path):
			try:
				local_path=path.split("/")[-1]
				urllib.request.urlretrieve(path, local_path)
				path=local_path
			except Exception as e:
				raise Error(str(e))
			#end exception
		#end download
		return path



