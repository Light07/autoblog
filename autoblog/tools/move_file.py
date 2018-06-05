# -*- coding: utf-8 -*-
import os
import shutil


class MoveFile:
    @staticmethod
    def move_file(source, target):
        if not os.path.exists(source) or not os.path.exists(target):
            raise FileExistsError("Source folder or target folder doesn't exist")
        if not os.path.isdir(source) or not os.path.isdir(target):
            raise Exception("parameter should be a folder")

        for root, dirs, files in os.walk(source, topdown=True):
            for dir in dirs:
                shutil.move(root+ os.sep + dir, target)
            for file in files:
                shutil.move(root + os.sep + file, target)
