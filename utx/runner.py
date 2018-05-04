#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import time
import unittest
import platform
from utx.BSTestRunner import BSTestRunner


class TestRunner:
    def __init__(self, title, case_path='testcase', report_path='report'):
        self.title = title
        self.case_path = case_path
        self.report_path = report_path

    def run_test(self, suite=None):
        if not os.path.exists(self.report_path):
            os.mkdir(self.report_path)
        report_file = os.path.join(self.report_path, "index.html")
        if os.path.exists(report_file):
            report_file_name_new = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(os.path.getctime(report_file)))
            os.rename(report_file, os.path.join(self.report_path, report_file_name_new + '.html'))
        if not suite:
            suite = unittest.TestLoader().discover(self.case_path)

        # with open(report_file, "wb") as f:            # 取消bstest-style风格报告
        #     runner = BSTestRunner(stream=f, title=self.title)
        #     runner.run(suite)

        runner = BSTestRunner(self.title, report_file)
        runner.run(suite)
        if "winodws" in platform.system().lower():
            print("测试完成，请查看报告")
            os.system("start report")
