#
# Copyright (c) nexB Inc. and others. All rights reserved.
# ScanCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/scancode-toolkit for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import os.path
import saneyaml

from packagedcode import readme 
from packages_test_utils import PackageTester


class TestReadme(PackageTester):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_parse_facebook_downloaded_from_as_download_url(self):
        test_file = self.get_test_loc('readme/facebook/downloaded-from-as-download_url/README.facebook')
        expected_loc = self.get_test_loc('readme/facebook/downloaded-from-as-download_url/README.facebook.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=True)

    def test_parse_facebook_download_link_as_download_url(self):
        test_file = self.get_test_loc('readme/facebook/download-link-as-download_url/README.facebook')
        expected_loc = self.get_test_loc('readme/facebook/download-link-as-download_url/README.facebook.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=True)

    def test_parse_facebook_source_as_homepage_url(self):
        test_file = self.get_test_loc('readme/facebook/repo-as-homepage_url/README.facebook')
        expected_loc = self.get_test_loc('readme/facebook/repo-as-homepage_url/README.facebook.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_facebook_source_as_homepage_url(self):
        test_file = self.get_test_loc('readme/facebook/source-as-homepage_url/README.facebook')
        expected_loc = self.get_test_loc('readme/facebook/source-as-homepage_url/README.facebook.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_facebook_website_as_homepage_url(self):
        test_file = self.get_test_loc('readme/facebook/website-as-homepage_url/README.facebook')
        expected_loc = self.get_test_loc('readme/facebook/website-as-homepage_url/README.facebook.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_facebook_project_as_name(self):
        test_file = self.get_test_loc('readme/facebook/project-as-name/README.facebook')
        expected_loc = self.get_test_loc('readme/facebook/project-as-name/README.facebook.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_facebook_missing_type(self):
        test_file = self.get_test_loc('readme/facebook/missing-type/README.facebook')
        expected_loc = self.get_test_loc('readme/facebook/missing-type/README.facebook.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_facebook_capitalized_filename(self):
        test_file = self.get_test_loc('readme/facebook/capital-filename/README.FACEBOOK')
        expected_loc = self.get_test_loc('readme/facebook/capital-filename/README.FACEBOOK.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_thirdparty_basic(self):
        test_file = self.get_test_loc('readme/thirdparty/basic/README.thirdparty')
        expected_loc = self.get_test_loc('readme/thirdparty/basic/README.thirdparty.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_google_basic(self):
        test_file = self.get_test_loc('readme/google/basic/README.google')
        expected_loc = self.get_test_loc('readme/google/basic/README.google.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_facebook_basic(self):
        test_file = self.get_test_loc('readme/facebook/basic/README.facebook')
        expected_loc = self.get_test_loc('readme/facebook/basic/README.facebook.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_chromium_basic(self):
        test_file = self.get_test_loc('readme/chromium/basic/README.chromium')
        expected_loc = self.get_test_loc('readme/chromium/basic/README.chromium.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_android_basic(self):
        test_file = self.get_test_loc('readme/android/basic/README.android')
        expected_loc = self.get_test_loc('readme/android/basic/README.android.expected')
        package = readme.parse(test_file)
        self.check_package(package, expected_loc, regen=False)

    def test_parse_invalid_readme(self):
        test_file = self.get_test_loc('readme/invalid/invalid_file')
        package = readme.parse(test_file)
        assert package == None
