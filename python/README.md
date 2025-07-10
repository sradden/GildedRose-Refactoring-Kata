# Gilded Rose starting position in Python

For exercise instructions see [top level README](../README.md)

Suggestion: create a python virtual environment for this project by navigating to the `python` directory and running:

- On MacOS/Linux:
```
python3 -m venv venv
```

Then activate the virtual environment:

- On MacOS/Linux:
  ```
  source venv/bin/activate
  ```

Install the dependencies:

```
pip install -r requirements.txt
```

## Run the unit tests from the Command-Line within project root

```
python -m pytest
```

### Run a specific test

```
python -m pytest tests/test_gilded_rose.py
```

## Run the TextTest fixture from the Command-Line

For e.g. 10 days:

```
python texttest_fixture.py 10
```

You should make sure the command shown above works when you execute it in a terminal before trying to use TextTest (see below).


## Run the TextTest approval test that comes with this project

There are instructions in the [TextTest Readme](../texttests/README.md) for setting up TextTest. You will need to specify the Python executable and interpreter in [config.gr](../texttests/config.gr). Uncomment these lines:

    executable:${TEXTTEST_HOME}/python/texttest_fixture.py
    interpreter:python

```
./start_texttest.sh
```

## Run the ApprovalTests.Python test

This test uses the framework [ApprovalTests.Python](https://github.com/approvals/ApprovalTests.Python). Run it like this:

```
python tests/test_gilded_rose_approvals.py
```

You will need to approve the output file which appears under "approved_files" by renaming it from xxx.received.txt to xxx.approved.txt.

## Assumptions
The following list of assumptions have been made in the implementation of this project:
- An [Item] name is case-insensitive, so "Aged Brie" and "aged brie" are considered the same item.
- The type of an item is determined by its name, so "Aged Brie" is always an aged brie item, "Sulfuras" is always a Sulfuras item, etc. This will have to be changed if we want to support items with the same name but different types, for example "Aged Brie" and "Aged Brie (vintage)".
- The text tests failed once i implemented [Conjured] because this was not part of the original requirements. The text tests were updated to include the new item type and its behavior.

## Future Improvements
- Add support for items with the same name but different types, for example "Aged Brie" and "Aged Brie (vintage)".
- Add type hints to the code to make it more readable and maintainable.
- Make [UpdatableItem] an abstract class to make the code more readable and maintainable.
- Add check constraints to the [Item] class to ensure that the `Quality` values passed during init are within the allowed ranges. For example, `Quality` should be between `0` and `50` but at the moment `Standard(Item("foo", 5, 53))` is valid.
- Move [UpdatableItem] subclasses to a separate module to make the code more modular and maintainable.