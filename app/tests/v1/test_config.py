import unittest
from flask import current_app, Flask
import instance 

app = Flask(__name__, instance_relative_config=True)

class TestConfig(unittest.TestCase):
    def test_config(self):
        app.config.from_object(instance.config.Config)
        self.assertTrue(app.config['DEBUG'] is False)

class TestDevelopmentconfig(unittest.TestCase):
    def test_development(self):
        app.config.from_object(instance.config.DevelopmentConfig)
        self.assertTrue(app.config['DEBUG'] is True)

class TestTestingconfig(unittest.TestCase):
    def test_testing(self):
        app.config.from_object(instance.config.TestingConfig)
        self.assertTrue(app.config['DEBUG'] is True)

class TestProductionconfig(unittest.TestCase):
    def test_production(self):
        app.config.from_object(instance.config.ProductionConfig)
        self.assertTrue(app.config['DEBUG'] is False)

class TestStagingconfig(unittest.TestCase):
    def test_staging(self):
        app.config.from_object(instance.config.StagingConfig)
        self.assertTrue(app.config['DEBUG'] is True)


if __name__ == "__main__":
    unittest.main()