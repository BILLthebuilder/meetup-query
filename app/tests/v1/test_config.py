import unittest
from flask import current_app, Flask
import instance 

app = Flask(__name__, instance_relative_config=True)

class TestConfig(unittest.TestCase):
    """A test case for the default configuration"""
    def test_config(self):
        app.config.from_object(instance.config.Config)
        self.assertTrue(app.config['DEBUG'] is False)

class TestDevelopmentconfig(unittest.TestCase):
    """A test case for the development configuration"""
    def test_development(self):
        app.config.from_object(instance.config.DevelopmentConfig)
        self.assertTrue(app.config['DEBUG'] is True)

class TestTestingconfig(unittest.TestCase):
    """A test case for the testing configuration"""
    def test_testing(self):
        app.config.from_object(instance.config.TestingConfig)
        self.assertTrue(app.config['DEBUG'] is True)

class TestProductionconfig(unittest.TestCase):
    """A test case for the production configuration"""
    def test_production(self):
        app.config.from_object(instance.config.ProductionConfig)
        self.assertTrue(app.config['DEBUG'] is False)

class TestStagingconfig(unittest.TestCase):
    """A test case for the staging configuration"""
    def test_staging(self):
        app.config.from_object(instance.config.StagingConfig)
        self.assertTrue(app.config['DEBUG'] is True)


if __name__ == "__main__":
    unittest.main()