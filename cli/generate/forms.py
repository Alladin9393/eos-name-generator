"""
Provide forms for command line interface's generate name commands.
"""
from marshmallow import (
    Schema,
    fields,
    validate,
)


class GenerateNameForm(Schema):
    """
    Get a list of names form.
    """

    num = fields.Integer(
        allow_none=True,
        strict=True,
        required=False,
        validate=[
            validate.Range(min=1, error='Num must be greater than 0.'),
        ],
    )
    numpy_random_generator = fields.Bool(required=False)
    numbers_probabilities = fields.Float(
        allow_none=True,
        strict=True,
        required=False,
        validate=[
            validate.Range(min=0, max=1, error='Numbers probabilities must be between 0 and 1.'),
        ],
    )
    seed_data_path = fields.String(required=False)
