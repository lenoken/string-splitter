import string_splitter

def test_split_empty_string_result_empty_array(self):
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = string_splitter.TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    expResult = []
    result = None
    cut = string_splitter.TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

