from loggerhead.tests.test_simple import BasicTests

import os
from turbogears import testutil
import cherrypy

class TestSurviveOverUpgrade(BasicTests):

    def test_upgrade(self):
        self.createBranch()

        f = open(os.path.join(self.bzrbranch, 'myfilename'), 'w')
        try:
            f.write("foo")
        finally:
            f.close()
        self.tree.add('myfilename')
        msg = 'a very exciting commit message'
        self.tree.commit(message=msg)

        self.setUpLoggerhead()

        testutil.create_request('/project/branch/changes')
        assert msg in cherrypy.response.body[0]

        from bzrlib.upgrade import upgrade
        from bzrlib.bzrdir import format_registry
        upgrade(self.bzrbranch, format_registry.make_bzrdir('dirstate-tags'))

        testutil.create_request('/project/branch/changes')
        assert msg in cherrypy.response.body[0]
