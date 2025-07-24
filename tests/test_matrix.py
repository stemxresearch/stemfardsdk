from sdk.analyze_matrix import analyze_matrix


def test_basic_analysis():
    result = analyze_matrix([[1, 2], [3, 4]])
    assert result.shape == [2, 2]
    assert result.is_square is True
    assert result.determinant == -2.0
