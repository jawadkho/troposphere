import unittest
from troposphere import Join
from troposphere.apigateway import Model


class TestModel(unittest.TestCase):
    def test_schema(self):
        # Check with no schema
        model = Model(
            "schema",
            RestApiId="apiid",
        )
        model.validate()

        # Check valid json schema string
        model = Model(
            "schema",
            RestApiId="apiid",
            Schema='{"a": "b"}',
        )
        model.validate()

        # Check invalid json schema string
        model = Model(
            "schema",
            RestApiId="apiid",
            Schema='{"a: "b"}',
        )
        with self.assertRaises(ValueError):
            model.validate()

        # Check accepting dict and converting to string in validate
        d = {"c": "d"}
        model = Model(
            "schema",
            RestApiId="apiid",
            Schema=d
        )
        model.validate()
        self.assertEqual(model.properties['Schema'], '{"c": "d"}')

        # Check invalid Schema type
        with self.assertRaises(TypeError):
            model = Model(
                "schema",
                RestApiId="apiid",
                Schema=1
            )

        # Check Schema being an AWSHelperFn
        model = Model(
            "schema",
            RestApiId="apiid",
            Schema=Join(':', ['{"a', ': "b"}']),
        )
        model.validate()


if __name__ == '__main__':
    unittest.main()
