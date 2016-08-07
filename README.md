# fodselsnummer
Used to generate and validate Norwegian birth numbers ("fødselsnummer")

## Installation
python setup.py install

## Testing
python -m unittest tests.fodselsnummer_tests

## Example usage
import fodselsnummer

fodselsnummer.check_fnr('12345678900')
